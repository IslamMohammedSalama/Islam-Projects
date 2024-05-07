from random import choice
from tkinter import *
from glob import glob

def reset():
    players = ['x','o']
    player = choice(players)
    title.config(text=(player + ' turn'))
    for row in range(3):
        for col in range(3):
            
            game_btns[row][col].config(text='')
            game_btns[row][col].config(bg='white')

    

def check_win():
    
    for row in range(3) :

        if (game_btns[row][0]['text'] == game_btns[row][1]['text'] 
            == game_btns[row][2]['text'] != '') :

            game_btns[row][0].config(bg='cyan')
            game_btns[row][1].config(bg='cyan')
            game_btns[row][2].config(bg='cyan')
            return True
        
    for col in range(3) :

        if (game_btns[0][col]['text'] == game_btns[1][col]['text'] 
            == game_btns[2][col]['text'] != '') :
            game_btns[0][col].config(bg='cyan')
            game_btns[1][col].config(bg='cyan')
            game_btns[2][col].config(bg='cyan')
            return True
        
    if (game_btns[0][0]['text'] == game_btns[1][1]['text'] 
        == game_btns[2][2]['text'] != '') :
            
            game_btns[0][0].config(bg='cyan')
            game_btns[1][1].config(bg='cyan')
            game_btns[2][2].config(bg='cyan')
            return True
    
    if (game_btns[0][2]['text'] == game_btns[1][1]['text'] 
        == game_btns[2][0]['text'] != '') :
            game_btns[0][2].config(bg='cyan')
            game_btns[1][1].config(bg='cyan')
            game_btns[2][0].config(bg='cyan')
            return True
    if check_emty_spase() == False :

        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='#ff0000')
        return 'tie'
    else :

        return False

def check_emty_spase():
    
    spase = 9
    for row in range(3) :
        for col in range(3) :
            if game_btns[row][col]['text'] != '' :

                spase -= 1

    if spase == 0 :

        return False
    
    else :

        return True

def next_turn(row, col):
    
    global player 

    if game_btns[row][col]['text'] == '' and check_win() == False :
        
        if player == players[0]:

            game_btns[row][col].config(text=player,foreground='red')

            if check_win() == False :

                player = players[1]

                title.config(text=(player + ' turn'))

            elif check_win() == True :

                title.config(text=(player + ' won ! '))

            elif check_win() == 'tie' :

                title.config(text= ' tie , no winer !')

            
        elif player == players[1]:

            game_btns[row][col].config(text=player,foreground='green')

            if check_win() == False :

                player = players[0]
                title.config(text=(player + ' turn'))

            elif check_win() == True :

                title.config(text=(player + ' won ! '))

            elif check_win() == 'tie' :

                title.config(text= 'tie , no winer !')

            


root = Tk()
root.title('tic tac toc')
root.config(bg='white')
root.resizable(False,False)

players = ['x','o']
player = choice(players)

title = Label(root , text=(player + ' turn') ,
 font=('consolas' , 40 , 'bold'),bg='white')
title.pack(side='top' )

buton = Button(text='reset',command=reset,font=('consolas' , 20 , 'bold') ,
               relief=GROOVE, border=0,bg='white').pack(side='top')

btns_frame = Frame(root, bg='#ffffff')
btns_frame.pack()

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", relief=GROOVE,font=('consolas', 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col),bg='#ffffff',bd=0)
        game_btns[row][col].grid(row=row, column=col)


root.mainloop()