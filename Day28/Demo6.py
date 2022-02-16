#Encapsulation -- Binding data with function - behaves like a single entity--
# class--- Declaration
#initialization
#untilization

class Baby:

    def __init__(self,new_name):
        self.name=new_name              #initialization

    def print_name(self):
        print(self.name)                #utilization


baby1=Baby("Arun")
baby1.print_name()

baby2=Baby("Akshara")
baby2.print_name()
