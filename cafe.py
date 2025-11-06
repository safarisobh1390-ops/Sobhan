import json
import time
import random

class Cafe:
    def __init__(self):
        self.menu = {}
        self.revenue = 0
        self.load_data()

    def load_data(self):
        try:
            with open('cafe_shop.json' , 'r') as file:
                data = json.load(file)
                self.menu = data.get('menu' , {})
        except FileNotFoundError:
            self.menu = {}
            self.revenue = 0

    def save_data(self):
        data = {
            'menu': self.menu,
            'revenue': self.revenue
        }
        with open('cafe_shop.json' , 'w') as file:
            json.dump(data , file)

    def show_menu(self):
        print('--- MENU ---')
        if not self.menu:
            print("We do not have any items!")
        else:
            for name, info in self.menu.items():
                print(f"{name} - ${info['price']} - stock : {info['stock']}")

    def add_item(self):
        name =input('Name item : ')
        if name in self.menu:
            print("We have this item in our list!")
        
        try:
            price = float(input("Price : "))
            stock =int(input("Stock : "))
        except ValueError:
            print("Invalid input!")
            return
        
        self.menu[name] = {'price' : price , 'stock' : stock}
        print('The item added!')

    def remove_item(self):
        name = input("Item name for removing : ")
        if name in self.menu:
            del self.menu[name]
            print("The item removed!")
        
        else:
            print(f"{name} did not find!")

    def order_item(self):
        costumer_choice = random.choice(list(self.menu))
        costumer_quantity =random.randint(1 , 5)
        print(f'Costumer : Hi!')
        print(f'Costumer : I want {costumer_quantity} {costumer_choice}')
        print("Do you have it?")
        print("Your choice : ")
        print("1.Yes I have!")
        print("2.No I have not!")
        choice =int(input(""))
        if choice == 1:
            name =input("Name itme : ")
            if name not in self.menu:
                print(f"{name} did not find!")
                return

            if self.menu[name]['stock'] < 0:
                print("Not enough stock!")
                return

            try:
                quantity = int(input("Quantity : "))
            except ValueError:
                print("Invalid input!")
                return

            if quantity > self.menu[name]['stock']:
                print("Out of stock!")
                return

            if quantity != costumer_quantity:
                print("Invalid input!")
                print(f"The coutumer want {costumer_quantity} {costumer_choice}")

            ask_name_coustumer = input("Coustumer name : ")
            print("Invoice :")
            print(f"Name : {ask_name_coustumer}")
            print(f'Order : {costumer_choice}')
            print(f"Quantity : {costumer_quantity}")
            print(f"It takes {totall_time} (Minute)")
            print(f"Each order price : {self.menu[name]['price']}")
            print(f"Totall price : {totall_price}")
            
            totall_price = self.menu[name]['price'] * quantity
            self.menu[name]['stock'] -= quantity
            self.revenue += totall_price
            totall_time = 10 * quantity
            print("We are making!")
            for timer in range(totall_time , -1 , -1):
                print(f"Preparing... {timer} seconds remaining")
                time.sleep(1)
        
            print(f"Order successful! Total: ${totall_price}")
            
        else:
            print("We do not have!")

    def show_revenue(self):
        print(f"Your revenue : ${self.revenue}")

    def run(self):
        while True:
            print("\n=== Coffee Shop Management ===")
            print("1. Show menu")
            print("2. Add item")
            print("3. Remove item")
            print("4. Order item")
            print("5. Show revenue")
            print("6. Save and exit")

            choice = int(input(""))
            if choice == 1:
                self.show_menu()
            elif choice == 2:
                self.add_item()
            elif choice == 3:
                self.remove_item()
            elif choice == 4:
                self.order_item()
            elif choice == 5:
                self.show_revenue()
            elif choice == 6:
                self.save_data()
                print("Data saved. Exiting...")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = Cafe()
    app.run()
