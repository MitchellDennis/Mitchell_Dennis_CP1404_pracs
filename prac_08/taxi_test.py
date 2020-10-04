
from prac_08.taxi import Taxi

prius = Taxi("Prius 1", 100)

prius.drive(40)
print(prius)
prius.start_fare()
prius.drive(100)
print(prius)

"""First output:
Prius 1, fuel = 60, odometer = 40, 40km on current fare, $1.23/km
Prius 1, fuel = 0, odometer = 100, 60km on current fare, $1.23/km"""

"""Second Output
Prius 1, fuel = 60, odometer = 40, 40km on current fare, $1.23/km
Prius 1, fuel = 0, odometer = 100, 60km on current fare, $1.23/km"""