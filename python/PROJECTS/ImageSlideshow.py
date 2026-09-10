# import tkinter for creating gui window , buttons , labels 
# import time module to pause between images
# import image and imagetk from pil 
# image - open and resize images
# imagetk - convert images to tkinter can display them
import tkinter as tk
import time
from PIL import Image, ImageTk , ImageOps


# create the main application window
root=tk.Tk()
root.title("Python Image Slideshow App") #set title 
root.geometry("1000x700") #set size

# create a list of image file paths
image_paths=[
    r"C:\Users\Sanyukta\OneDrive\画像\ドキュメント\seema pendrive\camera\20150903_203247.jpg",
    r"C:\Users\Sanyukta\OneDrive\画像\ドキュメント\seema pendrive\camera\IMG_20160805_152312_AO_HDR.jpg",
    r"C:\Users\Sanyukta\OneDrive\画像\ドキュメント\seema pendrive\camera\IMG_20170302_071706033 1.jpg",
    r"C:\Users\Sanyukta\OneDrive\画像\ドキュメント\seema pendrive\camera\20160402_202000.jpg",
    r"C:\Users\Sanyukta\OneDrive\画像\ドキュメント\seema pendrive\camera\IMG_20180628_115443573.jpg",
    r"C:\Users\Sanyukta\OneDrive\画像\ドキュメント\seema pendrive\camera\IMG_20180122_225137735.jpg"
]

# image processing
# set fixed size for all images
image_size=(900,600)

# list to store resized pil images
images=[]
# open and resize each image using pil
for path in image_paths:
    img=Image.open(path)  # open image
    img=ImageOps.exif_transpose(img)
    img = img.resize(image_size)  #resize image
    images.append(img)  # store images


# convert pil images to tkinter compatible images
photo_images=[]
for img in images:
    photo = ImageTk.PhotoImage(img)
    photo_images.append(photo)

# image display area
# label widget used as image frame
image_label=tk.Label(root)
image_label.pack(pady=20)

# slideshow function
def start_slideshow():
    # loop through all images
    for photo in photo_images:
        # set image on label
        image_label.config(image=photo)
        image_label.image = photo  # keep reference to image(important to avoid image dissappearing)
        root.update()  # update the gui to show the image
        time.sleep(2)  # pause for 2 secs before showing next image

# button
# button to start
play_button=tk.Button(
    root,
    text="Play Slideshow",
    font=("Serif Sans F",14),
    command=start_slideshow
)

# lace button on the window
play_button.pack(pady=10)

# start the event loop and keep the window open
root.mainloop()