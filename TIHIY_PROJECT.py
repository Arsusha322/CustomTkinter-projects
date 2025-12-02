import tkinter as Tk

sent = []
def encryption():
    sent.clear()
    s = input_text.get("1.0", Tk.END)
    key = key_t.get("1.0", Tk.END).strip()
    s = s.lower()
    if not key:
        raise ValueError("Введите ключ в виде числа")
    else:
        key = int(key) % 26
        alph = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        for i in range(0, len(s)):
            rez = alph.find(s[i])
            if s[i] == " ":
                result += " "
            elif rez != -1:
                rez = (rez + key) % 26
                result = result + alph[rez]
            else:
                result += s[i]

        output_text.config(state='normal')
        output_text.delete("1.0", Tk.END)
        output_text.insert("1.0", result)
        output_text.config(state='disabled')


def decryption():
    sent.clear()
    s = input_text.get("1.0", Tk.END)
    key = key_t.get("1.0", Tk.END).strip()
    s = s.lower()
    if not key:
        raise ValueError("Введите ключ в виде числа")
    else:
        key = int(key) % 26
        alph = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        for i in range(0, len(s)):
            rez = alph.find(s[i])
            if s[i] == " ":
                result += " "
            elif rez != -1:
                rez = (rez - key) % 26
                result = result + alph[rez]
            else:
                result += s[i]

        output_text.config(state='normal')
        output_text.delete("1.0", Tk.END)
        output_text.insert("1.0", result)
        output_text.config(state='disabled')


q = Tk.Tk()
q.geometry("595x700")
q.resizable(False, False)

key_title = Tk.Label(q, text='Ключ:', font=('Arial', 20))
key_title.grid(column=0, row=3, columnspan=2)
key_t = Tk.Text(q, font=('Arial', 40), width=7, bg='gray60', height=1)
key_t.grid(column=0, row=4, columnspan=2)

input_label = Tk.Label(q, text='Ввод:', font=('Arial', 15))
input_label.grid(column=0, row=0)
input_text = Tk.Text(q, width=37, height=30, bg='gray60')
input_text.grid(column=0, row=1)
output_label = Tk.Label(q, text='Результат:', font=('Arial', 15))
output_label.grid(column=1, row=0)
output_text = Tk.Text(q, width=36, height=30, bg='gray60')
output_text.grid(column=1, row=1, padx=3)
output_text.configure(state='disabled')

enc_btn = Tk.Button(q, text='Зашифровать', font=('Arial', 19), width=13, bg='gray60', command=encryption)
enc_btn.grid(column=0, row=2, sticky='n', pady=10, padx=40)
dec_btn = Tk.Button(q, text='Расшифровать', font=('Arial', 19), width=13, bg='gray60', command=decryption)
dec_btn.grid(column=1, row=2, sticky='n', pady=10, padx=40)

q.mainloop()