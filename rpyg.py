import random
import time
import pygame

# Initialize pygame mixer and load sound effects
pygame.mixer.init()
input_sound = pygame.mixer.Sound("audio/typewriter.mp3")
wasted_sound = pygame.mixer.Sound("audio/wasted_fx.mp3")
win_sound = pygame.mixer.Sound("audio/victory.mp3")
monster_sound = pygame.mixer.Sound("audio/monster.mp3")
sword_sound = pygame.mixer.Sound("audio/sword.mp3")
potion_sound = pygame.mixer.Sound("audio/potion.mp3")

# UI and message constants
space = "\n" * 40
line = "=_=_=_=_=_=_=_=_=_=_=_=_=_"
separator = "____________________________"
error_msg = "Error! Invalid Option! >:("
enter_msg = f"Press ENTER to continue...\n" + line * 2 + "\n"
indent = " " * 2

# Suggestions for developer mode
suggestions = [
    "*Improve aesthetics (colors, animations with time.sleep, etc).",
    "*Add background music using playsound.",
    "*Introduce rare enemies, bosses, or ability effects.",
    "*Attack damage multiplied according to selected weapon",
    "*Diversify encounter scenarios"
]

# List of possible enemy entities
small_entities = [
    "Rat", "Dog", "Mosquito", "Gremlin", "Ghoul", "Vampire", "Werewolf", "Mutant",
    "Revenant", "Demon", "Lizardman", "Hyena", "Wolf", "Boar", "Gargoyle", "Minotaur",
    "Basilisk", "Wraith", "Chimera", "Golem", "Harpy", "Sandworm", "Skeleton", "Zombie",
    "Imp", "Goblin", "Orc", "Troll", "Giant Spider", "Mummy", "Scorpion", "Slime"

]

# List of possible enemy emotions/adjectives
emotions = [
    "raging", "mouth gurgling", "rabid", "living dead", "ferocious", "snarling",
    "frenzied", "bloodthirsty", "growling", "savage", "crazed", "howling", "vicious",
    "rotting", "wretched", "ghastly", "twisted", "maddened", "foul", "malevolent",
    "demonic", "sinister", "horrific", "terrifying", "nightmarish", "grotesque"
]

# Enemy levels
levels = [1, 2, 3, 4, 5]

