## Storing my game data

print("Welcome to Landscaper!")

player = input("What is your name? ")

print(f"Hello {player}. Ready to start?")

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
                        [3] Reset
                        [4] Quit
                        """))
    if (user_input == 1):
        if (landscaper_data['tools'] == "teeth"):
            print(f"You made $1 cutting grass with your teeth! You now have ${landscaper_data['money']}.")

            landscaper_data['money'] += 1
        
        elif (landscaper_data['tools'] == "rusty scissors"):
            print(f"You made $5 cutting grass using the rusty scissors! You now have ${landscaper_data['money']}.")

            landscaper_data['money'] += 5

        elif (landscaper_data['tools'] == "push mower"):
            print(f"You made $50 cutting grass using the push mower! You now have ${landscaper_data['money']}.")
            
            landscaper_data['money'] += 50

        elif (landscaper_data['tools'] == "electric mower"):
            print(f"You made $100 cutting grass using the electric mower! You now have ${landscaper_data['money']}.")

            landscaper_data['money'] += 100

        elif (landscaper_data['tools'] == "team"):
            print(f"You made $250 cutting grass using your team! You now have ${landscaper_data['money']}.")

            landscaper_data['money'] += 250
            

    elif (user_input == 2):
        if (landscaper_data['tools'] == "teeth" and landscaper_data['money'] >= 5):
            print("You upgraded to rusty scissors! You now make $5 cutting grass!")

            landscaper_data['money'] -= 5
            landscaper_data['tools'] = "rusty scissors"

        elif (landscaper_data['tools'] == "rusty scissors" and landscaper_data['money'] >= 25):
            print("You upgraded to the push lawnmower! You now make $50 cutting grass!")

            landscaper_data['money'] -= 25
            landscaper_data['tools'] = "push mower"

        elif (landscaper_data['tools'] == "push mower" and landscaper_data['money'] >= 250):
            print("You upgraded to the electric mower! You now make $100 cutting grass!")

            landscaper_data['money'] -= 250
            landscaper_data['tools'] = "electric mower"

        elif (landscaper_data['tools'] == "electric mower" and landscaper_data['money'] >= 500):
            print("You upgraded to the team of starving students! You now make $250 cutting grass!")

            landscaper_data['money'] -= 500
            landscaper_data['tools'] = "team"

        else:
            print("You can't upgrade at this time. Come back later.")

    elif (user_input == 3):
        print("You reset the game! Everything has been set back to starting attributes!")
        landscaper_data['money'] = 0
        landscaper_data['tools'] = "teeth"

    elif (user_input == 4):
        landscaper_data['quit'] = True

    elif (landscaper_data['quit'] is True):
        print("You quit the game!")
        break

    else:
        print("You didn't select a listed option. Please try again.")

    if (landscaper_data['money'] >= 1000 and landscaper_data['tools'] == "team"):
        print("You made at least $1000 and have a team of students. Congratulations, you win!")
        break