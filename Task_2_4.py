my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in my_list:
    new_list = i.split(' ')
    name = new_list[-1]
    print('Привет ' + name.capitalize() + '!')