# Art Section
game_art = r""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⡿⢛⠛⣤⣤⠛⣯⠹⣶⣬⣛⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣾⠞⠋⣀⣈⣀⣸⣀⠿⠾⣀⣭⣈⠉⠙⢿⣿⣷⣯⣿⣭⣓⣦⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣦⣴⣿⣿⠷⢉⡩⠥⠤⠬⢴⣾⣿⣿⣿⣿⣿⣿⣛⣻⣿⣿⣿⣶⣶⣄⣀⣈⣉⠙⠛⢛⠻⠾⠿⢿⣿⣿⣯⣽⣶⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡿⠛⣉⣁⣀⣠⣴⣾⣿⣿⣶⡆⣶⣾⣿⣿⣿⣿⣿⣿⣿⣍⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣄⡈⠙⢻⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⢫⣭⡀⣩⣍⢻⣿⣿⣿⣿⣿⣿⣥⣼⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⢀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⢸⣿⣿⣿⣿⣿⠀⣤⡘⢻⡇⣿⠛⣠⡄⢸⡿⠿⠿⠿⠶⠾⠿⠿⠿⢿⣿⡟⠃⠀⠀⠀⠛⠛⠃⠀⠼⢿⣿⣿⣿⡀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠠⣿⣿⣿⣿⣿⠀⠿⠟⣡⡄⣦⡙⠿⠇⢸⣧⣴⣶⣶⠖⢲⣶⣶⣦⣼⠿⠇⠀⣀⡀⠈⠉⠿⢷⣶⣗⣸⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠀⣿⣿⣿⣿⣿⣷⣿⠸⠿⠃⠿⠟⢸⣶⣿⣿⣿⣿⣿⠀⢨⣿⣿⣿⣿⠀⠀⠠⠤⣿⣿⣿⣤⣄⣠⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠆⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⡿⠏⠀⠀⣉⣉⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢘⡿⠋⠀⠀⠀⠀⢸⣁⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣿⣿⣿⣿⡟⠛⢿⠀⢘⡿⠀⠀⢠⠀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠃⠀⠀⠀⠀⢸⠀⢸⣏⣀⡰⢚⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠉⠀⠀⠀⠀⠀⠀⢀⣼⠀⠸⣿⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡇⡀⢹⣿⣿⣿⣿⣿⡟⠋⠀⠀⠀⠀⠀⠀⡆⢀⣀⣤⣿⠀⢸⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣸⡇⠀⣾⣿⣿⣿⣿⣿⠃⠀⠀⢀⣀⠄⣘⣠⣶⣾⣿⣿⣿⠀⢰⡿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⠀⢰⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⠻⣿⣿⣿⣿⠛⠀⠀⠀⢸⠉⣴⣿⣿⣿⣿⣿⣿⣿⠀⢘⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⡟⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣅⠀⣿⣿⣿⣿⠀⠀⠀⠀⢸⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⢘⣟⠀⠀⢀⠀⠀⢰⣶⠄⡇⠀⠀⠀⠀⣿⣿⣿⣿⡇⢀⣿⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠯⣿⡄⢻⣿⣿⣿⢀⠀⠀⠀⠘⠀⠛⣿⣿⣿⣿⡿⠟⢻⠀⢸⣯⡀⠐⢨⣤⣿⣿⣿⠂⡅⠀⠀⠀⠀⣿⣿⣿⡟⢠⣿⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣇⡘⣿⣿⣿⣾⢆⣀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⢺⠀⢰⣿⣧⣿⣿⣿⣿⣿⠿⠉⠁⠀⢀⡠⣦⣿⣿⣿⠃⣸⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠩⣿⣿⣿⣧⣄⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⣹⠀⢨⣿⣿⣿⣿⣿⡟⠋⠀⠀⠀⠀⣏⣸⣿⣿⣿⠍⠀⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠸⢿⣿⣿⣿⣷⣶⣠⣤⣀⣀⣀⣀⣀⣤⣾⠀⢘⣿⣿⡿⠟⠁⠀⠀⠀⢤⢠⣰⣾⣿⣿⣿⠇⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣽⡆⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠸⣟⠛⠁⠀⠀⠀⠀⢆⣷⣾⣿⣿⣿⣿⠋⢰⣯⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣦⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢘⣯⠀⠀⢰⣤⣴⣼⣿⣿⣿⣿⣿⡿⠏⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣄⠈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠏⢹⠀⠸⣷⣶⣾⣾⣿⣿⣿⣿⣿⣿⣿⡿⠁⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⣷⣄⠙⢿⣿⣿⣿⣿⣿⡟⠃⠀⣸⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡏⢡⣲⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⢧⡈⠿⣿⣿⣿⣿⡇⢰⢸⣿⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⡠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣟⣦⠈⠿⣿⣿⣇⣸⣸⣿⠀⢰⣿⣿⣿⣿⣿⣿⠿⢃⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶⣄⠈⠻⢿⣿⣿⣿⠀⠰⣿⣿⣿⡿⠟⠁⣠⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣄⡈⠛⢿⣿⣤⣼⣿⡿⠟⠁⣀⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣦⣄⠛⢿⡿⠛⣀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⢠⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
potion_art = r"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣦⡈⠙⢿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢿⡈⢿⣄⠉⠛⢷⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢩⣿⠛⠛⠛⠿⣦⠈⢿⣤⣙⠻⠿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣿⠀⠀⢸⡇⠀⠀⠀⠀⠙⠷⣦⣈⠙⠛⢛⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠀⠀⣸⡇⠀⠀⣿⠁⠀⠀⢀⣀⣀⡀⣿⡟⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠏⠀⠀⠀⠀⣿⢁⣀⣤⡿⠶⠟⠛⠛⠛⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡏⠀⠀⢀⣠⣴⠿⠛⠉⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣹⣿⣿⣿⣿⣿
⣿⣿⣿⢀⣤⡶⠟⠉⠀⠀⠀⣀⣤⣴⠶⠾⠛⠛⠛⠛⠋⣿⠛⢻⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠛⠁⠀⠀⣀⣴⣶⠛⠉⢹⡇⠀⠀⠀⠀⠀⠰⣾⣿⠄⢸⣿⣿⣿⣿⣿⣿
⣿⣿⠁⠀⢀⣴⠾⠋⠀⣿⠀⠀⢸⣇⠀⠀⠀⠀⠀⣠⡟⠀⢀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣆⣴⡟⠁⠀⠀⠀⢹⡇⠀⠀⣿⠀⠀⣠⣀⣴⠟⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⠀⢀⣸⣷⠀⠀⢹⣧⣤⠾⢿⢅⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣬⣍⣹⡇⠀⠀⢿⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

