from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import sys
from datetime import datetime
from PyQt6.QtCore import QCoreApplication, qInfo, qDebug, QEventLoop
from logging import init_logging

from velib_python.dbusdummyservice import DbusDummyService

VERSION = "1.0.0"


def main():
    app = QCoreApplication(sys.argv)
    app.setApplicationVersion(VERSION)

    qInfo(f"dbus_renogy v{VERSION} started")
    qInfo(f"Built on {datetime.now().strftime('%b %d %Y')} at {datetime.now().strftime('%H:%M:%S')}")

    args = app.arguments()
    app.setApplicationName(args.pop(0))

    dbus_address = "system"
    debug = False

    while args:
        arg = args.pop(0)

        if arg == "-h" or arg == "--help":
            qInfo(sys.argv[0])
            qInfo("\t-h, --help")
            qInfo("\t Show this message.")
            qInfo("\t-V, --version")
            qInfo("\t Show the application version.")
            qInfo("\t-d, --debug")
            qInfo("\t Enable debug logging")
            qInfo("\t-b, --dbus")
            qInfo("\t dbus address or 'session' or 'system'")
            return 0

        if arg == "-v" or arg == "--version":
            qDebug(VERSION)
            return 0

        elif arg == "-d" or arg == "--debug":
            debug = True

        elif arg == "-b" or arg == "--dbus":
            if args:
                dbus_address = args.pop(0)

    init_logging(debug)
    #
    DBusGMainLoop(set_as_default=True)

    dummy_service = DbusDummyService(
        servicename='com.victronenergy.solarcharger.renogy',
        deviceinstance=1,
        paths={
            '/NrOfTrackers': {'initial': 1, 'update': 0},
            '/Pv/V': {'initial': 0, 'update': 1},
            '/Pv/I': {'initial': 0, 'update': 1},
            '/Pv/0/P': {'initial': 0, 'update': 1},
            '/Pv/0/MppOperationMode': {'initial': 2, 'update': 0},
            '/Pv/0/Name': {'initial': 'Tracker 1', 'update': 0},
        },
        productname='My Dummy Product',
        connection='My Dummy Connection',
        productid=1234
    )

    mainloop = GLib.MainLoop()
    mainloop.run()
    #

    return app.exec()


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
