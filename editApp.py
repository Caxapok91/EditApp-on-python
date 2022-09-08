from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()

window.title('Редактор')
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
