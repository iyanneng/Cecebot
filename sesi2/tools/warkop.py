import mains

def start():
    while True:
        print('ini warkop silahkan bayar didepan')
        harga=int(input ('total harga: '))
        
        if harga == 0:
            mains.menu()
    
if __name__ == '__main__':
    start()