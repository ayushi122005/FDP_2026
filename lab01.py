FILE_NAME = "finance_tracker.txt"

print("Enter your operation \n 1: Income \n 2: Expense \n 3:Balance \n 4:Exit")

def addEntry(entry_type, amount):
  if amount <= 0:
    print("Invalid amount.")
    return {}
  with open(FILE_NAME, "a") as file:
    file.write(f"{entry_type},{amount}\n")

  return f"({entry_type}: {amount})"

def balance():
  income = 0
  expense = 0
  with open(FILE_NAME, "r") as file:
    for line in file:
      entry_type, amount = line.strip().split(",")
      amount = float(amount)
      if entry_type == "Income":
        income += amount
      elif entry_type == "Expense":
        expense += amount
    
    b = income - expense
  return b

def main():
  
  while True:
    o = int(input("Enter operation: "))
    if o==1:
      addEntry("Income", float(input("Enter income amount: ")))
    elif o==2:
      addEntry("Expense", float(input("Enter expense amount: ")))
    elif o==3:
      print("Current Balance: ", balance())
    elif o==4:
      print("Exiting the program.")
      break
    else:
      print("Invalid operation selected.")
    
main()
