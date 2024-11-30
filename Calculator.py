import customtkinter as CTk

CTk.set_appearance_mode('light')

nums = ''

def count():
    global nums
    numbers = []
    math = []
    number = ''
    symbs = '×-+÷'

    for char in nums:
        if char in symbs:
            math.append(char)
            if number:
                numbers.append(float(number))
                number = ''
        else:
            number += char

    if number:
        numbers.append(float(number))

    while '×' in math or '÷' in math:
        for i in range(len(math)):
            if math[i] == '×':
                result = numbers[i] * numbers[i + 1]
                numbers[i] = result
                numbers.pop(i + 1)
                math.pop(i)
                break
            elif math[i] == '÷':
                if numbers[i + 1] == 0:
                    lbl_result.configure(text="Ошибка: деление на ноль")
                    return
                result = numbers[i] / numbers[i + 1]
                numbers[i] = result
                numbers.pop(i + 1)
                math.pop(i)
                break

    result = numbers[0]
    for i in range(len(math)):
        if math[i] == '+':
            result += numbers[i + 1]
        elif math[i] == '-':
            result -= numbers[i + 1]
    if result == int(result):
        lbl_result.configure(text=int(result))
    else:
        lbl_result.configure(text=result)

    nums = ''
def clear():
    global nums
    lbl_result.configure(text='Введите пример')
    nums = ''


def clicked(button):
    global nums
    nums += button
    lbl_result.configure(text=nums)


q = CTk.CTk()
q.geometry('400x500')
q.resizable(False, False)

top_frame = CTk.CTkFrame(q, width=400, height=80)
top_frame.grid(column=0, row=0, pady=(0, 15))
top_frame.grid_propagate(False)

bottom_frame = CTk.CTkFrame(q, width=400, height=410)
bottom_frame.grid(column=0, row=1)
bottom_frame.grid_propagate(False)

lbl_result = CTk.CTkLabel(top_frame, text='Введите пример', font=('Arial Bold', 30), text_color='white', fg_color='gray')
lbl_result.grid(column=0, row=0, sticky='nsew', padx=7, pady=10)

top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)

for i in range(4):
    bottom_frame.grid_rowconfigure(i, weight=1)
    bottom_frame.grid_columnconfigure(i, weight=1)

btn_umn = CTk.CTkButton(bottom_frame, text="×", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('×'))
btn_del = CTk.CTkButton(bottom_frame, text="÷", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('÷'))
btn_ready = CTk.CTkButton(bottom_frame, text="=", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=count)
btn_CE = CTk.CTkButton(bottom_frame, text="CE", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=clear)
btn_1 = CTk.CTkButton(bottom_frame, text="1", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('1'))
btn_2 = CTk.CTkButton(bottom_frame, text="2", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('2'))
btn_3 = CTk.CTkButton(bottom_frame, text="3", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('3'))
btn_plus = CTk.CTkButton(bottom_frame, text="+", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('+'))
btn_4 = CTk.CTkButton(bottom_frame, text="4", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('4'))
btn_5 = CTk.CTkButton(bottom_frame, text="5", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('5'))
btn_6 = CTk.CTkButton(bottom_frame, text="6", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('6'))
btn_minus = CTk.CTkButton(bottom_frame, text="-", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('-'))
btn_7 = CTk.CTkButton(bottom_frame, text="7", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('7'))
btn_8 = CTk.CTkButton(bottom_frame, text="8", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('8'))
btn_9 = CTk.CTkButton(bottom_frame, text="9", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('9'))
btn_0 = CTk.CTkButton(bottom_frame, text="0", font=('Arial Bold', 40), fg_color='gray', hover_color='orange3', command=lambda: clicked('0'))

btn_umn.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
btn_del.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
btn_ready.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
btn_CE.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
btn_1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
btn_2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
btn_3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
btn_plus.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
btn_4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
btn_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
btn_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
btn_minus.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
btn_7.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
btn_8.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
btn_9.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
btn_0.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

q.mainloop()
