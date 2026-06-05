from tkinter import *
from tkinter import messagebox,ttk

root = Tk()
root.title("Resturant Demo Using Tkinter")
root.geometry("1100x750")
# root.configure(bg="lime")


def add_to_cart(item, price):
    global item_id
    cart.append(price)
    tree.insert(
        "",
        END,
        values=(item_id, item, 1, f"₹ {price}")
    )
    item_id += 1
    calculate_bill()

def calculate_bill():
    total = sum(cart)
    service = total * 0.05
    gst = (total + service) * 0.18
    payable = total + service + gst
    
    total_var.set(f"₹ {total:.2f}")
    service_var.set(f"₹ {service:.2f}")
    gst_var.set(f"₹ {gst:.2f}")
    payable_var.set(f"₹ {payable:.2f}")    

def reset_bill():
    global item_id
    for row in tree.get_children():
        tree.delete(row)
    cart.clear()
    item_id = 1
    total_var.set("₹ 0.00")
    service_var.set("₹ 0.00")
    gst_var.set("₹ 0.00")
    payable_var.set("₹ 0.00")

def save_bill():
    messagebox.showinfo("Saved", "Bill Saved Successfully!")

def print_bill():
    messagebox.showinfo("Print", "Printing Bill...")



title = Label(root, text="🍽 Foodie's Restaurant", font=("Poppins", 34, "bold"), bg="#ff6b35", fg="white")
title.pack(fill=X)

main_frame = Frame(root, bg="#4dffff")
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

left_frame = Frame(main_frame)
left_frame.pack(side=LEFT, fill=BOTH, expand=True)

right_frame = Frame(main_frame, bg="white", bd=2 , relief=SOLID ,  width=400)
right_frame.pack(side=RIGHT, fill=Y)

menu_frame = Frame(left_frame)
menu_frame.grid(columnspan=6)

menu_items = [
    ("Butter Chicken", 180),
    ("Paneer Butter Masala", 260),
    ("Biryani", 280),
    ("Masala Dosa", 125),
    ("Chole Bhature", 140),
    ("Rajma Chawal", 160),
    ("Dal Tadka", 180),
    ("Tandoori Roti", 25),
    ("Naan", 35),
    ("Pav Bhaji", 150),
    ("Samosa", 30),
    ("Vada Pav", 40),
    ("Pani Puri", 60),
    ("Kadhai Paneer", 240),
    ("Chicken Curry", 300),
    ("Fish Curry", 340),
    ("Mutton Rogan Josh", 420),
    ("Veg Fried Rice", 170),
    ("Hakka Noodles", 180),
    ("Idli Sambhar", 90),
    ("Gulab Jamun", 80),
    ("Rasgulla", 70),
    ("Lassi", 60),
    ("Cold Coffee", 110)
]
cart = []
item_id = 1
row = 0
col = 0
for item, price in menu_items:

    card = Frame(left_frame, bg="white", bd=1, relief=SOLID, padx=22, pady=10 )
    card.grid(row=row, column=col, padx=10, pady=10)

    Label(card, text="🍛", font=("Arial", 24), bg="white").pack()
    Label(card, text=item, font=("Arial", 10, "bold"), bg="white", wraplength=120, justify=CENTER).pack(pady=5)
    Label(card, text=f"₹ {price}", font=("Arial", 11), fg="green", bg="white").pack()
    Button(card, text="Add", width=10, bg="#ff4d4d", fg="white", command=lambda i=item, p=price: add_to_cart(i, p)).pack(pady=5)
    col += 1
    if col == 6:
        col = 0
        row += 1

title1=Label(right_frame, text="Order Summary", font=("Poppins", 20, "bold"), bg="white")
title1.pack(fill=X, pady=20)

columns = ("ID", "Dish", "Qty", "Amount")
tree = ttk.Treeview(right_frame, columns=columns, show="headings",height=18)
for col_name in columns:
    tree.heading(col_name, text=col_name)
tree.column("ID", width=50)
tree.column("Dish", width=220)
tree.column("Qty", width=60)
tree.column("Amount", width=100)
tree.pack(padx=10, pady=10)

bill_frame = Frame(right_frame, bg="white")
bill_frame.pack(pady=20)

total_var = StringVar(value="₹ 0.00")
service_var = StringVar(value="₹ 0.00")
gst_var = StringVar(value="₹ 0.00")
payable_var = StringVar(value="₹ 0.00")

def bill_row(text, variable):
    row_frame = Frame(bill_frame, bg="white")
    row_frame.pack(fill=X, pady=5)

    Label(row_frame, text=text, font=("Arial", 11, "bold"), bg="white", width=18, anchor="w").pack(side=LEFT)
    Entry(row_frame, textvariable=variable, font=("Arial", 11), width=15, justify="right").pack(side=RIGHT)

bill_row("Total Amount", total_var)
bill_row("Service Charge", service_var)
bill_row("GST 18%", gst_var)
bill_row("Payable Amount", payable_var)

btn_frame = Frame(right_frame, bg="white")
btn_frame.pack(pady=20)

Button(btn_frame, text="Reset", width=10, font=("Pacifico", 12), bg="#005ce6", fg="white", command=reset_bill).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Save", width=10, font=("Pacifico", 12), bg="#29a329", fg="white", command=save_bill).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Print",width=10, font=("Pacifico", 12), bg="#cc0044", fg="white", command=print_bill).grid(row=0, column=2, padx=10)


root.mainloop()