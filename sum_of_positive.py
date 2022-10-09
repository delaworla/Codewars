# You get an array of numbers, return the sum of all of the positives ones.


def positive_sum(arr):
    return sum(item for item in arr if item > 0)