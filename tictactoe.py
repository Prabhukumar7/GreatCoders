board=['-','-','-',
       '-','-','-',
       '-','-','-']

# print(' __'+' __ __' ) 
# print('|'+ board[0] + '|' + board[1] + '|' + board[2]+'|') 
# print('|'+board[3] + '|' + board[4] + '|' + board[5]+'|')
# print('|'+board[6] + '|' + board[7] + '|' + board[8]+'|')

game_is_still_going = True 
winner = None
current_player ='x'

#display_borad

    

def play_game():
    
    display_board()    
    
    while game_is_still_going:
        
        handle_turn(current_player)
        
        check_game_over()
        
        flip_player()
        


    if winner == 'x' or winner == 'o':
        print('winner is:', winner)
    elif winner == None:
        print('Tie')

def display_board():
        
    print("\n" ) 
    print('| '+board[0] + ' | ' + board[1] + ' | ' + board[2]+' |') 
    print('| '+board[3] + ' | ' + board[4] + ' | ' + board[5]+' |')
    print('| '+board[6] + ' | ' + board[7] + ' | ' + board[8]+' |')
    print("\n" ) 
    
def handle_turn(player):
    
        print(player + '\'s turn' )
        position = input("enter the positon 1-9:")
        
        valid=False
        while not valid:
            while position not in ["1","2","3","4","5","6","7","8","9"]:
               position = input( "enter proper position") 
               
            position=int(position)-1
            
            if board[position] == "-" :
                valid  = True
            else:
                print('you can\'t go there')
                
        
        board[position]=player
        
        display_board()

        
        
def check_game_over():
    check_winner()
    check_tie()
    
def check_winner():
    
    global winner
    
    row_winner = check_row()
    column_winner = check_column()
    diagnoal_winner =check_diagonal()
    if row_winner:
        winner = row_winner    
    elif column_winner:
        winner = column_winner
        
    elif diagnoal_winner:
        winner =diagnoal_winner
    else:
        winner = None
    
    return
        
def check_row():
    
    global game_is_still_going
    row1 = board[0]==board[1]==board[2] != '-'
    row2 = board[3]==board[4]==board[5] != '-'
    row3 = board[6]==board[7]==board[8] != '-'
    
    if row1 or row2 or row3 :
        game_is_still_going = False
    
    if row1 :
        return board[0]
    elif row2:
        return board[3]
    elif row3 :
        return board[6]
    return

def check_column():
    global game_is_still_going
    column1 = board[0]==board[3]==board[6] != '-'
    column2 = board[1]==board[4]==board[7] != '-'
    column3 = board[2]==board[5]==board[8] != '-'
    
    if column1 or column2 or column3 :
        game_is_still_going = False
    
    if column1 :
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

    
    
    return

def check_diagonal():
    
    global game_is_still_going
    
    diagonal1 = board[0]==board[4]==board[8] != '-'
    diagonal2 = board[2]==board[4]==board[6] != '-'
   
    
    if diagonal1 or diagonal2 :
        game_is_still_going = False
    
    if diagonal1 :
        return board[0]
    elif diagonal2:
        return board[2]

    return

def check_tie():
    
    global game_is_still_going
    
    if "-" not in board :
        game_is_still_going= False
        
    return
        
def flip_player():
    
    global current_player
    
    if current_player == 'x' :
        current_player = 'o'
        
    elif current_player == 'o' :
        current_player = 'x'
        
    return
    
    
play_game()


