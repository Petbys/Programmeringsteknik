# Definition av klassen Dice
class Dice:   
    # Metoden init, skapar en tärning m sides sidor
    def __init__(self, sides):
        self.sides = sides
        # Slumpat ett heltal 1-self.sides
        self.value = random.randint(1, self.sides) 

# Testar klassen Dice
d1 = Dice()  # Skapar Dice-objektet d1
d2 = Dice()  # Skapar Dice-objektet d2

print(d1)    # Skriver ut objekten
print(d2)
