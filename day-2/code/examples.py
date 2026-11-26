# ----- Data types -----
product_name = "Notebook"   # str: text
stock_quantity = 25         # int: whole number
price = 12.50               # float: decimal number
is_available = True         # bool: True or False
supplier = None             # None: no value yet

print(type(product_name))
print(type(stock_quantity))
print(type(price))
print(type(is_available))
print(type(supplier))

# ----- Arithmetic operators -----
print(10 + 3)    # add       -> 13
print(10 - 3)    # subtract  -> 7
print(10 * 3)    # multiply  -> 30
print(10 / 3)    # divide    -> 3.333...
print(10 // 3)   # divide, whole number only -> 3
print(10 % 3)    # remainder -> 1

# ----- Update stock -----
stock = 25
stock = stock + 10   # new stock arrived
stock = stock - 3    # customer bought 3
print("Stock:", stock)   # 32
