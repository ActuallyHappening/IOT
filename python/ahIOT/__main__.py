try:
    import pretty_traceback
    pretty_traceback.install()
    print("Pretty traceback installed")
except ImportError:
    print("(Warning: pretty_traceback not installed)")
    pass    # no need to fail because of missing dev dependency