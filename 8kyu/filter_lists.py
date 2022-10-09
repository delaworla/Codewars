l = ([123, 'sam', 322, 'for'])

def filter_list(l):
    new_list = []
    for i in l:
        if type(i) !=  str:
            new_list.append(i)
    print( new_list)
    print(l)