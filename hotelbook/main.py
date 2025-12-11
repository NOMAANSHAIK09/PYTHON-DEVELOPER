import pandas as pd 

df = pd.read_csv("hotels1.csv",dtype={"id" : str})
df_cards=pd.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_cards_security=pd.read_csv("card_security.csv",dtype=str)

# class user:
#     def view_hotels(self):
#         pass
class Hotel:
    def __init__(self ,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv",index = False) 
        

    def available(self):
        result = df.loc[df["id"] == self.hotel_id, "available"]

        if result.empty:
            return False  # No such hotel ID

        availability = result.iloc[0]   # always a single value

        return availability == "yes"
        

class reservationtic:
    def __init__(self,cust_name,hotel_obj):
        self.cust_name = cust_name
        self.hotel = hotel_obj

    def generate(self):
        content=f"""than you for reservation 
        name : {self.cust_name} 
        hotel name : {self.hotel.name}"""
        return content


class CreditCard:
    def __init__(self,number):
        self.number = number
    def validate(self,expiration,holder,cvc):
        card_data = {"number":self.number, "expiration":expiration,"holder":holder,"cvc":cvc}

        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        
        if password == given_password:
            return True
        else:
            print("wrong password")
            return False
        
class SpaHotel(Hotel):
    def book_spa_package(self):
        pass



class SpaTicket:
    def __init__(self, cust_name, hotel_obj):
        self.cust_name = cust_name
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name: {self.cust_name}
        Hotel name: {self.hotel.name}
        """
        return content


        
print(df)
hotel_ID=input("enter id of hotel:")
hotel = Hotel(hotel_ID)
hotel = SpaHotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26",holder="JOHN SMITH",cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("enter your name:")
            reservation_ticket=reservationtic(name,hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a spa package?(yes or no) ")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(cust_name=name, hotel_obj=hotel)
                print(spa_ticket.generate())
            print("done payment")
        else:
            print("authentication filed")
else:
    print("Hotel is not ffree")
