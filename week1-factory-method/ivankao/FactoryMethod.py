def McDonaldsFactoryInterface(classname): # FactoryInterface

    run = {
        'MikesChickenNuggets': MikesChickenNuggets, 
        'BigMac': BigMac,
        'Fries': Fries,
        'Coke': Coke
    }
    
    return run[classname]()


class MikesChickenNuggets:

    def __init__(self):
        self.process = "Mike's Chicken Nuggets"
    
    def run(self):
        print(self.process)


class BigMac:
    
    def __init__(self):
        self.process = "BigMac"

    def run(self):
        print(self.process)


class Cheeseburger:
    
    def __init__(self):
        self.process = "Cheeseburger"

    def run(self):
        print(self.process)


class FiletOFish:
    
    def __init__(self):
        self.process = "Filet-O-Fish"

    def run(self):
        print(self.process)


class Fries:
    
    def __init__(self):
        self.process = "Fries"
        
    def run(self):
        print(self.process)
        
class Salad:
    
    def __init__(self):
        self.process = "Salad"
        
    def run(self):
        print(self.process)


class CornSoup:
    
    def __init__(self):
        self.process = "Corn Soup"
        
    def run(self):
        print(self.process)


class Coke:
    
    def __init__(self):
        self.process = "Coke"
        
    def run(self):
        print(self.process)


class Sprite:
    
    def __init__(self):
        self.process = "Sprite"
        
    def run(self):
        print(self.process)


class MealAbstractInterface: 

    def __init__(self, main=None, side=None, drink=None):
        self.main = main
        self.side = side
        self.drink = drink

    def run(self):
        print('Your combo meal includes: ')
        print("Main: ", end = '')
        self.main().run()
        print("Side: ", end = '')
        self.side().run()
        print("Drink: ", end = '')
        self.drink().run()


class McDonaldsFactoryAbstractInterface:
    
    def __init__(self, classname=None):
        self.process = classname
        self.meal_dict= {
            '1': {"main": BigMac, "side": Fries, "drink": Coke},
            '2': {"main": MikesChickenNuggets, "side": Fries, "drink": Coke},
            '3': {"main": FiletOFish, "side": Salad, "drink": Sprite},
            '4': {"main": Cheeseburger, "side": Fries, "drink": CornSoup},
        }

    def run(self):
        self.process.run()


if __name__ == '__main__':
    
    print('unit test 1 FactoryInterface')
    test1 = McDonaldsFactoryInterface('MikesChickenNuggets')
    test1.run()
    
    print('unit test 2 FactoryAbstractInterface')
    test2 = McDonaldsFactoryAbstractInterface()
    test2.process = MikesChickenNuggets()
    test2.run() # same as MikesChickenNuggets().run()
    
    print('unit test 3 MealAbstractInterface')
    test3 = McDonaldsFactoryAbstractInterface()
    print("Select Meal:")
    for key, value in test3.meal_dict.items():
        print(key, end = '. ')
        value["main"]().run()
        
    meal_number = input("Please Input Meal Number: ")
    if meal_number.isdigit() and meal_number in test3.meal_dict:
        test3.process = MealAbstractInterface(**test3.meal_dict[meal_number])
        test3.run()
    else :
        print("No Meal Bye Bye!")