import json
import os

# Загрузка данных из файла Invest.json
data = json.load(open('Invest.json', 'r', encoding='utf-8'))

# Обход каждого элемента в данных
def full_folders():
    for i in data:

        # Присвоение значения переменной io, если i['IO'] существует, иначе пустая строка
        io = i['IO'] if i['IO'] else ''

        # Присвоение значения переменной gp, если i['GP'] существует, иначе пустая строка
        gp = i['GP'] if i['GP'] else ''

        # Присвоение значения переменной pd, если i['PD'] существует, иначе пустая строка
        pd = i['PD'] if i['PD'] else ''

        # Проверка наличия i['IZ']
        if i['IZ']:
            # Формирование пути к папке вида 'folders/{DV}/{IO}/{GP}/{PD}/{IZ}'
            folders = 'folders/'+i['DV']+'/'+io+'/'+gp+'/'+pd+'/'+i['IZ']

            # Проверка существования папки folders/{DV}/{IO}/{GP}/{PD}/{IZ}
            if not os.path.exists(folders):
                # Создание папки folders/{DV}/{IO}/{GP}/{PD}/{IZ}, если она не существует
                os.makedirs(folders)


def short_folders():
    for i in data:

        # Присвоение значения переменной io, если i['IO'] существует, иначе пустая строка
        io = i['IO'] if i['IO'] else ''

        # Присвоение значения переменной gp, если i['GP'] существует, иначе пустая строка
        gp = i['GP'] if i['GP'] else ''

        # Присвоение значения переменной pd, если i['PD'] существует, иначе пустая строка
        pd = i['PD'] if i['PD'] else ''

        # Проверка наличия i['IZ']
        if i['IZ']:
            # Формирование пути к папке вида 'folders/{DV}/{IO}/{GP}/{PD}/{IZ}'
            folders = 'folders/' + i['DV'] + '/' + io + '/' + gp + '/' + pd + '/' + i['IZ']

            io = io.replace(' (IO)', '')
            iz = i['IZ'].replace(' (IZ)', '')
            short_folders = 'short_folders/' + io + '/' + iz

            # Проверка существования папки folders/{DV}/{IO}/{GP}/{PD}/{IZ}
            if not os.path.exists(short_folders):
                # Создание папки folders/{DV}/{IO}/{GP}/{PD}/{IZ}, если она не существует
                os.makedirs(short_folders)

short_folders()