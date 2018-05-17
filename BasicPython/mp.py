# Monkey patch

class MyClass:
    def f(self):
        print("f()")

import mp
def monkey_f(self):
    print("monkey_f()")


mp.MyClass.f = monkey_f
obj = mp.MyClass()
obj.f()
