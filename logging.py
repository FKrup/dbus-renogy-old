from PyQt6.QtCore import QLoggingCategory, qSetMessagePattern, QtMsgType

_debug_logging = False


def init_logging(log_debug):
    QLoggingCategory.defaultCategory().setEnabled(QtMsgType.QtDebugMsg, log_debug)
    qSetMessagePattern("%{type} %{message}")
    _debug_logging = log_debug


def debug_logging():
    return _debug_logging
