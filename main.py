import random

resturants =["Outback", "Eureka", "Chilis", "De vine"]


def random_resturant_picker():
    recom = random.choice(resturants)

    return recom



def main():
    answer = input("Not sure where to eat, press enter to get a recommendation or Press (q to quit) ")
    if answer == "q":
        print(" See you soon!")
    else:
        print(f" Our recommendation is {random_resturant_picker()}")

main(

)