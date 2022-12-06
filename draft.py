import random

players = []
characters = []
split_pools = []

def add_players(): 
    for i in range(2):
        players.append(str(input(f"First Team Player {i + 1}:\n")))
    for i in range(2):
        players.insert(i + 1, str(input(f"Second Team Player {i + 1}:\n")))

def draft(picks):
    characters.clear()
    split_pools.clear()
    for _ in range(4):
        split_pools.append([])
    for _ in range(picks):
        for i in range(4):
            while True:
                x = str(input(f"\n{players[i]}'s pick:\n"))
                if x in characters:
                    print(f"{x} has already been drafted. Pick a different " 
                    "character.")
                else: 
                    characters.append(x)
                    split_pools[i].append(x)
                    break

def assign_sin():
    print("\n")
    for i in range(4):
        print(players[i] + ": " + (random.choice(characters)))
    print("\n")

def assign_indi():
    print("\n")
    for i in range(4):
        print(players[i] + ": " + (random.choice(split_pools[i])))
    print("\n")

def menu_sin(picks):
    while True:
        action = str(input("Press Enter for next game\n"
            "Input 'r' to redraft with same teams\n"
            "Input 'i' to reassign from invidiaul pools\n"
            "Input 'q' to quit:\n"))
        if action == "":
            assign_sin()
        elif action == "r":
            draft(picks)
            assign_sin()
        elif action == "i":
            assign_indi()
            menu_indi(picks)
            break
        elif action == "q":
            break
        else:
            print("\nInvalid input\n")

def menu_indi(picks):
    while True:
        action = str(input("Press Enter for next game\n"
                "Input 'r' to redraft with same teams\n"
                "Input 's' to reassign all from one pool\n"
                "Input 'q' to quit:\n"))
        if action == "":
            assign_indi()
        elif action == "r":
            draft(picks)
            assign_indi()
        elif action == "s":
            assign_sin()
            menu_sin(picks)
            break
        elif action == "q":
            break
        else:
            print("\nInvalid input\n")


def mode_select(picks):
    print("\n")
    while True:
        mode = str(input("Input 's' to assign all players from the same pool\n"
                "Input 'i' to assign each player from their own pool:\n"))
        if mode == "s":
            assign_sin()
            menu_sin(picks)
            break
        elif mode == "i":
            assign_indi()
            menu_indi(picks)
            break
        else:
            print("Invalid input\n")

    
    
def main():   
    print("\nDrafted Random Doubles!\n")
        
    add_players()

    print("\n")

    while True:
            picks = int(input("How many character picks per player?\n"))
            if picks < 1:
                print("Input 1 or more for character picks.")
            else:
                break

    draft(picks)

    mode_select(picks)

main()