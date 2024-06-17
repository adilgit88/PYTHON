
import qrcode

img = qrcode.make("https://www.instagram.com")
img.save("qr1.png", "PNG")

