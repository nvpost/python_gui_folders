from tkinter import *

import json
data = json.load(open('Invest.json', 'r', encoding='utf-8'))

window = Tk()
window.title("Найти путь")
window.geometry("400x600")


def on_select(folders):
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

            # frame = Frame(
            #     window,
            #     padx=10,
            #     pady=3
            # )
            # frame.pack(expand=True)
            #
            # lb = Label(
            #     frame,
            #     text=i['IZ']
            # )
            listbox.insert(END, i['IZ'])
            # lb.grid(row=5, column=1)
            #
            # cal_btn = Button(
            #     frame,
            #     text="Открыть",
            #     command=lambda: openFolder(folders),
            #
            # )
            # cal_btn.grid(row=5, column=2)
    listbox.pack(fill=X, padx=5, pady=5)
    listbox.bind('<<ListboxSelect>>', lambda _: on_select(folders))
    scrollbar.config(command=listbox.yview)


def openFolder(p):
    print(p)


def doNewData(p):
    global data
    nn=[]

    for i in data:
        if i['IZ'] and p in i['IZ']:
            nn.append(i)
            print(i['IZ'])

    print (len(nn))
    drowProducts(nn)

phrase = ""
def keydown(e):
    global phrase
    phrase += e.char
    doNewData(phrase)
    print(phrase)






iz = Entry(window)

iz.bind("<KeyPress>", keydown)

iz.pack()



doNewData("")



window.mainloop()







