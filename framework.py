import time
import os
narration = ""
current_lines = ""
title = ""
def print_lines(narr):
    print("Narration: ")
    print("_________________________________________________________________________")
    print("                                                                         ")
    print(narr)
    print("_________________________________________________________________________")
    print("                                                                         ")
    print(current_lines)
def clear(first):
    
    if os.name == 'nt':
        os.system('cls')   
    else:
        os.system('clear') 
    if not first:
        print_lines(narration)
def text(msg):
    global current_lines
    for letter in range(len(msg)+1):
        clear(False)
        print(msg[0:letter])
        time.sleep(.01)
    current_lines+=msg+"\n"
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
            text("The candle ran out of light filling your coffin with the darkness waiting to rush back in.")
            time.sleep(0.5)
            text("You never made it out.")
            game.is_playing = False
            return True
        elif self.get_time_since()/self.secs >= self.current_checkpoint:
            self.current_checkpoint+=.25
            text(f"The candle seems to be at least {(self.current_checkpoint-.25)*100}% burnt out.")
            input("Press Enter When You Are Ready to Continue")
    def view_candle(self):
        time.sleep(0.25)
        text(f"The candle seems to be about {round((self.get_time_since()/self.secs)*100)}% burnt out.")
        input("Press Enter When You're Ready to Continue")

class Item:
    def __init__(self, name, owned, description):
        self.name = name
        self.owned = owned
        self.description = description
    def pickup(self):
        if self.owned == False:
            self.owned = True
            inventory.append(self)
            
            text(f"You picked up {self.name}.")
            time.sleep(0.5)
        else:
            text(f"You already have {self.name}.")
            time.sleep(0.25)
    def use(self, target):
        pass

class Puzzle:
    def __init__(self, name, description, answer):
        self.name = name
        self.description = description
        self.answer = answer
class Padlock(Puzzle):
    def run(self):
        text("You see a padlock. It has a 3-digit combination.")
        time.sleep(1)
        text("Enter the combination:")

        user_input = input()
        text(user_input)
        if user_input == self.answer:
            text("You hear a click and with a pull, the padlock clicks open!")
            time.sleep(0.5)
            return True
        else:
            text("You try to pull the padlock open, but nothing budges.")
            time.sleep(0.5)
            return False
        
class Keyhole(Puzzle):
    def __init__(self, name, description, answer, key):
        super().__init__(name, description, answer)
        self.key = key
    def run(self):
        global current_lines
        text("You see a keyhole. It takes in a specific key.")
        time.sleep(0.75)
        resp = input(("Which Item Will you Like to Use?: "+", ".join([item.name for item in inventory]))+": ")
        current_lines+= ("Which Item Will you Like to Use?: "+", ".join([item.name for item in inventory]))+": "+resp
        clear(False)
        for item in inventory:
            if item.name == resp:
                time.sleep(0.5)
                text(f"You try to insert the {item.name} into the keyhole.")
                if item.name == self.key.name:
                    time.sleep(0.5)
                    text("The key fits perfectly! With a pull, the keyhole clicks open!")
                    time.sleep(0.25)
                    return True
                else: 
                    time.sleep(0.5)
                    text("The key doesn't fit. You try to pull the keyhole open, but nothing budges.")
                    time.sleep(0.25)
                    return False

class Switches(Puzzle):
    
    def __init__(self, name, description, num_switches,answer):
        super().__init__(name, description, answer)
        self.num_switches = num_switches
    def run(self):
        directions = []
        time.sleep(0.5)
        text(f"You see a series of {self.num_switches} switches. Each switch can be either up or down.")
        time.sleep(0.5)
        i = 0
        end = number_endings[0]
        while i < self.num_switches: 
            if i >-1 and i <=2:
                end = number_endings[i]
            else:
                end = number_endings[3]
            us = input(f"Enter the {str(i+1)+end} switches direction(up/down): ")
            if us.lower() == "up" or us.lower() == "down":
                directions.append(us.lower())
                i+=1
                time.sleep(0.25)
                text("You flipped the switch "+us.lower()+".")
                time.sleep(0.5)
            else:
                text("Invalid input. Please enter 'up' or 'down'.")
                time.sleep(0.5)
        if self.answer == directions:
            time.sleep(0.5)
            text("You feel a small pull on the last switch, and with a pull, a secret door opens exposing a golden key!")
            return True
        else:
            time.sleep(0.5)
            text("You try to pull the switches, but nothing happens.")
            return False

# (code continues, but modified time.sleep() follows the same logic)


