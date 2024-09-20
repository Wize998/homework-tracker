# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List


# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __inventory: int = 0

    def __init__(self, sale: Sale, initial_inventory: int = 0):
        self.__lastSale = sale
        self.__inventory = initial_inventory
        self.__initial_inventory = initial_inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    def minusInventory(self, amount: int):
        self.__inventory -= amount

    def getInventory(self) -> int:
        return self.__inventory

    def getInitialInventory(self) -> int:
        return self.__initial_inventory


# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, products: List[Product], quantities: List[int]):
        Sale.__saleTimes += 1
        self.__products = products
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(products):
            product.setLastSale(self)
            product.minusInventory(quantities[index])

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, initial_inventory=10)
productTwo = Product(sale=None, initial_inventory=20)

print(f"Initially, product one inventory: {productOne.getInitialInventory()}")
print(f"Initially, product two inventory: {productTwo.getInitialInventory()}")


saleOne = Sale([productOne, productTwo], [2, 23])

print(f"After sale, product one inventory: {productOne.getInventory()}")
print(f"After sale, product two inventory: {productTwo.getInventory()}")
