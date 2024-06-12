from tkinter import *
from PIL import Image, ImageTk
from random import randint

main = Tk()
main.title("Rock Paper Scissor")
main.configure(background="#5FCBF8")

# pictures
rock_img = ImageTk.PhotoImage(Image.open("rock_paper_scissor/rock2.png"))
paper_img = ImageTk.PhotoImage(Image.open("rock_paper_scissor/paper2.png"))
scissor_img = ImageTk.PhotoImage(Image.open("rock_paper_scissor/scissor2.png"))

rock_img_comp = ImageTk.PhotoImage(Image.open("rock_paper_scissor/rock1.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("rock_paper_scissor/paper1.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("rock_paper_scissor/scissor1.png"))

# insert picture
user_label = Label(main, image=scissor_img,bg="#5FCBF8")
comp_label = Label(main, image=scissor_img_comp, bg="#5FCBF8")
comp_label.grid(row=1,column=0)
user_label.grid(row=1, column=4)

# score
playerScore = Label(main, text = 0, font=100, bg="#5FCBF8", fg="#131213")
compScore = Label(main, text = 0, font=100, bg="#5FCBF8", fg="#131213")

compScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

# indicators
user_indicator = Label(main, text = "Player", font=50,bg="#5FCBF8", fg="#131213")
comp_indicator = Label(main, text = "Computer", font=50,bg="#5FCBF8", fg="#131213")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

# Message
msg = Label(main, text = "", font=50, bg="#5FCBF8", fg="#131213")
msg.grid(row=3, column=2)

# update message 
def updateMessage(x):
    msg['text'] = x

# update user Score 
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

# update comp score 
def updateCompScore():
    score = int(compScore['text'])
    score += 1
    compScore['text'] = str(score)

# check winner 
def checkWinner(player, computer):
    if player == computer:
        updateMessage("Tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("You Lose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":  
            updateMessage("You Lose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    else:
        pass


# update Choices 

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user    
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkWinner(x, compChoice) 




# buttons
rock = Button(main,width=20, height=2, text="ROCK",bg="#FF3E4D",fg="BLACK", command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(main,width=20, height=2, text="PAPER",bg="#FAD02E",fg="BLACK", command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(main,width=20, height=2, text="SCISSOR",bg="#8EF228",fg="BLACK", command=lambda:updateChoice("scissor")).grid(row=2,column=3)





main.mainloop()