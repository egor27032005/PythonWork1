import time


def getTime():
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%m.%d,%H:%M:%S", named_tuple)
    return time_string

