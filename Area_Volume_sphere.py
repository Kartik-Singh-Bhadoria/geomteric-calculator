from tkinter import*
from math import pi
root = Tk()
root.geometry("800x800")
root.configure(background="#363636")

area_label = Label(root, font=("Arial", 14), fg = "white", bg ="#363636")
area_label.place(x = 360, y= 240)

volume_label = Label(root, font=("Arial", 14), fg = "white", bg ="#363636")
volume_label.place(x = 360, y= 290)

def area_sphere(event = None):
    try:
        r = float(e.get())
        print(r)
        area = 4*pi*(r**2)
        volume = (4.0/3.0)*pi*r**3
        #area_label = Label(root, text = f"Area of the sphere is {area:.3f}", font=("Arial", 14), fg = "white", bg ="#363636")
        #area_label.place(x = 360, y= 240)
        area_label.config(text = f"Area of the sphere is {area:.3f}")
        volume_label.config(text = f"Volume of the sphere is {volume:.3f}")
        e.delete(0,END)

    except ValueError:
        print("ValueError")
        area_label.config(text="❌ Please enter a valid radius")
        volume_label.config(text ="")



c = Canvas(root, height=160,width=160,background="#363636", highlightbackground="#363636")
c.place(x=100,y=100)
sphere = c.create_oval(10, 10, 150, 150, outline="white", width=2)
circle = c.create_oval(150,90,10,70,outline="white")

radius_label = Label(root,text = "Enter the radius of sphere",font=("Arial", 14),fg ="White", bg = "#363636")
radius_label.place(x=360,y=100)
e = Entry(root, width= 50, bg="#363636", fg ="white")
e.place(x=360, y = 140)
e.bind("<Return>",area_sphere)


root.mainloop()