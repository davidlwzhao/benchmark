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

