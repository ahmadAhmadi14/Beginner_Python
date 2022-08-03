class A:
    def show(self):
        print('this is class A')

class B:
    def show(self):
        print('this is class B')

class C(A,B):
    def show(self):
        print('this is class c')

object = C()
object.show() #print out is this is class C
#method resolution order// multiple inheritance
# use help to check method resolution order
# help(object)