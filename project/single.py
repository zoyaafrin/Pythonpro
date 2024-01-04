class base:
    a=10
    b=20
    def _init_(self,c):
        self.c=c
class derived(base):
    def _init_(self,c,d,e):
        super()._init_(c)
        self.e=e
        self.d=d
obj=derived(5,56,57)        