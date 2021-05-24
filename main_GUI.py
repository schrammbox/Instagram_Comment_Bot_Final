import main
from tkinter import *
from tkinter import font


if __name__ == '__main__':

    root = Tk()
    root.title("Instagram Bot")
    root.geometry("800x400")
    frame = Frame(root, width=700, height=300)
    font1 = font.Font(size=14)
    fontLabel = font.Font(size=13)
    Label(frame, text="Hashtag:", font=font1).place(x=50, y=120)
    e1 = Entry(frame, width=70, borderwidth=2)
    e1.place(x=230, y=124)
    Label(frame, text="Kommentar:", font=font1).place(x=50, y=180)
    e2 = Entry(frame, width=70, borderwidth=2)
    e2.place(x=230, y=184)
    search_button = Button(frame, text='Search and comment', command=lambda: main.instance.post_comments(e1.get(), e2.get()))
    search_button.place(x=339, y=270)
    frame.pack(expand=TRUE, fill=BOTH)
    topLabel = Label(frame, text="", fg='red', justify=LEFT)
    topLabel.pack()
    root.mainloop()