import tkinter as tk
import mega_clever as mc

def makeBoardCanvas():
    board = [[0 for _ in range(20)] for _ in range(20)] # make 20x20 array

    for i in range(20):
        for j in range(20):
            # append canvas to the array
            board[i][j] = tk.Canvas(app, width=40,height=40,border=0,bg="white",cursor="hand2")

    return board

def setBoardPosition(board):
    for i in range(20):
        for j in range(20):
            board[i][j].grid(column=j,row=i)

    return board
    

app = tk.Tk() # create instance

# set window size
app.geometry('840x840')
app.minsize(840, 840)
app.maxsize(840, 840)

app.title('Mega Clever') # set title of the window
board = setBoardPosition(makeBoardCanvas()) # initialize 20x20 board

# game start!!
n = int(input('Input the number of player (2-4 players) : '))
n_pass = 0
game_end = False

# game loop
while True:

    if game_end:
        break

    for id in range(1, n+1):

        if n_pass == n:
            game_end = True
            break

        print('player', id, 'turn!!')

    ##################################################################################################  

        # user input
        pq = False
        while(not pq):
            checker=input("Press ==>'P' to play and ==> 'Q' to quit ==> ")
            if checker=='q' or checker=='p':
                pq = True
        
        if checker.lower()=="q":
            print("Turn end.")
            n_pass += 1
            continue
        elif checker.lower()=="p":
            print("Start")

    ###############################################################################################  

        #flag
        flag = True
        x,y,flag=mc.flag_x(flag)

    ###############################################################################################

        # select block
        z=0
        z=mc.select_block(z)
        
    ###############################################################################################  

        form=1
        blk=mc.block[z]

        # rotate block
        blk=mc.rotate_block(form,blk)
        
    ##################################################################################################
    
        #validate block
        pss = True
        while pss and not mc.validate_play(mc.board, blk, x, y, id):
            print('Please select new (x,y) position')
            flag = True
            while flag:
                try:
                    print("Press path to place a block!! ")
                    x=input("X = ")

                    if x.lower()=='pass':
                        n_pass += 1
                        pss = False
                        break
                    
                    x=int(x)
                    y=int(input("Y = "))

                    if x<0 or y<0 or x>19 or y>19:
                        print('position out of range!!')
                        continue

                    flag=False
                except:
                    print("Only number!!")

        if flag == False:

            n_pass = 0

            # place block
            for i in range(x, x+5):
                for j in range(y, y+5):
                    if 0<=i<=19 and 0<=j<=19:
                        mc.board[i][j] = id if mc.block[z][i-x][j-y] else 0

            # change color in the GUI's board
            colorlis=['white','red','green','blue','yellow']
            for i in range(20):
                for j in range(20):
                    if mc.board[i][j] !=0:
                        board[j][i] = tk.Canvas(app, width=40,height=40,border=0,bg=colorlis[mc.board[i][j]],cursor="hand2").grid(column=j,row=i)

            # print board
            print('\n')
            for i in mc.board:
                print(i)

app.mainloop()