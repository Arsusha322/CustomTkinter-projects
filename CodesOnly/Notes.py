import customtkinter as CTk

CTk.set_appearance_mode('dark')

q = CTk.CTk()
q.geometry('350x550')
q.resizable(False, False)
q.grid_rowconfigure(0, weight=1)
q.grid_rowconfigure(1, weight=1)


upper_frame = CTk.CTkFrame(q, width=350, height=130)
upper_frame.grid(column=0, row=0, sticky='n')
upper_frame.grid_propagate(False)

bottom_frame = CTk.CTkFrame(q, width=350, height=400)
bottom_frame.grid(column=0, row=1, sticky='s')
bottom_frame.grid_propagate(False)


text = CTk.CTkTextbox(bottom_frame, text=(open(neededtext, r)), width=330, height=380, fg_color='gray14')
text.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)


q.mainloop()