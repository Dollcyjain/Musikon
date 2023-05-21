import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import imutils
from functools import partial
from pygame import mixer

SET_WIDTH = 1334
SET_HEIGHT = 831

def play(song):
    mixer.init()
    mixer.music.load(f"audio\\{song}.mp3")
    mixer.music.play()
    pass
def start(win):
    print("In start")
    win.delete('all')
    frame = cv2.cvtColor(cv2.imread("music.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=1172, height=280)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(670, 0, image=frame, anchor=tkinter.N)

    btn = tkinter.Button(window, text="Kesariya (From \'Brahamastra\')", width=50 ,bg="yellow", font="San 18 bold", command=partial(play, "kesariya"))
    canvas.create_window(650, 340, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Sauda Khara Khara (From \'Good Newwz\')", width=50, bg="pink", font="San 18 bold", command=partial(play, "sauda khara khara"))
    canvas.create_window(650, 390, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Lut Gaye (From \'Mumbai Saga\')", width=50, bg="red", font="San 18 bold", command=partial(play, "lut gaye"))
    canvas.create_window(650, 440, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Raataan Lambiyaan (From \'Shershah\')", width=50, font="San 18 bold", command=partial(play, "raataan lambiyaan"))
    canvas.create_window(650, 490, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Pyaar Hota Kayi Baar Hai (From \'Tu Jhoothi Mai Makkar\')", width=50, bg="Blue", fg="white" ,font="San 18 bold", command=partial(play, "pyaar"))
    canvas.create_window(650, 540, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Jhoome Jo Pathaan (From \'Pathaan\')", width=50, bg="Black", fg="white", font="San 18 bold", command=partial(play, "pathaan"))
    canvas.create_window(650, 590, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Baarish Ban Jaana", width=50, bg="orange", font="San 18 bold", command=partial(play, "baarish"))
    canvas.create_window(650, 640, anchor=tkinter.S, window=btn)
    btn = tkinter.Button(window, text="Fikar not (\'From Chhichhore\')", width=50, bg="purple1", font="San 18 bold", command=partial(play, "fikar not"))
    canvas.create_window(650, 690, anchor=tkinter.S, window=btn)

window = tkinter.Tk()
window.title("MUSIKON by Dollcy jain")
cv_img = cv2.cvtColor(cv2.imread("musikon.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()
btn = tkinter.Button(window, text="Start", width=50, bg="green", font="San 18 bold", command=partial(start, canvas))
canvas.create_window(650, 700, anchor=tkinter.S, window=btn)

window.mainloop()