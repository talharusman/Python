from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, rental_price):
        self._make = make
        self._model = model
        self._rental_price = rental_price
        self._availability = True

    @abstractmethod
    def display_details(self):
        pass

    def check_availability(self):
        return self._availability

    def calculate_rental_cost(self, days):
        return self._rental_price * days

    def rent(self):
        if self._availability:
            self._availability = False
        else:
            raise Exception("Vehicle is already rented.")

    def return_vehicle(self):
        self._availability = True

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def rental_price(self):
        return self._rental_price

    @property
    def availability(self):
        return self._availability


class Car(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        return f"Car: {self.make} {self.model}, Rental Price: ${self.rental_price:.2f}, Available: {'Yes' if self.availability else 'No'}"


class SUV(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        return f"SUV: {self.make} {self.model}, Rental Price: ${self.rental_price:.2f}, Available: {'Yes' if self.availability else 'No'}"


class Truck(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        return f"Truck: {self.make} {self.model}, Rental Price: ${self.rental_price:.2f}, Available: {'Yes' if self.availability else 'No'}"


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self._customer = customer
        self._vehicle = vehicle
        self._start_date = start_date
        self._end_date = end_date

    def display_details(self):
        return f"Rental Reservation: {self._customer.name} rented {self._vehicle.display_details()} from {self._start_date} to {self._end_date}"

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def customer(self):
        return self._customer


class Customer:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._rental_history = []

    @property
    def name(self):
        return self._name

    @property
    def contact_info(self):
        return self._contact_info

    def display_rental_history(self):
        if not self._rental_history:
            print("No rental history available.")
        else:
            for reservation in self._rental_history:
                print(reservation.display_details())

    def add_rental_reservation(self, reservation):
        self._rental_history.append(reservation)


def display_details(obj):
    if isinstance(obj, Vehicle):
        print(obj.display_details())
    elif isinstance(obj, RentalReservation):
        print(obj.display_details())
    else:
        raise ValueError("Invalid object type")


class RentalService:
    def __init__(self):
        self._available_vehicles = []
        self._customers = []


    def add_vehicle(self, vehicle):
        self._available_vehicles.append(vehicle)

    def add_customer(self, customer):
        self._customers.append(customer)

    def find_vehicle(self, make, model):
        for vehicle in self._available_vehicles:
            if vehicle.make == make and vehicle.model == model and vehicle.check_availability():
                return vehicle
        return None


    def rent_vehicle(self, customer, make, model, start_date, end_date):
        vehicle = self.find_vehicle(make, model)
        if vehicle:
            vehicle.rent()
            reservation = RentalReservation(customer, vehicle, start_date, end_date)
            customer.add_rental_reservation(reservation)
            print(f"Vehicle rented successfully: {vehicle.display_details()}")
        else:
            print("Vehicle not available")

    def return_vehicle(self, customer, make, model):
        for reservation in customer._rental_history:

            if reservation.vehicle.make == make and reservation.vehicle.model == model:
                reservation.vehicle.return_vehicle()
                print(f"Vehicle returned successfully: {reservation.vehicle.display_details()}")
                return
            
        print("No matching rental found")

    def display_all_vehicles(self):
        for vehicle in self._available_vehicles:
            display_details(vehicle)

    def display_all_customers(self):
        for customer in self._customers:
            print(f"Customer: {customer.name}, Contact: {customer.contact_info}")

            customer.display_rental_history()


car = Car("Toyota", "Corolla", 50)
suv = SUV("Honda", "CR-V", 75)
truck = Truck("Ford", "F-150", 100)

customer = Customer("Talha Rusman", "123-456-7890")

service = RentalService()
service.add_vehicle(car)
service.add_vehicle(suv)

service.add_vehicle(truck)
service.add_customer(customer)

service.rent_vehicle(customer, "Toyota", "Corolla", "2024-09-29", "2024-10-02")
service.display_all_vehicles()


service.return_vehicle(customer, "Toyota", "Corolla")
service.display_all_vehicles()
