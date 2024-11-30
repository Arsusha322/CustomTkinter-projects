import customtkinter as CTk

CTk.set_appearance_mode('dark')

q = CTk.CTk()
q.geometry('1400x800')
q.resizable(False, False)

ships = 20


def reset():
    global ships, left_buttons, right_buttons
    ships = 20
    for buttons in [left_buttons, right_buttons]:
        for row in buttons:
            for btn in row:
                btn.configure(fg_color="gray", text="", state='enabled')


def play_together():
    print("Играть вдвоем: функция пока не реализована")


def set_randomly():
    print("Расставить случайно: функция пока не реализована")


def set_bymyself():
    global ships
    if ships == 0:
        if validate_ships(left_buttons):
            print("Корабли расставлены корректно. Игра может начаться!")
        else:
            print("Ошибка в расстановке кораблей.")
    else:
        print(f"Осталось расставить {ships} кораблей!")


def on_cell_click(button):
    global ships
    if ships > 0:
        button.configure(fg_color='orange3', state='disabled')
        ships -= 1


def validate_ships(buttons):
    grid = [[1 if btn.cget("fg_color") == "orange3" else 0 for btn in row] for row in buttons]

    visited = [[False for _ in range(10)] for _ in range(10)]
    ship_lengths = []

    def dfs(x, y):
        stack = [(x, y)]
        ship_cells = []

        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            ship_cells.append((cx, cy))

            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and grid[nx][ny] == 1:
                    stack.append((nx, ny))

        return ship_cells

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1 and not visited[i][j]:
                ship = dfs(i, j)
                ship_lengths.append(len(ship))

                if not all(cell[0] == ship[0][0] for cell in ship) and not all(cell[1] == ship[0][1] for cell in ship):
                    print("Ошибка: Корабль не является линейным!")
                    return False

                for x, y in ship:
                    for nx, ny in [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]:
                        if (nx, ny) not in ship and 0 <= nx < 10 and 0 <= ny < 10 and grid[nx][ny] == 1:
                            print("Ошибка: Корабли не должны соприкасаться!")
                            return False

    required_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    if sorted(ship_lengths) != sorted(required_lengths):
        return False

    return True


q.grid_columnconfigure(0, weight=1)
q.grid_columnconfigure(1, weight=1)
q.grid_rowconfigure(0, weight=1)
q.grid_rowconfigure(1, weight=0)

left_frame = CTk.CTkFrame(q, width=590, height=600)
left_frame.grid(column=0, row=0, pady=(10, 5), padx=(10, 5), sticky='nsew')
left_frame.grid_propagate(False)

right_frame = CTk.CTkFrame(q, width=590, height=600)
right_frame.grid(column=1, row=0, pady=(10, 5), padx=(5, 10), sticky='nsew')
right_frame.grid_propagate(False)

bottom_frame = CTk.CTkFrame(q, width=1200, height=90)
bottom_frame.grid(column=0, row=1, columnspan=2, pady=(5, 10), padx=10, sticky='nsew')
bottom_frame.grid_propagate(False)

bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)
bottom_frame.grid_rowconfigure(0, weight=1)

btn_reset = CTk.CTkButton(bottom_frame, text='Сбросить', fg_color='gray', hover_color='orange3', height=60,
                          font=('Arial Bold', 15), command=reset)
btn_reset.grid(column=0, row=0, sticky='w', padx=10)

btn_play_together = CTk.CTkButton(bottom_frame, text='Играть вдвоем', fg_color='gray', hover_color='orange3', height=60,
                                  font=('Arial Bold', 15), command=play_together)
btn_play_together.grid(column=1, row=0, sticky='e', padx=10)

btn_set_bymyself = CTk.CTkButton(bottom_frame, text='Начать игру', fg_color='gray', hover_color='orange3',
                                 height=60, font=('Arial Bold', 15), command=set_bymyself)
btn_set_bymyself.grid(column=2, row=0, sticky='e', padx=10)

btn_set_randomly = CTk.CTkButton(bottom_frame, text='Расставить случайно', fg_color='gray', hover_color='orange3',
                                 height=60, font=('Arial Bold', 15), command=set_randomly)
btn_set_randomly.grid(column=3, row=0, sticky='e', padx=10)

button_size = 50
letters = "ABCDEFGHIJ"

left_buttons = []
for i in range(10):
    CTk.CTkLabel(left_frame, text=letters[i], width=button_size, height=button_size).grid(row=i + 1, column=0, padx=5,
                                                                                          pady=5)
    CTk.CTkLabel(left_frame, text=str(i + 1), width=button_size, height=button_size).grid(row=0, column=i + 1, padx=5,
                                                                                          pady=5)

    row_buttons = []
    for j in range(10):
        button = CTk.CTkButton(left_frame, text='', width=button_size, height=button_size, fg_color="gray", hover_color="orange3")
        button.grid(row=i + 1, column=j + 1, padx=5, pady=5)
        button.configure(command=lambda b=button: on_cell_click(b))
        row_buttons.append(button)
    left_buttons.append(row_buttons)

right_buttons = []
for i in range(10):
    CTk.CTkLabel(right_frame, text=letters[i], width=button_size, height=button_size).grid(row=i + 1, column=0, padx=5, pady=5)
    CTk.CTkLabel(right_frame, text=str(i + 1), width=button_size, height=button_size).grid(row=0, column=i + 1, padx=5, pady=5)

    row_buttons = []
    for j in range(10):
        button = CTk.CTkButton(right_frame, text='', width=button_size, height=button_size, fg_color="gray", hover_color="orange3")
        button.grid(row=i + 1, column=j + 1, padx=5, pady=5)
        row_buttons.append(button)
    right_buttons.append(row_buttons)

q.mainloop()
