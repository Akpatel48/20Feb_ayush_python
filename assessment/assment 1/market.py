import logging  #impor libreri
logging.basicConfig(filename='market.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  #add log file path
def market():   #welcome market
    global role
    print("\t\t\tWELCOME TO FRUIT MARKET")
    print("\t\t\t1) Manager")
    print("\t\t\t2) Customer")
    role = int(input("Enter your role: "))  #coise your role
    logging.info(f"Role selected: {role}")


def add_stock(stock):       #add fruit stock
    print("ADD FRUIT STOCK")
    fn = input("Enter fruit name: ")
    qut = int(input("Enter quantity (in kg): "))
    price = int(input("Enter price: "))
    stock[fn] = {'qty': qut, 'price': price}
    logging.info(f"Fruit added: {fn}, Quantity: {qut}, Price: {price}")

def view_stock(stock):  #show fruit stock
        print(stock)
        logging.info(stock)


def update_stock(stock):    #update fruit stock
    up = input("Enter the fruit to update: ")
    if up in stock:
        qut = int(input("Enter quantity (in kg): "))
        price = int(input("Enter price: "))
        stock[up]['qty'] = qut
        stock[up]['price'] = price
        logging.info(f"Fruit updated: {up}, New Quantity: {qut}, New Price: {price}")
    else:
        print("Fruit not found in stock.")
        logging.warning(f"Attempted to update non-existing fruit: {up}")

def printdata(stock):   #print all data
    print("\t\t\tFruit Market Manager")
    print("\t\t\t1) Add Fruit Stock")
    print("\t\t\t2) View Fruit Stock")
    print("\t\t\t3) Update Fruit Stock")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_stock(stock)
    elif choice == 2:
        view_stock(stock)
    elif choice == 3:
        update_stock(stock)
    y = input("Do you want to perform more operations? (Press 'y' for yes and 'n' for no): ")
    if y.lower() == 'y':
        printdata(stock)

stock = {}
market()
if role == 1:   #check choice
    printdata(stock)
elif role == 2:
    None
