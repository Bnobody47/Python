import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:\Users\Bnobody_47\Pictures/{}.png'.forma(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Screenshot",
    command=screenshot)

button.pack(side=tk.LEFT)
Close = tk.Button(
    frame,
    text="QUIT",
    command=quit)
Close.pack(side=tk.LEFT)

root.mainloop()