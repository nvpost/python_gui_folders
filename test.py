from tkinter import *
from tkinter.ttk import *

import json
data = json.load(open('Invest.json', 'r', encoding='utf-8'))

window = Tk()
window.title("Найти путь")
window.geometry("800x800")




# frame = Frame(
#     window,
#     padx=10,
#     pady=10
# )

# frame.pack(expand=True)

lb = Label(
    window,
    text="Нужно найти устройство и кликнуть - откроется папка"
)
lb.pack()


iz = Entry(window)
iz.pack()


def go_to_folder(folders):
    print(folders)

listbox = False
scrollbar = False
def drowProducts(data):

    global listbox
    global scrollbar
    if listbox:
        listbox.destroy()
    if scrollbar:
        scrollbar.destroy()


    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(window, yscrollcommand=scrollbar.set, height=100)
    for i in data:

        io = i['IO'] if i['IO'] else ''
        gp = i['GP'] if i['GP'] else ''
        pd = i['PD'] if i['PD'] else ''

        if i['IZ']:
            folders = 'folders/' + i['DV'] + '/' + io + '/' + gp + '/' + pd + '/' + i['IZ']
            product_name = i['IZ'].replace(' (IZ)', '')
            listbox.insert(END, product_name)

    listbox.pack(fill=X, padx=5, pady=5)
    listbox.bind('<<ListboxSelect>>', lambda _: go_to_folder(folders))
    scrollbar.config(command=listbox.yview)


def doNewData(p):
    global data
    nn=[]
    if p == '':
        drowProducts(data)
        return
    for i in data:
        if i['IZ'] and p in i['IZ']:
            nn.append(i)
            # print(i['IZ'])
    print (len(nn))
    drowProducts(nn)

phrase = ""
def keydown(e):
    global phrase
    global iz
    print('iz', iz.get())
    print(e.keycode)

    if e.keycode == 8:
        # Удаление символа
        phrase = phrase[:-1]
    else:
        phrase = phrase + e.char
    doNewData(phrase)
    print('phrase', phrase)

iz.bind("<KeyPress>", keydown)





doNewData("")



window.mainloop()







