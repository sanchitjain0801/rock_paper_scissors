
from tkinter import *
import random


array = ['rock', 'paper', 'scissors']

score = 0


def press(u_choice):
    global score
    user_choice.set(u_choice)
    c_choice = random.choice(array)
    computer_choice.set(c_choice)
    if(u_choice == 'scissors'):
        if(c_choice == 'rock'):
            score = score - int(1)
            result.set("YOU LOOSE SCORE : " + str(score))
        elif(c_choice == 'paper'):
            score = score + int(1)
            result.set("YOU WIN SCORE : " + str(score))
        else:
            result.set("IT'S A TIE SCORE :" + str(score))
    if(u_choice == 'paper'):
        if(c_choice == 'scissors'):
            score = score - int(1)
            result.set("YOU LOOSE SCORE : " + str(score))
        elif(c_choice == 'rock'):
            score = score + int(1)
            result.set("YOU WIN SCORE : " + str(score))
        else:
            result.set("IT'S A TIE SCORE :" + str(score))
    if(u_choice == 'rock'):
        if(c_choice == 'paper'):
            score = score - int(1)
            result.set("YOU LOOSE SCORE : " + str(score))
        elif(c_choice == 'scissors'):
            score = score + int(1)
            result.set("YOU WIN SCORE : " + str(score))
        else:
            result.set("IT'S A TIE SCORE :" + str(score))


def Reset():
    global score
    result.set("")
    computer_choice.set("")
    user_choice.set("")
    score = 0


if __name__ == "__main__":
    window = Tk()
    window.geometry('500x300')
    window.config(bg='black')

    window.resizable(0, 0)

    window.title("RPS")

    Label(window, bg='black', fg='white', text='ROCK PAPER SCISSIOR',
          font='arial 15 bold').pack()

    Label(window, bg='black', fg='white', text='Select any one',
          font='arial 10 bold').place(x=20, y=30)

    user_choice = StringVar()
    computer_choice = StringVar()
    result = StringVar()
    Button(window, font='arial 10 bold', text='ROCK', width=6, command=lambda: press('rock'),
           bg='OrangeRed', padx=2, pady=2).place(x=100, y=60)

    Button(window, font='arial 10 bold', text='PAPER', width=6, command=lambda: press('paper'),
           bg='OrangeRed', padx=2, pady=2).place(x=230, y=60)

    Button(window, font='arial 10 bold', text='SCISSORS', width=8, command=lambda: press('scissors'),
           bg='OrangeRed', padx=2, pady=2).place(x=350, y=60)

    Label(window, bg='black', fg='white', text='YOU CHOOSED',
          font='arial 10 bold').place(x=35, y=100)
    uc = Entry(window, width=20, fg='red', font='arial 12 bold',
               bg='black', textvariable=user_choice).place(x=140, y=100)

    Label(window, bg='black', fg='white', text='COMPUTER CHOOSED',
          font='arial 10 bold').place(x=35, y=140)
    uc = Entry(window, width=20, fg='red', font='arial 12 bold',
               bg='black', textvariable=computer_choice).place(x=190, y=140)

    uc = Entry(window, width=30, fg='red', font='arial 12 bold',
               bg='black', textvariable=result).place(x=130, y=170)

    Button(window, font='arial 10 bold', text='RESET', width=6,
           command=Reset, bg='LimeGreen', padx=2).place(x=230, y=210)

    window.mainloop()
