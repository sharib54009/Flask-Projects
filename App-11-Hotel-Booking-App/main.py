import pandas as pd

df = pd.read_csv('hotels.csv', dtype = {'id' : str})
df_cards = pd.read_csv('cards.csv', dtype =str).to_dict(orient='records')


class Hotel:
    
    def __init__(self, Hotel_id):
        self.hotel_id = Hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'No'
        try:
            df.to_csv('hotels.csv', index=False)
            print("Hotel booked successfully!")
        except PermissionError:
            print("Cannot save the CSV file. Close Excel or check file permissions.")
        pass
    
    def available(self):
        """Checks is the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False            
        pass
    

class ReservationTicket:
    
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is you booking Data:
        Name = { self.customer_name }
        Hotel_name = {self.hotel.name}
        """
        return content
    
    
class CreditCard:
    def __init__(self, number):
        self.number = number
    
    
    def validate(self, expiration, cvv, holder):
        """Validates the credit card details"""
        cards_data = {"number": self.number, "expiration": expiration,  "cvv": cvv, "holder": holder}
        if cards_data in df_cards:
            return True
        else :
            return False
        
       
        
    
    
print(df)

Hotel_ID = input("Enter the hotel ID you want to book: ")
hotel = Hotel(Hotel_ID)
if hotel.available():
    
    credit_card = CreditCard(number="1234")
    if credit_card.validate( expiration="12/26", cvv="123",  holder="JOHN SMITH" ):
        hotel.book()
        name = input("Enter your name: ")
        Reservation_ticket = ReservationTicket(customer_name = name, hotel_object = hotel)
        print(Reservation_ticket.generate())
    else:
        print("Invalid credit card details. Booking failed.")
else:
    print("Sorry, the hotel is not available for booking.")
