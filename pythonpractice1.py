'''class dog():

    #class atribute
    attr="mammel"

    #instance atribute or objects atributes
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour


#object instantiation or object creation
rodger=dog("roddger","ehite")
tommy=dog("tommy","black")

#acessing the class atribute
print("roddger is a {}".format(rodger.__class__.attr))
print("tommy is a {}".format(tommy.__class__.attr))

#acessing the instance atribute or ibject atribute
print("my name is {} ".format(rodger.name))
print("my colour is {} ".format(rodger.colour))

print("my name is {} ".format(tommy.name))
print("my colour is {} ".format(tommy.colour))


#creating class and object with methods

class vechicle():

    class_atribute="bike"

    #constructing class atributes
    def __init__(self,name,model,cc,price):
        self.name=name
        self.model=model
        self.cc=cc
        self.price=price

    #creating class methods

    def specifications(self):
        print("{} unicorn maximmun speed is ".format(self.cc))
        print("bike name is {} ".format(self.name))
        print("bike model is {} ".format(self.model))
        print("bike price is {} ".format(self.price))


#creating objects
bike1=vechicle("unicorn","2022","160","135000\-")

#object calling through its method
bike1.specifications()
print(bike1.name)'''

#inheritance

class person():

    #instances atribute or object atribute
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("person name is ",self.name)
        print("person age is ",self.age)

    def americans(self):
        print("person name is ",self.name)
        print("person age is ",self.age)

person1=person("narayana",27)
person1.display()
print(person1.name)

class employee(person):

    def __init__(self,name,age,id,location):
        self.id=id
        self.location=location
        person.__init__(self,name,age)

    def display(self):
        print("employee name is ",self.name)
        print("employee age is ",self.age)
        print("employee id is ",self.id)
        print("employee location is ",self.location)

    def americans(self):
        print("american(canadians) name",self.name)
        print("american age is ",self.age)
        print("american location is ",self.location)
        print("american id is ",self.id)
#types of calling objects

#object.methodname()
#print(classname.methodname(object))
#print(object.__dict__) to print information in dictonary

american=employee("alex",age=27,location="canada",id=567) #example of key word arguments
person2=person("venkatesh",28)
employee1=employee("rajesh",28,789,"yuusafguda")
person2.display() #obj.methodname
employee1.display()

print("obj calling by class name")
print(person.display(person1))
print("employee1 info")
print(employee.display(employee1))

print(person1.__dict__)
print(person2.__dict__)
print(employee1.__dict__)
print(person1.display())
american.display()


































