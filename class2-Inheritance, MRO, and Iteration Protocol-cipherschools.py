# class a:
#     x=5
# class b(a):
#     pass
# class c(b):
#     x=7
# class d(c):
#     x=10
#     y=12
# obj= d()
# print(obj.x)
# print(obj.y)
a= range(5)
it= a.__iter__()
# print(it)
print(it.__next__())


