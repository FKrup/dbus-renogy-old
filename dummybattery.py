import platform
from gi.repository import GLib

from vedbus import VeDbusService


class DummyBattery(object):
    def __init__(self):
        self._dbusservice = VeDbusService('com.victronenergy.battery.diy')
        self._paths = {
            '/Dc/0/Voltage': {'initial': 54.0},
            '/Dc/0/Current': {'initial': 0.926},
            '/Dc/0/Power': {'initial': 50.0}
        }

        # Create the management objects, as specified in the ccgx dbus-api document
        self._dbusservice.add_path('/Mgmt/ProcessName', __file__)
        self._dbusservice.add_path('/Mgmt/ProcessVersion', 'Unkown version, and running on Python ' + platform.python_version())
        self._dbusservice.add_path('/Mgmt/Connection', 'Not implemented')

        # Create the mandatory objects
        self._dbusservice.add_path('/DeviceInstance', 0)
        self._dbusservice.add_path('/ProductId', 0)
        self._dbusservice.add_path('/ProductName', 'DIY Battery')
        self._dbusservice.add_path('/FirmwareVersion', 0)
        self._dbusservice.add_path('/HardwareVersion', 0)
        self._dbusservice.add_path('/Connected', 1)

        for path, settings in self._paths.items():
            self._dbusservice.add_path(
                path, settings['initial'], writeable=True, onchangecallback=self._handlechangedvalue)

        GLib.timeout_add(1000, self._update)

    def _update(self):
        with self._dbusservice as s:
            for path, settings in self._paths.items():
                if 'update' in settings:
                    update = settings['update']
                    if callable(update):
                        s[path] = update(path, s[path])
                    else:
                        s[path] += update
        return True

    def _handlechangedvalue(self, path, value):
        return True