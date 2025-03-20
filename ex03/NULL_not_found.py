import math


def NULL_not_found(object: any) -> int:
    if object is None:
        print(f'Nothing: {object} {type(object)}')
        return 0
    elif isinstance(object, bool) and not object:
        print(f'Fake: {object} {type(object)}')
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(f'Cheese: {object} {type(object)}')
        return 0
    elif isinstance(object, int) and object == 0:
        print(f'Zero: {object} {type(object)}')
        return 0
    elif isinstance(object, str) and not object:
        print(f'Empty: {object} {type(object)}')
        return 0
    else:
        print('Type not Found')
        return 1
