# Shopping Cart Design
class User:
    user_lst = [] # class variable
    def __init__(self,username, password):
        self.username = username # instance variable
        self.password = password

class Item:
    def __init__(self, itemID,price, description,quantity):
        self.itemID = itemID
        self.price = price
        self.description = description
        self.quantity = quantity

class ShoppingBasket:
    # {{"name":'rahat} }
    user_lst = [] # [{"name": "rahat", "password": "123"}, {"name": "naim", "password": "124"}] --> dictionary
    # [["rahat", "1234"], ["naim", "1234"]] --> list
    user_ordered_data = {} # {"rahat" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}, {"itemID" : 13, "price" : 200, "description" : 'abdc', "quantity" : 12}]}
    itemsDB = [] # [{"itemID": itemID, "price": price, "description": description},{"itemID": itemID, "price": price, "description": description}]
    
    def get_userslst(self):
        return self.user_lst
    
    def create_account(self):
        name = input("Введите своё имя: ")
        # password = input("Enter your password: ")
        isNameExist = False # True mane hocche user already ache, False mane hocche notun user
        for user in self.get_userslst(): # user already ache kina seta check
            if user['username'] == name:
                print("kabuuum!!")
                isNameExist = True
                break
            
        if isNameExist == False:  # notun ekjon user uni, unake misty khawao
            password = input("Введите свой пароль: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Аккаунт успешно создан!")
        
    def addItemToCart(self, username):
        itemid = input("Введите ID предмета: ")
        quantity = int(input("Введите количество предметов: "))
        flag = 0 # item unavailable
        price = 0
        for i in self.itemsDB:
            if i['itemID'] == itemid and i['quantity'] >= quantity:
                price = i['price']
                flag = 1 # item available
                break
        if flag == 0: # item unavailable
            print("Предмет не найден")
        else: # item available
            if self.user_ordered_data.get(username) == None:
                self.user_ordered_data[username] = []
            
            self.user_ordered_data[username] += [{'itemID': itemid, 'price': price,'quantity': quantity}]
                
    def updateProductCart(self, username):
        itemid = input("Введите ID предмета: ")
        quantity = int(input("Введите обновленный номер количества: ")) 
        for i in self.user_ordered_data[username]:
            if i.get('itemID') == itemid:
                if quantity <= i['quantity']:
                    i['quantity'] += quantity 
                else:
                    print("Нет в наличии")
                    break
    def deleteProductCart(self, username, itemid):
        flag = 0 # item unavailable
        for i in self.itemsDB:
            if i['itemID'] == itemid:
                flag = 1 # item available
                print("Доступно")
                break
        if flag: # item available
            for i in self.user_ordered_data[username]:
                if i['itemID'] == itemid : # searching the itemID
                    self.user_ordered_data[username].remove(i)
                    
    def showCart(self, username):
        print("ID предмета \t Цена предмета \t Количество предметов")
        total_price = 0
        if self.user_ordered_data.get(username) is not None:
            for i in self.user_ordered_data[username]:
                print(f"{i['itemID']} \t\t {i['price']} \t\t {i['quantity']}")   
                total_price += i['price']*i['quantity']
            print("______________________________________________________")
            print(f"Итоговая цена = {total_price}")
        else:
            print("\nПусто\n")
            
            
    # for admin only
    def addItemToDatabase(self): # admin product create korben
        itemId = input("Введите ID предмета: ")
        isItemAvailable = False
        for i in self.itemsDB:
            if i['itemID'] == itemId:
                isItemAvailable = True
                break
        if isItemAvailable == False:
            description = input("Введите описание товара: ")
            price = float(input("Введите цену товара: "))
            quantity = int(input("Введите количество товара: "))
            self.new_item = Item(itemId,price, description, quantity)
            self.itemsDB.append(vars(self.new_item))  
        else:
            print("\nэлемент уже добавлен\n")
    def delProductFromDatabase(self):
        itemId = input("Введите ID предмета: ")         
        for i in self.itemsDB:
            if i['itemID'] == itemId:
                self.itemsDB.remove(i)
                print("\nЭлемент удален успешно\n")
    
    def showItemsTable(self):
        print("ID предмета \t Предмет удален \t Цена предмета \t Количество предметов")
        for i in self.itemsDB:
            print(f"{i['itemID']}\t\t {i['description']} \t\t\t {i['price']} \t\t\t {i['quantity']}")


basket = ShoppingBasket()

while True:
    print("\n1. Создайте аккаунт\n2. Войдите в аккаунт \n3. Выход\n")
    user_choice = int(input("Сделайте выбор: "))
    
    if user_choice == 3:
        break
    elif user_choice == 1:
        basket.create_account()
    elif user_choice == 2:
        name = input("Введите своё имя: ")
        password = input("Введите свой пароль: ")
        isAdmin = False # normal
        flag = 0
        if name == "admin" and password == "123":
            isAdmin = True # se ekjon admin
        if isAdmin == False: #normal user/customer
            isNameExist = False # True mane hocche amar customer, False mane hocche fraud
            for user in basket.user_lst:
                if user['username'] == name and user['password'] == password:
                    isNameExist = True
                    break
            if isNameExist: # se hocche amar customer
                while True:
                    print("\nДобро пожаловать в корзину покупок")
                    print("\n1. Добавьте товар в корзину \n2. Обновите свою корзину\n3. Удалите свою корзину\n4. покажите свою корзину \n5. Выход\n")
                    choice = int(input("Сделайте выбор: "))
                    if choice == 1:
                        basket.addItemToCart(name)
                    elif choice == 2:
                        basket.updateProductCart(name)
                    elif choice == 3:
                        item = input("Введите ID предмета: ")
                        basket.deleteProductCart(name, item)
                    elif choice == 4:
                        basket.showCart(name)
                    else:
                        break
        else:
            while True:
                print(f"\nЗдаров админ, добро пожаловать!\n")
                print(f"1. Добавить новый элемент \n2. Показать таблицу элементов \n3. Удалить элемент\n4. Выход")
                a = int(input("Сделайте выбор: "))
                if a == 5:
                    break
                elif a == 1:
                    basket.addItemToDatabase()
                elif a == 2:
                    basket.showItemsTable()
                elif a == 3:
                    basket.delProductFromDatabase()
                elif a == 4:
                    break     
                
        


        
                
# 1. Add item to your Cart
# 2. show your cart
# 3. update your cart
# 4. deleteProductCart
            
        
        
            
# b = ShoppingBasket()                
# b.create_account()
# print(b.get_userslst())
# {}, {}
# a = [{"itemID": 12, "price": 300, "description": "description", "quantity": 4},{"itemID": 13, "price": 300, "description": "description", "quantity" : 5}]

# flag = 0 # item unavailable
# for i in a:
#     if i['itemID'] == 15 and i['quantity'] <= 4:
#         print("Items available")
#         flag = 1 # item available
#         break
    
# if not flag: # item unavailable
#     print("Items not available")

# a = {"rahat" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}]}
# # for i in a['rahat']:
# #     if i['itemID'] == 12:
# #         i['quantity'] = 134 
# # print(a['rahat'])

# for i in a['rahat']:
#     if i['itemID'] == 12: # searching the itemID
#         a['rahat'].remove(i)
# print(a['rahat'])

# b = {"rahat" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}, {"itemID" : 13, "price" : 200, "description" : 'abdc', "quantity" : 12}], "naim" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}, {"itemID" : 13, "price" : 200, "description" : 'abdc', "quantity" : 12}]}

# print(b.keys())
