import qrcode

image = qrcode.make("http://idaxdigital.com")
image.save("idax_qrcode.png")
