#Mengimpor modul
import json

#Class untuk melakukan transfering dua arah dari database ke program
class Database:

    #Menginisiasi index agar fungsi didalam class ini dapat digunakan
    #di class yang lain
    def __init__(self,index):
        self.index = index
        
    #Mengambil data pada database admin
    def ambil_data_admin(self):
        with open("database\\admin.json",mode="r") as admin_data:
            data_admin = json.load(admin_data)
            return data_admin

    #Membuat dan menyimpan database admin
    def save_data_admin(self,data_admin):
        with open("database\\admin.json",mode="w") as admin_data:
            json.dump(data_admin,admin_data,indent=4)
 
    #Mengambil data pada database member
    def ambil_data_member(self):
        with open("database\\member.json",mode="r") as member_data:
            data_member = json.load(member_data)
            return data_member

    #Membuat dan menyimpan database member
    def save_data_member(self,data_member):
        with open("database\\member.json",mode="w") as member_data:
            json.dump(data_member,member_data,indent=4)

    #Mengambil data pada database barang
    def ambil_data_barang(self):
        with open("database\\item.json",mode="r") as barang_data:
            data_barang = json.load(barang_data)
            return data_barang

    #Membuat dan menyimpan database barang
    def save_data_barang(self,data_barang):
        with open("database\\item.json",mode="w") as barang_data:
            json.dump(data_barang,barang_data,indent=4)

    #Mengambil data pada database order
    def ambil_data_order(self):
        with open("database\\order.json",mode="r") as order_data:
            data_order = json.load(order_data)
            return data_order

    #Membuat dan menyimpan database order
    def save_data_order(self,data_order):
        with open("database\\order.json",mode="w") as order_data:
            json.dump(data_order,order_data,indent=4)

    #Mengambil data pada database user
    def ambil_data_user(self):
        with open("database\\user.json",mode="r") as user_data:
            data_user = json.load(user_data)
            return data_user
            
    #Membuat dan menyimpan database order
    def save_data_user(self,data_user):
        with open("database\\user.json",mode="w") as user_data:
            json.dump(data_user,user_data,indent=4)