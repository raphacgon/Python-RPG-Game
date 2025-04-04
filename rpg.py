import random
"""
Text-Based Adventure Game
==========================

This is a simple text-based RPG-style adventure game where the player takes on the role of a wandering adventurer.
The game is built around random encounters, decision-making, and a basic combat system.

Game Features:
--------------
- Gender Selection: Players choose their gender, which determines pronoun use throughout the story.
- Weapon Choice: Players pick between an Iron Sword or a Silver Dagger at the beginning of the game.
- Enemy Encounters: In each round, the player encounters a randomly selected creature with a randomly assigned emotion and level.
- Level System: Enemies have levels ranging from 1 to 5, influencing the difficulty of the fight.
- Combat System: Players choose between different combat strategies and must guess a number behind the scenes to succeed.
    - Successful fights reward the player with an extra life.
    - Failed fights result in life loss.
- Run Away Mechanic: Players can flee from combat, but only up to 3 times. After the third attempt, escape becomes impossible.
- Life System: The player starts with 3 lives. Gaining or losing lives depends on the outcome of each battle.
- Narrative Feedback: Each action is narrated with randomly selected scenario descriptions for immersion.
- Game Over: The game ends when the player reaches 20 rounds, loses all lives or gets 10 x❤️.

It's a lightweight experiment in interactive fiction, inspired by classic RPG themes, but kept intentionally simple.
"""
bugs = [""]
space = "\n"*40
error_msg = "Error! Invalid Option! >:("
user_name = input("Hello, Adventurer! How shall you be called?\n").capitalize()
suggestions = [
    "Improve aesthetics (colors, animations with time.sleep, etc).",
    "Add background music using playsound.",
    "Introduce rare enemies, bosses, or ability effects.",
    "Attack damage multiplied according to selected weapon"
]
line = "=_=_=_=_=_=_=_=_=_=_=_=_=_="

if user_name in ["dev", "DEV", "Dev", "Raphael"]:
    print(f"{line}\n-=-DEVELOPER MODE-=-\n-GODMODE IS ENABLED-\nImprovement Suggestions:\n" +"\n".join(suggestions))
print(f"{line}")

while True:
    user_gender = input("Are you a She or a He?\n1-She\n2-He\n")  # Defines the player gender
    print(f"{line}")

    if user_gender == "1":
        user_gender = "she"
        user_pos = "her"
        user_pos2 = user_pos
        break
    elif user_gender == "2":
        user_gender = "he"
        user_pos = "his"
        user_pos2 = "him"
        break
    else:
        print(f"{error_msg}")
        print(f"{line}")

small_entity = [
    "Rat", "Dog", "Mosquito", "Gremlin",
    "Ghoul", "Vampire", "Werewolf", "Mutant",
    "Revenant", "Demon", "Lizardman",
    "Hyena", "Wolf", "Boar"
]

emotion_list = ["raging", "mouth gurgling", "rabid", "living dead"]
level_list = [1, 2, 3, 4, 5]

while True:
    weapon_choice = input("What's your weapon of choice?\n1-An Iron Sword\n2-A Silver Dagger\n")
    print(f"{line}")
    if weapon_choice == "1":
        weapon_choice = "Iron Sword"
        break
    elif weapon_choice == "2":
        weapon_choice = "Silver Dagger"
        break
    else:
        print(f"{error_msg}")
        print(f"{line}")

fight_options = f"What should {user_name} do?\n1-Fight\n2-Run away\n"


enter_sm = f"Press ENTER to continue...\n{line}\n"

def fight_sys(entity, life, emotion, level):
    #: Handles combat mechanics, determining win or loss scenarios.
    while True:
        fight_choice = input(
            "Time to fight! Choose your next move to proceed.\n1-Precision stab\n2-Dodge and counterattack\n3-Brute force attack\n")
        print(f"{line}")

        if level < 3:
            fight_numbers = ["1", "2", "3"]
        elif level == 3:
            fight_numbers = ["1", "2", "3", "4"]
        elif level == 4:
            fight_numbers = ["1", "2", "3", "4", "5"]
        else:
            fight_numbers = ["1", "2", "3", "4", "5", "6"]

        fight_number = random.choice(fight_numbers)

        win_scenarios = [
            f"{user_name} frowns and swings {user_pos} {weapon_choice} towards the {emotion} {entity}, striking it down.",
            f"{user_name} overpowers the {entity} with a clean hit, making it flee.",
            f"{user_name} swiftly dodges and counters, taking down the {emotion} {entity}.",
            f"{user_name} glares at the {emotion} {entity}, gripping {user_pos} {weapon_choice} tightly.\nWith a swift and powerful swing, {user_gender} slashes through the air, the sheer force of the attack sending dust flying.\nThe {entity} hesitates, sensing that it is no match for {user_name}.\nWith one last defiant snarl, the creature scampers away, choosing to live another day. {user_name} watches it go, victorious but ever cautious.",
            f"The {emotion} {entity} growls and prepares to attack, but {user_name} wastes no time.\nWith a burst of speed, {user_name} swings {user_pos} {weapon_choice} with full force, striking the creature square in the chest.\nThe impact sends the {entity} rolling back, stunned and whimpering.\nIt scrambles to its feet and flees into the darkness, defeated. {user_name} wipes {user_pos} weapon clean and continues the journey, unshaken."
        ]

        lose_scenarios = [
            f"{user_name} swings but the {emotion} {entity} dodges and bites back, forcing a retreat.",
            f"{user_name} miscalculates an attack and the {entity} retaliates viciously, making escape the only option.",
            f"{user_name} is overwhelmed and knocked down, barely managing to flee.",
            f"{user_name} grips {user_pos} {weapon_choice} tightly and strikes at the {emotion} {entity}. But the creature is relentless, dodging every attack with ease.\nAfter a fierce struggle, {user_name} is exhausted.\n{user_pos.capitalize()} legs feel weak, and {user_pos} vision blurs. The only choice left is to flee before it's too late.",
            f"{user_name} slashes at the {emotion} {entity}, but the blow barely grazes it. The creature retaliates with a vicious swipe, knocking {user_name} to the ground.\nAs {user_pos} weapon slips from {user_pos} grasp, panic sets in.\nThere's no choice but to scramble to {user_pos} feet and escape before it's too late."
        ]

        if fight_choice in fight_numbers:
            if level == 1 or fight_choice == fight_number or user_name in ["Raphael", "dev", "DEV", "Dev"]:
                life += 1
                print(random.choice(win_scenarios))
                print(f"{line}\n{user_name} WON 1 x❤️ and now has {life} x❤️.")
                print(f"{line}")
                input(f"{enter_sm}")
            else:
                print(random.choice(lose_scenarios))
                life -= 1
                print(f"{line}\n{user_name} LOST 1 x❤️ and now has {life} x❤️.")
                print(f"{line}")
                input(f"{enter_sm}")
            return life
        else:
            print(f"{error_msg}")