def gender_selection():
    # Ask the player to select their gender and return pronouns
    while True:
        gender = input(f"{space}{line}\nAre you She or He?\n{separator}\n1-She\n{separator}\n2-He\n")
        input_sound.play()
        print(line * 2)
        time.sleep(0.4)

        if gender == "1":
            return "she", "her"
        elif gender == "2":
            return "he", "his"
        else:
            print(error_msg)
            input(enter_msg)
            input_sound.play()
def potion_system(player):
   # Random chance to find a potion after player's turn
        if random.randint(1, 36) in [1,12]:  # 5% chance
            print("You found a potion!")
            print(potion_art)
            potion_sound.play()
            time.sleep(2)
            player['potions'] += 1
            print(f"\nTotal potions: {player['potions']}.")

def weapon_selection():
   # Ask the player to select their weapon
    while True:
        weapon = input(
            f"{space}\n{line * 2}\nChoose your weapon:\n{separator * 2}\n1-Iron Sword\n{separator * 2}\n2-Silver Dagger\n")
        input_sound.play()
        print(line)
        if weapon == "1":
            weapon_choice = "Iron Sword"
            print(f"\nYou chose the {weapon_choice}.\n")
            return weapon_choice

        elif weapon == "2":
            weapon_choice = "Silver Dagger"
            print(f"\nYou chose the {weapon_choice}.\n")
            return weapon_choice
        else:
            print(error_msg)
            input(enter_msg)
            input_sound.play()
def run_away_scene(entity, emotion, player_name, player_pos, player_gender, player):
    # Print a random scenario for running away from an enemy    
    run_scenarios = [
        f"{player_name} turns and runs as fast as {player_pos} legs can carry {player_gender}, escaping the {emotion} {entity}.",
        f"{player_name} barely dodges the {emotion} {entity}'s claws and sprints away.",
        f"{player_name} throws dirt in the {entity}'s face to escape.",
        f"As the {entity} lunges, {player_name} leaps aside and escapes.",
        f"{player_name} vanishes into ruins before the {emotion} {entity} can react.",
        f"{player_name} narrowly escapes after stumbling.",
        f"A roar erupts, but {player_name} is already gone.",
        f"{player_name} dashes through underbrush, the {entity} just behind.",
        f"{player_name} leaps over logs, escaping through fog.",
        f"{player_name} dives into a river and floats away.",
        f"A crate blocks the {emotion} {entity} just long enough.",
        f"With a burst of energy, {player_name} climbs a ledge.",
        f"{player_name} hides in a cave and the {entity} moves on.",
        f"The {emotion} {entity} howls, but {player_name} is already gone."
    ]
    print(space + line * 2 + "\n" + random.choice(run_scenarios))
    print(f"You fled safely. HP remain unchanged.")
    print(line * 2)
    potion_system(player)  # Chance to find a potion after running away
    input(enter_msg)
    input_sound.play()

