import random

def rolldice(min,max):
    print("Currently rolling your dice.....")
    number = random.randint(min,max)
    print(f"The number that you got is : {number}")
    
rolldice(1,6)
    
