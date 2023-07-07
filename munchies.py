class Snack:
    def __init__(self,snack_id,name,price,available):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.available = available

class Canteen:
    def __init__(self):
        self.inventory =[]
        self.sales.records=[]

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

