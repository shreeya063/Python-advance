class Car:
    def __init__(self, reg_no="Not selected", cur_spd=0, max_spd=0, dist=0):
        self.reg_no = reg_no
        self.max_spd = max_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def accelerate(self, change_of_speed):
        self.cur_spd = self.cur_spd + change_of_speed
        if self.cur_spd >= self.max_spd:
            self.cur_spd = self.max_spd
        elif self.cur_spd <= 0:
            self.cur_spd = 0
        return self.cur_spd

    def drive(self, drive):   # here drive is the time of travel
        self.dist = self.dist + self.cur_spd*drive
        return self.dist


class ElectricCar(Car):
    def __init__(self, reg_no, max_spd, capacity):
        self.capacity = capacity
        super().__init__(reg_no, max_spd)

    def type_of_car_drive(self):
        print(f"\nRegistration: {self.reg_no}, Speed: {self.cur_spd} km/h, Capacity: {self.capacity} kWh, Type-Electric")


class GasolineCar(Car):
    def __init__(self, reg_no, max_spd, volume):
        self.volume = volume
        super().__init__(reg_no, max_spd)

    def type_of_car_drive(self):
        print(f"\nRegistration: {self.reg_no}, Speed: {self.cur_spd} km/h, Capacity: {self.volume}L, Type-Gasoline")


# Main Program
cars = []

tesla = ElectricCar("ABC-15", 180, 52.5)
BMW_m8 = GasolineCar("ACD-123", 165, 32.3)

# appending cars
cars.append(tesla)
cars.append(BMW_m8)

# Distance count
hours = 3
for car in cars:
    car.type_of_car_drive()
    car.drive(hours)
    print(f"Distance travelled in {hours} hours: {car.dist} km")
    pass
