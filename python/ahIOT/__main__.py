try:
    import pretty_traceback
    pretty_traceback.install()
except ImportError:
    pass    # no need to fail because of missing dev dependency