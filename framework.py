import time
import os
def print_lines():
    print("_________________________________________________________________________")
    print("                                                                         ")
    print("You wake up after a 'great' night, laying in complete darkness.")

    print("You feel around and realize your in a very small box just bigger than the length of your body.")

    print("You feel something that feels like a candle to your right.")

    print("You have a lighter in your pocket from the night before.")

    print("you light the candle and it all becomes clear.")

    print("YOU ARE IN A COFFIN!")

    print("Remember this candle won't last forever...")

    print("You see a number scratched into the wood of the coffin.")

    print("It reads: 547")

    print("those numbers are now available in your inventory.")
    print("_________________________________________________________________________")
    print("                                                                         ")

def clear(first):
    
    if os.name == 'nt':
        os.system('cls')   
    else:
        os.system('clear') 
    if not first:
        print_lines()
inventory = []
number_endings = ["st", "nd", "rd", "th"]

class Candle:
    def __init__(self, secs):
        self.start_time = int(time.time())
        self.current_checkpoint = .25
        self.secs = secs
    def get_time_since(self):
        return int(time.time())-self.start_time
    def checkpoint_test(self, game):
        if self.get_time_since()/self.secs >= 1:
            print("The candle ran out of light filling your coffin with the darkness waiting to rush back in.")
            time.sleep(2)
            print("You never made it out.")
            game.is_playing = False
            return True
        elif self.get_time_since()/self.secs >= self.current_checkpoint:
            self.current_checkpoint+=.25
            print(f"The candle seems to be at least {(self.current_checkpoint-.25)*100}% burnt out.")
            input("Press Enter When You Are Ready to Continue")
    def view_candle(self):
        time.sleep(1)
        print(f"The candle seems to be about {round((self.get_time_since()/self.secs)*100)}% burnt out")

class Item:
    def __init__(self, name, owned, description):
        self.name = name
        self.owned = owned
        self.description = description
    def pickup(self):
        if self.owned == False:
            self.owned = True
            inventory.append(self)
            
            print(f"You picked up {self.name}.")
            time.sleep(2)
        else:
            print(f"You already have {self.name}.")
            time.sleep(1)
    def use(self, target):
        pass

class Puzzle:
    def __init__(self, name, description, answer):
        self.name = name
        self.description = description
        self.answer = answer
class Padlock(Puzzle):
    def run(self):
        print("You see a padlock. It has a 3-digit combination.")
        time.sleep(4)
        print("Enter the combination:")

        user_input = input()
        if user_input == self.answer:
            print("You hear a click and with a pull, the padlock clicks open!")
            time.sleep(2)
            return True
        else:
            print("You try to pull the padlock open, but nothing budges.")
            time.sleep(2)
            return False
        
class Keyhole(Puzzle):
    def __init__(self, name, description, answer, key):
        super().__init__(name, description, answer)
        self.key = key
    def run(self):
        print("You see a keyhole. It takes in a specific key.")
        time.sleep(3)
        resp = input(("Which Item Will you Like to Use?: "+", ".join([item.name for item in inventory]))+": ")
        for item in inventory:
            if item.name == resp:
                time.sleep(2)
                print(f"You try to insert the {item.name} into the keyhole.")
                if item.name == self.key.name:
                    time.sleep(2)
                    print("The key fits perfectly! With a pull, the keyhole clicks open!")
                    time.sleep(1)
                    return True
                else: 
                    time.sleep(2)
                    print("The key doesn't fit. You try to pull the keyhole open, but nothing budges.")
                    time.sleep(1)
                    return False

class Switches(Puzzle):
    
    def __init__(self, name, description, num_switches,answer):
        super().__init__(name, description, answer)
        self.num_switches = num_switches
    def run(self):
        directions = []
        time.sleep(2)
        print(f"You see a series of {self.num_switches} switches. Each switch can be either up or down.")
        time.sleep(2)
        i = 0
        end = number_endings[0]
        while i < self.num_switches: 
            if i >-1 and i <=2:
                end = number_endings[i]
            else:
                end = number_endings[3]
            us = input(f"Enter the {str(i+1)+end} switches direction(up/down):")
            if us.lower() == "up" or us.lower() == "down":
                directions.append(us.lower())
                i+=1
                time.sleep(1)
                print("You flipped the switch "+us.lower()+".")
                time.sleep(2)
            else:
                print("Invalid input. Please enter 'up' or 'down'.")
                time.sleep(2)
        if self.answer == directions:
            time.sleep(2)
            print("You feel a small pull on the last switch, and with a pull, a secret door opens exposing a golden key!")
            return True
        else:
            time.sleep(2)
            print("You try to pull the switches, but nothing happens.")
            return False
            
        

