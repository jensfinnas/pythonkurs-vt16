# coding:  utf-8

import csvkit

fil = open("valresultat_2014.csv", 'rb')
csv_lasare = csvkit.DictReader(fil, delimiter=',')

for rad in csv_lasare:
    print(rad)

