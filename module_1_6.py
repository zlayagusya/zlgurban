my_dict = {'Maxim': 1998, 'Darya': 1999, 'Vadim': 1988}
print('Dict:', my_dict)
print('Existing value:', my_dict['Darya'])
print('Not existing value:',my_dict.get('Anton'))
my_dict.update({'Car': 'honda', 'car': 'mitshubishi'})
print('Modified dictionary:',my_dict)
a = my_dict.pop('Darya')
print('Deleted value:', a)
my_set = {1,1,2,3,'manager','manager', 1.5,'sister',(1,2,3),(1,2,3)}
print('Set:', my_set)
my_set.add('mother')
print('Modified set:',my_set)
my_set.remove('sister')
print('Deleted value:', my_set)