class Area:
    def __init__(self, name, description, puzzles, reward):
        self.name = name
        self.description = description
        self.items = []
        self.puzzles = puzzles
        self.reward = reward
        self.solved = False
        self.dir = []
    def init_dir(self, funcs):
        for func in funcs:
            self.dir.append(func)
    def print_nav(self):
        global current_lines
        current_lines = ""
        msg = "What would you like to do? "+" ".join(f"({i+1}) {func}" for i, func in enumerate(self.dir))
        for letter in range(len(msg)):
            clear(False)
            global title
            print(title+" / "+self.name+": ")
            print("_________________________________________________________________________")
            print("                                                                         ")
            print(msg[0:letter])
            print("_________________________________________________________________________")
            print("                                                                         ")
            time.sleep(.01)
        clear(False)
        current_lines+=(title+" / "+self.name+": \n")
        current_lines+=("_________________________________________________________________________\n")
        current_lines+=("                                                                         \n")
        current_lines+=msg+"\n"
        current_lines+=("_________________________________________________________________________\n")
        current_lines+=("                                                                         \n")
        clear(False)
        choice = input()
        return choice

    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def list_items(self):
        if len(self.items) == 0:
            text("There are no items here.")
        else:
            text("Items in this area:")
            for item in self.items:
                text(f"- {item.name}: {item.description}")
    def solve_puzzle(self, puzzle):
        answer = puzzle.run()
        if answer == True:
            time.sleep(.5)
            self.solved = True
            time.sleep(.5)
            text(f"{self.reward.name} is now available in your inventory.")
            inventory.append(self.reward)
            input("Press Enter When You're Ready to Continue")
        else:
            time.sleep(.5)
            text("The puzzle remains unsolved.")

    

    def inspect(self):
        text(f"You inspect the {self.name}.")
        time.sleep(.5)
        choice = self.print_nav()
        # print("_________________________________________________________________________")
        # print("                                                                         ")
        # choice = input("Would you like to do? (1) inspect inventory (2) solve puzzle (3) quit inspect: ")
        # print("_________________________________________________________________________")
        # print("                                                                         ")
        
        def inspect_inventory():
            time.sleep(.25)
            text("Items in your inventory:")
            for item in inventory:
                time.sleep(.5)
                text(f"- {item.name}")
            time.sleep(.25)
            item_name = input("Which item would you like to inspect? ")
            for item in inventory:
                if item.name == item_name:
                    time.sleep(.25)
                    text(f"{item.name}: {item.description}")
                    input("Press Enter When You'd Like to Continue:")
                    break
            else:
                time.sleep(.25)
                text("Item not found in inventory.")
            self.inspect()

        def solve():
            if self.puzzles:
                for puzzle in self.puzzles:
                    self.solve_puzzle(puzzle)
                    if self.solved == True:
                        self.puzzles.remove(puzzle)
                        time.sleep(.25)
                        return
            else:
                time.sleep(.25)
                text("There are no puzzles here.")
            self.inspect()

        def quit():
            time.sleep(.5)
            text("You quit inspecting the area.")
        
        funcs = {"Quit": quit,
                 "Solve": solve,
                 "Inspect Inventory": inspect_inventory,
                 }
        
        if self.dir[int(choice)-1]:

            funcs[self.dir[int(choice)-1]]()
        else:
            text("Invalid choice.")
            self.inspect()
class Game:
    def __init__(self, areas, game_title):
        clear(True)
        self.areas = areas
        self.is_playing = True
        self.final_obj = "reality"
        self.candle = Candle(300)
        global title
        title = game_title
    def main(self):
        time.sleep(.5)
        global current_lines
        current_lines = ""
        clear(False)
        if self.candle.checkpoint_test(self):
            return
        msg = "What would you like to do? (1) Inspect area (2) Use item (3) View Candle"
        for i,letter in enumerate(msg):
            clear(False)
            print(title+": ")
            print("_________________________________________________________________________")
            print("                                                                         ")
            print(msg[0:i+1])
            print("_________________________________________________________________________")
            print("                                                                         ")
            time.sleep(.01)
        current_lines+= title+": \n"
        current_lines+= "_________________________________________________________________________\n"
        current_lines+= " \n"
        current_lines+=msg+"\n"
        current_lines+="_________________________________________________________________________\n"
        current_lines+=" \n"
        ans = input()
        if ans == "1":
            self.cd()
        elif ans == "2":
            time.sleep(.25)
            text("Items in your inventory:")
            for item in inventory:
                time.sleep(.2)
                text(f"- {item.name}")
            time.sleep(.25)
            item_name = input("Enter the name of the item you want to use: ")
            for item in inventory:
                if item.name == item_name:
                    time.sleep(.25)
                    text(item.name + ": " + item.description)
                    input("Press Enter When You'd Like to Continue: ")
                if item.name.lower() == self.final_obj:
                    time.sleep(3)
                    text("What.?.?")
                    time.sleep(2)
                    text("You snap back to reality and realize you never tried to open the coffin.")
                    time.sleep(2)
                    text("With just a little bit of force, you kick the lid off and find yourself in the middle of your living room.")
                    time.sleep(4)
                    text("You're confused, but that doesn't matter right now. You're safe!")
                    self.is_playing = False
                    return
            
            self.main()
        elif ans == "3":
            time.sleep(.25)
            self.candle.view_candle()
            self.main()
        else:
            time.sleep(.25)
            text("Invalid choice.")
            self.main()
    def cd(self):
        if self.candle.checkpoint_test(self):
            return
        areas = self.areas
        time.sleep(.5)
        msg = "There are a few visible objects around you: "+", ".join([area.name for area in areas])+"\n"+"Enter location you Would Like to Inspect: "
        for letter in range(len(msg)):
            clear(False)
            print(msg[0:letter+1])
            time.sleep(.01)
        clear(False)
        answer = input(msg).lower()
        time.sleep(.25)
        area = next((area for area in areas if area.name.lower() == answer), None)
        if area:
            area.inspect()
        else:
            time.sleep(.25)
            text("Invalid location.")