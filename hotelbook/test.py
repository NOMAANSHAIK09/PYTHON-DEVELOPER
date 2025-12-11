import pandas as pd 

df = pd.read_csv("hotels1.csv",dtype={"id" : str})


# class user:
#     def view_hotels(self):
#         pass
class Hotel:
    def __init__(self ,hotel_id):
        self.hotel_id = hotel_id
        

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels1.csv",index=False) 
        

    def available(self):
        result = df.loc[df["id"] == self.hotel_id, "available"]

        if result.empty:
            return False  # No such hotel ID

        availability = result.iloc[0]   # always a single value

        return availability == "yes"
        

class reservationtic:
    def __init__(self,cust_name,hotel_obj):
        pass

    def generate(self):
        #content = f"names of the customer hotel"
        pass

print(df)
hotel_ID=input("enter id of hotel:")
hotel = Hotel(hotel_ID)


if hotel.available():
    hotel.book()
    name = input("enter your name:")
    reservation_ticket=reservationtic(name,hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not ffree")
