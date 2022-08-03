constants = {}
constants["machine"] = {
    "BUILTIN": 2,
    "TEST_BUILTIN": 2,
    "TEST_RED": 13,
    "TEST_YELLOW": 12,
    "TEST_GREEN": 14,
    "TEST_BLUE": 27
}


def _dict_add(d1, d2):
    tmp = d1.copy()
    tmp.update(d2)
    return tmp
