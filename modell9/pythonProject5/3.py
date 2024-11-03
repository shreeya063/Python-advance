list_of_changes_speed = [30, 70, 50, -200]
# Car class defined.
class Car:
    def __init__(self, reg_no="Not selected", cur_spd=0,  max_spd=0, dist=0):
        self.reg_no = reg_no
        self.cur_spd = cur_spd
        self.max_spd = max_spd
        self.dist = dist

    def accelerate(self, change_of_speed):
        self.cur_spd = self.cur_spd + change_of_speed
        return self.cur_spd

    def drive(self, drive):     # here drive is the time of travel
        self.dist = self.dist + self.cur_spd*drive
        return self.dist

car = Car()

# checking preset info, set the current speed as 50 for example. Also max speed as 240
car = Car("ABC-123", 50, 240, 0)

print(f"\nVehicle Preset Info: Current speed = {car.cur_spd} km/h\n\nRegistration ID: {car.reg_no}\nCurrent Speed: {car.cur_spd} km/h\n"
      f"Max speed: {car.max_spd} km/h"
      )

# For loop for listing out the changes in speed of the car.
number_info = 0
for i in list_of_changes_speed:
    number_info = number_info + 1
    car.drive(1)
    car.accelerate(i)
     # time = distance/speed
    print(f"\n\nVehicle Status {number_info}:(The speed changes by {i} km/h)\n\nRegistration ID: {car.reg_no}\nCurrent Speed: {car.cur_spd} km/h\n"
          f"Max speed: {car.max_spd} km/h\nDistance: {car.dist} km"
          )