list1 = [23, 45, 67, 89]
list2 = [2, 3, 56, 66]

res = map(lambda x, y: x + y, list1, list2)
print(list(res))

def square(x):
    return x * x

a = [2, 7, 89, 45]

res = map(square, a)
print("The square is:")
print(list(res))
