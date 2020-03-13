# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


#### PRIMARY BASE CLASS ####

class Vehicle:
        pass

### FLIGHT VEHICLES BASE CLASS ###
class FlightVehicle(Vehicle):
    pass


### GROUND VEHICLES BASE CLASS ###
class GroundVehicle(Vehicle):
    pass



class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass

