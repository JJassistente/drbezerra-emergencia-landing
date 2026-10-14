import qrcode

url = "https://drbezerraemergencia.jjassistentebot.tech"
print("QR target:", url)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#1c2b47", back_color="white")
out = r"C:\Users\Usuário\drbezerra-emergencia-landing\img\qrcode-bsltech.png"
img.save(out)
print("saved:", out, img.size)
