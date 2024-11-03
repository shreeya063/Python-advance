import random

# Car class defined.
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

# Main Program

car_list = []

# Adding car objects in a list using a for loop
total_cars_in_game = 10
for i in range(total_cars_in_game):
    max_spd = random.randint(100, 200)
    reg_no = "ABC-"+str(i+1)
    car_list.append(Car(reg_no, max_spd=max_spd))

# listing out the game conditions, race finishes when race_over condition remains "True".
total_dist_to_cover = 10000
race_over = False
while not race_over:
    for car in car_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.dist >= total_dist_to_cover:
            race_over = True
            print(f"\nThe Car with Registration no. = {car.reg_no}, Distance = {car.dist} km won the race!\n")


for car in car_list:
    print(f"Registration no. = {car.reg_no}, Distance = {car.dist} km")
    # Here in the for loop the car with maximum distance ex. 10,000km+ is the 1st place

print(f"\nRace Finished!")
