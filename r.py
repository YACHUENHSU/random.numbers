import random
start = input('請隨機決定數字範圍開始值: ')
end = input('請隨機決定數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
i = 0
while True:
	num = input('請猜個數字: ')
	num = int(num)
	i = i + 1
	if num == r:
		print('恭喜您猜對')
		print('你總共猜了',i,'次')
		break
	else:
		if num > r:
			print('要小於這個數字')
		elif num < r:
			print('要大於這個數字唷')
	print('這是你猜的第',i,'次')
