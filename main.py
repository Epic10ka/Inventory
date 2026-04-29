from time import sleep
import json

#constants
NAME = "name"
QUANTITY = "quantity"
PRICE = "price"
def invalid_opt():
    print()
    print('\033[1;91mINVALID OPTION\033[m'.center(62))
    print()

def data_save(data):
    with open('stock.json', 'w') as file:
        json.dump(data, file, indent = 4)

def data_load():
    try:
        with open('stock.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

stock = data_load()

def add_product():
    print('\033[1;97m————————————————————'.center(60))
    print('\033[1;97mNEW PRODUCT\033[m'.center(64))
    while True:
        print('\033[1;97m————————————————————'.center(60))
        product = input('                    PRODUCT NAME: ').strip().title()
        print('--------------------'.center(52))
        while True:
            try:
                quantity = int(input('                     \033[1;97mQUANTITY: \033[m'))
                break
            except ValueError:
                print()
                print('\033[1;91mError. Type only int numbers\033[m'.center(65))
                print()

        print('\033[1;97m--------------------\033[m'.center(62))

        while True:
            try:
                price = float(input('\033[1;97m                       PRICE: \033[m'))
                break
            except ValueError:
                print()
                print('\033[1;91mError. Type only numbers\033[m'.center(65))
                print()

        products = {
            NAME: product,
            QUANTITY: quantity,
            PRICE: price
        }
        #ADDING PRODUCT
        stock.append(products)
        #SAVING PRODUCT
        data_save(stock)
        print()
        while True:
            again = input('\033[1;97m              ADD MORE PRODUCTS? [Y/N]: \033[m').strip().upper()[0]

            if again == 'Y':
                break
            elif again == 'N':
                return
            else:
                invalid_opt()

def list_products():
    while True:
        if not stock:
            print()
            print('\033[1;91mNO PRODUCTS IN STOCK\033[m'.center(62))
            sleep(0.81)
            break
        print('\033[1;97m————————————————————'.center(60))
        print('PRODUCTS LIST'.center(52))
        print('————————————————————\033[m'.center(55))
        for n, product in enumerate(stock):
            print(
                f'\033[1;97mPRODUCT {n + 1}: {product[NAME]} | \033[1;92mR${product[PRICE]:.2f}\033[m | \033[1;97mQUANTITY: {product[QUANTITY]}'.center(85))
        print()
        while True:
            back = input('             BACK TO MENU? [Y/N]: \033[m').strip().upper()[0]
            if back == 'Y':
                return
            elif back == 'N':
                break
            else:
                invalid_opt()

def product_remove():
    while True:
        if not stock:
            print()
            print('\033[1;91mNO PRODUCTS IN STOCK\033[m'.center(62))
            sleep(0.8)
            break

        print('\033[1;97m————————————————————'.center(60))
        print('REMOVE PRODUCT'.center(52))
        print('————————————————————\033[m'.center(55))
        for n, product in enumerate(stock):
            print(f'   \033[1;97m[{n+1}] {product[NAME]}\033[m | \033[1;92mR${product[PRICE]:.2f}\033[m'.center(70))
        print()
        print()
        print('\033[1;97mSELECT PRODUCT\033[m'.center(62))
        print()

        try:
            remove = int(input('                        >'))-1
        except ValueError:
            invalid_opt()
            continue

        if 0 <= remove < len(stock):

            #REMOVING PRODUCT
            stock.pop(remove)
            data_save(stock)
            #DATA SAVING

            print()
            print('\033[1;92mProduct REMOVED\033[m'.center(62))
            print()

            while True:
                again = input('\033[1;97m           REMOVE ANOTHER PRODUCT? [Y/N]: \033[m').strip().upper()[0]
                if again == 'Y':
                    if not stock:
                        print()
                        print('\033[1;91mNO PRODUCTS IN STOCK\033[m'.center(62))
                        sleep(0.8)
                        return
                    break

                elif again == 'N':
                    print('\033[1;92mOK\033[m'.center(62))
                    sleep(0.6)
                    return
                else:
                    invalid_opt()
                    sleep(0.6)
        else:
            invalid_opt()
            sleep(0.6)

def main():
    while True:
        print()
        print('\033[1;97m        ╔══════════════════════════════════╗')
        print('        ║          \033[1;94mPRODUCTS STOCK\033[m          ║')
        print('\033[1;97m        ║══════════════════════════════════║')
        print('        ║        [1]ADD NEW PRODUCT        ║')
        print('        ║                                  ║')
        print('        ║        [2]LIST PRODUCTS          ║')
        print('        ║                                  ║')
        print('        ║        [3]REMOVE PRODUCTS        ║')
        print('        ║                                  ║')
        print('        ║             \033[1;91m[4]EXIT              \033[1;97m║')
        print('        ╚══════════════════════════════════╝\033[m')

        accessing = input('                        > ').strip().upper()
        match accessing:
            case '1' | 'ADD':
                add_product()
            case '2' | 'LIST':
                list_products()
            case '3' | 'REMOVE':
                product_remove()
            case '4' | 'EXIT':
                exit()
            case _:
                invalid_opt()

if __name__ == '__main__':
    main()