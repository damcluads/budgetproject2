
class Budget:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
            old_balance = self.balance
            self.balance = self.balance + amount

            return f"old: {old_balance}, New:{self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "insufficient cash"
        else:
            old_balance = self.balance
            self.balance = self.balance - amount
        return f"old: {old_balance}, New:{self.balance}"

    def get_balance(self):
        feedback = f"your balance is {self.balance}"
        return feedback
    def transfer (self,amount,transfer_to):
        if self.balance < amount:
            return "insufficent fund"
        else:
            self.balance = self.balance - amount
            transfer_to.balance = transfer_to.balance + amount

            feedback = f"you transfered ${amount} to {transfer_to.name} budget\n"
            feedback += f"The balance for {self.name} is now {self.balance} while\n"
            feedback += f"The balance for {transfer_to.name} is now {transfer_to.balance}"

            return feedback

            return

food_budget = Budget('food', 5000)
clothing_budget = Budget('clothing', 500)
entertainment_budget = Budget('entertainment', 2000)

print(f"you have created a {food_budget.name} budget with ${food_budget.balance}")

print(food_budget.deposit(500))
print(food_budget.withdraw(2000))
print(food_budget.transfer(1000,clothing_budget))
print(food_budget.get_balance())
print(clothing_budget.get_balance())
print(entertainment_budget.get_balance())
