#
indexes = []
values = []
list_new = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in list_new:
    if i.isdigit() == True:
        index = list_new.index(i)
        indexes.append(index)
        values.append(i)

    if i[0] == '+':
        index = list_new.index(i)
        indexes.append(index)
        values.append(i)

indexes_rev = list(reversed(indexes))
values_rev = list(reversed(values))
count = len(values_rev)
for j in values_rev:
    index_1 = values_rev.index(j)
    if len(j) == 1:
        new_str = '0'+j
        list_new.pop(indexes_rev[index_1])
        list_new.insert(indexes_rev[index_1], '"')
        list_new.insert(indexes_rev[index_1]+1, new_str)
        list_new.insert(indexes_rev[index_1]+2, '"')
    elif j[0]== '+':
        new_str_1 = j.lstrip('+')
        if len(new_str_1) == 1:
            new_str_1 = '+0' + new_str_1
            list_new.pop(indexes_rev[index_1])
            list_new.insert(indexes_rev[index_1] , '"')
            list_new.insert(indexes_rev[index_1]+1, new_str_1)
            list_new.insert(indexes_rev[index_1] + 2, '"')
    else:
        new_str_1 = j
        list_new.pop(indexes_rev[index_1])
        list_new.insert(indexes_rev[index_1], '"')
        list_new.insert(indexes_rev[index_1] + 1, new_str_1)
        list_new.insert(indexes_rev[index_1] + 2, '"')
print(' '.join(list_new))

