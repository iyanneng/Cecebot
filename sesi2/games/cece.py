import random
import mains

def start():
    while True:
        bentuk_goa = "|_|"
        goa_gosong =[bentuk_goa] * 4 
        
        cece_position = random.randint(1, 4)
        
        goa = goa_kosong.copy()
        goa[cece_position - 1] = "|0_0|"
        
        goa_kosong = ' '.join(goa_gosong)
        goa = ' '.join(goa)
        
        print(f'Coba perhatikan goa dibawah ini\n\n{goa_kosong}\n')
        
        pilihan_user = int(input("menurut kamu di goa nomor berapakah CECE berada? [1, 2, 3, 4]: "))
        
        if pilihan_user == cece_position :
            print(f"\n\nSelamat kamu menang")
            
        else :
            print(f"\n{goa}\n\nDuhhh kamu salah")
            
        play_again = input("\n\napakah ingin melanjutkan gamenya lagi? [y/n]")
        if play_again == "n":
            mains.menu()
        
if __name__ == '__main__':
    start()