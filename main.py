#Import required libraries
import os
from pickle import TRUE
import subprocess

#Shows all containers with their states
#Tüm containerları gösterir
def show():
	subprocess.call("docker ps -a", shell=True)

#Shows logs given container
#Log kayıtlarını gösterir
def show_log():
    print("Var olan tüm konteynırlar şu şekildedir: \n")
    print(show() , "\n")
    containerName = input("\nLog kaydını görmek istediğiniz konteynırın ID'sini girin: \n")
    if (containerName==0) :
        print("error message")
    subprocess.run("docker logs -f --details " + containerName, shell=True)
    #Possible bug: timeout

#Stops given container
#İstenen konteynırı durdurur
def stop():
    print("Var olan tüm konteynırlar şu şekildedir: \n")
    print(show(), "\n")
    containerName = input("\nDurdurmak istediğiniz konteynırın ID'sini girin: \n")
    if (containerName==0) :
        print("error message\n")
    subprocess.run("docker stop " + containerName, shell=True)



#Shows runable functions
#Yapılabilecek fonksiyonları gösterir
def showFunctions():
	#NOT
	#BU FONKSİYON MAINDE OLMALI
	#THIS FUNCTION NEEDS TO BE IN MAIN

	#Show all functions
    print("1- Tüm konteynırları listele\n")
    print("2- Bir konteynırın logunu göster\n")
    print("3- Bir konteynırı durdurun\n")


    #Take user's choice as number
    choice = input("Lütfen istediğiniz işlemin numarasını girin:\n")

    #run chosen function
    while (choice != '0'):
        if (choice == '1'):
            return show() 
        elif (choice == '2'):
            return show_log()
        elif (choice == '3'):
            return stop()
        else:
            break

        """
        elif (choice == '2'):
            return X
        
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        """
        

print(showFunctions())

#print(stop())




