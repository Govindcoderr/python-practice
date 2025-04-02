class Employee:
    name = " "
    Email =" "

    def details(self):
        moblie_no =9819213466
        Address = "Ram-nivashi(company appartmant),new link road,Andheri"
        Employee_id = 1234
        print(f"Name is this  :{self.name}")
        print(f"moblie no is this :{moblie_no}")
        print(f"Address is this:{Address}")
        
        
       
class senior_employee(Employee):
    position = "hight"
    salery = "more than nomal employee"
    
    def senior_details(self):
        print("its higher position so we don't provide any details ! sorry sir !")


Rohit = Employee()
Rohit.name ="Rohit Sharma"
Rohit.Employee_id =4321
Rohit.Email ="govidxzx@gmail.com"


# print(Rohit.name,Rohit.Employee_id,Rohit.Email) 
Rohit.details()


virat=senior_employee()
virat.name="Virat koli"

virat.senior_details()
