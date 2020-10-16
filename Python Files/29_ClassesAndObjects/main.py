'''
Author: Pratyush
Description: Class is group of similar functions and objects
'''
class Enemy:
    life = 3

    def attack(self):
        print('ouch')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('You are dead')
        else:
            print("Life's left: " + str(self.life))

enemy1 = Enemy()  # Created Enemy object
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()