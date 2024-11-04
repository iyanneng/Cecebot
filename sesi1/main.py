import random

welcome_message = "WELCOME TO CECE GAMES!"
cece_positon = random.randint(1, 4)

print(welcome_message)

name_user = input("masukkan nama anda: ")

print(f'''
halo {name_user}!coba perhatikan goa di bawah ini
\_/ \_/ \_/ \_/ 
''')

pilihan_user = int(input("menurut kamu dimana CECE berada? 1 /2 /3 /4: "))

if pilihan_user == cece_positon:
    print(f"HOREEEYY {name_user} MENANG! posisi CECE ada di goa nomor {cece_positon} dan pilihanmu adalah goa nomor {pilihan_user}.")
    
else:
    print(f"YAHH KAMU KALAH, CECE bukan disitu, tapi ada di goa nomor {cece_positon} sedangkan kamu memilih goa nomor {pilihan_user}")
   