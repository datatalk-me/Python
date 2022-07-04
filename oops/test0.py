class car:
    def __init__(self,milage,year,make,model):
        self.milage=milage
        self.year=year
        self.make=make
        self.model=model

    def age(self,current_year):
        return current_year-self.year

    def mileage_in_km(self):
        return self.milage*1.60934


    def __str__(self):
        return "This is a {} {} {} {}".format(self.year,self.make,self.model,self.milage)



nano = car(10,2020,"TATA","nano")

audi = car(20,2020,"TATA","audi")

print(nano)
print(audi)


print(nano.age(2022))

print(nano.mileage_in_km())


print(nano)