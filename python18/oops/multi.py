class papa:
    property1 = "Home" 
    parents_name ="Son of Sharma ji"
   
class mummy :
   behavior = "Nature"
   cooking_style ="Recipe:- south indian"

class Son(papa,mummy):
    def inherit(self):
        name = "Virat"
        print(f" My name:{name} {self.parents_name}")
        print(f"parents property:{self.property1}")
        print(f" behavior:{self.behavior}")
        print(f" cooking_style:{self.cooking_style}")


virat = Son()

virat.inherit()