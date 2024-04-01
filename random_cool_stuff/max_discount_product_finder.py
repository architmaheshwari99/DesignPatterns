"""
Given the amazon top deals data which included productId,timestamp,discuount,
we have to return the products which will give more discount and particular time window.

"""

class Product:
    def __init__(self, productId, startTime, endTime, discount):
        self.productId = productId
        self.startTime = startTime
        self.endTime = endTime
        self.discount = discount

def getMaxDiscountProducts(start, amazonProducts):
    amazonProducts = sorted(amazonProducts, key = lambda x, y: x.startTime < y.startTime)
    amazonProducts = filter(lambda x: x.startTime>start or x.endTime>start, amazonProducts)

#     can use a PQ as well, select the products starting from the start time 'start' which gives
#     the maximum discount.


if __name__ == '__main__':
    amazonProducts = [Product(1,12,13,90), Product(2,12,15,5), Product(3,12,16,90),
                     Product(4,4,7,65), Product(5,5,9,98),Product(6,7,10,85) ]
    start = 9
    getMaxDiscountProducts(start, amazonProducts)