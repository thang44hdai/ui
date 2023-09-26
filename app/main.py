import tkinter as tk
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

def show_play_screen():
    play_frame.pack()
    main_frame.pack_forget()

def show_main_screen():
    main_frame.pack()
    play_frame.pack_forget()

def start_clicked():
    print("Start button clicked")

def end_clicked():
    print("End button clicked")

def show_clicked():
    print("Show button clicked")

app = tk.Tk()
app.title("Two Screens")
app.geometry("800x600")
app.resizable(False, False)

# Main Screen (Next Button)
main_frame = tk.Frame(app, width=800, height=600)
main_frame.pack()

# Create a Canvas to draw the gradient background
canvas = tk.Canvas(main_frame, width=800, height=300, bg="red")
canvas.pack()

# Create a white background for the bottom half
bottom_frame = tk.Frame(main_frame, width=800, height=300, bg="white")
bottom_frame.pack()

# Create a button with text "Next" and custom style
next_button = ttk.Button(main_frame, text="Next", style="TButton", command=show_play_screen)
next_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=30)

# Play Screen (Contains Start, End, Show Buttons)
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

# Custom style for the Main Screen Next Button
style.configure("Custom.TButton",
                font=("Helvetica", 14),
                padding=10,
                background="#44475a",  # Background color (Dracula color)
                foreground="black")     # Text color (black)

start_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
end_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
show_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
back_button.place(relx=0.05, rely=0.05, anchor=tk.NW, width=100, height=30)

# Initially, show the Main Screen
show_main_screen()

app.mainloop()
