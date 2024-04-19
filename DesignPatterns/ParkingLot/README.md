System Requirments
1. Parking Lot should have multiple floors
2. Parking lot should have entry and exit points
3. Customers can collect ticket from entry and pay at exit
4. Customer can pay the ticket at automated exit panel or to the parking attendent
5. Can pay via cash and card
6. Customer can pay at the info portal on each floor, if they have paid there, no need to pay at exit
7. If parking is full, show the message on the board
8. Parking spot can be of different types: Bike, Car, Handicapped, Electric
9. Should support different vehicles like Car, Bike, truck etc
10. Each floor should have a display board showing free spots
11. Payment model should be $4 for first hour, $3.5 for second and $2.5 for remaining hours

## Use Cases
#### Actors
1. Admin: Responsible for adding and modifying parking floors, parking spots, entrance and exit panels, payment booths, adding and removing parking attendants
2. Customer: Can purchase a parking ticket
3. Parking Attendant: Takes cash for a ticket payment
4. System: Display message on the boards, assign spots, compute and generate bills

### Use cases
1. Add/Remove/Edit a parking floor
2. Add/Remove/Edit a parking spot
3. Add/Remove parking attendant
4. Take Ticket
5. Scan Ticket
6. Credit Card payment
7. Cash payment
8. Add/Modify parking rates


## Entities

### Models
1. Account
   1. Account
   2. Address
   3. PersonalInfo
   4. Contact
   5. Admin
   6. ParkingAttendant
   7. Valet
   8. AccountStatus(ENUM)
2. Vehicle
   1. Vehicle
3. Payment
   1. Payment
   2. PaymentStatus(ENUM)
   3. CreditCardPayment
   4. CashPayment
4. Parking
   1. ParkingSpot
   2. ParkingFloor
   3. ParkingLot
   4. ParkingRate
   5. ParkingTicket
   6. ParkingSpotStatus(ENUM)
   7. ParkingSpotType(ENUM)

## Activity Diagram
1. Picking a slot
2. 