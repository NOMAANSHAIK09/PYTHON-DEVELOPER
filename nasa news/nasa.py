import streamlit as st 
import requests



st.title("Today's News")


api_key="OzWlGNaY5pJLXqA5bXqUnn3m0uGmZiNUvNypceqh"
url= "https://api.nasa.gov/planetary/apod?"\
    f"api_key={api_key}"

response1=requests.get(url)
data = response1.json() 

tittle = data["title"]
image_url=data["url"]
explanation=data["explanation"]

st.header(tittle)
filepath = "img.png"
response2 = requests.get(image_url)
with open(filepath,"wb") as file:
    file.write(response2.content)
st.image(filepath)
st.write(explanation)

# url_image = "https://apod.nasa.gov/apod/image/2510/WitchBroom_Meyers_1080.jpg"


# st.image(url_image)
# response = requests.get(url)
# data = response.json()

# #tittle = data["title"]
# explanation = data["explanation"]

# #st.title(tittle)
# st.write(explanation)


# response = requests.get(url_image)

# im = response.content(url_image)

# with open("imange.jpg","wb") as file:
#     file.write(im)