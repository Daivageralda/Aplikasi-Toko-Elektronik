#Mengimpor function dari modul file
import dumper

#Mengimpor modul eksternal
import pwinput
import time
from bcrypt import re
from termcolor import colored

#Class untuk melakukan login
class Option:

    #Menginisiasi class index didalam class option
    def __init__(self,index):
        self.index = index

    #Function untuk melakukan login
    def login(self,pesan=None):

        #variabel untuk menampung data admin dan member
        admin = self.index.database.ambil_data_admin()
        member = self.index.database.ambil_data_member()

        #Function dari modul untuk membersihkan terminal
        dumper.clear_terminal()
        print(colored("Home/Login","green"))

        #Parameter untuk menampilkan pesan saat function di return
        print()
        if pesan : print(pesan)

        print()
        #Input username dan password
        username = input("Username : ")
        password = pwinput.pwinput("Password : ")

        #Untuk verifikasi data admin dan inputan
        for idx_admin in range(len(admin)):
            if admin[idx_admin]["username"] == username and admin[idx_admin]["password"] == password:

                #Mengisi nilai variabel role dan nama dengan valuenya masing-masing
                role = admin[idx_admin]["role"]
                nama = admin[idx_admin]["nama"]
                print(colored("\nLogin Berhasil","blue"))
                time.sleep(2)

                #Mengembalikan variabel role
                return role,nama

            #untuk melanjutkan perulangan for
            else: continue

        #Untuk verifikasi data member dan inputan
        for idx_member in range(len(member)):
            if member[idx_member]["username"] == username and member[idx_member]["password"] == password:

                #Mengisi variabel role dan nama dengan valuenya masing-masing
                role = member[idx_member]["role"]
                nama = member[idx_member]["nama"]
                print(colored("\nLogin berhasil","blue"))
                time.sleep(2)

                #Mengembalikan variabel role dan nama
                return role,nama

            #Untuk melanjutkan perulangan for
            else: continue

        #Mengembalikan function login apabila user atau password salah
        return self.login(colored("Username dan password tidak cocok"))

    #Function untuk melakukan logout
    def logout(self):
        return self.index.first()
    
    #Function untuk memasukkan data diri user
    def userPrivilige(self,pesan=None):

        #Function modul untuk membersihkan terminal
        dumper.clear_terminal()

        #Variabel untuk mengambil data user
        read_user = self.index.database.ambil_data_user()

        print(colored("Home/User","green"))
        print()
        #Percabangan untuk menampilkan pesan
        if pesan : print(pesan)
        print()

        #Variabel input
        nama    = input("Nama         : ") or "User"
        email   = input("E-Mail       : ")
        alamat  = input("Alamat       : ")
        phone   = input("No. Telepon  : ")
        role    = "user"
        format_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        #Validasi input
        if not nama.isalpha() : return self.userPrivilige(colored("Format nama tidak didukung","red"))
        if not re.fullmatch(format_email,email) : return self.userPrivilige(colored("E-mail tidak valid","red"))
        if not email : return self.userPrivilige(colored("E-mail tidak valid","red"))
        if not alamat.isalnum() and not alamat:return self.userPrivilige(colored("Alamat tidak valid","red"))
        if not alamat : return self.userPrivilige(colored("Alamat tidak valid","red"))
        if not phone.isnumeric() : return self.userPrivilige(colored("Nomor telepon tidak valid","red"))
        if not phone : return self.userPrivilige(colored("Nomor telepon tidak valid","red"))

        #Variabel untuk menyimpan data
        read_user.append({
            "nama"      : nama,
            "email"     : email,
            "alamat"    : alamat,
            "phone"     : phone,
            "role"      : role
        })

        #Function untuk save data user
        self.index.database.save_data_user(read_user)
        return role,nama