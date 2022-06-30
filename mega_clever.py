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
def validate_play(board, block, form, row, col):

    # check overlap
    for i in range(row, row+5):
        for j in range(col, col+5):
            if board[i][j] == 1 and block[i-row][j-col] == 1:
                return False
    
    # check face
    for i in range(row, row+5):
        for j in range(col, col+5):
            if block[i-row][j-col] == 1:
                if board[i-1][j]==1 or board[i+1][j]==1 or board[i][j-1]==1 or board[i][j+1]==1:
                    return False

    # check corner
    for i in range(row, row+5):
        for j in range(col, col+5):
            if block[i-row][j-col] == 1:
                if board[i-1][j-1]==1 or board[i-1][j+1]==1 or board[i+1][j-1]==1 or board[i+1][j+1]==1:
                    return True
                # temp
                if (i==0 and j==0) or (i==0 and j==20) or (i==20 and j==0) or (i==20 and j==20):
                    return True

    return False
    

##################################################################################################

# initialize board (20*20)
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

# game loop
while True:

    # user input
    checker=input("Press ==>'P' to play and ==> 'Q' to quit ==> ")

    if checker=="Q":
        print("Turn end.")
        break
    elif checker=="P":
        print("Start")
    else:
        print("Try again!!!")
        continue

    flag = True
    while flag:
        try:
            x=int(input("X = "))
            y=int(input("Y = "))
            z=int(input("Z = "))
            flag=False
        except:
            print("Only number!!")

    # place block
    if validate_play(board, block[z], 0, x, y):
        for i in range(x, x+5):
            for j in range(y, y+5):
                board[i][j] = block[z][i-x][j-y]
        
        # print board
        print('\n')
        for i in board:
            print(i)

##################################################################################################