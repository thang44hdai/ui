from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Adding a Title or Heading to the List")

element_list = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
txt_output = Text(root, height=50, width=50)
txt_output.pack()
for item in element_list:
   txt_output.insert(END, item + "\n")

root.mainloop()