board = [[0 for _ in range(20)] for _ in range(20)]

print('\nBefore\n')
for i in board:
    print(i)

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

# custom
x = 5 # row
y = 8 # column
z = 9 # block no.

for i in range(x, x+3):
    for j in range(y, y+5):
        board[i][j] = block[z][i-x][j-y]

print('\nAfter\n')
for i in board:
    print(i)