import random

def rou_g(player):
    print("hi")



class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.plane_health = 300
        self.plane_fuel = 100

    def attack(self, player_2):
        """
        attacks another player for 10 damage
        :param player2:
        :return:
        """
        player_2.health -= 10
        print(f"{self.name} attacked {player_2.name}! [10 dmg]")

    def game_russian(self, player_2):
        shot = 1
        player_list = [self, player_2]
        print(f"{self.name} challenged {player_2.name} to Russian Roulette!")
        while self.health > 0 and player_2.health > 0:
            for turn in player_list:
                print("*Spinning the barrel*")
                bullet = random.randint(1, 6)
                # print(f"Bullet is {bullet}") #remove later after testing
                if turn == self:
                    print(f"{self.name}'s turn. Click.")
                    if shot != bullet:
                        input("Press Enter to shoot")
                        print("Nothing happened.")
                        input("Press Enter to continue")
                    else:
                        input("Press Enter to shoot")
                        self.health -= 9999
                        print(f"Bang! {self.name} died")
                        break
                elif turn == player_2:
                    print(f"{player_2.name}'s turn. Click.")
                    if shot != bullet:
                        input("Press Enter to shoot")
                        print("Nothing happened.")
                        input("Press Enter to continue")
                    else:
                        input("Press Enter to shoot")
                        player_2.health -= 9999
                        print(f"Bang! {player_2.name} died")
                        break

        if self.health > 0:
            print("You won.")
        else:
            print("Game Over")


player1 = Player("Meeri")
player2 = Player("Sam")

input("Press Enter to play Russian Roulette.")
player1.game_russian(player2)