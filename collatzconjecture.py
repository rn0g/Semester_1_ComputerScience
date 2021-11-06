##Collatz Conjecture
#rn0g
import time 

def time_conversion(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60 
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(minutes), seconds))


def collatz_conjecture(x):
    start_time = time.time()
    even_numbers = 0
    odd_numbers = 0
    calculations = 0
    while True:    
        if x % 2 == 0:
            x = x//2
            print("Result: ", x)
            even_numbers = even_numbers + 1
            calculations = calculations + 1

        if x % 2 > 0:
            x = 3*x+1
            print("Result: ", x)
            odd_numbers = odd_numbers + 1
            calculations = calculations + 1
        if x == 2:
            break
    end_time = time.time()
    print("-"*30)
    print("Number of calculations: ", calculations)
    print("Number of even numbers: ", even_numbers)
    print("Numbers of odd numbers: ", odd_numbers)
    time_lapsed = end_time - start_time
    time_conversion(time_lapsed)

    print("Done")
    
            
    

a_number = int(input("Type a number: "))
collatz_conjecture(a_number)
print("Coded by rn0g")
    
    
