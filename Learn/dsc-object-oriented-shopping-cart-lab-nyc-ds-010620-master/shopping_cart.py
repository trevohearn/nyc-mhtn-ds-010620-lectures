class ShoppingCart():
    # write your code here
    def __init__(self, employee_discount=None):
        self.total = 0
        self.employee_discount = employee_discount
        self.items = []
    def add_item(self, name, price, quantity=1):
        for x in range(0, quantity):
            self.items.append({name:price})
            self.total += price
        return self.total
    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        
        price_li = list(map(lambda x: list(x.values())[0], self.items))
        price_li.sort()
        length = len(price_li)
        print(price_li)
        if (len(price_li) % 2 == 0): #even
            num1 = price_li[(int(length)) / 2]
            num2 = price_li[ (int(length) / 2) - 1 ]
            return ( num1 + num2 ) / 2
        else: #odd
            return price_li[int((len(price_li) - 1) / 2)]
        return price_li

    def apply_discount(self):
        if (self.employee_discount == None):
            return 'Sorry, there is no discount to apply'
        elif (self.employee_discount > 0):
            self.total = self.total * (1 - (self.employee_discount / 100))
        return self.total

    def void_last_item(self):
        item = self.items.pop()
        print(item)
        print(self.total)
        self.total -= list(item.values())[0]
        print('-' + str(list(item.values())[0]))
        print(self.total)
        return self.items.pop()
    def print_item_list(self):
        for x in self.items:
            print(x)