def combat(player, entity, emotion, player_name, player_pos, player_gender, enemy, level, name, weapon_choice):
    # Main combat loop between player and enemy
    print(f"\nYou encountered a {enemy['name'].upper()}!")
    pygame.mixer.music.load("audio/battle.mp3")
    pygame.mixer.music.play(-1)
    if 'defense_cooldown' not in player:
        player['defense_cooldown'] = 0

    while player['hp'] > 0 and enemy['hp'] > 0:
        # Show potion count if available
        if player['potions'] > 0:
            print(f"\n{line}YOUR TURN_{line}\n\n {indent*5}| Potions: {player['potions']} | HP: {player['hp']} | Foe's HP: {enemy['hp']} |\n\n")
        else:
            print(f"\n{line}YOUR TURN_{line}\n\n {indent*6}| HP: {player['hp']} | Foe's HP: {enemy['hp']} |\n\n")

        while True:
            # Player chooses action
            action = input("What do you do? \n1-Attack\n2-Defend\n3-Drink Potion:\n")
            input_sound.play()
            time.sleep(1)
            if player['defending']:
                player['defending'] = False
                print("Your defense has ended.")

            if action == '1':
                # Attack action
                print(space)
                if name in ["Raphael", "Dev"]:
                    dmg = 100  # Special case for developer mode
                elif level <= 2:
                    dmg = random.randint(10, 40)
                elif level == 3:
                    dmg = random.randint(10, 35)
                elif level >= 4:
                    dmg = random.randint(5, 30)
                else:
                    dmg = 0

                if dmg > 30:
                    print("Critical hit!")
                print(f"\n{separator}\nYou strike and deal {dmg} damage.\n{separator}\n")
                enemy['hp'] -= dmg
                print(f"{enemy['name'].upper()} now has {enemy['hp']} HP.\n\n")
                potion_system(player)  # Chance to find a potion after attacking
                input(enter_msg)
                input_sound.play()
                break

            elif action == '2':
                # Defend action
                if player['defense_cooldown'] == 0:
                    player['defending'] = True
                    player['defense_cooldown'] = 2  # 2-turn cooldown for defense
                    print("You brace for the next attack.")
                    potion_system(player)  # Chance to find a potion after defending
                else:
                    print("You're still recovering and can't defend this turn.\nYou lose your turn.")
                break

            elif action == '3' and player['potions'] == 0:
                # Try to drink potion but none available
                print("You try to drink a potion but you don't have one.\nYou lose your turn.\n")
                break

            elif action == '3' and player['potions'] > 0:
                # Drink potion and restore HP
                print("You drank a potion and you're HP has been restored.")
                player['hp'] = 100
                player['potions'] -= 1
                break
            elif action not in ["1", "2", "3"]:
                print(error_msg)

        

        # Enemy's turn if still alive
        if enemy['hp'] > 0:
            print(f"\n{line}\n{enemy['name'].upper()}'s turn:\n{line}\n\n")
            time.sleep(1)
            if random.random() < 0.9:
                # Enemy attacks
                if name == "Loser":
                    dmg = random.randint(100, 110)
                elif level == 2:
                    dmg = random.randint(5, 20)
                elif level == 3:
                    dmg = random.randint(5, 25)
                elif level >= 4:
                    dmg = random.randint(10, 35)
                else:
                    dmg = random.randint(1, 15)

                if player['defending']:
                    dmg = max(0, dmg - 10)
                    print(f"You defend against the {enemy['name'].upper()} attack and take only {dmg} damage.\n\n")
                    input(enter_msg)
                    input_sound.play()
                else:
                    if dmg > 30:
                        print("Critical hit!")
                    print(f"{enemy['name'].upper()} attacks and you take {dmg} damage.\n\n")
                    time.sleep(1)
                player['hp'] -= dmg
                print(f"\n{separator}\nYou now have {player['hp']} HP.\n\n\n")
                time.sleep(1)
            else:
                # Enemy hesitates and does not attack
                print(f"{enemy['name']} hesitates.")
                time.sleep(2.5)
        # Decrease defense cooldown if active
        if player['defense_cooldown'] > 0:
            player['defense_cooldown'] -= 1

    pygame.mixer.music.stop()
    # Victory and defeat scenarios
    win_scenarios = [
        f"{player_name} frowns and swings {player_pos} {weapon_choice} towards the {emotion} {entity}, striking it down.",
        f"{player_name} overpowers the {entity} with a clean hit, making it flee.",
        f"{player_name} swiftly dodges and counters, taking down the {emotion} {entity}.",
        f"{player_name} glares at the {emotion} {entity}, gripping {player_pos} {weapon_choice} tightly.\n"
        f"With a swift and powerful swing, {player_gender} slashes through the air, the sheer force of the attack sending dust flying."
        f"\nThe {entity} hesitates, sensing that it is no match for {player_name}.\n"
        f"With one last defiant snarl, the creature scampers away, choosing to live another day. {player_name} watches it go, victorious but ever cautious.",
        f"The {emotion} {entity} growls and prepares to attack, but {player_name} wastes no time.\n"
        f"{player_name} grips {player_pos} {weapon_choice} tightly, eyes locked on the {emotion} {entity}.\n"
        f"With a burst of speed, {player_name} swings {player_pos} {weapon_choice} with full force, striking the creature square in the chest.\n"
        f"The impact sends the {entity} rolling back, stunned and whimpering.\n"
        f"It scrambles to its feet and flees into the darkness, defeated. {player_name} wipes {player_pos} weapon clean and continues the journey, unshaken.",
        f"{player_name} faces the {emotion} {entity}, adrenaline's pumping.\n"
        f"With a fierce battle cry, {player_name} charges at the {emotion} {entity}, ready to strike."
        f"\nThe {entity} snarls and lunges, but {player_name} is faster.\n"
        f"{player_name} swings {player_pos} {weapon_choice} with all {player_pos} might, landing a decisive blow.\n"
        f"The {emotion} {entity} staggers back, defeated, and with a final growl, it turns and flees into the shadows.\n"   
    ]
    lose_scenarios = [
        f"{player_name} swings but the {emotion} {entity} dodges and bites back, forcing a retreat.",
        f"{player_name} miscalculates an attack and the {entity} retaliates viciously, making escape the only option.",
        f"{player_name} is overwhelmed and knocked down, barely managing to flee.",
        f"{player_name} grips {player_pos} {weapon_choice} tightly and strikes at the {emotion} {entity}." 
        f"But the creature is relentless, dodging every attack with ease.\nAfter a fierce struggle, {player_name} is exhausted.\n"
        f"{player_pos.capitalize()} legs feel weak, and {player_pos} vision blurs. The only choice left is to flee before it's too late.",
        f"{player_name} slashes at the {emotion} {entity}, but the blow barely grazes it." 
        f"The creature retaliates with a vicious swipe, knocking {player_name} to the ground."
        f"\nAs {player_pos} weapon slips from {player_pos} grasp, panic sets in.\n"
        f"There's no choice but to scramble to {player_pos} feet and escape before it's too late.",
        f"\nThe {emotion} {entity} growls, sensing victory, and {player_name} knows that running is the only option left."
        f"\nWith a final glance back, {player_name} sprints away, heart pounding, leaving the defeated {entity} behind."
        f"\nThe {emotion} {entity} watches as {player_name} disappears into the distance, scared and breathless."
    ]
    if player['hp'] <= 0:
        # Player defeated
        print("\nYou have been defeated!\n\n")
        monster_sound.play()
        print(line * 2 + "\n" + (random.choice(lose_scenarios)))
        input(enter_msg)
        input_sound.play()
        time.sleep(1.5)
        wasted_sound.play()
        return False
    else:
        # Player wins
        print(f"\nYou defeated the {enemy['name']}!\n\n")
        print(line * 2 + "\n" + (random.choice(win_scenarios)))
        sword_sound.play()
        win_sound.play()
        input(enter_msg)
        input_sound.play()
        time.sleep(1.5)
        pygame.mixer.music.load("audio/adventure.mp3")
        pygame.mixer.music.play(-1)
        return True

