import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("SCREENSHOT TAKER")

canvas1 = tk.Canvas(root, width = 150, height = 50)
canvas1.pack()

def takeScreenshot ():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

myButton = tk.Button(text="TAKE SCREENSHOT", command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(50, 60, window=myButton)

root.mainloop()