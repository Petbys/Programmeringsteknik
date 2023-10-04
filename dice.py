import random

# Definition av klassen Dice
class Dice:   
    # Metoden init, skapar en tärning m sides sidor
    def __init__(self, sides):
        self.sides = sides
        # Slumpat ett heltal 1-self.sides
        self.value = random.randint(1, self.sides) 

    # Metoden str, ger en textrepresentation av objektet
    def __str__(self):
        return f'Sidor: {self.sides:2d}, värde: {self.value:2d}'
       
    def getValue(self):
        return self.value
    
    def getSides(self):
        return self.sides

       
       # Slår tärningen
    def roll(self):
        self.value = random.randint(1, self.sides) 

# Testar klassen Dice
d1 = Dice(6)  # Skapar Dice-objektet d1
d2 = Dice(12)  # Skapar Dice-objektet d2

for i in range(5):
    d1.roll()
    d2.roll()
    
    


