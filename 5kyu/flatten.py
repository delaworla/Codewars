# For this exercise you will create a global flatten method. The method takes in any number of arguments and flattens them into a single array. 
# If any of the arguments passed in are an array then the individual objects within the array will be flattened so that they exist at the same 
# level as the other arguments. Any nested arrays, no matter how deep, should be flattened into the single array result.

# The following are examples of how this function would be used and what the expected results would be:

# flatten(1, [2, 3], 4, 5, [6, [7]]) # returns [1, 2, 3, 4, 5, 6, 7]
# flatten('a', ['b', 2], 3, None, [[4], ['c']]) # returns ['a', 'b', 2, 3, None, 4, 'c']


def flatten(*args):
    flattened = []
    
    for arg in args:
        if type(arg) == list:
            flattened.extend(flatten(*arg))
        else:
            flattened.append(arg)
        
    return flattened


def flatten(*args):
    flattenedArray =[]

    for arg in args:
        if type(arg) == list:
            flattenedArray.extend(flatten(*args))
        else:
            flattenedArray.append(arg)
    return flattenedArray