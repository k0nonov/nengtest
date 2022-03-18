correct_ip = False
while not correct_ip:
    ip = input('Введите IP (пример 10.0.1.1): ') or '10.0.1.1'
    correct_ip = True

    if len(ip.split('.')) != 4:
        correct_ip = False
    else:
        for i in ip.split('.'):
            if not (i.isdigit() and int(i) in range(256)):
                correct_ip = False
                break

    if not correct_ip:
        print('Неправильный Адресс')
    else:
        if 1 <= int(ip.split('.')[0]) <= 223:
            print('Unicast')
        elif int(ip.split('.')[0]) in range(224,239):
            print('Multicast')
        elif ip == '255.255.255.255':
            print('Local broadcast')
        elif ip == '0.0.0.0':
            print('Unassigned')
        else:
            print('Unused')
