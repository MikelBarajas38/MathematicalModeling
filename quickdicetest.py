import random
import matplotlib.pyplot as plt

def test():

    count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}

    for i in range(100):

        dice_roll = str(i * 6)

        if(len(dice_roll) < 3):
            dice_roll = '0' * (3 - len(dice_roll)) + dice_roll

        print(dice_roll)
        print(i*6)
        count[dice_roll] = count[dice_roll] + 1

    for i,c in count.items():
        print(i,c)

def dice_roll(n):

    count = {}

    for i in range(n):

        dice_roll = int(random.random() * 6) + 1

        if dice_roll not in count:
            count[dice_roll] = 0

        count[dice_roll] = count[dice_roll] + 1

    for i,c in count.items():
        print(i,c,c/n)

def plot_dice_roll(n):

    plt.plot(0, .166, 'ro')

    plt.show()  

#test()
#print()
dice_roll(1000000)
plot_dice_roll(1000000)