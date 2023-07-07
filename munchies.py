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

                    