from c2 import C2
class C1:
    def __init__(self,objacked_value):
        self.objacked_value=objacked_value
    def updater(self):
        self.objacked_value += 1*C2(self.objacked_value).updater2()
        print("yoyo",self.objacked_value)
#        return(self.objacked_value)
