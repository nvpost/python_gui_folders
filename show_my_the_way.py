from tkinter import *
import tkinter.messagebox as mb
import os

import json
data = json.load(open('Invest.json', 'r', encoding='utf-8'))

window = Tk()
window.title("Найти путь")
window.geometry("800x800")

phrase = ""
folders_dict = {}

frame = Frame(
    window
)
lb = Label(
    frame,
    font=('Roboto', 15),
    text="Нужно найти устройство, кликнуть - откроется папка: "
)
lb.grid(row=5, column=2)



iz = Entry(frame)
iz.grid(row=5, column=4)

frame.config(width=100)
frame.pack(anchor="nw", pady=10)

show_akytec = False
def print_selection():
    global show_akytec
    show_akytec = not show_akytec
    doNewData(phrase)


c1 = Checkbutton(window, text='Показывать Akytec', onvalue=1, offvalue=0, command=print_selection)
c1.pack()


def go_to_folder(evt):
    global folders_dict
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print(value)
    path = folders_dict[value]
    print('path', path)
    # # path = "J:/dev/python_projects/11"
    path = os.path.realpath(path)
    if os.path.isdir(path):
        # print('есть')
        os.startfile(path)
    else:
        # print('нет')
        msg = "Нет такой папки, обратитесь к админу"
        mb.showerror("Ошибка", msg)

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

            local_path = 'P:/06_Управление жизненным циклом продуктов и услуг/Хранилище материалов/Продукты/'
            explorer_path = i['DV'] + '/' + io + '/' + gp + '/' + pd + '/' + i['IZ']

            path = local_path + i['DV'] + '/' + io + '/' + gp + '/' + pd + '/' + i['IZ']

            product_name = i['IZ'].replace(' (IZ)', '')

            folders_dict[product_name] = path
            listbox.insert(END, product_name)


    listbox.pack(fill=X, padx=5, pady=5)
    listbox.bind('<<ListboxSelect>>', go_to_folder)
    scrollbar.config(command=listbox.yview)

def clear_data(i_iz):
    if "поверка" in i_iz.lower() or "архив" in i_iz.lower():
        return False
    else:
        return True

def doNewData(p):
    global data
    global show_akytec

    nn=[]
    for i in data:
        if i['IZ'] and p in i['IZ'] and clear_data(i['IZ']):
            if show_akytec:
                nn.append(i)
            else:
                if 'Akytec' not in i['IZ']:
                    nn.append(i)
            # print(i['IZ'])
    # print ('len nn', len(nn))
    drowProducts(nn)


def keydown(e):
    global phrase
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

