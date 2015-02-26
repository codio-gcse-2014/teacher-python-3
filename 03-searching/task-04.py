import random

my_list = ["Bob","Anna","Amir","Shahiza","Constanz","Elvis"]

def pick_one():
    position_picked = random.randint(0,len(my_list)-1)

    return my_list.pop(position_picked)

third_prize = pick_one()
second_prize = pick_one()
first_prize = pick_one()

template = "Third prize {}, Second prize {}, ***FIRST PRIZE*** {}"

print(template.format(third_prize,second_prize,first_prize))
