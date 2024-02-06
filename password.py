#密碼重試程式
password = 'a123456'
count = 4
while count>0:
	attempt = input('請輸入密碼')
	if attempt == password:
		print('登入成功')
		break
	elif attempt != password:
		print(f'密碼錯誤!還有{count-1}次機會!')
		count -= 1
	if count == 0:
		print('沒有嘗試機會了試著登入信箱')
		break