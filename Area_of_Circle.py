from tkinter import*

root = Tk()
root.geometry("800x800")
root.configure(bg = "#363636")

c = Canvas(root, height=150,width=150, background ="#363636", highlightbackground="#363636")
c.place(x=100,y=100)

area_l = Label(
            root,
            bg="#363636",
            fg="white",
            font=("Arial", 14)
        )
area_l.place(x=270, y=250)

def get_radius(event=None):
    try:
        r = float(e.get())
        area = pi * (r ** 2)

        area_l.config(text=f"Area of the circle is: {area:.2f}")        
    except ValueError:
        print("Please enter valid value")

circle = c.create_oval(150,150,10,10, fill ="#363636",outline="white")

e = Entry(root,width=25,bg="#363636", fg="white")
e.place(x=550,y=200)
e.bind("<Return>", get_radius)

pi = 3.14

radius_l = Label(root,text="Enter the radius of Circle :", bg="#363636",fg ="white", font =("Arial", 16, "bold"))
radius_l.place(x= 270, y=195)

root.mainloop()