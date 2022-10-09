# In this little assignment you are given a string of space separated numbers, 
# and have to return the highest and lowest number.

text = "1 4 5 77 9 0"

def highest_lowest_num(str1):
    num_list = list(map(int, str1.split()))
    return max(num_list), min(num_list)

print("Original string:", text)
print("Highest and lowest number of the said string:",highest_lowest_num(text))
text = "-1 -4 -5 -77 -9 0"
print("\nOriginal string:", text)
print("Highest and lowest number of the said string:",highest_lowest_num(text))
text = "0 0"
print("\nOriginal string:", text)
print("Highest and lowest number of the said string:",highest_lowest_num(text))

