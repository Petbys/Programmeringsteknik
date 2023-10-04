import dice # Klassen PokerDice måste känna till klassen Dice

class PokerDice:
    def __init__(self,antal):
        self.dice_list = []
        self.antal=antal
        for i in range(antal):
            self.dice_list.append(dice.Dice(6))

    def __str__(self):
        # Använder metoden getValue i Dice
        return str(sorted([d.getValue() for d in self.dice_list])) 
    
    def antaldice(self):
        return self.antal
        
    
    def roll(self):
        for d in self.dice_list:
            d.roll()      # Använder rollmetoden i Dice


# Test av klassen PokerDice
print('Pokertärningar:')
pd = PokerDice(2)
print('antal tärningar: ', pd.antaldice())
for i in range(10):
    pd.roll()
    print(pd)