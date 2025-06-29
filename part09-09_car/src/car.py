class Car:
    def __init__(self):
        self.__amout_of_petrol: int = 0
        self.__odometer: int = 0

    def fill_up(self):
        self.__amout_of_petrol = 60
        
    def drive(self, km: int):
        if self.__amout_of_petrol > km:
            self.__odometer += km
            self.__amout_of_petrol -= km
        else:
            self.__odometer += self.__amout_of_petrol
            self.__amout_of_petrol = 0
    
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amout_of_petrol} litres"

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)