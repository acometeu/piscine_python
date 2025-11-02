from math import isnan

def NULL_not_found(object: any) -> int:
    if (object == None):
        print(f"Nothing: None {type(object)}")
    elif (type(object) == float and isnan(object) == True):
        print(f"Cheese: nan {type(object)}")
    elif (type(object) == int and object == 0):
        print(f"Zero: 0 {type(object)}")
    elif (type(object) == str and object == ""):
        print(f"Empty: {type(object)}")
    elif (type(object) == bool and object == False):
        print(f"Fake: False {type(object)}")
    else:
        print("Type not Found")
        return (1)
    return (0)