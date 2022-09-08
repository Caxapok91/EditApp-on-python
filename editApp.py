from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()

'''
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        frame = Frame(master=window, relief=RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=1, pady=1)
        label = Label(master=frame,text = f'Row{i}\nColumn {j}')
        label.pack(padx=10,pady=10)

text = Text(width=50, height=7)
text.insert(1.0, 'Hello')
text.insert(2.0, '\nHello')
text.insert(3.0, '\nHello')
text.delete(1.0, 1.2)
print(text.get(2.0, 2.2))
text.pack(side=LEFT)
fname = askopenfilename(title = 'Select', filetypes = [('Текстовыйе файлы', '*.txt'),('All files', '*.*')])

print(fname)


def change(event):
    b['fg'] = 'red'
    b['activeforeground'] = 'red'


b = Button(text='RED', width=10, height=3)
b.bind('<Button-1>', change)
b.bind('<Return>', change)
b.pack()
'''
window.title('Редактор')
window.iconbitmap('Images/cat30.ico')
window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=1)


def openfile():
    filePath = askopenfilename(
        filetypes=[("Text Files", "*.txt"),
                   ("All Files", "*.*")])
    if not filePath:
        return
    textEdit.delete('1.0', END)
    with open(filePath, 'r', encoding='utf-8') as myfile:
        text = myfile.read()
        textEdit.insert(END, text)
        window.title(f'Редактируем - {filePath}')


def savefile():
    filePath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"),
                   ("Все файлы", "*.*")],
    )
    if not filePath:
        return
    with open(filePath, 'w', encoding='utf-8') as savefile:
        text = textEdit.get('1.0', END)
        savefile.write(text)
    window.title(f'Сохранили- {filePath}')


textEdit = Text(window)
textEdit.grid(row=0, column=1, sticky="nsew")
frameLeftSide = Frame(window)
frameLeftSide.grid(row=0, column=0, sticky="ns")
btnOpen = Button(frameLeftSide, text='Open', width=10, height=2, command=openfile)
btnOpen.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btnSave = Button(frameLeftSide, text='Save', width=10, height=2, command=savefile)
btnSave.grid(row=1, column=0, sticky="ew", padx=5)

window.mainloop()
