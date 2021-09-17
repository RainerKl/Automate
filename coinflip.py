import random 
numberOfStreaks = 0 
for experimentNumber in range(10000): 
    # Code that creates a list of 100 'heads' or 'tails' values. 
    flips=[]
    for i in range(100):
        flips.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(len(flips)): 
        if flips[j:j+6]==([1,1,1,1,1,1] or [0,0,0,0,0,0]):
            numberOfStreaks +=1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))