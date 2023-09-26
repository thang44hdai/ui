import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
def show_play_screen():
    play_frame.pack()
    main_frame.pack_forget()

def show_main_screen():
    main_frame.pack()
    play_frame.pack_forget()

def start_clicked():
    print("")

def end_clicked():
    print("")

def show_clicked():
    print("")

app = tk.Tk()
app.title("Two Screens")
app.geometry("800x600")
app.resizable(False, False)

# Màn hình 1
main_frame = tk.Frame(app, width=800, height=600)
main_frame.pack()

# Tạo background đỏ của màn hình 1
canvas = tk.Canvas(main_frame, width=800, height=160, bg="red")
canvas.pack()

# Tạo background trắng của màn hình 1
bottom_frame = tk.Frame(main_frame, width=800, height=440, bg="white")
bottom_frame.pack()

# Image Button
image = Image.open("face.jpg")  # Replace with your image file path
image = image.resize((400, 296))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)

next_button = tk.Button(main_frame, image=photo, bd=0, command=show_play_screen)
next_button.photo = photo
next_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER, width=400, height=290)

# Logo
image = Image.open("ptit.png")  # Replace with your image file path
image = image.resize((100, 100))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(main_frame, image=photo)
image_label.photo = photo
image_label.place(relx=0.05, rely=0.05, anchor=tk.NW)

# Title App
font_title = customtkinter.CTkFont(family="Montserrat", size=25, weight= "bold")
text_label = tk.Label(main_frame, text="FACE RECOGNITION PTIT", font=font_title, fg="white", bg="red")
text_label.place(relx=0.5, rely=0.1, anchor=tk.N)

# Màn hình thứ 2
play_frame = tk.Frame(app, bg="red", width=800, height=600)

start_button = ttk.Button(play_frame, text="Start", style="TButton", command=start_clicked)
end_button = ttk.Button(play_frame, text="End", style="TButton", command=end_clicked)
show_button = ttk.Button(play_frame, text="Show", style="TButton", command=show_clicked)
back_button = ttk.Button(play_frame, text="Back", style="TButton", command=show_main_screen)

style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                background="#44475a",
                foreground="black")

start_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
end_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
show_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
back_button.place(relx=0.05, rely=0.05, anchor=tk.NW, width=100, height=30)

# Initially, show the Main Screen
show_main_screen()

app.mainloop()
