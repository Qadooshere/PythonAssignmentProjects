import qrcode
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from qrcode.main import QRCode


def gen_qrcode(employee_code, name):
    try:
        qr = qrcode.QRCode(box_size=20)

        qr.add_data(employee_code)
        img = qr.make_image()
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("qrfont.ttf", 30)

        draw.text((300, 520), employee_code, font=font)
        draw.text((300, 550), name, font=font)
        img.save("testing.png")
        return (True, employee_code)
    except Exception:
        raise Exception("Error occured in gen_qrcode func in genqr.py")