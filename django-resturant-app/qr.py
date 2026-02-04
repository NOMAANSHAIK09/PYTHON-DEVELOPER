import qrcode

img=qrcode.make('https://127.0.0.1:8000')
img.save('restaurant_qr.png')