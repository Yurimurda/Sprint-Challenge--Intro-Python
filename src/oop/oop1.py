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

# Base Class
class Vehicle:
    def __init__(self, Vehicle):
        self.Vehicle = Vehicle
    
    def VehicleCheck(self):
        print("I am a Vehicle")
        
# Ground Classes
class GroundVehicle(Vehicle):
    def __init__(self, Vehicle):
        self.Vehicle = GroundVehicle
        pass

class Car(GroundVehicle):
    def __init__(self, GroundVehicle):
        self.GroundVehicle = Car
        pass

class MotorCycle(GroundVehicle):
    def __init__(self, GroundVehicle):
        self.GroundVehicle = MotorCycle
        pass


# Air Classes

class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    def __init__(self, FlightVehicle):
        self.FlightVehicle = Airplane
        pass

class StarShip(FlightVehicle):
    def __init__(self, FlightVehicle):
        self.FlightVehicle = StarShip
        pass

