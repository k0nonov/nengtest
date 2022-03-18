ip = input('Введите IP (пример 10.0.1.1): ') or '10.0.1.1'



if int(ip.split('.')[0]) <= 223:
	print('Unicast')
elif int(ip.split('.')[0]) in range(224,239):
	print('Multicast')
elif ip == '255.255.255.255':
	print('Local broadcast')
elif ip == '0.0.0.0':
	print('Unassigned')
else:
	print('Unused')

