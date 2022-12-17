def array_diff(a, b):
    #your code here
    for i in b:
        while i in a:
            a.remove(i)
    return a
    