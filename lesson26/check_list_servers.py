def summ_all(*args):
    print(args)
    result=0
    for i in args:
        result += i
    return result

print(summ_all(10, 20))