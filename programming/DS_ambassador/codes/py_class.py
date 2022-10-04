"""
Class combines data (variables) and functions
keywords: class, self, __init__, attributes, methods
"""

class Player():
    # self is a reference to the class itself
    # self is the first argument of every class function
    def __init__(self, hp=50, mp=20):
        self.lvl = 1  # level
        self.hp = hp  # health points
        self.mp = mp  # magic points
        # these self. variables are called attributes

    # functions inside a class are called methods
    def method1(self):
        print("This is method 1")

    def challenge(self, name):
        print(f"I challenge you, {name}!")

    def get_lvl(self):
        return self.lvl

    def level_up(self):
        self.lvl += 1 # equivalent to self.lvl = self.lvl + 1

    def exlixir(self, type='hp'):
        if type == 'hp':
            print('You have been healed!')
            self.hp += 20

        elif type == 'mp':
            print('You have been restored!')
            self.mp += 10

        else:
            print("Invalid type")


# Create an object of Player class
player1 = Player()
player1.method1()              # This is method 1
player1.challenge('Jack')      # I challenge you, Jack!
print(player1.get_lvl())       # 1
player1.level_up()
print(player1.get_lvl())       # 2
player1.exlixir('hp')          # You have been healed!
player1.exlixir('mp')          # You have been restored!
print(player1.hp, player1.mp)  # 70 30


# Another object of Player class
player2 = Player(mp=10) # indep to player1
print(player2.hp, player2.mp) # 50 10


# Inheritance
class Mage(Player):
    def __init__(self):
        super().__init__() # call the __init__ of the parent class
        self.mp = 100

    def fireball(self):
        print('Fireball!')

    def exlixir(self):
        Player.exlixir(self, 'mp')


mage1 = Mage()
mage1.fireball()            # Fireball!
mage1.exlixir()             # You have been restored!
print(mage1.hp, mage1.mp)   # 50 110
