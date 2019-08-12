from IPython.display import clear_output
import random

def display_board(board):
    print('   |   |   ' )
    print(' '+ board[1] + ' |' + ' ' + board[2] + ' |' + ' ' + board[3] + ' ')
    print('___|___|___')
    print('   |   |   ' )
    print(' '+ board[4] + ' |' + ' ' + board[5] + ' |' + ' ' + board[6] + ' ')
    print('___|___|___')
    print('   |   |   ' )
    print(' '+ board[7] + ' |' + ' ' + board[8] + ' |' + ' ' + board[9] + ' ')

def player_input():
    while True:
        marker = input('Please input X or O to start this game game: ')
        if marker == 'X' or marker == 'O':
            print(f'You choose {marker}!')
            return marker
            break
        else:
            print(f'Your choose {marker} is invalid, please input X or O!')
            continue

def place_marker(board, marker, position):
    while True:
        if marker == 'X' or marker == 'O':
            board[position] = marker
            return board

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

def choose_first():
    while True:
        marker = None
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        if x > y:
            print('X go first')
            marker = 'X'
            return marker
            break
        if x < y:
            print('O go first')
            marker = 'O'
            return marker
            break
        if x == y:
            continue

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    while True:
        next_pos = input('plz input your next move (num:1-9)')
        
        # 嘗試確定是否為整數
        try:
            next_pos = int(next_pos)
        except:
            print("oops! it's not int, try again")
            continue
        
        # 判斷位置
        if next_pos not in range(0,10):
            print('your input is invalid!')
            continue
        elif space_check(board, next_pos):
            return next_pos
            break
        else:
            print('your position has been occupied!, plz try another blank')
            continue

def replay():
    while True:
        confirm = input('try again? (Y/N)')
        if confirm == 'Y' or confirm == 'y':
            return True
            break
        elif confirm == 'N' or confirm == 'n':
            return False
            break
        else:
            print('please answer Y or N')
            continue

def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        #空版面
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        #使用者先輸入要當誰
        marker = player_input()
        print(marker)
        #決定誰開始 回傳marker
        marker = choose_first()
        print(marker)
        #開始遊戲的循環
        #先確定遊戲是否為滿版面, 如果不是才往下走
        while not full_board_check(board): 
            #show 畫面
            print('目前是' + marker + '選擇')
            display_board(board)
            #選數字, 包含判斷是否為空格
            position = player_choice(board)
            #放格子
            place_marker(board, marker, position)
            #確認是否會贏, 有贏就回傳是否重來 break
            if win_check(board, marker):
                print(marker + 'win!')
                replay_check = replay()
                break
            #沒贏就轉換腳色繼續while
            else:
            #轉換順序
                if marker == 'X':
                    marker = 'O'
                elif marker == 'O':
                    marker = 'X'
                continue
        
        if full_board_check(board):
            print('tited!')
            replay()
        if replay_check:
            continue
        else:
            break

main()