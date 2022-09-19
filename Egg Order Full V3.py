'''
Egg Order Program
Python Practice Assessment
Jayden Houghton

Changelog:
- Changed delivery from a text entry to a checkbox
- Added order charge to total cost
'''
from tkinter import*
import tkinter.messagebox


#--- functions ---

#name input and error trap
def name_check(name):
    try:
        if name.isalpha():
            return True
        elif name == "" or name == " ":
            tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter a name")
        else:
            tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter a name")
    except ValueError:            
        tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter a name")

#number of eggs input and error trap
def number_check(number):
    try:
        if str.isdigit(str(number)):
            return True
        elif number == "" or number == " ":
            tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter the number of eggs")
        else:
            tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter the number of eggs")
    except ValueError:            
        tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter the number of eggs")

#check if delivery checkbox is checked
def delivery_check():
    deliveryState = checkState.get()
    if deliveryState == 1:
        return True
    else:
        return False

#check if text has been inputted
def address_check(address):
    try:
        if address == "" or address == " ":
            return False
        else:
            return True

    except ValueError:            
        return True

#confirm the entered information and process
def confirm():
    global orders
    global total_eggs
    global e_cost
    name = entry_name.get()
    number = int(entry_number.get())
    delivery = delivery_check()
    cost = round(e_cost*float(number), 2)
    address = ""
    
    if delivery:
        address = entry_address.get()
        cost += 2
        
        if name_check(name) and number_check(number) and address_check(address):
            answer = tkinter.messagebox.askquestion("Confirm Information", "Please check that the following information is correct:\n"
                "Name: {}\nNumber: {}\nDelivery: {}\nAddress: {}\nOrder Cost: ${}".format(name, number, delivery, address, cost))
        else:
            answer = "no"
            tkinter.messagebox.showinfo("Jayden's Egg Farm", "Please enter an address to deliver to")
            
    else:
        if name_check(name) and number_check(number):
            answer = tkinter.messagebox.askquestion("Confirm Information", "Please check that the following information is correct:\n"
                "Name: {}\nNumber: {}\nDelivery: {}\nOrder Cost: ${}".format(name, number, delivery, cost))
        else:
            answer = "no"
        
        
    if answer == "yes":
        orders += 1
        total_eggs += number
        
        orders_names.append(name)
        orders_eggs.append(number)
        orders_delivery.append(delivery)
        orders_address.append(address)

#confirm the entered information and process
def stats():
    global total_eggs
    global orders
    if orders > 0:
        average = total_eggs/orders
        average = int(round(average/12, 0))
    else:
        average = 0
    tkinter.messagebox.showinfo("Jayden's Egg Farm", "Daily Stats: \nNumber of orders: {}\nAverage number of eggs (dozens): {}".format(orders, average))


#initialise variables
orders = 0
total_eggs = 0
cost = 0
e_cost = 0.35

orders_names = []
orders_eggs = []
orders_delivery = []
orders_address = []

     
#--- set up tkinter ---

#set up root
root = Tk()
root.title("Jayden's Egg Farm")

root.geometry("400x229")
root.resizable(0,0)

checkState = IntVar()

#set up frames
topFrame = Frame(root, bg="blue")
topFrame.grid(row=0, sticky=NSEW)

formFrame = Frame(root, bg="grey97")
formFrame.grid(row=1, sticky=NSEW)

buttonFrame = Frame(root, bg="grey97", pady=10)
buttonFrame.grid(row=2, sticky=NSEW)

bottomFrame = Frame(root, bg="black")
bottomFrame.grid(row=3, sticky=NSEW)

#--- header bar ---
photo = PhotoImage(file="Egg_Small.png")
logo = Label(topFrame, image=photo, width=30, height=30, bg="black")
logo.grid(sticky=W, row=0, column=0)

space = Label(topFrame, text="", width=7, bg="blue")
space.grid(row=0, column=1)

title = Label(topFrame, text="Jayden's Egg Farm", bg="blue", fg="white", font="Helvetica 17 bold")
title.grid(row=0, column=2)

space1 = Label(topFrame, text="", width=7, bg="blue")
space1.grid(row=0, column=3)

statsButton = Button(topFrame, text="Stats", command=stats, padx=4, pady=3)
statsButton.grid(sticky=E, row=0, column=4)

#--- form section ---
label_name = Label(formFrame, text="Name", bg="grey97")
label_number = Label(formFrame, text="Number of eggs", bg="grey97")
label_delivery = Label(formFrame, text="Delivery (yes/no)", bg="grey97")
label_address = Label(formFrame, text="Address:", bg="grey97")

label_name.grid(row=0, column=0, sticky=E, padx=(150, 0))
label_number.grid(row=1, column=0, sticky=E)
label_delivery.grid(row=2, column=0, sticky=E)
label_address.grid(row=3, column=0, sticky=E)

entry_name = Entry(formFrame)
entry_number = Entry(formFrame)
checkBox = Checkbutton(formFrame, variable=checkState, bg="grey97")
entry_address = Entry(formFrame)

entry_name.grid(row=0, column=1, pady=5)
entry_number.grid(row=1, column=1, pady=5)
checkBox.grid(row=2, column=1, sticky=W)
entry_address.grid(row=3, column=1, pady=5)

#--- enter button ---
submitButton = Button(buttonFrame, text="Submit", command=confirm, bg="orange", pady=5, padx=5)
submitButton.grid(row=0, column=1)

space3 = Label(buttonFrame, text="", width=24, bg="grey97")
space3.grid(row=0, column=0)

#--- footer bar ---
label_bottom = Label(bottomFrame, text="Jayden Houghton Programs© 2020", bg="black", fg="white", padx=105, pady=5)
label_bottom.grid()

root.mainloop()
