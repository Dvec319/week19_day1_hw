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
                        [2] Quit
                        """))
    if (user_input == 1):
        landscaper_data['money'] += 1
        print(f"You made $1 cutting grass with your teeth! You now have ${landscaper_data['money']}.")

    if (user_input == 2):
        landscaper_data['quit'] = True

    if (landscaper_data['quit'] is True):
        print("You quit the game!")
        break

    if (landscaper_data['money'] >= 10):
        print("You win")
        break