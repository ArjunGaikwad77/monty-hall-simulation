import random

def monty_hall_simulation(trials=10000, doors=3):
    
    stay_wins = 0
    switch_wins = 0

    for _ in range(trials):
        prize_door = random.randint(0, doors-1)

        player_choice = random.randint(0, doors-1)

        possible_doors = [d for d in range(doors) if d != player_choice and d != prize_door]
        monty_opens = random.choice(possible_doors)

        if player_choice == prize_door:
            stay_wins += 1

        remaining_doors = [d for d in range(doors) if d != player_choice and d != monty_opens]
        switched_choice = random.choice(remaining_doors)
        if switched_choice == prize_door:
            switch_wins += 1

    return (stay_wins/trials*100, switch_wins/trials*100)


if __name__ == "__main__":
    trials = 10000
    
    stay3, switch3 = monty_hall_simulation(trials, doors=3)
    print(f"--- 3 DOORS ---")
    print(f"Win percentage (Stay)   : {stay3:.2f}%")
    print(f"Win percentage (Switch) : {switch3:.2f}%")

    stay4, switch4 = monty_hall_simulation(trials, doors=4)
    print(f"\n--- 4 DOORS ---")
    print(f"Win percentage (Stay)   : {stay4:.2f}%")
    print(f"Win percentage (Switch) : {switch4:.2f}%")
