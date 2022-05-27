my_list = [57.8, 46.51, 97, 30.22, 12, 7, 21.38, 63.14, 18.62, 93.4]
for i in my_list:
    if type(i) == int:
        print(f'{i} руб. 00 коп.,', end="")
    else:
        new_list = str(i).split('.')
        if len(new_list[1]) == 1:
            new_list[1] = new_list[1] + '0'
        print(f'{new_list[0]} руб. {new_list[1]} коп.,', end="")
print()
print(sorted(my_list))
my_list.sort(reverse = True)
print(my_list)
new_list1 = (sorted(my_list[:5],reverse=True))
print(new_list1)
new_list1.reverse()
print(new_list1)