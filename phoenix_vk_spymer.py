import vk_api
import time

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")



tok=input("введите токен:")
count=input("введите переменную для работы с параметром рандом айди:")
num=input("введите номер:")
count=int(count)
p=1

ses=vk_api.VkApi(token=tok)
vk=ses.get_api()

def sen(text):
	global count

	vk.messages.send(peer_id=-94631511,message=text, random_id=count )
	count=count+1

def spam():
	global p
	try:
		sen(num)
		time.sleep(9)
		sen("Ввести другой номер телефона")
	except:
		print("error")
		time.sleep(9)
		spam()
	else:
		p=str(p)
		print("запрос отправлен" " " +p)
		time.sleep(9)
		p=int(p)
		p=p+1
		spam()
spam()