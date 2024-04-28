## Models
1. Product
   1. id
   2. ProductType
   3. price
   4. rack_id
2. Coin
   1. id (value)
   2. count
3. Transaction
   1. ts
   2. product_id
   3. price
4. Rack
   1. id
   2. product_id
5. Display
   1. message

## Controller
1. VendingMachineController

## Services
1. InventoryService
2. PaymentService
3. DispenseMoneyService
