## Storing my game data

print("Welcome to Landscaper!")

landscaper_data = {
    "money": 0,
    "tools": "teeth",
    "quit": False
}

while(True):
    print(f"""
          You have ${landscaper_data['money']} and are currently using your {landscaper_data['tools']} to cut grass.""")
    user_input = int(input(""" 
                        What would you like to do?
                        [1] Cut Grass
                        [2] Upgrade Tool
                        [3] Quit
                        """))
    if (user_input == 1):
        if (landscaper_data['tools'] == "teeth"):
            landscaper_data['money'] += 1
            print(f"You made $1 cutting grass with your teeth! You now have ${landscaper_data['money']}.")
        
        if (landscaper_data['tools'] == "rusty scissors"):
            landscaper_data['money'] += 5
            print(f"You made $5 cutting grass using the rusty scissors! You now have ${landscaper_data['money']}.")

    if (user_input == 2):
        if (landscaper_data['tools'] == "teeth" and landscaper_data['money'] >= 5):
            print("You upgraded to rusty scissors! You now make $5 cutting grass!")

            landscaper_data['money'] -= 5
            landscaper_data['tools'] = "rusty scissors"
        else:
            print("You can't upgrade at this time. Come back later.")

    if (user_input == 3):
        landscaper_data['quit'] = True

    if (landscaper_data['quit'] is True):
        print("You quit the game!")
        break

    if (landscaper_data['money'] >= 10):
        print("You win")
        break