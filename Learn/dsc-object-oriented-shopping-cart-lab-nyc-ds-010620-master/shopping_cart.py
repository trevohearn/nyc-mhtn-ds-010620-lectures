class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
    def add_item(self, name, price, quantity=1):
        for x in range(0, quantity):
            self.items.append({name:price})
            self.total += price
    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        
        price_li = list(map(lambda x: list(x.values())[0], self.items))
        price_li.sort()
        print(price_li)
        if (len(price_li) % 2 == 0): #even
            num1 = price_li[(int(len(price_li)
            return price_li
        else: #odd
            return price_li[int((len(price_li) - 1) / 2)]
        return price_li

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass
    def print_item_list(self):
        for x in self.items:
            print(x)