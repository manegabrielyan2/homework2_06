#number 3 2.06 
"""
def tofuture():
    hour = 70
    while hour > 12:
        hour = int(input("please enter an hour between 1 and 12!"))
    time = int(input("Please enter am(1) or pm(2)!"))
    how_far = int(input("How many hours ahead?"))
    if time == 2 and hour + how_far < 12:
        new_time = hour + how_far 
        print(f'New hour: {new_time} pm.')
    if time == 2 and hour + how_far >12 and hour + how_far < 24:
        new_time = hour + how_far -12
        print(f'New hour: {new_time} am.')
    if time == 1 and how_far + hour<12:
        new_time = hour + how_far
        print(f"New hour:", new_time, "am.")
    if time == 1 and how_far + hour > 12:
        new_time =  hour + how_far - 12
        print(f"New hour:", new_time, "pm.")

tofuture()
"""
