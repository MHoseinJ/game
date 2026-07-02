from enum import Enum

class Type(Enum):

    WARN = "warn"
    ERROR = "error"
    INFO = "info"

def print_suffix(type: Type):

    match type:
        case Type.ERROR.value:
            print("\33[41m[ERROR]: \033[0m")
        case Type.WARN.value:
            print("\33[43m[WARN]: \033[0m")
        case Type.INFO.value:
            print("\33[100m[INFO]: \033[0m")
        case default:
            print("")

def log(type: Type, msg: str):
    print_suffix(type)
    print(msg)
