#! bin/python3


import getpass
from  instaloader import *



print("\n\n*********** IG NOOB OSINT ***********")

class IGram:
    def __init__(self):
        self.chose = int(input("""

chose the options
                               
[1] download all content from target
[2] show all follower from target
[3] show all following from target
[0] exit
                               
[+] chose options: """))
        
        self.deklar = Instaloader()

    @property
    def target(self):
        targe = input("[+] username target: ")
        return targe
    
    @property
    def run(self):
        match self.chose:
            case 1:
                print(f"opsi {self.chose} download all content\n")
                try:
                    downld = instaloader.Instaloader().download_profile(self.target, profile_pic_only=False)
                    if downld:
                       print("downloading.............")
                    else:
                       pass
                    print("download successfuly")

                except (instaloader.ConnectionException, ConnectionAbortedError, ConnectionError) as error:
                    print("cheking your connection", error)

                except (SyntaxError, ValueError, NameError) as err:
                    print("checking your source code", err)


            case 2:
                print(f"opsi {self.chose} show followers\n")
                print("login to your account instagram")
                try:
                    login =  self.deklar.login(user=input("[+] your username: "), passwd=getpass.getpass())
                    coon = instaloader.Profile.from_username(self.deklar.context, self.target)
                    print("\n")
                    print("username: ", coon.full_name)
                    print("userid: ",  coon.userid)
                    print("num flowr: ", coon.followers)
                    print("num fwigs: ", coon.followees)
                    print("bio: ", coon.biography)
                    print("url bio: ", coon.external_url)
                    print("\n")
                    if coon:
                         show = coon.get_followers()
                         for look in show:
                             print(look)
                    else:
                        print("login gagal coba lagi")
                        print("tidak tau bahasa ingris")

                except (instaloader.ConnectionException, ConnectionError) as e:
                    print("checking your connection and try again", e)

                except (SyntaxError, ValueError, NameError) as err:
                    print("checking your source code", err)
                
            case 3:
                print(f"opsi {self.chose} download all followers\n")
                print("login to your account instagram")
                try:
                    login = self.deklar.login(user=input("[+] your username: "), passwd=f"[+] your {getpass.getpass()}")
                    coon = instaloader.Profile.from_username(self.deklar.context, self.target)
                    print("\n")
                    print("username: ", coon.full_name)
                    print("userid: ",  coon.userid)
                    print("num flowr: ", coon.followers)
                    print("num fwigs: ", coon.followees)
                    print("bio: ", coon.biography)
                    print("url bio: ", coon.external_url)
                    print("\n")
                    if coon:
                         show = coon.get_followees()
                         for look in show:
                             print(look)
                    else:
                        print("login gagal coba lagi")
                        print("tidak tau bahasa ingris")

                except (instaloader.ConnectionException, ConnectionError) as e:
                    print("checking your connection and try again", e)

                except (SyntaxError, ValueError, NameError) as err:
                    print("checking your source code", err)


            case 0:
                pass    

            
            

ob = IGram()

ob.run
                        
                
        


    
