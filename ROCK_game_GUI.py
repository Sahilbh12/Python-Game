from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk, Image
import random
import time
import pygame

# main f2 creation
root = Tk()
root.geometry("1894x1000")
# root.maxsize(925,725)
root.title("ROCK PAPER SCISSOR GAME")
root.wm_iconbitmap("rock game bg10.jpg")

p_choice = StringVar()


# final output f2

def start():
    pygame.mixer.init()
    pygame.mixer.music.load("START.mp3")
    pygame.mixer.music.play(loops=0)
    if agreevalue.get() == 1:
        tmsg.showinfo(
            "Opponent", f"THE MATCH IS BETWEEN {namevalue.get()} VS COMPUTER \nPress \'OK\'")
        time.sleep(1)
        statusvar.set("Loading...")
        sbar.update()
        # time.sleep(1)
        statusvar.set("Ready now")

        root = Tk()
        root.geometry("1894x1000")
        root.title("ROCK PAPER SCISSOR GAME")

        f2 = Frame()
        f2.place(x=0, y=0)

        photos = []
        image = Image.open(f"rock game bg.png")
        # image.ANTIALIAS remove blur effect of image
        image = image.resize((1894, 1000), Image.ANTIALIAS)
        photos.append(ImageTk.PhotoImage(image))
        Label(f2, image=photos[0], anchor="ne").place(x=0, y=0)

        image_rock1 = ImageTk.PhotoImage(Image.open("rock.png"))
        image_paper1 = ImageTk.PhotoImage(Image.open("paper.png"))
        image_scissor1 = ImageTk.PhotoImage(Image.open("scissor.png"))
        image_rock2 = ImageTk.PhotoImage(Image.open("rock.png"))
        image_paper2 = ImageTk.PhotoImage(Image.open("paper.png"))
        image_scissor2 = ImageTk.PhotoImage(Image.open("scissor.png"))

        label_player = Label(f2, image=image_scissor1)
        label_computer = Label(f2, image=image_scissor2)
        label_computer.grid(row=1, column=0)
        label_player.grid(row=1, column=4)

        computer_score = Label(f2, text=0, font=("arial", 60, "bold"), fg="blue")
        player_score = Label(f2, text=0, font=("arial", 60, "bold"), fg="blue")
        computer_score.grid(row=1, column=1)
        player_score.grid(row=1, column=3)

        computer_indicator = Label(f2, font=("arial", 41, "bold"), text="COMPUTER", fg="blue")
        versus = Label(f2, font=("arial", 41, "bold"), text="VS", fg="blue")
        player_indicator = Label(f2, font=("arial", 41, "bold"), text=namevalue.get(), fg="blue")
        computer_indicator.grid(row=0, column=1)
        versus.grid(row=0,column=2)
        player_indicator.grid(row=0, column=3)

        final_message = Label(f2, font=("arial", 40, "bold"), bg="red", fg="white")
        final_message.grid(row=1, column=2)

        def updateMessage(a):
            final_message['text'] = a

        def computer_update():
            final = int(computer_score['text'])
            final += 1
            computer_score["text"] = str(final)

        def player_update():
            final = int(player_score['text'])
            final += 1
            player_score["text"] = str(final)

        def reveal(p, c):
            # tmsg.showinfo("Player choose",f"Player chooses {p}\nComputer chooses {c}")

            if(p == c):
                updateMessage("It's a tie!!")
            elif(p == "rock"):
                if c == "paper":
                    updateMessage("Computer Wins!!")
                    pygame.mixer.music.load("Player lose.wav")
                    pygame.mixer.music.play(loops=0)
                    computer_update()
                else:
                    updateMessage("Player Wins!!")
                    pygame.mixer.music.load("Player win.wav")
                    pygame.mixer.music.play(loops=0)
                    player_update()

            elif(p == "paper"):
                if c == "scissor":
                    updateMessage("Computer Wins!!")
                    pygame.mixer.music.load("Player lose.wav")
                    pygame.mixer.music.play(loops=0)
                    computer_update()
                else:
                    updateMessage("Player Wins!!")
                    pygame.mixer.music.load("Player win.wav")
                    pygame.mixer.music.play(loops=0)
                    player_update()

            elif p == "scissor":
                if c == "rock":
                    updateMessage("Computer Wins!!")
                    pygame.mixer.music.load("Player lose.wav")
                    pygame.mixer.music.play(loops=0)
                    computer_update()
                else:
                    updateMessage("Player Wins!!")
                    pygame.mixer.music.load("Player win.wav")
                    pygame.mixer.music.play(loops=0)
                    player_update()

            else:
                pass

        def choice_update(a):
            c_choice = random.choice(["rock", "paper", "scissor"])
            pygame.mixer.music.load("selection.wav")
            pygame.mixer.music.play(loops=0)
            if c_choice == "rock":
                label_computer.configure(image=image_rock2)
            elif c_choice == "paper":
                label_computer.configure(image=image_paper2)
            else:
                label_computer.configure(image=image_scissor2)

            if a == choose[0]:
                label_player.configure(image=image_rock1)
            elif a == choose[1]:
                label_player.configure(image=image_paper1)
            else:
                label_player.configure(image=image_scissor1)

            reveal(a, c_choice)

        choose = ["rock", "paper", "scissor"]
        photo = PhotoImage(file="rock.png")
        photo1 = PhotoImage(file="paper.png")
        photo2 = PhotoImage(file="scissor.png")
        Radiobutton(f2, variable=p_choice, value=choose[0],
                    image=photo, command=lambda: choice_update(choose[0])).grid(row=2, column=1)
        Radiobutton(f2, variable=p_choice, value=choose[1],
                    image=photo1, command=lambda: choice_update(choose[1])).grid(row=2, column=2)
        Radiobutton(f2, variable=p_choice, value=choose[2],
                    image=photo2, command=lambda: choice_update(choose[2])).grid(row=2, column=3)

        
        root.mainloop()


