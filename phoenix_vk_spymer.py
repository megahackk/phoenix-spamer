try:
	import time
	import os
	import vk_api
except:
	i=print("[Для работы нужно установить модули]")
	pass


try:
	print(i)
except:
	i="[Программа запущена]"
else:
	pass


print(" ")
print(" ")

p=1
count=1

if i=="[Для работы нужно установить модули]":
	pass
else:
	i=""


def send(text,d):
	global count
	if d==1:
		vk1.messages.send(peer_id=-94631511,message=text, random_id=count )
		count=count+1	
	elif d==2:
		vk2.messages.send(peer_id=-94631511,message=text, random_id=count )
		count=count+1

def doses():
	global vk1
	global vk2
	global ses1
	global ses2

	if work_mod==0:
		ses1=vk_api.VkApi(token=tok1)
		vk1=ses1.get_api()
	else:
		ses2=vk_api.VkApi(token=tok2)
		vk2=ses2.get_api()
		ses1=vk_api.VkApi(token=tok1)
		vk1=ses1.get_api()
		


def GetToks():
	global tok1
	global tok2
	global work_mod
	global i
	tok1=input("Введите первый токен: ")
	a=input("Второй токен?  Y/N ")
	if a=="n":
		work_mod=0
	elif a=="y":
		tok2=input("Введите второй токен: ")
		work_mod=1
	else:
		i="[Неверный ввод токенов]"
	doses()
	i="[Токен/ы введен/ы]"
	main()

def GetNum():
	global i
	global num
	num=input("Введите номер:")
	i="[Номер установлен]"
	main()

def GetTime():
	global i
	global timeq
	print("1 час-3600 секунд")
	timeq=input("Введите время")
	i="[Время в "+ str(timeq) +" секунд установлено]"
	main()


def start():
	global i
	print("")
	try:
		timeq=timeq+timeq
	except:
		timeq=0
	else:
		pass
	print("[Работа...]")
	time.sleep(timeq)
	if work_mod==0:
		onetok()
	elif work_mod==1:
		twotok()
	main()




def onetok():
	global num
	global p
	try:
		send(num,1)
		time.sleep(9)
		send("Ввести другой номер телефона",1)
	except:
		print("[Ошибка...]")
		time.sleep(9)
		onetok()
	else:
		print("[Запрос отправлен "  +str(p)+"]")
		time.sleep(9)
		p=p+1
		onetok()




def twotok():
	global num
	global p
	try:
		send(num,1)
		time.sleep(9)
		send("Ввести другой номер телефона",1)
		send(num,2)
		time.sleep(9)
		send("Ввести другой номер телефона",2)
	except:
		print("[Ошибка...]")
		time.sleep(9)
		twotok()
	else:
		print("[Запрос отправлен "  +str(p)+"]")
		print("[Запрос отправлен "  +str(p+1)+"]")
		p=p+2
		twotok()		

def moduls():
	global i
	print("[Загрузка...]")
	os.system("pip install vk_api")
	i="[Модуль загружен]"
	main()

def upd():
	global i
	func=input("Вы уверены что хотите обновить Y/N ")
	if func=="y":
		os.system("cd && rm -rf phoenix-spamer && git clone https://github.com/megahackk/phoenix-spamer && cd phoenix-spamer && python3 phoenix_vk_spymer.py")
	elif func=="n":
		i="[Обновление отменено]"
	else:
		print("")
		print("[Неверный ввод]")
		print(" ")
		upd()


def main():
	global i
	os.system('cls' if os.name=='nt' else 'clear')
	print("!!!"+i+"!!!")
	print(" ")
	print("Phoenix spamer by vk_api")
	print("Version-2.0")
	print("1;{[Вводы токена}]")
	print("2;{[Ввод номерa}]")
	print("3;{[Установка таймера}]")
	print("4;{[Мой ютуб канал}]")
	print("5;{[Запуск спамера}]")
	print("6;{[Установка модулей}]")
	print("7;{[Обновление}]")
	print("")
	func=input("Что будем делать: ")
	if   func==str(1):
		GetToks()
	elif func==str(2):
		GetNum()
	elif func==str(3):
		GetTime()
	elif func==str(4):
		print("")
		print("https://www.youtube.com/channel/UCC0-w64BrjxtcFfLE9wAJBQ")
	elif func==str(5):
		start()
	elif func==str(6):
		moduls()
	elif func==str(7):
		upd()
	else:
		print("")
		main()
main()
