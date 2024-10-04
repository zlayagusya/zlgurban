immutable_var = (1, "inviseble", True, 'a')
print('Immutable tuple:', immutable_var)
#immutable_var[0] = 5
#print(immutable_var) - ошибка
# кортеж, тип данных tuple (неизменяемый тип данных) - значения внутри кортежа неизменяемы и
# назначаются единожды)
mutable_list = [1, 3, "football", False]
mutable_list[2] = 'hockey'
mutable_list[3] = 'True'
mutable_list[0] = 15
print('Mutable list:',mutable_list)