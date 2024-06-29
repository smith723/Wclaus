#! bin/python3


import getpass
from  instaloader import *



class instagram_downloader:
    user_name = input("[+] username target: ")
    def __init__(self):
        self.user_name = input("[+] masukan user name instagram anda: ")
        self.password  = getpass.getpass() 
        self.deklarasi = Instaloader()
        self.login = self.deklarasi.login(self.user_name, self.password)
        self.dek =  instaloader.Profile.from_username(self.deklarasi.context, instagram_downloader.user_name)

    def show_fwers(self):
            try:
                follower = self.dek.get_followers()
                print("tunggu sedang di proses.....")
                for lihat in follower:
                    print(lihat)
                print("selesai.....")
            except (NameError, ValueError, SyntaxError):
                    print("ada kesalahan pada code")

            except ConnectionException:
                    print("periksa konesi dan coba lagi")

    def show_fwings(self):
        try:
            followings = self.dek.get_followees()
            print("\ntunggu sedang di prosess....\n")
            for show in followings:
                print(show)
            print("selesai.......")

        except (ValueError, SyntaxError):
                print("ada kesalahan pade code")

        except instaloader.ConnectionException:
                print("periksa konesi dan coba lagi")        

    def download_p(self):
         print(F"profile [{instagram_downloader.user_name}] sedang di download")
         instaloader.Instaloader().download_profile(instagram_downloader.user_name)
         print("download selesai,,,,,")
         


    def run(self):
        opsi = int(input("""
____opsi___
            
[1] look followers
[2] show followings
[3] download isi profile
[0] exit
                         
masukan opsi: """))
        match opsi:
            case 1:
               self.show_fwers()

            case 2:
                self.show_fwings()
              
                    
            case 3:
                self.download_p()
            case 0:
                pass

                    
                

ob = instagram_downloader()
ob.run()
