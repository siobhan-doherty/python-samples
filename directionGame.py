available_exits = ["east", "north east", "south"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose direction: ")
    if chosen_exit in ["Quit", "quit", "QUIT"]:
        print("Game Over")
        break

print("Thank you for playing")