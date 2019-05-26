__all__ = ['search1', 'search2', 'search3', 'search_inputs']


from string import ascii_letters


def search1(arr, target):
    for element in arr:
        if element == target:
            return True
    return False


def search2(arr, target):
    unique = set(arr)
    size = len(unique)
    unique.add(target)
    if len(unique) > size:
        return True
    return False


def search3(arr, target):
    return target in arr


test_arr = ascii_letters*944 + '3' + ascii_letters*56
test_target = '3'
search_inputs = (test_arr, test_target)