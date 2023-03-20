


def adding(x:int,y:int) -> int:    
    return x + y

def adding(x:str,y:str) -> str:    
    return x + y
    


def userinteraction():
    a = int(input('What is the first number do you want to add: '))
    b = int(input('What is the second do you want to add: '))
    print(f'the result is {adding(a,b)}')




userinteraction()

    
    
