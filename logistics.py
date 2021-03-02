'''
This module creates a simple logistic system.
'''
import random


class Location:  # pylint: disable=too-few-public-methods
    '''
    Class that creates the address (city and postoffice of Ukrposhta).
    '''

    def __init__(self, city: str, postoffice: int):

        self.city = city
        self.postoffice = postoffice


class Item:  # pylint: disable=too-few-public-methods
    '''
    Class which describes the product which is to be delivered.
    '''

    def __init__(self, name: str, price: float):

        self.name = name
        self.price = price

    def __str__(self):

        return f"Name of the product:{self.name}, its price:{self.price}"


class Vehicle:  # pylint: disable=too-few-public-methods
    '''
    Displays the vehicle by which the delivery will be made.
    '''

    def __init__(self, vehicleNo: int):

        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:  # pylint: disable=too-few-public-methods
    '''
    Contains all information about the order and the user.
    '''

    def __init__(self, user_name: str, city: str, postoffice: str,
                 items: list):

        self.orderId = random.randint(100000000, 199999999)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.city = city
        self.postoffice = postoffice

    def __str__(self):

        return f"Your order number is {self.orderId}"

    def calculateAmount(self):
        '''
        Calculate total sum of all user's orders.
        '''
        total = 0
        for item in self.items:
            total += item.price
        return total

    def assignVehicle(self, vehicle: Vehicle):
        '''
        Returns True or False whether the vehicle is available at the moment.
        '''
        return vehicle.isAvailable


class LogisticSystem:  # pylint: disable=too-few-public-methods
    '''
    The main class, which stores all information about users, \
    orders and transportation
    '''

    def __init__(self, vehicles):

        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        '''
        Places order to the order list, depending on whether there is an \
        available vehicle or not.
        '''
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                self.orders.append(order)
                vehicle.isAvailable = False
            return "There is no available vehicle to deliver an order."

    def trackOrder(self, orderId: int):
        '''
        Returns information about the order.
        '''
        for order in self.orders:
            if orderId == order.orderId:
                return f"Your order #{orderId} is sent to {order.city}. \
Total price: {order.calculateAmount()} UAN"
            return "No such order"