def run_away_sys(entity, emotion, life):
    #: Manages the scenario where the player runs away from an enemy.
    run_scenarios = [
    f"{user_name} turns around and runs as fast as {user_pos} legs can carry {user_pos2}, leaving the {emotion} {entity} behind.",
    f"{user_name} barely dodges the {emotion} {entity}'s claws and sprints away, heart pounding.",
    f"{user_name} throws dirt into the eyes of the {entity}, using the distraction to make a quick escape.",
    f"As the {entity} lunges, {user_name} leaps to the side and dashes into the woods.",
    f"The {emotion} {entity} snarls, but {user_name} vanishes behind the ruins before it can react.",
    f"{user_name} trips but quickly rolls back up, narrowly escaping the {entity}'s grasp.",
    f"The {entity} lets out a deafening roar, but {user_name} is already gone, running for dear life.",
    f"Without a second thought, {user_name} takes off, hearing the {entity} crashing through the underbrush behind.",
    f"{user_name} leaps over a fallen tree and dashes through the fog, escaping the {emotion} {entity}.",
    f"The {entity} lunges forward, but {user_name} dives into a river, letting the current carry {user_pos2} to safety.",
    f"{user_name} kicks a wooden crate towards the {emotion} {entity}, creating just enough of a delay to flee.",
    f"With a burst of adrenaline, {user_name} climbs up a rocky ledge, leaving the {entity} growling below.",
    f"{user_name} sees no other option and bolts into a nearby cave, hoping the {entity} won’t follow.",
    f"The {emotion} {entity} howls, but {user_name} is already disappearing over the horizon, refusing to look back."
    ]

    print(random.choice(run_scenarios))
    print(f"You fled safely. Your lives remain the same: {life} x❤️")
    print(f"{line}")
    input(f"{enter_sm}")

def game():
    #: Main function controlling the game loop, enemy encounters, and player choices.
    rounds = 0
    run_attempts = 0
    life = 3

    while rounds < 20 and life > 0:
        rounds += 1
        entity = random.choice(small_entity)
        emotion = random.choice(emotion_list)
        level = random.choice(level_list)
        print(f"{space}{line}\n {user_name} is walking down the road when suddenly a lvl.{level} {emotion} {entity} appears! \n{line}\nNº of ❤️:{life}\n{line}\n")

        while True:
            choice1 = input(fight_options)
            print(f"{line}")

            if choice1 == "1":
                life = fight_sys(entity, life, emotion, level)
                break
            elif choice1 == "2":
                run_attempts += 1
                if run_attempts >= 4:
                    print("You hurt your feet and can't run anymore.")
                    life = fight_sys(entity, life, emotion, level)
                    break
                run_away_sys(entity, emotion, life)
                break
            else:
                print(f"{error_msg}")
                print(f"{line}")

        print(f"Rounds Played: {rounds}")
        print(f"{line}")
        if life == 0:
            print(f"You have been defeated by lvl.{level} {entity}...\n{line}\n THANKS FOR PLAYING! :)")
            input(f"{enter_sm}")
            break
        elif rounds == 20 and life > 0:
            print(f"CONGRATULATIONS!!! YOU WON!!!\n Nº. of lives ❤️:{life}\nTHANKS FOR PLAYING! :)")
            input(f"{enter_sm}")
            break
        elif life >= 10:
            print(f"CONGRATULATIONS!!! YOU WON!!!\n Nº. of lives ❤️:{life}\nTHANKS FOR PLAYING! :)")
            input(f"{enter_sm}")
            break



game()
