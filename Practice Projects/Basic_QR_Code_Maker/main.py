import qrcode
import qrcode.image.svg

"""
img = qrcode.make("Hello world! This is Skylan!")
img.save('code.png')
"""


qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=1)

qr.add_data("https://github.com/Skywreck99/Projects")
qr.make(fit=True)
img = qr.make_image(fill_color = "orange", back_color = "black")
img.save("advanced.png")

"""
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!", image_factory=factory)
svg_img.save("myqr.svg")
"""