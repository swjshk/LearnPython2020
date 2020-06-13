# Pyhton Object-Oriented Programming

class Employee():
    
    raise_amount = 1.04 #class variable; stored in class not the instance;
                        # python first check if instance has a instance var with that name. If not it check the class var

    def __init__(self,first,last,pay): #self is always the first argument; init is a function
        self.first = first #instance variable
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@SE.com'

    def fullname(self): #self is always there; fullname is a function
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #self is the instance created;  

emp_1 = Employee('Max', 'Sang', 50000) # constructor init will run automatically  
emp_3 = Employee('Xin', 'Zhang', 60000)

print(emp_1.email) # init
print(emp_3.email)

print(emp_1.fullname()) # function
print(emp_3.fullname())

print(emp_1.__dict__) # instance dict doesn't contain the class var raise_amount
print(Employee.__dict__) #dict for a class


# emp_1.fullname()   #emp_1 is the instance
# Employee.fullname(emp_1)  # same as above this is how python run in the background emp_1 = self
 

# emp_1 = Employee()
# emp_3 = Employee()

# print(emp_1) #<__main__.Employee object at 0x1059861d0>
# print(emp_3) #<__main__.Employee object at 0x105986198>


#instance data 
# emp_1.first = 'Max'
# emp_1.last = 'sang'

#class data

