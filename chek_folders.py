import os

import json
data = json.load(open('Invest.json', 'r', encoding='utf-8'))
not_counter = 0
c = 0
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

        path = os.path.realpath(path)
        if not os.path.isdir(path):
            not_counter +=1
            print(product_name, 'нет', explorer_path)
        else:
            c +=1

print('нет вот столько: ', not_counter)
print('есть вот столько: ', c)

