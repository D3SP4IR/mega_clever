##################################################################################################

# initialize board (20*20)
from tabnanny import check


board = [[0 for _ in range(20)] for _ in range(20)]

# initialize block (21 pieces)
block = [

[[1,1,1,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],
 
[[1,1,1,1,0],
 [0,0,0,1,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,1,0,0],
 [0,1,0,0,0],
 [0,1,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[0,1,0,0,0],
 [1,1,1,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,1,1,0],
 [0,1,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,0,0,0],
 [0,1,1,1,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,0,0,0],
 [0,1,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[0,1,0,0,0],
 [1,1,1,0,0],
 [0,1,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,0,0,0,0],
 [1,1,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,1,1,1],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,0,0,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,0,0,0,0],
 [1,0,0,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,0,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,0,0,0,0],
 [1,1,0,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,0,0,0],
 [1,0,0,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,0,0,0,0],
 [1,1,0,0,0],
 [0,1,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,1,1,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],

[[1,1,0,0,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]],
 
[[1,1,0,0,0],
 [1,1,0,0,0],
 [1,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0]]

]

##################################################################################################

# transpose matrix
def transpose(block):
    new_block = [[0 for _ in range(5)] for _ in range(5)]
    row = col = 5
    for i in range(row):
        for j in range(col):
            new_block[j][i] = block[i][j]
    return new_block

##################################################################################################

# flip matrix
def row_reverse(block):
    return block[::-1]

##################################################################################################

# INPUT: matrix, nth form
def block_rotation(block, form):

    if form >= 4:
        block = row_reverse(block)
        form -= 4

    for _ in range(form):
        block = row_reverse(transpose(block))

    return block

##################################################################################################

# check overlap -> check face -> check corner
def validate_play(board, block, row, col, id):

    # check overlap
    for i in range(row, row+5):
        for j in range(col, col+5):
            # if index out of range
            if not (0<=i<=19 and 0<=j<=19):
                if block[i-row][j-col] == 1:
                    return False
                continue
            if board[i][j] != 0 and block[i-row][j-col] == 1:
                return False
    
    # check face
    for i in range(row, row+5):
        for j in range(col, col+5):
            if block[i-row][j-col] == 1:
                if 0<=i-1<=19 and 0<=j<=19:
                    if board[i-1][j]==id:
                        return False
                if 0<=i+1<=19 and 0<=j<=19:
                    if board[i+1][j]==id:
                        return False
                if 0<=i<=19 and 0<=j-1<=19:
                    if board[i][j-1]==id:
                        return False
                if 0<=i<=19 and 0<=j+1<=19:
                    if board[i][j+1]==id:
                        return False

    # check corner
    for i in range(row, row+5):
        for j in range(col, col+5):
            if block[i-row][j-col] == 1:
                if 0<=i-1<=19 and 0<=j-1<=19:
                    if board[i-1][j-1]==id:
                        return True
                if 0<=i-1<=19 and 0<=j+1<=19:
                    if board[i-1][j+1]==id:
                        return True
                if 0<=i+1<=19 and 0<=j-1<=19:
                    if board[i+1][j-1]==id:
                        return True
                if 0<=i+1<=19 and 0<=j+1<=19:
                    if board[i+1][j+1]==id:
                        print(14)
                        return True

                # 1....2
                # ......
                # ......
                # 3....4

                if (i==0 and j==0 and id==1) or (i==0 and j==19 and id==2) or (i==19 and j==0 and id==3) or (i==19 and j==19 and id==4):
                    return True

    return False

##################################################################################################

# flag
def flag_x(flag):
    while flag:
        try:
            print("Press path to place a block!! ")
            x=int(input("X = "))
            y=int(input("Y = "))
            if x<0 or y<0 or x>19 or y>19:
                print('position out of range!!')
                continue
            flag=False
        except:
            print("Only number!!")
    return x,y,flag

##################################################################################################

#select block
def select_block(z):
    while True:

        # show current block
        print()
        for a in block[z]:
            for b in a:
                print('#' if b==1 else ' ', end='')
            print()
        print()

        blocknum_check=input("Press 'OK' to select and 'NEXT' to choose another block. ")

        if blocknum_check.lower()=="ok":
            break
        elif blocknum_check.lower()!="next":
              continue
        z+=1
        z=0 if z>20 else z
    return z

###############################################################################################

# rotate block
def rotate_block(rotateblock_numcheck,form,blk):
    while rotatedblock_numcheck:

        # show selected block
        print()
        for a in blk:
            for b in a:
                print('#' if b==1 else ' ', end='')
            print()
        print()

        asktoflip=input("Press 'F' to flip and 'OK' to place a block.")

        if asktoflip.lower()=="ok":
            break
        elif asktoflip.lower()=="f":
            blk=block_rotation(blk,form)
            form+=1
            form=0 if form>7 else form
        else:
            continue
    return blk

##################################################################################################

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
        x,y,flag=flag_x(flag)

    ###############################################################################################

        # select block
        z=0
        z=select_block(z)
        
    ###############################################################################################  

        rotatedblock_numcheck=True
        form=1
        blk=block[z]

        # rotate block
        blk=rotate_block(rotatedblock_numcheck,form,blk)
        
    ##################################################################################################
    
        #validate block
        pss = True
        while pss and not validate_play(board, blk, x, y, id):
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
                        board[i][j] = id if block[z][i-x][j-y] else 0
            
            # print board
            print('\n')
            for i in board:
                print(i)

    ##################################################################################################

print('GAME OVER!!')