import pandas as pd

df = pd.read_csv('hotels.csv')

class Hotel:
    
    def __init__(self, id):
        pass
    
    def book(self):
        pass
    
    def available(self):
        pass
    

class ReservationTicket:
    
    def __init__(self, name, hotel):
        pass
    
    def generate(self):
        pass
    
    
print(df)

id = input("Enter the hotel ID you want to book: ")
hotel = Hotel(id)
if hotel.available:
    hotel.book()
    name = input("Enter your name: ")
    
    Reservation_ticket = ReservationTicket(name, hotel)
    Reservation_ticket.generate()
else:
    print("Sorry, the hotel is not available for booking.")
