import os
c = input("Choose your environment: [0] pip : ")

if c == "0":
    os.system("pip install socket")
    os.system("pip install socks")
    os.system("pip install ssl")
    os.system("pip install argparse")
    os.system("pip install time")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install urllib.parse")
    os.system("pip install sys ")
   

if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")