class Area:
    def __init__(self, name, description, puzzles, reward):
        self.name = name
        self.description = description
        self.items = []
        self.puzzles = puzzles
        self.reward = reward
        self.solved = False
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def list_items(self):
        if len(self.items) == 0:
            print("There are no items here.")
        else:
            print("Items in this area:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")
    def solve_puzzle(self, puzzle):
        answer = puzzle.run()
        if answer == True:
            time.sleep(2)
            self.solved = True
            time.sleep(2)
            print(f"{self.reward.name} is now available in your inventory.")
            inventory.append(self.reward)
            input("Press Enter When You're Ready to Continue")
        else:
            time.sleep(2)
            print("The puzzle remains unsolved.")
    def inspect(self):
        print(f"You inspect the {self.name}.")
        time.sleep(2)
        clear(False)
        print("_________________________________________________________________________")
        print("                                                                         ")
        choice = input("Would you like to do? (1) inspect inventory (2) solve puzzle (3) quit inspect: ")
        print("_________________________________________________________________________")
        print("                                                                         ")
        if choice == "1":
            time.sleep(1)
            print("Items in your inventory:")
            for item in inventory:
                time.sleep(.2)
                print(f"- {item.name}")
            time.sleep(1)
            item_name = input("Which item would you like to inspect?")
            for item in inventory:
                if item.name == item_name:
                    time.sleep(1)
                    print(f"{item.name}: {item.description}")
                    input("Press Enter When You'd Like to Continue:")
                    break
            else:
                time.sleep(1)
                print("Item not found in inventory.")
            self.inspect()
        elif choice == "2":
            if self.puzzles:
                for puzzle in self.puzzles:
                    self.solve_puzzle(puzzle)
                    if self.solved == True:
                        self.puzzles.remove(puzzle)
                        time.sleep(1)
                        print(f"You solved the {puzzle.name} puzzle!")
            else:
                time.sleep(1)
                print("There are no puzzles here.")
            self.inspect()
        elif choice == "3":
            time.sleep(2)
            print("You quit inspecting the area.")
            
        else:
            print("Invalid choice.")
            self.inspect()
class Game:
    def __init__(self, areas):
        clear(True)
        self.areas = areas
        self.is_playing = True
        self.final_obj = "reality"
        self.candle = Candle(300)
    def main(self):
        time.sleep(2)
        clear(False)
        if self.candle.checkpoint_test(self):
            return
        
        print("_________________________________________________________________________")
        print("                                                                         ")
        print("What would you like to do? (1) Inspect area (2) Use item (3) View Candle")
        print("_________________________________________________________________________")
        print("                                                                         ")
        
        ans = input()
        if ans == "1":
            self.cd()
        elif ans == "2":
            time.sleep(1)
            print("Items in your inventory:")
            for item in inventory:
                time.sleep(.2)
                print(f"- {item.name}")
            time.sleep(1)
            item_name = input("Enter the name of the item you want to use: ")
            for item in inventory:
                if item.name == item_name:
                    time.sleep(1)
                    print(item.name + ": " + item.description)
                    input("Press Enter When You'd Like to Continue:")
                if item.name.lower() == self.final_obj:
                    time.sleep(7)
                    print("What.?.?")
                    time.sleep(2)
                    print("You snap back to reality and realize you never tried to open the coffin.")
                    time.sleep(2)
                    print("With just a little bit of force, you kick the lid off and find yourself in the middle of your living room.")
                    time.sleep(4)
                    print("You're confused, but that doesn't matter right now. You're safe!")
                    self.is_playing = False
                    return
            
            self.main()
        elif ans == "3":
            time.sleep(1)
            self.candle.view_candle()
            self.main()
        else:
            time.sleep(1)
            print("Invalid choice.")
            self.main()
    def cd(self):
        if self.candle.checkpoint_test(self):
            return
        areas = self.areas
        time.sleep(2)
        answer = input("There are a few visible objects around you: "+", ".join([area.name for area in areas])+"\n"+"Enter location you Would Like to Inspect: ").lower()
        time.sleep(1)
        area = next((area for area in areas if area.name.lower() == answer), None)
        if area:
            area.inspect()
        else:
            time.sleep(1)
            print("Invalid location.")