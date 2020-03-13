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
    def __init__():
        pass

### FLIGHT VEHICLES BASE CLASS ###
class FlightVehicle(Vehicle):
    def __init__():
        super().__init__()


### GROUND VEHICLES BASE CLASS ###
class GroundVehicle(Vehicle):
    def __init__():
        super().__init__()



class Car(GroundVehicle):
    def __init__():
        super().__init__()


class Motorcycle(GroundVehicle):
    def __init__():
        super().__init__()


class Airplane(FlightVehicle):
    def __init__():
        super().__init__()


class Starship(FlightVehicle):
    def __init__():
        super().__init__()

