__version__ = "0.25.1.post1"
init_error = None

def _print2stderr(msg):
    sys.stderr.write(msg + '\n')

try:
    from .skycoin import *
except (AttributeError, ImportError) as _err :
    init_error = _err

    import sys, traceback
    _print2stderr("Error initializing skycoin package. Details:")
    traceback.print_exception(*sys.exc_info())
    _print2stderr("\n\nInport succeeded but package load failed")

