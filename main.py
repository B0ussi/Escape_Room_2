import framework
import time
print("_____________________")
print("")
input("Press Enter To Start")
print("_____________________")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")
time.sleep(2)

areas = []

silver_key = framework.Item("Silver Key",False, "A shiny silver key that fits the silver keyhole.")
gold_key = framework.Item("Gold Key",False, "A shiny gold key that fits the gold keyhole.")
note = framework.Item("Note", False, "A note that reads: The first, is sometimes also the best. Undead Demons Utter Unholy Desires.")
padlock = framework.Padlock("Padlock", "A small padlock with a 3-digit combination.", "547")
padlock_box = framework.Area("Padlock Box", "A small box with a padlock on it.",[padlock], silver_key )

reality = framework.Item("Reality", False, "A note that reads: If your're reading this, you are probably scared for your life. \n Just know, you're the one that said you wouldn't drink too much.\n Just kick the lid off, no one ever locked it.")

silver_keyhole = framework.Keyhole("Silver Keyhole", "A keyhole that takes in a silver key.", "Silver key", silver_key)
silver_box = framework.Area("Silver Box", "A small box with a silver keyhole on it.", [silver_keyhole], note)

gold_keyhole = framework.Keyhole("Gold Keyhole", "A keyhole that takes in a gold key.", "Gold Key", gold_key)
gold_box = framework.Area("Gold Box", "A small box with a gold keyhole on it.", [gold_keyhole], reality )

switches_puzzle = framework.Switches("Switches Puzzle", "A series of switches that can be either up or down.", 5, ["up", "down", "up","up", "down"])

switches = framework.Area("Switches", "A series of switches that can be either up or down.",[switches_puzzle], gold_key)

title = "The Coffin Accident"
areas = [padlock_box, gold_box, silver_box, switches]
for area in areas:
    area.init_dir(["Inspect Inventory", "Solve", "Quit"])
narr = ""

def add_narration(msg, sec = 3):
    global narr
    for i in range(len(msg)):
        framework.clear(True)
        print(title+": ")
        print("_________________________________________________________________________")
        print("                                                                         ")
        print(narr)
        print(msg[0:i])
        time.sleep(.01)
    time.sleep(sec)
    narr+=msg

game = framework.Game(areas, title)

add_narration("You wake up after a 'great' night, laying in complete darkness.\n")
add_narration("You feel around and realize you're in a very small box just bigger than the length of your body.\n")
add_narration("You feel something that feels like a candle to your right.\n")
add_narration("You have a lighter in your pocket from the night before.\n")
add_narration("you light the candle and it all becomes clear.\n")
add_narration("YOU ARE IN A COFFIN!\n")
add_narration("Remember this candle won't last forever...\n")
add_narration("You see a number scratched into the wood of the coffin.\n")
add_narration("It reads: 547\n",2)
add_narration("those numbers are now available in your inventory.\n")

framework.narration = narr

numbers = framework.Item("Numbers", False, "The numbers 547 scratched into the wood of the coffin.")
framework.inventory.append(numbers)
is_playing = True
while is_playing:
    game.main()
    is_playing = game.is_playing