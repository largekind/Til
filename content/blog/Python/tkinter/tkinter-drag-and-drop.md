---
title: "Tkinter Drag and Drop"
date: 2023-07-11T23:45:09+09:00
---

# Tkinterでドラッグ&ドロップを解析する方法

## 概要

Tkinter上でドラッグ&ドロップを見れるようにする

具体的にはマウスのON/OFFをイベントとして登録し、その情報を得られるようにする

## サンプルコード

以下は適当に選択した画像を表示、そこから矩形領域を選択した場合に座標をとる

``` python

import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Global variables
image = None
start_x = None
start_y = None
end_x = None
end_y = None

def select_image():
    global image

    # Open a file dialog and select an image file
    filepath = filedialog.askopenfilename()

    # Load the image using OpenCV
    image = cv2.imread(filepath)

    # Convert the image from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the image to PIL format
    image = Image.fromarray(image)

    # Convert the image to Tkinter format
    image_tk = ImageTk.PhotoImage(image)

    # Display the image
    image_label.config(image=image_tk)
    image_label.image = image_tk

def on_mouse_down(event):
    global start_x, start_y

    # Record the start coordinates
    start_x = event.x
    start_y = event.y

def on_mouse_up(event):
    global end_x, end_y

    # Record the end coordinates
    end_x = event.x
    end_y = event.y

    # Print the coordinates
    print(f"Start: ({start_x}, {start_y}), End: ({end_x}, {end_y})")

# Create a Tkinter window
window = tk.Tk()

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Create a button to select an image
select_button = tk.Button(window, text="Select Image", command=select_image)
select_button.pack()

# Bind the mouse events to the image label
image_label.bind("<Button-1>", on_mouse_down)
image_label.bind("<ButtonRelease-1>", on_mouse_up)

# Start the Tkinter event loop
window.mainloop()

```

