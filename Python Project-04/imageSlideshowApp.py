#Creating an Image Slideshow App
import tkinter as tk
import time
from PIL import Image, ImageTk

#Main Window

mainWindow = tk.Tk()
mainWindow.title("Image Slider")
mainWindow.geometry("1000x800")

#List of image paths
image_paths = [
    r"\Users\User\OneDrive\Documents\Python\Project Project-04\Iamges\image-01.jpg",
    r"\Users\User\OneDrive\Documents\Python\Project Project-04\Iamges\image-02.png",
    r"\Users\User\OneDrive\Documents\Python\Project Project-04\Iamges\image-03.jpg",
    r"\Users\User\OneDrive\Documents\Python\Project Project-04\Iamges\image-04.jpg",
    r"\Users\User\OneDrive\Documents\Python\Project Project-04\Iamges\image-05.jpg",
]

image_size = (600,700)
images = []
for eachPath in image_paths:
    img = Image.open(eachPath)
    img = img.resize(image_size)
    images.append(img)

#Convert PIL images into tkinter compatible iamge

conImages = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    conImages.append(photo)

#Label widget to keep photo

image_label = tk.Label(mainWindow)
image_label.pack(pady=30)

#Slideshow function

def start_slideshow():
    for photo in conImages:
        image_label.config(image = photo)
        image_label.image = photo

        mainWindow.update()
        time.sleep(3)

#Button

play_Button = tk.Button(
    mainWindow,
    text = "Play slideshow",
    font = ("Times New Roman",20),
    command = start_slideshow
)

play_Button.pack(pady=30)

mainWindow.mainloop()