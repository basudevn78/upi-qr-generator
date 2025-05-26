import qrcode
import tkinter as tk
from PIL import ImageTk

# Get UPI ID from user
upi_id = input("Enter your UPI ID: ")
upi_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

# Generate QR code
qr_img = qrcode.make(upi_url).convert("RGB")

# Setup Tkinter window
window = tk.Tk()
window.title("Scan to Pay")
window.geometry("300x350")
window.resizable(False, False)

# Bring window to front
window.lift()
window.attributes('-topmost', True)
window.after(1000, lambda: window.attributes('-topmost', False))  # Let it behave normally after showing

# Convert QR to Tkinter-compatible image
qr_img = qr_img.resize((250, 250))
qr_tk = ImageTk.PhotoImage(qr_img)

# Add label and QR image
label = tk.Label(window, text="Scan the QR to Pay", font=("Calibri Body", 14))
label.pack(pady=10)

qr_label = tk.Label(window, image=qr_tk)
qr_label.pack(pady=10)

# Run the window
window.mainloop()
