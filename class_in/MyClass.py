# -*- coding: UTF-8 -*-

class MyClass:
    """This is a simple class"""
    i = 12345
    def f(self):
        return 'hello world'


x = MyClass()

print('MyClass attribute i is : ', x.i)
print('MyClass method f is : ', x.f())
