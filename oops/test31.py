# encapsuation of the class

class tyres:
    def __init__(self,width,aspect_ratio,rim_width):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.rim_width = rim_width

    def __str__(self):
        return  str(self.width) + ' ' + str(self.aspect_ratio) + ' ' + str(self.rim_width)


class engine:
    def __init__(self,power,torque,fuel_consumption):
        self.power = power
        self.torque = torque
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return str(self.power) + ' ' + str(self.torque) + ' ' + str(self.fuel_consumption)


class body:
    def __init__(self,width,height,length):
        self.width = width
        self.height = height
        self.length = length

    def __str__(self):
        return str(self.width) + ' ' + str(self.height) + ' ' + str(self.length)


class car:
    def __init__(self,tyres,engine,body):
        self.tyres = tyres
        self.engine = engine
        self.body = body

    def __str__(self):
        return str(self.tyres) + '\n' + str(self.engine) + '\n' + str(self.body)


t = tyres(20,20,20)
e = engine(200,200,200)
b = body(200,200,200)
c = car(t,e,b)
print(c)