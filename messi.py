import tkinter as tk
from sketchpy import canvas

# Crear ventana Tkinter principal
root = tk.Tk()
root.withdraw()

# Crear objecto de clase canvas.sketch
Messi = canvas.sketch(x_offset=290, y_offset=320)

# Dibujar a Messi
Messi.draw_fn("Resources/background1", co=(116,172,223), mode=0)
Messi.draw_fn("Resources/background2", co=(255, 255, 255), mode=0)
Messi.draw_fn("Resources/background3", co=(116,172,223), mode=0)

Messi.draw_fn("Resources/face_out", co=(233, 183, 151), mode=0)
Messi.draw_fn("Resources/beard_out", co=(30, 25, 31), mode=0)

Messi.draw_fn("Resources/chin1", co=(204, 139, 124), mode=0)
Messi.draw_fn("Resources/chin2", co=(204, 139, 124), mode=0)

Messi.draw_fn("Resources/lip_lower", co=(214, 125, 100), mode=0)
Messi.draw_fn("Resources/lip_upper", co=(186, 30, 21), mode=0)

Messi.draw_fn("Resources/nostril", co=(8, 15, 29), mode=0)
Messi.draw_fn("Resources/nose_curve", co=(128, 69, 56), mode=0)
Messi.draw_fn("Resources/right_eyebrow", co=(12, 16, 22), mode=0)
Messi.draw_fn("Resources/left_eyebrow", co=(12, 16, 22), mode=0)

Messi.draw_fn("Resources/noseline", co=(12, 16, 22), mode=0)

Messi.draw_fn("Resources/eyelid", co=(13, 15, 23), mode=0)
Messi.draw_fn("Resources/eye", co=(17, 12, 20), mode=0)
Messi.draw_fn("Resources/sclera", co=(230, 231, 229), mode=0)
Messi.draw_fn("Resources/eyeball", co=(15, 25, 15), mode=0)
Messi.draw_fn("Resources/eyeball_centre", co=(230, 231, 229), mode=0)

Messi.draw_fn("Resources/hair_outline", co=(12, 16, 25), mode=0)
Messi.draw_fn("Resources/hair_shade1", co=(12, 16, 25), mode=0)
Messi.draw_fn("Resources/hair_shade2", co=(61, 44, 52), mode=0)
Messi.draw_fn("Resources/hair_shade3", co=(119, 64, 75), mode=0)
Messi.draw_fn("Resources/hair_shade4", co=(119, 64, 75), mode=0)
Messi.draw_fn("Resources/hair_shade5", co=(61, 44, 52), mode=0)
Messi.draw_fn("Resources/hair_shade6", co=(119, 64, 75), mode=0)
Messi.draw_fn("Resources/hair_shade7", co=(61, 44, 52), mode=0)
Messi.draw_fn("Resources/hair_shade8", co=(61, 44, 52), mode=0)

Messi.draw_fn("Resources/throat", co=(245, 207, 171), mode=0)
Messi.draw_fn("Resources/throat_shade1", co=(236, 180, 153), mode=0)
Messi.draw_fn("Resources/throat_shade2", co=(236, 180, 153), mode=0)

Messi.draw_fn("Resources/ear_line1", co=(16, 10, 8), mode=0)
Messi.draw_fn("Resources/ear_line2", co=(16, 10, 8), mode=0)
Messi.draw_fn("Resources/ear_line3", co=(16, 10, 8), mode=0)
Messi.draw_fn("Resources/ear_shade1", co=(212, 138, 124), mode=0)
Messi.draw_fn("Resources/ear_shade2", co=(212, 138, 124), mode=0)
Messi.draw_fn("Resources/ear_shade3", co=(212, 134, 122), mode=0)

Messi.draw_fn("Resources/beard_shade1", co=(124, 77, 75), mode=0)
Messi.draw_fn("Resources/beard_shade2", co=(127, 76, 76), mode=0)

Messi.draw_fn("Resources/face_shade1", co=(209, 137, 122), mode=0)
Messi.draw_fn("Resources/face_shade2", co=(208, 138, 119), mode=0)

Messi.draw_fn("Resources/eye_shade1", co=(209, 143, 126), mode=0)
Messi.draw_fn("Resources/eye_shade2", co=(209, 143, 126), mode=0)

Messi.draw_fn("Resources/face_shade3", co=(245, 207, 171), mode=0)
Messi.draw_fn("Resources/face_shade4", co=(240, 208, 169), mode=0)

Messi.draw_fn("Resources/forhead_shade1", co=(202, 135, 119), mode=0)

Messi.draw_fn("Resources/tshirt", co=(255, 255, 255), mode=0)
Messi.draw_fn("Resources/tshirt_color1", co=(116,172,223), mode=0)
Messi.draw_fn("Resources/tshirt_color2", co=(255, 255, 255), mode=0)
Messi.draw_fn("Resources/tshirt_color3", co=(0, 0, 0), mode=0)

# Mantener la ventana abierta
root.mainloop()