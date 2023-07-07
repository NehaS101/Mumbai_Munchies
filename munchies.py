class Snack:
    def __init__(self,snack_id,name,price,available):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.available = available

class Canteen:
    def __init__(self):
        self.inventory =[]
        self.sales_records=[]

    def add(self,snack):
        self.inventory.append(snack)

    def remove(self,snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack.id:
                self.inventory.remove(snack)
                break
            else:
                print("Snack not found") 

    def update(self,snack_id,available):
        for snack in self.inventory:              
            if snack.snack_id == snack.id:
                snack.available = available
                break
            else:
                print("Snack not found")

    def recorder(self,snack_id):
          for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.available:
                    self.sales_records.append(snack)
                    snack.available = False
                    print(f"Sale recorded for {snack.name}.")
                else:
                    print(f"{snack.name} is not available.")
                break
            else:
                 print("Snack not found in inventory.")     
    
    def display(self):
        print("Snack Inventory:")
        for snack in self.inventory:
            print(f"ID: {snack.snack_id}\tName : {snack.name}\tprice : {snack.price}\tAvailable : {snack.available}")

    def display_Sales(self):             
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"ID: {snack.snack_id}\tName: {snack.name}\tPrice: {snack.price}")

def main():
    canteen = Canteen()

    while True:
        print("\nCanteen Management System")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Record Sale")
        print("5. Display Inventory")
        print("6. Display Sales Records")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            snack_id = input("Enter snack ID: ")
            name = input("Enter snack name: ")
            price = float(input("Enter snack price: "))
            available = input("Is the snack available? (yes/no): ").lower() == "yes"
            snack = Snack(snack_id, name, price, available)
            canteen.add(snack)
            print("Snack added to inventory.")

        elif choice == "2":
            snack_id = input("Enter snack ID: ")
            canteen.remove(snack_id)

        elif choice == "3":
            snack_id = input("Enter snack ID: ")
            available = input("Is the snack available? (yes/no): ").lower() == "yes"
            canteen.update(snack_id, available)

        elif choice == "4":
            snack_id = input("Enter snack ID: ")
            canteen.recorder(snack_id)

        elif choice == "5":
            canteen.display()

        elif choice == "6":
            canteen.display_Sales()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
