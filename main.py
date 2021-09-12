from tkinter import *

# Create window object
app = Tk()

# Part
part_text = StringVar

# Heading
part_label = Label(app, text="dearEarth", font=('bold', 20), pady=20)
part_label.grid(row=0, column=0, sticky=W)

# Latitude
part_label = Label(app, text="Latitude", font=('', 14), pady=20)
part_label.grid(row=1, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=1, column=1)

# Longitude
part_label = Label(app, text="Longitude", font=('', 14), pady=20)
part_label.grid(row=1, column=2, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=1, column=3)

# App Main
app.title('dearEarth')
app.geometry('700x350')

# Start Program
app.mainloop()
