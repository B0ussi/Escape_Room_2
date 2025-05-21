import framework
silver_key = framework.Item("Silver Key",False, "A shiny silver key that fits the silver keyhole.")

padlock = framework.Padlock("Padlock", "A small padlock with a 3-digit combination.", "547")
padlock_box = framework.Area("Padlock Box", "A small box with a padlock on it.",[padlock], silver_key )


silver_keyhole = framework.Keyhole("Silver Keyhole", "A keyhole that takes in a silver key.", "Silver key", "Silver Key")
silver_box = framework.Area("Silver Box", "A small box with a silver keyhole on it.", [silver_keyhole], [silver_key])

gold_keyhole = framework.Keyhole("Gold Keyhole", "A keyhole that takes in a gold key.", "Gold Key", "Gold Key")
gold_key = framework.Item("Gold Key",False, "A shiny gold key that fits the gold keyhole.")
gold_box = framework.Area("Gold Box", "A small box with a gold keyhole on it.", [gold_keyhole], [gold_key])

switches_puzzle = framework.Switches("Switches Puzzle", "A series of switches that can be either up or down.", 5, ["up", "down", "up","up", "down"])

switches = framework.Area("Switches", "A series of switches that can be either up or down.",[switches_puzzle], gold_key)

areas = [padlock_box, gold_box, silver_box, switches]

game = framework.Game(areas)
print("You wake up after a 'great' night, laying in complete darkness.")
print("You feel around and realize your in a very small box just bigger than the length of your body.")
print("You feel something that feels like a candle to your right.")
print("You have a lighter in your pocket from the night before.")
print("you light the candle and it all becomes clear.")
print("YoU ARE IN A COFFIN!")
print("You see a number scratched into the wood of the coffin.")
print("It reads: 547")
print("those numbers are now available in your inventory.")
numbers = framework.Item("Numbers", False, "The numbers 547 scratched into the wood of the coffin.")
framework.inventory.append(numbers)
game.main()

