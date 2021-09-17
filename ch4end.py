spam = ['apples', 'bananas', 'tofu', 'cats']

def sentence(x):
    if len(x)==0:
        print('nothin to report') 
    else:
        for i in range(len(x)):
            print(x[i], end="")
            if i==len(x)-2:
                print(' and ', end="")
            else:
                if i!=len(x)-1:
                    print (', ', end="")
    print()
                
tomato=['1', '2', '3', '4', '5', '6']
sentence(spam) 
sentence(tomato)
sentence([]) 