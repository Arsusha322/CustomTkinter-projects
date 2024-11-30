import customtkinter as CTk
from random import randint

turns = 0
game_over = False
second_player = False
current_player = 'X'  # Начинаем с игрока "X"

def second_player_check():
    global second_player
    second_player = True
    global current_player
    current_player = 'X'  # Включение 2-го игрока, начинаем с X

def change_appearance_mode(mode):
    CTk.set_appearance_mode(mode)

def check_winner():
    global game_over
    winning_combinations = [
        [btn1, btn2, btn3],
        [btn4, btn5, btn6],
        [btn7, btn8, btn9],
        [btn1, btn4, btn7],
        [btn2, btn5, btn8],
        [btn3, btn6, btn9],
        [btn1, btn5, btn9],
        [btn3, btn5, btn7]
    ]

    for combination in winning_combinations:
        values = [btn.cget('text') for btn in combination]
        if values[0] == values[1] == values[2] != '':
            game_over = True
            winner = values[0]
            lbl_right_turn.configure(text=f"Победитель: {winner}!", font=('Arial Bold', 25))
            for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
                btn.configure(state='disabled')
            break

def computer_turn():
    global turns, game_over
    if game_over:
        return

    btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # 1. Попробовать выиграть
    for combo in winning_combinations:
        values = [btns[i].cget('text') for i in combo]
        if values.count('O') == 2 and values.count('') == 1:
            index = combo[values.index('')]
            btns[index].configure(text='O', font=('Arial Bold', 60), state='disabled')
            turns += 1
            check_winner()
            return

    # 2. Заблокировать победу противника
    for combo in winning_combinations:
        values = [btns[i].cget('text') for i in combo]
        if values.count('X') == 2 and values.count('') == 1:
            index = combo[values.index('')]
            btns[index].configure(text='O', font=('Arial Bold', 60), state='disabled')
            turns += 1
            check_winner()
            return

    # 3. Сделать ход в центр, если он свободен
    if btns[4].cget('text') == '':
        btns[4].configure(text='O', font=('Arial Bold', 60), state='disabled')
        turns += 1
        check_winner()
        return

    # 4. Сделать ход в угол, если он свободен
    for i in [0, 2, 6, 8]:
        if btns[i].cget('text') == '':
            btns[i].configure(text='O', font=('Arial Bold', 60), state='disabled')
            turns += 1
            check_winner()
            return

    # 5. Сделать случайный ход, если другие варианты невозможны
    for i in range(9):
        if btns[i].cget('text') == '':
            btns[i].configure(text='O', font=('Arial Bold', 60), state='disabled')
            turns += 1
            check_winner()
            return

def turn(button):
    global turns, game_over, current_player
    if game_over:
        return

    btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

    match button:
        case 1:
            btn1.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 2:
            btn2.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 3:
            btn3.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 4:
            btn4.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 5:
            btn5.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 6:
            btn6.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 7:
            btn7.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 8:
            btn8.configure(text=current_player, font=('Arial Bold', 60), state='disabled')
        case 9:
            btn9.configure(text=current_player, font=('Arial Bold', 60), state='disabled')

    turns += 1
    check_winner()

    if turns < 9 and not game_over:
        if second_player:
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            computer_turn()

        lbl_right_turn.configure(text=f"Ход игрока: {current_player}", font=('Arial Bold', 25))

def reset():
    global second_player, turns, game_over, current_player
    turns = 0
    game_over = False
    current_player = 'X'
    lbl_right_turn.configure(text='Ваш ход:', font=('Arial Bold', 25), text_color='gray')
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.configure(text='', font=('Arial Bold', 60), state='normal')
    second_player = False

q = CTk.CTk()
q.geometry('700x400')
q.resizable(False, False)

q.grid_columnconfigure(0, weight=0)
q.grid_columnconfigure(1, weight=1)
q.grid_columnconfigure(2, weight=0)
q.grid_rowconfigure(0, weight=1)

left_frame = CTk.CTkFrame(q, width=150, height=600)
left_frame.grid(column=0, row=0, sticky='nws')
left_frame.grid_propagate(False)
left_frame.columnconfigure(0, weight=1)

right_frame = CTk.CTkFrame(q, width=500, height=600)
right_frame.grid(column=2, row=0, sticky='nse')
right_frame.grid_propagate(False)
right_frame.columnconfigure((0, 1, 2), weight=1)
right_frame.grid_rowconfigure((1, 2, 3), weight=1)

lbl_left_title = CTk.CTkLabel(left_frame, text='Крестики\nнолики', font=('Arial Bold', 25), text_color='gray')
lbl_left_title.grid(column=0, row=0, pady=5, sticky='we')

btn_left_reset = CTk.CTkButton(left_frame, text='Сбросить', hover_color='orange3', fg_color='gray', width=135, command=reset)
btn_left_reset.grid(column=0, row=1, pady=(20, 8))

btn_left_2players = CTk.CTkButton(left_frame, text='2 игрока', hover_color='orange3', fg_color='gray', width=135, command=second_player_check)
btn_left_2players.grid(column=0, row=2, pady=(8, 200))

combobox_left_change = CTk.CTkOptionMenu(left_frame, values=['System', 'Dark', 'Light'], fg_color='gray', button_color='gray23', state='readonly', command=change_appearance_mode)
combobox_left_change.grid(column=0, row=3, sticky='sw', padx=10, pady=10)
combobox_left_change.set('System')

lbl_right_turn = CTk.CTkLabel(right_frame, text='Ваш ход:', font=('Arial Bold', 25), text_color='gray')
lbl_right_turn.grid(column=0, row=0, columnspan=3, pady=(15, 30), sticky='we')

btn1 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(1))
btn2 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(2))
btn3 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(3))
btn4 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(4))
btn5 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(5))
btn6 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(6))
btn7 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(7))
btn8 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(8))
btn9 = CTk.CTkButton(right_frame, text='', width=200, height=100, hover_color='orange3', fg_color='gray', command=lambda: turn(9))

btn1.grid(column=0, row=1, padx=5, pady=5)
btn2.grid(column=1, row=1, padx=5, pady=5)
btn3.grid(column=2, row=1, padx=5, pady=5)
btn4.grid(column=0, row=2, padx=5, pady=5)
btn5.grid(column=1, row=2, padx=5, pady=5)
btn6.grid(column=2, row=2, padx=5, pady=5)
btn7.grid(column=0, row=3, padx=5, pady=5)
btn8.grid(column=1, row=3, padx=5, pady=5)
btn9.grid(column=2, row=3, padx=5, pady=5)

q.mainloop()
