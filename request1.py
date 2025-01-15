import url, request1, pprint, time
from colorama import Fore, Style, Back
from datetime import datetime
def exitt(exit1: str|float) -> None:
    if exit1 == '1':
        print("\nBizni hizmatimizdan foydalanganingizdan mamnunmiz!!!\n")
        exit()

def menu() -> None : 
    print(f"{Fore.YELLOW}Currency Converter {Fore.RESET}{Fore.GREEN}dasturiga xush kelibsiz! \n(Agar dasturni tugatmoqchi bo1lsandiz 0 buyrugidan foydalaning){Fore.RESET}")
    print(f"{Fore.CYAN}Mavjud valyutalar:{Fore.RESET}")

    requests_sums = request1.get(url.URL)

    requests_list = requests_sums.json()

    result = map(lambda x: x['code'], requests_list)
    print(f"{Fore.BLUE}{list(result)}{Fore.RESET}", end="\n\n")


def add_result(valyuta) ->None:
    
    hozirgi_vaqt = datetime.now()

    time_result = hozirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S")
    
    with open("valyuta.txt", "a") as file:
        file.write(f"{time_result} da yaratildi: {str(valyuta)}\n\n")


def return_result() -> int: 
    while True:
        try:
            summa = float(input("Summani kiriting: "))
            if summa != 0:    
                valyuta1 = input('Qaysi valyutadan konvertatsiya qilmoqchisiz (masalan, USD):')
                exitt(valyuta1)
                if valyuta1 == '0':
                    print(f"{Fore.RED}Buncha tez ketyabsiz??? {Fore.RESET}")
                    exit()

                valyuta2 = input('Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                exitt(valyuta2)
                if valyuta2 == '0':
                    print(f"{Fore.RED}Buncha tez ketyabsiz??? {Fore.RESET}")
                    exit()

                requests_sums = request1.get(url.URL)

                requests_list = requests_sums.json()
                
                count_check = 0

                if valyuta1.upper() == 'UZS':
                    while True:
                        for valyuta in requests_list: 
                            if valyuta2.upper() == valyuta["code"]:
                                result = f"Natija: {summa} UZS = {round(summa / float(valyuta['cb_price']), 2)} {valyuta['code']}"
                                add_result(result)
                                print(f"\n{Fore.LIGHTCYAN_EX}Natija: {summa} UZS = {round(summa / float(valyuta['cb_price']), 2)} {valyuta['code']}{Fore.RESET}")
                                count_check +=1
                                break
                        if count_check == 0:
                            print(f"\n{Fore.RED}Siz kiritgan ->{Fore.YELLOW} '{valyuta2}' {Fore.RESET}{Fore.RED}valyuta mavjud emas, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
                            valyuta2 = input(f'Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                            exitt(valyuta2)
                        else:
                            break
                else:
                    count_check = 0
                    while True:
                        for valyuta in requests_list:
                            if valyuta1.upper() == valyuta['code']:
                                while True:
                                    for val in requests_list:
                                        if valyuta2.upper() == val['code']:
                                            count_check +=1
                                            result = f"\nNatija: {summa} {valyuta['code']} = {round(float(valyuta['cb_price']) / float(val['cb_price'])*summa, 2)} {val['code']}"
                                            add_result(result)
                                            print(f"\n{Fore.LIGHTCYAN_EX}Natija: {summa} {valyuta['code']} = {round(float(valyuta['cb_price']) / float(val['cb_price'])*summa, 2)} {val['code']}{Fore.RESET}")        
                                    if count_check == 0:
                                        print(f"\n{Fore.RED}Siz kiritgan -> {Fore.YELLOW}'{valyuta2}'{Fore.RED} valyuta mavjud emas, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
                                        valyuta2 = input('Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                                        exitt(valyuta2)
                                    else:
                                        break  
                        if count_check == 0:
                            print(f"\n{Fore.RED}Siz kiritgan -> {Fore.YELLOW}'{valyuta1}' {Fore.RED}valyuta mavjud emas, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
                            valyuta1 = input('Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                            exitt(valyuta1)
                        else:
                            break  
            
            else:
                print(f"{Fore.RED}Buncha tez ketyabsiz??? {Fore.RESET}")
                exit()
        except ValueError:
                        
            print(f"{Fore.RED}Faqat butun yoki float son kiriting!{Fore.RESET}\n")
            

            