class Vehicle:
    def getdetails(self):
        self.make=input("Enter vehicle Brand name:")
        self.year=int(input("Enter manufacture year"))
        self.colour=input("Enter model colour:")
    def display_info(self):
        print("Brand Name:",self.make,"\nManufacture Year:",self.year,"\nColour:",self.colour)
class Car(Vehicle):
    def getcardetails(self):
        print("Enter car detail...")
        super().getdetails()
        self.model=input("Enter car model name:")
        self.capacity=input("Enter capacity:")
    def display_car(self):
        print("\n\t---CAR DETAILS---")
        super().display_info()
        print("\nModel:",self.model)
        print("\nCar Capacity:",self.capacity)
class Bike(Vehicle):
    def getbikedetails(self):
        print("Enter bike detail...")
        super().getdetails()
        self.type=input("Enter bike type:")
        self.mile=input("Enter bike mileage:")
    def display_bike(self):
        print("\n\t---BIKE DETAILS---")
        super().display_info()
        print("Bike Type:",self.type)
        print("Mileage per hour :",self.mile)
v1=Car()
v2=Bike()
v1.getcardetails()
v2.getbikedetails()
print("\n\t---VEHICLE DETAILS---")
v1.display_info()
v2.display_bike()
