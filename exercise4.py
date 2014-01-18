cars=50
drivers=20
cars_not_driven=cars-drivers
space_in_a_car=4
passengers=80
cars_driven=drivers
car_pool_capacity=drivers*space_in_a_car
avg_passengers_per_car=passengers/cars_driven
print "there are",cars,"cars available"
print "there are only",drivers,"drivers available"
print "there will be",cars_not_driven,"empty cars today"
print "we can transport",car_pool_capacity,"people today"
print "we have",passengers,"people to carpool today"
print "we need 2 put",avg_passengers_per_car,"in each car"