def game():
    # Main game loop and flow
    print(space)
    print(game_art)
    name = input(
        f"{indent*9}======= Hello Adventurer! =======\n{indent*9}===={indent*2}What is your name? {indent}====\n{indent*9}=================================\n").capitalize()
    input_sound.play()

    # Developer mode for special names
    if name in ["Dev", "DEV", "dev", "Raphael"]:
        print(line + "\n-=-DEVELOPER MODE-=-\n-GODMODE ENABLED-\nSuggestions:\n" + "\n".join(suggestions))
        input(enter_msg)
        input_sound.play()
    player_gender, player_pos = gender_selection()

    weapon_choice = weapon_selection()

    # Initialize player stats
    player = {"name": name, "hp": 100, "potions": 1, "defending": False, 'lives': 0, "fled": 0}
    round_counter = 0

    # Main adventure loop
    while player['hp'] > 0:
        round_counter += 1
        entity = random.choice(small_entities)
        emotion = random.choice(emotions).capitalize()
        level = random.choice(levels)
        enemy_name = f"lvl.{level} {emotion} {entity}"
        enemy = {"name": enemy_name, "hp": 80}
        if player['hp'] <= 0:
            break

        print(f"{space}Round Nº {round_counter}\n")
        print(f"{name} is walking down the road when suddenly a {enemy_name} appears!\n" + line * 3)
        time.sleep(2.5)
        print(f"HP: {player['hp']}")

        while True:
            # Player chooses to fight or run
            action = input("\nWhat will you do?\n1 - Fight\n2 - Run\n")
            input_sound.play()
            print(line * 2)

            if action == "1":
                # Fight the enemy
                if combat(player, entity, emotion, name, player_pos, player_gender, enemy, level, name, weapon_choice):
                    player['lives'] += 1
                else:
                    player['lives'] -= 1
                    # Reset HP after defeat
                break

            elif action == "2":
                # Attempt to run away
                player['fled'] += 1
                if player['fled'] >= 4:
                    print("You can't run anymore, your feet are injured.")
                    input(enter_msg)
                    input_sound.play()
                else:
                    run_away_scene(entity, emotion, name, player_pos, player_gender, player)
                    round_counter -= 1  # Do not count the round if player runs away
                    break
            else:
                print(error_msg)

        # Game over if player HP is 0 or less
        if player['hp'] <= 0:
            print(
                f"{space}{line * 2}\nYOU LOSE.\n{line}\nYou ran out of HP and died!\n{line}\n{player['name']} was defeated in round {round_counter} by {enemy_name}...")
            pygame.mixer.music.load("audio/game_over_music.mp3")
            pygame.mixer.music.play(-1)
            time.sleep(2)
            print("\nThanks for playing!")
            input(enter_msg)
            input_sound.play()
            break

        # Win condition after 10 rounds
        if round_counter == 10:
            print(f"CONGRATULATIONS!!! YOU WON!!!\n{line}\n HP: {player['hp']}\n{line}\nTHANKS FOR PLAYING!")
            pygame.mixer.music.load("audio/victory.mp3")
            pygame.mixer.music.play(-1)
            input(enter_msg)
            input_sound.play()
            break

if __name__ == '__main__':
    # Main entry point: loop to allow replaying the game
    while True:
        pygame.mixer.music.load("audio/adventure.mp3")
        pygame.mixer.music.play(-1)
        game()
        choice = input("Play again?\n1 - Yes\n2 - No\n")
        if choice != "1":
            break

