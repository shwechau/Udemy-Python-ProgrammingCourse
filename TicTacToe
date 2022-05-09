from IPython.display import clear_output

def print_board(board):
    clear_output()
    print(board[9]+'|'+board[8]+'|'+board[7])
    print('-'+'|'+'-'+'|'+'-')
    print(board[6]+'|'+board[5]+'|'+board[4])
    print('-'+'|'+'-'+'|'+'-')
    print(board[3]+'|'+board[2]+'|'+board[1])
     
def place_marker(board, marker, position):
    #position = input('enter the position where you wnat to place the marker from 1to9:')
    board[position] = marker
    print_board(board)
    
def pick_player():
    marker = ''
    while marker!='x' and marker!='o':
        marker=input('Player1:please choose X or o -').lower()       
    if marker == 'x':
        return ('x','o')
    else:
        return ('o','x')

def winner(board,marker):
    return board[1]==board[2]==board[3]==marker or board[2]==board[5]==board[8]==marker or board[3]==board[6]==board[9]==marker or board[1]==board[4]==board[7]==marker or board[2]==board[5]==board[7]==marker or board[4]==board[5]==board[6]==marker or board[7]==board[8]==board[9]==marker or board[1]==board[5]==board[9]==marker or board[3]==board[5]==board[7]==marker

def right_wrong(pos):
    m=int(pos)
    if m>9 or m<1:
        newpos=input("Please enter an input between 1 to 9:")
        right_wrong(newpos)
    else:
        return True   
    
def board_space(board,pos):
    unused = int(pos)
    if board[unused]!=" ":
        print("you have entered repeated characters")
        unused = input("Please enter unused marker position:")
        return board_space(board,unused)
    else:
        return unused
    
def gamestart(newGame):
    userInput=True
    if newGame!='y' and newGame!='n':
        newGame = input('you can only enter (Y/N):').lower()
        return gamestart(newGame)
    elif newGame=='y':
        userInput=True
    else:
        userInput=False
        print('Game ended')
    return userInput 
    
def tic_tac():
    pos=0
    i=1
    player1,player2 = pick_player()
    last_used =0
    s=''
    x=False
    newGame=''
    print(f'player1: {player1}')
    print(f'player2: {player2}')
    board = [" "]*10
    while(i<10):
        position = input("Enter the position of your marker from 1 to 9:")
        if i%2==0:
            marker=player2
        else:
            marker=player1
        if position.isdigit():
            pos=int(position)
            x=right_wrong(pos)
            if x:
                empty=board_space(board,pos)
                space=int(empty)
                i+=1
                place_marker(board,marker,space)
                if winner(board,marker):
                    if marker==player1:
                        print('Player1:You won')
                    else:
                        print('Player2: You won')          
                    newGame=input('Do you wanna play again (Y/N):').lower()
                    tictac= gamestart(newGame)
                    if tictac:
                        i=1
                        tic_tac()
                    else:
                        i=20
                        break
                else:
                    print('No one won')
                
        else:
            print("Please enter an input between 1 to 9")
            
tic_tac()
            
