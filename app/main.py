import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
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
    
def add_path():
    path = filedialog.askopenfilename()  # Hiển thị hộp thoại chọn tệp
    # Thực hiện xử lý với đường dẫn được chọn

#----------------------------------------------------------------------------------------------------------------------
app = tk.Tk()
app.title("Face Recognition App")
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

#-----------------------------------------------------------------------------------------------------------------
# Màn hình thứ 2
play_frame = tk.Frame(app, bg="red", width=800, height=600)

# Tạo background đỏ của màn hình 2
canvas = tk.Canvas(play_frame, width=800, height=50, bg="red")
canvas.pack()

# Tạo background trắng của màn hình 2
bottom_frame = tk.Frame(play_frame, width=800, height=550, bg="white")
bottom_frame.pack()

#Start Button
image = Image.open("scan.jpg")  # Replace with your image file path
image = image.resize((800, 300))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
back_button = tk.Button(play_frame, image=photo, command=start_clicked)
back_button.photo = photo
back_button.place(relx=0, rely=0.08, width=800, height=300)

add_path_button = ttk.Button(play_frame, text="Thêm lớp học", style="TButton", command=add_path)
end_button = ttk.Button(play_frame, text="End", style="TButton", command=end_clicked)
show_button = ttk.Button(play_frame, text="Show", style="TButton", command=show_clicked)
# Back Button
image = Image.open("ptit.png")  # Replace with your image file path
image = image.resize((40, 40))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
back_button = tk.Button(play_frame, image=photo, command=show_main_screen)
back_button.photo = photo
back_button.place(relx=0.01, rely=0.01, anchor="nw", width=40, height=40)


style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                background="#44475a",
                foreground="black")

add_path_button.place(relx=0.2, rely=0.04, anchor=tk.CENTER)
end_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
show_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


# Initially, show the Main Screen
show_main_screen()

app.mainloop()
