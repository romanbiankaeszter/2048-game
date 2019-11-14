import random
#import os


board= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

def placenumber(board):
    row=random.randint(0,len(board)-1)
    col=random.randint(0,len(board[row])-1)
    if board[row][col]==0:
        board[row][col]=2
        return True
    return False
 

def rand_num(board):
    counter=0
    while counter<1:
        if placenumber(board) is True:
            counter+=1
def right_move(board):
    for row in board:
        row = right_move_row(row)
        right_combine(row)

def left_move(board):
    for row in board:
        row=left_move_row(row)
        left_combine(row)

def right_move_row(row):
    n = len(row)
    while 0 in row: 
        row.remove(0)
    for i in range(n -len(row)):
        row.insert(0,0)
    return row

def left_move_row(row):
    n = len(row)
    while 0 in row: 
        row.remove(0)
    for i in range(n -len(row)):
        row.append(0)
    return row

def right_combine(row):
    i=3
    for i in range(3,0,-1):
        if row[i]==row[i-1]:
            row[i]=row[i] * 2
            row[i-1]=0
            row=right_move_row(row)
        else:
            continue
    return row

def left_combine(row):
    i=0
    for i in range(0,3,1):
        if row[i]==row[i+1]:
            row[i]=row[i] * 2
            row[i+1]=0
            row=left_move_row(row)
        else:
            continue
    return row
def full_board(board):
    lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                lst.append(board[i][j])
    if len(lst) == 16:
        return True

#def cls():
    #os.system('cls' if os.name=='nt' else 'clear')

def up_move(col):
    a = []
    for i in range(len(board)):
        

            






def main():
    j=0
    while j<1:
        rand_num(board)
        j+=1
    while  not full_board(board):
        #cls()
        rand_num(board)
        for i in board:
            print(i)
        a=input("A,S,D,W:")
        if a=="D" or a=="d" or a=="6":
            right_move(board)
        if a=="A" or a=="a" or a=="4":
            left_move(board)






if __name__=='__main__':
    main()