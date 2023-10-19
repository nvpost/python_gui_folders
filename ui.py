import json
import sys
import os
from PyQt5.QtWidgets import *

data = json.load(open('Invest.json', 'r', encoding='utf-8'))



app = QApplication(sys.argv)
mywindow = QWidget()
mylayout = QFormLayout()


mylayout.addRow(QLineEdit('Найти').keyPressEvent())
for i in data:

    io = i['IO'] if i['IO'] else ''
    gp = i['GP'] if i['GP'] else ''
    pd = i['PD'] if i['PD'] else ''

    if i['IZ']:
        folders = 'folders/'+i['DV']+'/'+io+'/'+gp+'/'+pd+'/'+i['IZ']

        mylayout.addRow(QLabel(i['IZ'] +" - "+ folders), QPushButton('Перейти'))


mywindow.setLayout(mylayout)
mywindow.show()


def keyPressEvent(event):
    print(event)

app.setStyle('Fusion')
sys.exit(app.exec_())