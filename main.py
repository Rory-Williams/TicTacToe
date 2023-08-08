#tic tac toe
from random import randint, choice

def get_move():
    move = ''
    move_input = False
    while not move_input:
        move = input('Please input move location as coords from 1,1 to 3,3: ')
        move = move.split(',')
        if len(move) == 2:
            if move[0].isnumeric() and move[1].isnumeric():
                if 0 < int(move[0]) < 4 and 0 < int(move[1]) < 4:
                    move_input = True
                    print(move)
        else:
            print('Please just enter two integers separated with single comma in format: "3,2"')
    move = [int(x)-1 for x in move]
    return move

def print_board(moves):
    print(f'{moves[0][0]} ¦ {moves[0][1]} ¦ {moves[0][2]}\n'
          f'{moves[1][0]} ¦ {moves[1][1]} ¦ {moves[1][2]}\n'
          f'{moves[2][0]} ¦ {moves[2][1]} ¦ {moves[2][2]}\n')

def select_first_player():
    if randint(0,1):
        print('Computer starts')
        return 1
    else:
        print('User starts')
        return 0

def find_empty_spot(moves):
    empty_spaces = []
    for idx_r, row in enumerate(moves):
        for idx_c, column in enumerate(row):
            if ' ' in column:
                empty_spaces.append([idx_r, idx_c])
    print(f'empty space: {empty_spaces}')
    return empty_spaces

def check_win(moves, letter):
    for row in moves: #check rows
        matching = [s for s in row if letter in s]
        # print(len(matching))
        if len(matching) == 3:
            print('row matching:')
            return True
    for idx in range(3):
        # print(idx)
        column_lists = [item[idx] for item in moves]
        matching = [s for s in column_lists if letter in s]
        # print(len(matching))
        if len(matching) == 3:
            print(len(matching))
            return True
    diag1 = [moves[0][0],moves[1][1],moves[2][2]]
    matching = [s for s in diag1 if letter in s]
    if len(matching) == 3:
        print('diag 1 true')
        return True
    diag2 = [moves[0][2], moves[1][1], moves[2][0]]
    matching = [s for s in diag2 if letter in s]
    if len(matching) == 3:
        print('diag 2 true')
        return True
    return False

running_game = 1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while running_game:
        moves = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        player = select_first_player() #1 = computer, 0 = user
        playing = 1 #set playing loop
        print_board(moves)
        while playing:
            if player: #computer (C)
                empty_space_lst = find_empty_spot(moves)
                place = choice(empty_space_lst)
                moves[place[0]][place[1]] = 'C'
                print_board(moves)
                player = 0
                if check_win(moves, 'C'):
                    print('comp is winner')
                    playing = 0
            else: #user
                loop_move = 1
                move = get_move()
                while loop_move:
                    if moves[move[0]][move[1]] == ' ':
                        moves[move[0]][move[1]] = 'U'
                        loop_move = False
                    else:
                        'Cant place there, please try again'
                        move = get_move()
                print_board(moves)
                player = 1
                if check_win(moves, 'U'):
                    print('user is winner')
                    playing = 0
        keep_playing = input('keep playing (y/n)?')
        if keep_playing.lower() == 'n':
            running_game = 0
            # get_move()
            # print_board(moves)
        # running_game = 0


