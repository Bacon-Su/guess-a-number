import random

start = input('請輸入開始的數值:')
end = input('請輸入結束的數值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
print(r)

count = 0

while True:
	num = input('請輸入數字:')
	num = int(num)
	count += 1
	if num == r:
		print('你猜中了!')
		print('你總共猜了', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print ('比答案小') 
	print('你已經猜了', count, '次')