from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
import logging
import _thread as thread

from dbusdummyservice import DbusDummyService


def main():
    logging.basicConfig(level=logging.DEBUG)
    thread.daemon = True

    DBusGMainLoop(set_as_default=True)

    path_UpdateIndex = '/UpdateIndex'
    pvac_output = DbusDummyService(
        servicename='com.victronenergy.solarcharger.renogy',
        deviceinstance=0,
        paths={
        '/Ac/Power': {'initial': 0},
        '/Ac/L1/Voltage': {'initial': 0},
        '/Ac/L2/Voltage': {'initial': 0},
        '/Ac/L3/Voltage': {'initial': 0},
        '/Ac/L1/Current': {'initial': 0},
        '/Ac/L2/Current': {'initial': 0},
        '/Ac/L3/Current': {'initial': 0},
        '/Ac/L1/Power': {'initial': 0},
        '/Ac/L2/Power': {'initial': 0},
        '/Ac/L3/Power': {'initial': 0},
        '/Ac/Energy/Forward': {'initial': 0},
        '/Ac/Energy/Reverse': {'initial': 0},
        path_UpdateIndex: {'initial': 0},
    })

    logging.info('Connected to dbus, and switching over to GLib.MainLoop() (= event based)')
    mainloop = GLib.MainLoop()
    mainloop.run()

if __name__ == '__main__':
    main()
