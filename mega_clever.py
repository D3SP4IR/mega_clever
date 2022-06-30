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

    if checker.lower()=="q":
        print("Turn end.")
        break
    elif checker.lower()=="p":
        print("Start")
    else:
        print("Try again!!!")
        continue

    flag = True
    while flag:
        try:
            print("Press path to place a block!! ")
            x=int(input("X = "))
            y=int(input("Y = "))
            flag=False
        except:
            print("Only number!!")
    block_numcheck=True
    z=0
    while block_numcheck:
        print(block[z])
        blocknum_check=input("Press 'OK' to select and 'NEXT' to choose another block. ")
        if blocknum_check.lower()=="ok":
            break
        elif blocknum_check.lower()!="next":
            continue
        z+=1
        if z>20:
            z-=20
    
    rotatedblock_numcheck=True
    form=0
    blk=block[z]
    while rotatedblock_numcheck:
        print(blk)
        asktoflip=input("Press 'F' to flip and 'OK' to place a block.")
        if asktoflip.lower()=="ok":
            break
        elif asktoflip.lower()=="f":
            blk=block_rotation(blk,form)
            form+=1
            if form>7:
                form-=20
        else:
            continue
    # place block    
    for i in range(x, x+5):
        for j in range(y, y+5):
            board[i][j] = block[z][i-x][j-y]

    # print board
    print('\n')
    for i in board:
        print(i)

##################################################################################################