import customtkinter as CTk

CTk.set_appearance_mode('dark')

def clear():
    with open('neededtext.txt', 'w') as w:
        w.write('')
    text.configure(state='normal')
    text.delete("0.0", "end")
    text.configure(state='disabled')

def add_totext():
    text.configure(state='normal')
    with open('neededtext.txt', 'a') as r:
        r.write(entry.get() + '\n')
    entry.delete(0, 'end')
    with open('neededtext.txt', 'r') as t:
        content = t.read()
        text.delete("0.0", "end")
        text.insert("0.0", content)
    text.configure(state='disabled')

q = CTk.CTk()
q.geometry('350x550')
q.resizable(False, False)
q.grid_rowconfigure(0, weight=1)
q.grid_rowconfigure(1, weight=1)

upper_frame = CTk.CTkFrame(q, width=350, height=130)
upper_frame.grid(column=0, row=0, sticky='n')
upper_frame.grid_propagate(False)

upper_frame.grid_columnconfigure((0, 1), weight=1)
upper_frame.grid_rowconfigure((0, 1), weight=1)

bottom_frame = CTk.CTkFrame(q, width=350, height=400)
bottom_frame.grid(column=0, row=1, sticky='s')
bottom_frame.grid_propagate(False)

text = CTk.CTkTextbox(bottom_frame, width=330, height=380, fg_color='gray14')
text.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

try:
    with open('neededtext.txt', 'r') as t:
        content = t.read()
        text.delete("0.0", "end")
        text.insert("0.0", content)
    text.configure(state='disabled')

    entry = CTk.CTkEntry(upper_frame, width=300, height=40, placeholder_text='Введите то, что хотите добавить')
    entry.grid(column=0, row=0, columnspan=2, sticky='nwe', padx=25, pady=(20, 10))

    btn_add = CTk.CTkButton(upper_frame, text='Добавить', font=('Arial', 20), text_color='white', fg_color='gray', hover_color='orange3', width=150, command=add_totext)
    btn_add.grid(column=0, row=1, sticky='e', padx=(0, 10), pady=(10, 20))

    btn_clear = CTk.CTkButton(upper_frame, text='Очистить', font=('Arial', 20), text_color='white', fg_color='gray', hover_color='orange3', width=150, command=clear)
    btn_clear.grid(column=1, row=1, sticky='w', padx=(10, 0), pady=(10, 20))

    q.mainloop()

except:
    entry = CTk.CTkEntry(upper_frame, width=300, height=40, placeholder_text='Введите то, что хотите добавить')
    entry.grid(column=0, row=0, columnspan=2, sticky='nwe', padx=25, pady=(20, 10))

    btn_add = CTk.CTkButton(upper_frame, text='Добавить', font=('Arial', 20), text_color='white', fg_color='gray',
                            hover_color='orange3', width=150, command=add_totext)
    btn_add.grid(column=0, row=1, sticky='e', padx=(0, 10), pady=(10, 20))

    btn_clear = CTk.CTkButton(upper_frame, text='Очистить', font=('Arial', 20), text_color='white', fg_color='gray',
                              hover_color='orange3', width=150, command=clear)
    btn_clear.grid(column=1, row=1, sticky='w', padx=(10, 0), pady=(10, 20))

    q.mainloop()