
import sys
import requests

def ascii():
    print("""


   	_                                      _         _   
    | |  __ _ __   __ __ _  ___   ___  _ __ (_) _ __  | |_ 
 _  | | / _` |\ \ / // _` |/ __| / __|| '__|| || '_ \ | __|
| |_| || (_| | \ V /| (_| |\__ \| (__ | |   | || |_) || |_ 
 \___/  \__,_|  \_/  \__,_||___/ \___||_|   |_|| .__/  \__|
                                               |_|         
 __  __  _         _   __  _             
|  \/  |(_) _ __  (_) / _|(_)  ___  _ __ 
| |\/| || || '_ \ | || |_ | | / _ \| '__|
| |  | || || | | || ||  _|| ||  __/| |   
|_|  |_||_||_| |_||_||_|  |_| \___||_|   
                                         


Thx To Ardho
go follow Ig
https://instagram.com/ardho.ainullah

Support by 
Fakhri Alauddin
https://instagram.com/fakhrialauddin13

""")


ascii()

try:
    js_file = input("==> Masukkan File (/path/file.js) : ")
    with open(js_file, 'r') as c:
         js = c.read()
except FileNotFoundError:
       sys.exit("==> File Tidak Ditemukan")

payload = {'input': js}
url = 'https://javascript-minifier.com/raw'
print("Requesting mini-me of {}. . .".format(c.name))
result = requests.post(url, payload).text

rename = input("==> Mau Ganti Nama File? (default:file.min.js) (y/n) : ")
if rename.upper() == "Y":
   named = input("==> Nama File Baru (ex: script.min.js) : ")
elif rename.upper() == "N":
       named = "%s.min"%(str(c.name))
else:
     print ("[!] option false");sys.exit()

with open(named, 'w') as m:
     m.write(result)

print("Minification complete. See {}".format(m.name))