
class Order :

    def __init__(self  , cart , customer):

        self.customer = customer
        self. cart = cart

    def __len__(self):

        return len(self.cart)
    
    def __call__(self):

        print(f"{self.customer}")
        
    def __str__(self):

        return f"{self.customer} bought {self.cart}"
        
    def __repr__(self):

        return f"order (list of itmes and customer name)"
        
    def __bool__(self) :
        return len(self.cart) > 0 

    def __add__(self , other) :
        """
        this function takes one pramater:
        other: string
        """
        new_card = self.cart.copy()
        new_card.append(other)
        return Order(new_card , self.customer)
order = Order(["nnnnn","nnnnnnnnnnn","nNNNNNNNNNNNNNNNN"],"islam mohamed")
print((order+"ffff"))
print(order)
order+= "52555"
print(order)
print(bool(order))
order.add_item("56256")
print(Order.cart)
order.__add__()
if order :

    print(f"{order.customer} order is processing")
else :
    print("shoping cart is emply ")
