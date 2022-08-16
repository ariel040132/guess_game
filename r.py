import random

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1  # count += 1
	num = input("請輸入1~100的隨機數：")
	num = int(num)
	if num == r:
		print("這是你猜的第", count, "次")
		print("恭喜，猜對了！")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("這是你猜的第", count, "次")
		