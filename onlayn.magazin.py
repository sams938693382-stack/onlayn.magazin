import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Telefonlar ro'yxati (nomi, narxi, rasm yo'li)
phones = [
    ("iPhone 14", 1200, "images/iphone14.png"),
    ("iPhone 13", 1000, "images/iphone13.png"),
    ("iPhone 12", 800, "images/iphone12.png"),
    ("Samsung S23", 1100, "images/s23.png"),
    ("Samsung S22", 950, "images/s22.png"),
    ("Samsung A54", 500, "images/a54.png"),
    ("Xiaomi Mi 13", 700, "images/mi13.png"),
    ("Xiaomi Redmi Note 12", 300, "images/redmi12.png"),
    ("Xiaomi Poco X5", 350, "images/pocox5.png"),
    ("Huawei P50", 900, "images/p50.png"),
    ("Huawei Nova 10", 600, "images/nova10.png"),
    ("Huawei Mate 40", 1000, "images/mate40.png"),
    ("Oppo Find X5", 850, "images/findx5.png"),
    ("Oppo Reno 8", 550, "images/reno8.png"),
    ("Oppo A78", 400, "images/a78.png"),
    ("Vivo V27", 600, "images/v27.png"),
    ("Vivo Y36", 300, "images/y36.png"),
    ("Vivo X80", 900, "images/x80.png"),
    ("Realme GT 3", 650, "images/gt3.png"),
    ("Realme C55", 250, "images/c55.png"),
    ("Realme Narzo 60", 300, "images/narzo60.png"),
    ("OnePlus 11", 900, "images/op11.png"),
    ("OnePlus Nord 3", 500, "images/nord3.png"),
    ("OnePlus 10 Pro", 850, "images/op10.png"),
    ("Google Pixel 7", 700, "images/pixel7.png"),
    ("Google Pixel 6", 600, "images/pixel6.png"),
    ("Google Pixel 5", 450, "images/pixel5.png"),
    ("Sony Xperia 5", 800, "images/xperia5.png"),
    ("Sony Xperia 1", 1000, "images/xperia1.png"),
    ("Sony Xperia 10", 500, "images/xperia10.png")
]

cart = []

root = tk.Tk()
root.title("📱 Telefon Magazin")
root.geometry("800x600")
root.configure(bg="#1e1e2f")

# Sarlavha
label_title = tk.Label(root, text="Telefon Magazin", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="#00ffcc")
label_title.pack(pady=10)

# Frame
main_frame = tk.Frame(root, bg="#2b2b3c")
main_frame.pack(pady=10)

# Listbox
listbox = tk.Listbox(main_frame, width=40, height=15, bg="#121212", fg="white", font=("Arial", 11))
listbox.grid(row=0, column=0, padx=10)

# Rasm joyi
img_label = tk.Label(main_frame, bg="#2b2b3c")
img_label.grid(row=0, column=1, padx=10)

# Telefonlarni chiqarish
for phone in phones:
    listbox.insert(tk.END, f"{phone[0]} - ${phone[1]}")

# Rasmni yangilash
current_img = None

def show_image(event):
    global current_img
    selected = listbox.curselection()
    if selected:
        path = phones[selected[0]][2]
        try:
            img = Image.open(path)
            img = img.resize((200, 200))
            current_img = ImageTk.PhotoImage(img)
            img_label.config(image=current_img)
        except:
            img_label.config(text="Rasm topilmadi", fg="red")

listbox.bind("<<ListboxSelect>>", show_image)

# Savatchaga qo'shish
def add_to_cart():
    selected = listbox.curselection()
    if selected:
        item = phones[selected[0]]
        cart.append(item)
        messagebox.showinfo("Qo'shildi", f"{item[0]} savatchaga qo'shildi")
    else:
        messagebox.showwarning("Xatolik", "Telefon tanlang!")

# Savatchani ko'rish
def view_cart():
    if not cart:
        messagebox.showinfo("Savatcha", "Savatcha bo'sh")
        return
    text = "Savatcha:\n"
    total = 0
    for item in cart:
        text += f"{item[0]} - ${item[1]}\n"
        total += item[1]
    text += f"\nJami: ${total}"
    messagebox.showinfo("Savatcha", text)

# Tugmalar
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=15)

btn_add = tk.Button(btn_frame, text="➕ Savatchaga", command=add_to_cart,
                    bg="#00ffcc", fg="black", font=("Arial", 12, "bold"))
btn_add.grid(row=0, column=0, padx=10)

btn_view = tk.Button(btn_frame, text="🛒 Savatcha", command=view_cart,
                     bg="#ffcc00", fg="black", font=("Arial", 12, "bold"))
btn_view.grid(row=0, column=1, padx=10)

root.mainloop()
