import random

r = random.randint(1,100)
while True:
	num = input('請猜個數字: ')
	num = int(num)
	if num == r:
		print('恭喜您猜對')
		break
	else:
		if num > r:
			print('要小於這個數字')
		elif num < r:
			print('要大於這個數字唷')
