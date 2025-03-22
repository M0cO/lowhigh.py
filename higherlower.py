logo = ("""
 _   _ _       _                   
| | | (_) __ _| |__   ___ _ __     
| |_| | |/ _` | '_ \ / _ \ '__|    
|  _  | | (_| | | | |  __/ |       
|_| |_|_|\__, |_| |_|\___|_|       
      | ||___/____      _____ _ __ 
      | |   / _ \ \ /\ / / _ \ '__|
      | |__| (_) \ V  V /  __/ |   
      |_____\___/ \_/\_/ \___|_|   
""")

def compare_values(list):
    user_choices = []

    index = 0
    name = data[index]['name']
    key1 = data[index]['stream_count']

    for i in range(1, len(data)):
        name2 = data[i]['name']
        key2 = data[i]['stream_count']

        print(f"Which do you think has a higher amount of streams?")
        user_choice = input(f"\nChoose 'A' or 'B'\nA. {name}\nB. {name2}\n").lower()

        if user_choice == 'a':
            correct_answer = key1
            chosen_name = name
        elif user_choice == 'b':
            correct_answer = key2
            chosen_name = name2
        else:
            print('invalid, please choose A or B')
            continue


        # Check if the user's choice is correct
        if correct_answer == max(key1, key2):
            print('correct')
            user_choices.append((chosen_name, correct_answer))

            # Update the current item to the chosen one for the next comparison
            name = chosen_name
            key1 = correct_answer
        else:
            print("incorrect")
            break

        print()
    return user_choices


data = [
    {
        'name': 'Tekken 8',
        'stream_count': 49,
    },
    {
        'name': 'Mortal Kombat 1',
        'stream_count': 26,
    },
    {
        'name': 'Dota 2',
        'stream_count': 472,
    },
    {
        'name': 'OverWatch 2',
        'stream_count': 195,
    },
    {
        'name': 'Fortnite',
        'stream_count': 404,
    },
    {
        'name': 'World of Warcraft',
        'stream_count': 503,
    },
    {
        'name': 'Marvel Rivals',
        'stream_count': 338,
    },
    {
        'name': 'Monster Hunter Wilds',
        'stream_count': 335,
    },
    {
        'name': 'Street Fighter 6',
        'stream_count': 108,
    },
    {
        'name': 'Leage of Legends',
        'stream_count': 875,
    },
    {
        'name': 'Counter Strike',
        'stream_count': 682,
    },
    {
        'name': 'MineCraft',
        'stream_count': 252,
    }
]

print(logo)
result = compare_values(data)
print("User's correct choices:", result)
