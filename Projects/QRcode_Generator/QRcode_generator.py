import qrcode #This is module used to create QR codes

# This method creates a qrcode of this url
img = qrcode.make("https://youtu.be/vsWxs1tuwDk?si=xWFRiUMeYNCKpG-H")

# Saving the QR code in files to access it
img.save("winning_speech.jpg")


# These are the properties that can be applied to the QRcode like changing its colour, background or size
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('Some data') #This is the URL added in the property
qr.make(fit=True) #Creating that QRcode with respective property

img = qr.make_image(fill_color="black", back_color="red") #Saving that image by setting the back and front color
img.save("winget.png")

img.show()