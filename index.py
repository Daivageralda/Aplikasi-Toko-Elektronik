#Mengimpor function dari modul file
import dumper
from termcolor import colored
#Mengimpor class dari file dan direktori berbeda
from opt import Option

from data import Database

from menu.adminMenu import menuAdmin
from menu.userMenu import menuUser

from controller.barang import tadbirBarang

from user.userShow import dataDiri

#Class pertama yang dijalankan
#Class untuk menampung seluruh class dari file terpisah
class Index:

    #Menginisiasikan tiap class
    def __init__(self):
        self.option = Option(self)

        self.database = Database(self)

        self.menuadmin = menuAdmin(self)
        self.menuuser = menuUser(self)

        self.tatBar = tadbirBarang(self)

        self.datDir = dataDiri(self)
        #Function yang akan dijalankan pertama kali
        self.first()

    #Function untuk mengambil nilai role dan nama dari funtion login
    #pada class Option
    def first(self,pesan=None,keluar = False):

        #Modul yang berisi function untuk membersihkan terminal
        dumper.clear_terminal()
        print(colored("Home","green"))
        print()

        #Percabangan untuk menghentikan program
        if keluar == True:print("\nTerimakasih :)"),exit()
        if pesan : print(pesan),print()

        print("[1] Login")
        print("[2] User")
        print("[3] Exit")

        choose = input("Choose : ")

        #Percabangan login admin dan member
        if choose == "1":

            #Variabel untuk menjalankan login dan mengambil value (dari return function
            role = self.option.login()

            #Percabangan untuk mengecek nilai role
            if role != None: return self.masuk_menu(role)

        #Percabangan login user
        elif choose == "2":

            #Variabel untuk menjalankan login dan mengambil value dari return function
            role = self.option.userPrivilige()
            
            #Percabangan untuk mengecek nilai role
            if role != None: return self.masuk_menu(role)

        #Percabangan untuk end program
        elif choose == "3": return self.first("Terimakasih :)",True)

        #Percabangan untuk mengembalikan function apabila kondisinya else
        else : return self.first(colored("Input salah","red"),False)

    #Function untuk menjalankan menu sesuai role dari akun terkait
    def masuk_menu(self,role):
        if role[0] == "admin" : return self.menuadmin.menu(role)
        elif role[0] == "member"or"user" : return self.menuuser.menu(role)