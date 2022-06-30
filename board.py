board = [[0 for _ in range(20)] for _ in range(20)]
block = [

    [[1,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]],
    
    [[1,1,1,1,0],
    [0,0,0,1,0],
    [0,0,0,0,0]],

    [[1,1,1,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]],

    [[0,1,0,0,0],
    [1,1,1,0,0],
    [1,0,0,0,0]],

    [[1,1,1,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0]],

    [[1,1,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]],

    [[1,1,0,0,0],
    [0,1,1,0,0],
    [0,0,1,0,0]],

    [[0,1,0,0,0],
    [1,1,1,0,0],
    [0,1,0,0,0]],

    [[1,0,0,0,0],
    [1,1,1,0,0],
    [0,0,1,0,0]],

    [[1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0]],

    [[1,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]],

    [[1,0,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,0]],

    [[1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]],

    [[1,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,0]],

    [[1,0,0,0,0],
    [1,1,0,0,0],
    [1,0,0,0,0]],

    [[1,1,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]],

    [[1,0,0,0,0],
    [1,1,0,0,0],
    [0,1,0,0]],

    [[1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,0,0]],

    [[1,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]],

    [[1,1,0,0,0],
    [1,0,0,0,0],
    [1,1,0,0,0]],
    
    [[1,1,0,0,0],
    [1,1,0,0,0],
    [1,0,0,0,0]]

    ]
while True:
    # input
    checker=input("Press ==>'P' to play and ==> 'Q' to quit ==> ")
    if checker=="Q":
        print("Turn end.")
        break
    elif checker=="P":
        print("Start")
    else:
        print("Try again!!!")
        continue
    flag=True
    while flag:
        try:
            x=int(input("X = "))
            y=int(input("Y = "))
            z=int(input("Z = "))
            flag=False
        except:
            print("Only number!!")
    
    
    

    print('\nBefore\n')
    for i in board:
        print(i)

    

    

    for i in range(x, x+3):
        for j in range(y, y+5):
            board[i][j] = block[z][i-x][j-y]

    print('\nAfter\n')
    for i in board:
        print(i)