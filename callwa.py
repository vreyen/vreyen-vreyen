import requests, Json ,os

os.system("clear")
print("\nDisarankan Spam 30 Menit Sekali")
print("Nomer Target Di Awali (8xxx)")
no = input("Nomer Target : 0")
jum = int(input("Jumlah : "))
for i  in range(jum):
  reg = requests.get("https://id.jagreward.com/member/vrifi-mobile/(no)")
  print("\nKeterangan : "+reg.Json/()["messege"])
