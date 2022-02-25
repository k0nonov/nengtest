ipadd = input('Введите IP аддрес сети (например 10.10.10.0/24): ') or '10.10.10.0/24'
ip_oct1, ip_oct2, ip_oct3, ip_oct4 = ipadd.split('/')[0].split('.')
mask = ipadd.split('/')[1]
ip_output = '''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''
mask_output = '''Mask:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''
mask_bin = '1'*int(mask)+'0'*(32-int(mask))
mask1, mask2, mask3, mask4 = int(mask_bin[0:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:32],2)

print('\n','-'*30)
print(ip_output.format(int(ip_oct1),int(ip_oct2),int(ip_oct3),int(ip_oct4)))
print(mask_output.format(mask1,mask2,mask3,mask4))

