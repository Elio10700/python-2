# zip function

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

s2 = list(zip(a, b))
print(s2)

# reverse zipping
s1 = (10, 20, 30)
s2 = (100, 200, 300)

s3 = zip(s1, s2[::-1])
print(list(s3))

stock = ['infosys', 'tcs', 'reliance']
price = [234, 678, 982]

dic1 = {stocks: prices for stocks, prices in zip(stock, price)}
print(dic1)
