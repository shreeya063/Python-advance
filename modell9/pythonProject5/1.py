class Car:
    def __init__(self, reg_no="Not selected", cur_spd=0,  max_spd=0, dist=0):
        self.reg_no = reg_no
        self.cur_spd = cur_spd
        self.max_spd = max_spd
        self.dist = dist

# Checking the Default script
car = Car()

print(f"\nVehicle Info:\n\nRegistration ID: {car.reg_no}\nCurrent Speed: {car.cur_spd} km/h\nMax speed: {car.max_spd} km/h"
      f"\nCovered distance: {car.dist} km")

# Defining the values given from the question
car = Car("ABC-123", car.cur_spd, 142, car.dist)

print(f"\nVehicle Info:\n\nRegistration ID: {car.reg_no}\nCurrent Speed: {car.cur_spd} km/h\nMax speed: {car.max_spd} km/h"
      f"\nCovered distance: {car.dist} km")