# "                     "
photos = []

image = Image.open(f"rock game bg.png")
# image.ANTIALIAS remove blur effect of image
image = image.resize((1894, 1000), Image.ANTIALIAS)
photos.append(ImageTk.PhotoImage(image))
Label(root, image=photos[0], anchor="ne").place(x=0, y=0)

Label(root, text="                     ", font=("Times New Roman", 68, "bold"), fg="#0000b3").grid(row=0, column=0)
Label(root, text="\n\n", font=("Times New Roman", 30, "bold"), fg="#0000b3").grid(row=0, column=1)
Label(root, text="WELCOME TO GAME", font=("Times New Roman",
      68, "bold"), fg="#0000b3").grid(row=0, column=1)

image = Image.open(f"rock game bg10.jpg")
# image.ANTIALIAS remove blur effect of image
image = image.resize((365, 255), Image.ANTIALIAS)
photos.append(ImageTk.PhotoImage(image))
Label(root, image=photos[1], anchor="ne").grid(row=1, column=1)

# Label(root, text="GAME",font=("Times New Roman",68,"bold"), fg="#0000b3").grid(row=2,column=0)
Label(text="\n\n", font=("Times New Roman", 10, "bold"),
      fg="#2d00b3").grid(row=3, column=1)
Label(text="Enter player name: ", font=("Times New Roman",
      35, "bold"), fg="#2d00b3").grid(row=4, column=1)
namevalue = StringVar()
nameentry = Entry(root, textvariable=namevalue, relief=SUNKEN, borderwidth=3)
nameentry.grid(row=5, column=1)

Label(root, text="\n", font=("Times New Roman", 10, "bold"),
      fg="#2d00b3").grid(row=6, column=1)

agreevalue = IntVar()
agreeentry = Entry(root, textvariable=agreevalue)
Label(root, text="\n", font=("Times New Roman", 2, "bold"),
      fg="#2d00b3").grid(row=10, column=1)
agreeservice = Checkbutton(text="Would you want to use this name for further?", font=(
    "Times New Roman", 15, "bold"), variable=agreevalue)
agreeservice.grid(row=11, column=1)

# Label(root,text="\n",font=("Times New Roman",10,"bold"),fg="#2d00b3").grid(row=12,column=1)
Button(root, text="START", font=("ALGERIAN", 15), fg="white", bg="green",
       borderwidth=5, relief=SUNKEN, command=start).grid(row=13, column=1)

statusvar = StringVar()
Label(root, text="\n", font=("Times New Roman", 5, "bold"),
      fg="#2d00b3").grid(row=14, column=1)
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=SW)
sbar.grid(row=15, column=1)


root.mainloop()
