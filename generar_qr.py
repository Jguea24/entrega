import qrcode

# URL de tu proyecto publicado en GitHub Pages
url = "https://jguea24.github.io/entrega/"

# Configuración del QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4
)

# Agregar la URL
qr.add_data(url)
qr.make(fit=True)

# Crear imagen
imagen = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Guardar
imagen.save("qr_fernanda.png")

print("====================================")
print("   🌻 QR GENERADO CORRECTAMENTE 🌻")
print("====================================")
print(f"URL: {url}")
print("Archivo: qr_fernanda.png")