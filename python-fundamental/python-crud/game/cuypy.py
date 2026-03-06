import random
import main

def start():
    while True:
        bentuk_goa = "|_|"
        banyak_goa = [bentuk_goa] * 4

        cuypy_position = random.randint(1,3)
        goa = banyak_goa.copy()
        goa[cuypy_position] ="|_|"

        banyak_goa[cuypy_position - 1] = "|0_0|"

        goa = '  '.join(goa)
        banyak_goa = '  '.join(banyak_goa)
        print(f'\ncoba perhatikan goa dibahaw ini\n{goa} ')


        pilihan_pemain = int(input("\nmenurut kamu di goa nomor berapa cuypay berada?: "))



        # jawaban
        if pilihan_pemain == cuypy_position:
            print(f"{banyak_goa} \n\n Selamat kamu benar cuypy berada di goa nomor {cuypy_position}, KAMU MENANG!!")   
        else:
            print(f"{banyak_goa} \n yah,kamu salah CUYPY bukan berada di goa nomor{pilihan_pemain} tapi ada di goa nomor{cuypy_position},COBA LAGII!!")
        
        play_again = input("\n\napakah kamu ingin mengulang game nya?[y/n]")
        if play_again == "n":
           main.menu()

if __name__ == '__main__':
    start()
       
    