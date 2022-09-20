import subprocess

macchanger_question1 = input("\nMac Adresinizi degitirmek ister misiniz? [Y/n] : ")

if macchanger_question1 == 'Y':
	
	macchanger_question2 = int(input("\n(1) kendi MAC adresim\n(2) rastgele MAC adresim\ncevap : "))
	
	match macchanger_question2:
		
		case 1:
			
			mac_adress = input("\nmac adresini giriniz : ")
			print("\n")	
			
			subprocess.call(["iwconfig"])
			interface = input("\narayüzünüzü giriniz : ")
			print("\nmac adresi işlemizniz başlatıldı")

			subprocess.call(["ifconfig",interface,"down"])
			subprocess.call(["ifconfig",interface,"hw","ether",mac_adress])
			subprocess.call(["ifconfig",interface,"up"])
			print("\n")
			
			with open("/sys/class/net/eth0/address") as myselfmacadress:
				system_mac_address = myselfmacadress.read().rstrip()
			
			
			subprocess.call(["ifconfig"]) 
			
		case 2:
			
			print("\n")
			subprocess.call(["iwconfig"])
			interface = input("\narayüzünüzü giriniz : ")
			print("\nmac adresi işlemizniz başlatıldı\n")
			subprocess.call(["ifconfig",interface,"down"])
			subprocess.call(["macchanger","-r",interface])
			subprocess.call(["ifconfig",interface,"up"])
			print("mac adresiniz değişti")
			
			print("\n")
			subprocess.call(["ifconfig"])
			
		case _:
			
			print("hatalı tuşlama yaptınız")
			
elif macchanger_question1 == 'n':
	
	print("MAC adresi değiştirilmiyor")
	
else :
	
	print("Hatalı tuşlama yaptınız")		
