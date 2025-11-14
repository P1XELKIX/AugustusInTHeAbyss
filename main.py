"""
ignore this just makes sure it runs on school computers (you can also run 
these on school computers; if you double click the python file they open in 
terminal and will run properly with full colour and stuff idrk why
import subprocess
subprocess.run(["pip", "install", "pygame", "rich", "progress", "playsound3"])

Imports :)
Random - to make random number / Time - to bake delays
Pygame - to load and play music
Rich - loading screens and colouring text
Playsound3 - load and play sound effects 
Progress - used for completion bars 
Threading - run seperate code in the backround while smething else is happening
"""


import random, time, pygame, progress, threading, playsound3
from rich.console import Console
from progress.spinner import Spinner
from rich import print
console = Console()


# stray variable cos needed in cool words
skip = False

# Cool Text - prints text letter by letter with different colours and speeds
def normalPrint(words): # define function as normal print
    letters = list(words) # seperates word into list of letters
    for letter in letters: # for each letter print then delay repeat
        print (letter, end="", flush=True) # prints without moving to new line
        if not skip: # if skip active skips delay and prints imediately
            time.sleep(0.04) # how long the delay is per letter


# printed when an item is displayed
def itemPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[yellow3]{letter}[/yellow3]", end="")
        if not skip:
            time.sleep(0.04)


# printed when displaying money
def moneyPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[orange3]{letter}[/orange3]", end="")
        if not skip:
            time.sleep(0.04)


#
def shopPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[slate_blue1]{letter}[/slate_blue1]", end="")
        if not skip:
            time.sleep(0.06)


#
def fastPrint(words):
    letters = list(words)
    for letter in letters:
        print (letter, end="", flush=True)
        if not skip:
            time.sleep(0.015)


#
def questionOptionPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[green4]{letter}[/green4]", end="")
        if not skip:
            time.sleep(0.04)


#
def questionPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[spring_green3]{letter}[/spring_green3]", end="")
        if not skip:
            time.sleep(0.06)


#
def titlePrint(title):
    letters = list(title)
    for letter in letters:
        console.print (
            f"[underline bold purple]{letter}[/underline bold purple]", end=""
            )
        if not skip:
            time.sleep(0.08)


#
def subTitlePrint(title):
    letters = list(title)
    for letter in letters:
        console.print (f"[deep_sky_blue1]{letter}[/deep_sky_blue1]", end="")
        if not skip:
            time.sleep(0.07)


#
def errorPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[red3]{letter}[/red3]", end="")
        if not skip:
            time.sleep(0.1)


#
def damagePrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[bright_red]{letter}[/bright_red]", end="")
        if not skip:
            time.sleep(0.1)


#
def spamtonPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[sky_blue2]{letter}[/sky_blue2]", end="")
        if not skip:
            rand = random.randint(1,30)
            if rand > 29:
                time.sleep(0.4)
            else:
                time.sleep(0.02)


#
def alucardPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[orange_red1]{letter}[/orange_red1]", end="")
        if not skip:
            time.sleep(0.05)


#
def playerPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[yellow2]{letter}[/yellow2]", end="")
        if not skip:
            time.sleep(0.05)


#
def gameEndPrint(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[red]{letter}[/red]", end="")
        time.sleep(0.7)
         

# ask user to set volume
volume_set = False
while not volume_set: # while volume isn't set
    questionOptionPrint(
        "How loud do you want the music? *100 is loud recommended %10"
        )

    volume = float(input("\n%")) # input volume as a float

    if 0 <= volume <= 100: # make sure volume is 0 - 100
        questionOptionPrint(f"\nSet volume to {volume}? ")
        questionPrint("[Y/n]")

        answer = input("\n").strip().lower() # input 

        if answer == "y": # set volume
            subTitlePrint("\nVolume Set")
            volume /= 100 # volume / 100 becaues pygame uses 0 to 1 for volume
            volume_set = True # exit while loop

        elif answer == "n": # skip and ask for volume again
            pass
        
        else: # not y/n
            errorPrint("\nhuh?")
    else: # number outside of 0 - 100 inputted
        errorPrint("\nInvalid Volume")


# Music - changes music and shows loading spinner
print("")
with console.status( # show spinner while part below it is running
    "[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner = "line"
    ):
    pygame.init # initialises pygame 
    pygame.mixer.init() # initialises pygame sound mixer
    pygame.mixer.music.set_volume(volume) # set volume to user chosen percentage
    pygame.mixer.music.load("music/rudebuster_boss.mp3") # load song
    # loop indefinetly (loops = -1) fade in for 5 seconds (fade_ms = 5000)
    pygame.mixer.music.play(loops = -1, fade_ms = 5000)
    time.sleep(0.5) # delay end of loading screen for 0.5 second cos cool innit




fastPrint( # ask if user wants to have text print instantly
    "\nDo you want the text to print instantly or do the really epic cool " 
    "printing where it prints it out slowly and is only for cool people? "
)
questionOptionPrint("\nReally cool epic text? ")
questionPrint("[Y/n]")

answer = input("\n").lower().strip()

if answer == "y":
    normalPrint("ty :)")

elif answer == "n":
    errorPrint("aww :(")
    time.sleep(0.5)
    skip = True # removes delay

else: # if they input anything that isnt y/n assume cool text print
    errorPrint("error assuming you want the epic text mwuhahahaha")


# Variable
alive = True # whether alive
character_chosen = False # is character chosen
player_stats = { # define stats
"health": 1, 
"strength": 0, 
"charisma": 0, 
"dexterity": 0, 
"perception": 0
}

player_items = ["stick"] # define items player has
player_weapons = {} # define weapons player has
money = 250 # define money on player
in_shop = False # are they in the shop?

# Do they want to print the adventurers description, stats and weapons?
questionOptionPrint( 
    "\nDo you want to display different character and their"
    " stats/weapons ")
questionPrint("[Y/n]")

answer = input("\n").lower().strip()

if  answer == "y":


# Display characters and their items/stats
    normalPrint("\nChoose one of these four adventurers\n")

# Warrior
    titlePrint("\nWarrior")
    fastPrint( # warrior description
        "\nWarrior have considerable strength and defense making them the "
        "easiest to play while still being powerful with a fairly even stat "
        "distribution"
        )
    subTitlePrint("\n\nStats")
    fastPrint( # warrior stats
        "\nStrength - 16 Charisma - 14 Dexterity - 12 Perception - 14 "
        "Health - 130"
        )
    subTitlePrint("\n\nWeapons")
    fastPrint("\nLongsword\nDagger")

# Rouge
    titlePrint("\n\nRouge")
    fastPrint( # rouge description
        "\nRouge has low strength and health but with high damage making them "
        "a difficult Character to play but powerful"
        )
    subTitlePrint("\n\nStats")
    fastPrint( # rouge stats
        "\nStrength - 16 Charisma - 12 Dexterity - 18 Perception - 16 "
        "Health - 70"
        )
    subTitlePrint("\n\nWeapons")
    fastPrint("\nKatar\nDagger")

# Barbarian
    titlePrint("\n\nBarbarian")
    fastPrint( # barbarian description
        "\nWith their high damage and low health the barbarian is a glass "
        "cannon dealing high damage but with little in ways of defense"
        )
    subTitlePrint("\n\nStats")
    fastPrint( # barbarian stats
        "\nStrength - 20 Charisma - 10 Dexterity - 12 Perception - 12 "
        "Health - 100"
        )
    subTitlePrint("\n\nWeapons")
    fastPrint("\nBattle axe\nHatchet")

# Paladin
    titlePrint("\n\nPaladin")
    fastPrint( # paladin description
        "\nPaladin has high defense and decent offense making it a powerful "
        "combatant matched with good charisma although stealth will be off "
        "the table for the most part"
        )
    subTitlePrint("\n\nStats")
    fastPrint( # paladin stats
        "\nStrength - 14 Charisma - 18 Dexterity - 6 Perception - 14 "
        "Health - 160"
        )
    subTitlePrint("\n\nWeapons")
    fastPrint("\nShort sword\nShield")

elif answer == "n":
    subTitlePrint("\nskipped..")

else:
    errorPrint("error skiping anyway :)")

# Choose character
subTitlePrint("\n\nEnter a number to choose")
questionOptionPrint(
    "\n1) Warrior"
    "\n2) Rouge"
    "\n3) Barbarian"
    "\n4) Paladin\n"
    )


def characterSelect(number, character):
    global character_chosen
    global your_character

    if answer == number: # checks their answer is the one for this character
        questionOptionPrint(f"You Choose {character}? ")
        questionPrint("[Y/n]") # asks if right character

        check = input("\n").strip().lower()

        if check == "y": # if right set character and set character_chosen true
            normalPrint(f"Your class is now {character}\n")
            character_chosen = True
            your_character = character
        elif check == "n": # if wrong character go back and ask again
            pass
        else: # if not y/n just go back and print error
            errorPrint("error :/\n")


# Uses function ^ to confirm whether you chose the right character
while not character_chosen:
    questionPrint("which do you choose")

    answer = int(input("\n"))
    characterSelect(1, "Warrior")
    characterSelect(2, "Rouge")
    characterSelect(3, "Barbarian")
    characterSelect(4, "Paladin")

# Dice - functions for each dice if called return random number 
# between 1 and d_ then add multiplier
def d2(mult): # function using mult
    num = random.randint(1,2) + mult # random number between 1 & 2 + multiplier
    return num # return the random number with multiplier


def d4(mult):
    num = random.randint(1,4) + mult
    return num


def d6(mult):
    num = random.randint(1,6) + mult
    return num


def d8(mult):
    num = random.randint(1,8) + mult
    return num


def d10(mult):
    num = random.randint(1,10) + mult
    return num


def d12(mult):
    num = random.randint(1,12) + mult
    return num


def d20(mult):
    num = random.randint(1,20) + mult
    return num

# Set stats depending on character chosen
if your_character == "Warrior": # check if ____ is the name of your class
   player_stats.update({ # set stats and health as dictionary (stat:value)
    "health": 130,
    "strength": 16,
    "charisma": 14,
    "dexterity": 12,
    "perception": 14
    })
   player_weapons.update({ # set weapons as tuples in dictionary (tuple:values)
       "main": ("longsword", d8),
       "secondary": ("dagger", d4)
   })

elif your_character == "Rouge":
    player_stats.update({
    "health": 70,
    "strength": 16,
    "charisma": 12,
    "dexterity": 18,
    "perception": 16
    })
    player_weapons.update({
       "main": ("katar", d10),
       "main": ("dagger", d6)
   })
    
elif your_character == "Barbarian":
    player_stats.update({
    "health": 100,
    "strength": 20,
    "charisma": 10,
    "dexterity": 12,
    "perception": 12
    })
    player_weapons.update({
       "main": ("battle axe", d10),
       "secondary": ("hatchet", d4)
   })
    
elif your_character == "Paladin":
    player_stats.update({
    "health": 160,
    "strength": 14,
    "charisma": 18,
    "dexterity": 6,
    "perception": 14
    })
    player_weapons.update({
       "main": ("short sword", d6),
       "secondary": ("shield", d4)
   })
    
else: # if character isnt one of the 4 here somehow just exit program
      # cos it went wrong somewhere probably wont happen hopefully
    errorPrint("huh? you shouldn't be here :/")
    exit()
# how to call from dictionary print(player_weapons["main"] [1] (0) )

# loading just cos 
with console.status(
    "[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"
    ):
   time.sleep(1)

# Title - just words innit
titlePrint("\nwelcome to BOBLIN\n\n")

# Opening - Prints into
fastPrint(
    "You approach  the town you'd been looking for the past 3 years it is an "
    "adventuring town built around the main landmark the great orouborus "
    "dungeon a seemingly endless maze with one grand door large enough to "
    "allow thousands of adventurers to enter and exit at the same time. "
    "Although being called a dungeon it spans into the sky as far as the eye "
    "can see and is said to house the gods at the top although no ones ever "
    "made it that far you look around and also see a tavern named grillby's "
    "for meals and resting and a run down shop with a sign that says Pluey? "
    "You have no idea what that means and decide to ignore it for now and "
    "continue to the town square"
    )


# Variables - change stats to multipliers so i an just ad or take away them 
# mult stat - 10 / 2 e.g strength = 14 | 14 - 10 / 2 | mult = 2 
strength_mult = int((player_stats["strength"] - 10) / 2)
charisma_mult = int((player_stats["charisma"] - 10) / 2)
dexterity_mult = int((player_stats["dexterity"] - 10) / 2)
perception_mult = int((player_stats["perception"] - 10) / 2)
# variables - keep track of where you've been and how many times
dungeon_visits = 0 # how many times been to dungeon
tavern_visits = 0 # how many times been to tavern
pluey_visits = 0 # how many times been to shop
runs = 0 # how many times completed dungeon
number_per_shop_item = {}
shop_options = ({
        "broken sword": "Buy THE BIG ONE",
        "frayed bowtie": "Buy BSHOT BOWTIE",
        "health pot": "Buy H.POISON",
        "silver key": "Buy SuperKEY (ExTrEmE)",
        "leave": "Leave plueys"
})


# Spamtons Shop Function 
def openShop(): # define entering the shop use to open spamtons deals shop
    global money # global money so you can charge prices
    global approach # global approach so you can return to town after

    in_shop = True # set in shop true so while in shop loop repeats while there
    spamtonPrint( # spamton talking
        "AND I HAVE JUST. "
        "\nTHE THING. "
        "\nYOU NEED. "
        "\nTHAT'S [[BARGAIN$]]."
        )
    titlePrint("\n\nS͠P̷A͜M̴T̛O͞N͢'͠S͡ ̵$$D͜E͜A̷L̡Z̸$$ ͝S͠H͘O̢}") # title spamton shop

    while in_shop: # shop loop
        for item in player_items: # for every item in players items
            try: # dont crash if dont work
                # delete shop option named item if its their
                del shop_options [item]
            except: # if not just pass
                pass
        print("")        

        if "broken sword" not in player_items: # if player doesnt have it
            shopPrint("\nTHE BIG ONE  [D£ 100]") # print item option

        if "frayed bowtie" not in player_items:
            shopPrint("\nBSHOT BOWTIE  [D£ 60]")

        shopPrint("\nH.POISON  [D£ 30]")

        if "silver key" not in player_items:
            shopPrint("\nSUPER KEY (ExTrEmE) [D£ 100]")

        # print how much money u got
        moneyPrint(f"\n\nYou Have D£ {money} Kromer") 

        subTitlePrint("\n\nwould you like to buy anything?")
        
        """
This part prints out each option step by step of the for loop below ☟
'num (key, option)' - set num for each key and value in shop options
'enumerate(shop_options.items())' - number each item in dictionary shop options
'start = 1' - starting at 1
'print(f"{num}{option}")' - print number of option and option
'number_per_shop_item[num] = key' - set dictionary num_per_shop_item number of 
item and assign it value key (string name)
'print("[1 -> max]")' - prints the available input options as between 1 and max
"""
        for num, (key, option) in enumerate(shop_options.items(), start = 1):
            questionOptionPrint(f"\n{num}) {option}")
            number_per_shop_item[num] = key
        questionPrint(f" [1 -> {len(shop_options)}]")


        answer = int(input("\n")) # input answer
        if 1 <= answer <= len(shop_options): # make sure input is valid
            # answer is turned into string attributed to number
            answer = number_per_shop_item.get(answer) 

            if answer == "broken sword": # answer is compared to each string
                # if player has enough money and doesnt already have item
                if (money >= 100 and "broken sword" not in player_items):
                    subTitlePrint("\nYou bought THE BIG ONE")
                    moneyPrint("\n- D£ 100")
                    itemPrint("\n+ 1 broken sword")
                    player_items.append("broken sword") # add to player_items
                    money -= 100 # take 100 money as per price
                else: # if player doesnt have enough money
                    errorPrint("not enough money")

            elif answer == "frayed bowtie":
                if (money >= 60 and "frayed bowtie" not in player_items):
                    subTitlePrint("\nYou bought BSHOT BOWTIE")
                    moneyPrint("\n- D£ 60")
                    itemPrint("\n+ 1 frayed bowtie")
                    player_items.append("frayed bowtie")
                    money -= 60
                else:
                    ErrorPrint("not enough money")

            elif answer == "health pot":
                if money >= 30:
                    subTitlePrint("\nYou bought H.POSION")
                    moneyPrint("\n- D£ 30")
                    itemPrint("\n+ 1 health potion")
                    player_items.append("health potion")
                    money -= 30
                else:
                    errorPrint("not enough money")

            elif answer == "silver key":
                if (money >= 100 and "silver key" not in player_items):
                    subTitlePrint("\nYou bought SUPER KEY (ExTrEmE")
                    moneyPrint("\n- D£ 100")
                    itemPrint("\n+ 1 silver key")
                    player_items.append("silver key")
                    money -= 100
                else:
                    errorPrint("not enough money")

            elif answer == "leave":
                normalPrint(
                    "you wander back wondering what those weird items did"
                    )
                approach = 0 # return to town center
                in_shop = False # exit while in_shop loop
        else:
            errorPrint("invalid number")


def openTavern():
    pass



# MAIN GAME LOOP - keeps the game in a big loop so it doesnt end until u die
while alive:
   print("") # <-- console below removes this instead of important text
   # Change music - changes music and shows loading spinner
   with console.status( # show spinner while part below it is running
        "[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"
        ):
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load("music/field_of_hopes.mp3")
        pygame.mixer.music.play(loops = -1, fade_ms = 2000)
        time.sleep(0.5)
    # select where to go
   subTitlePrint("\n\nChoose a number to travel : ")
   questionOptionPrint(
        "\n1) Approach ouroboros dungeon "
        "\n2) Look in Grillbys "
        "\n3) Pluey? "
        )
   questionPrint("\nWhere do you want to go?")

   approach = int(input("\n"))


# ---- DUNGEON ----
   while approach == 1: # dungeon dunne work yet
        print("") # <-- console below removes this instead of important text
        # Music Change
        with console.status(
            "[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"
            ):
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("music/vs_susie.mp3")
            pygame.mixer.music.play(loops = -1, fade_ms = 1000)
            time.sleep(0.5)

        subTitlePrint(
            "\nas you approach the dungeon you decide it isn't finished yet "
            "and pluey might have some [$DEAL$!] maybe"
            )
        questionOptionPrint("\nReturn to city center?")
        questionPrint("[Y/n]")

        answer = input("\n").strip().lower()

        if answer == "y":
            fastPrint(
                "As you walk back you think it might be for the best but "
                "maybe at a later time *cough cough nudge nudge wink wink"
                )
            approach = 0

        elif answer == "n":
            fastPrint(
                "you decide to sit here and wait till the end of time maybe "
                "your enjoying the music, maybe you are convinced theres more "
                "but sadly i didnt have enough time but plueys definitely "
                "really cool so maybe go there after re-loading this ??"
                )
            while alive == True:
                pass
                time.sleep(1)

        else:
            errorPrint(
                "oh no an error thats so sad well too bad you missed out on "
                "all the dungeon content better luck next time"
                )
            
            exit()


# ---- GRILLBY'S ----
   while approach == 2: # this dont work neither
        print("") # <-- console below removes this instead of important text
        # Music Change
        with console.status(
            "[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"
            ):
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("music/sans_shop.mp3")
            pygame.mixer.music.play(loops = -1, fade_ms = 1000)
            time.sleep(0.5)


        if tavern_visits == 0:
            fastPrint(
                "You enter the tavern for the first time and are suddenly "
                "blinded by a warm light. coming from the center of the bar."
                "\nTables are scattered around the room as groups of "
                "adventurers huddle round them playing various card games "
                "and laughing over meals"
                "\nA balcony spans the upper layer of the room looming over "
                "parts of the tavern, carrying many shady looking people "
                "along with body guards and a weird purple glow "
                )
            subTitlePrint("\nwhere would you like to go?")
            questionOptionPrint(
                "\n1) head towards bar"
                "\n2) head upstairs"
                "\n3) return to town square"
                )
            questionPrint("\n[1 -> 3]")
            answer = int(input("\n"))
            
            if answer == 1:
                fastPrint(
                "\nYou walk towards the bar where a large flaming bear shakes "
                "what seems to be a very medieval cocktail shaker while "
                "smoking an absurdly long churchwarden and donning a mighty "
                "fedora with ear holes"
                )

                alucardPrint	(
                    "\nWell Well Well haven't seen you round these parts "
                    "before what could I do for you"
                    )
                fastPrint("\nThey say in a gruff new york accent")
                playerPrint(
                    '\n1) "I heard you sell meals and rooms"'
                    '\n2) "The people upstairs?"'
                    '\n3) "not included yet"'
                    '\n4) "not included yet"'
                    )
                if pluey_visits >= 1:
                    playerPrint('\n5) "Whats with plueys?"')
                answer = int(input("\n"))
                if answer == 1:
                    pass
                if answer == 2:
                    pass
                if answer == 3:
                    pass
                if answer == 4:
                    pass
                if answer == 5:
                    pass
                  

            elif answer == 2:
                pass
            elif answer == 3:
                normalPrint("you head back to town")
                approach = 0
            




# ---- PLUEY ----
   while approach == 3:
        print("") # <-- console below removes this instead of important text
        # Music Change 
        with console.status(
            "[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"
            ):
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("music/spamton_meeting.mp3")
            pygame.mixer.music.play(loops = -1, fade_ms = 1000)
            time.sleep(0.5)

        # If its their first time in pluey
        if pluey_visits == 0:
            fastPrint(
                "You stumble into pluey not sure what to expect. Its cold and "
                "baren, the room is empty barring the rows of book shelves "
                "lining the outer walls and single old oak desk centred at "
                "the then end of the room. It faces you but you can barely "
                "make out its shape as all that illuminates is the faint "
                "glow from the open door behind you."
                )
            subTitlePrint("\n\nDo you want to leave or look closer?")
            questionOptionPrint( # where go in Pluey?
                "\n1) leave and come back later "
                "\n2) inspect table "
                "\n3) items"
                )
            questionPrint("\nWhat do you do?")
            
            answer = int(input("\n"))

            if  answer == 1: # try to leave pluey
                damagePrint("you attempt to leave ")
                fastPrint(
                    "and remember you left the door wide open allowing you "
                    "to leave with ease you decide to head back to the town "
                    "square "
                    )
                # set location to town square
                approach = 0

            elif answer == 2: # try inspect table
                print("you roll a die to see if you notice anything\n")
                with console.status( # rolling dice spinner
                    "[violet]rolling...[/violet]", spinner="dots"
                    ):
                    time.sleep(1)
                # rolls die and returns num (number rolled + mult)
                num = d20(perception_mult)
                subTitlePrint( # display dice rolled and what mult added
                    f"you rolled: {num - perception_mult} "
                    f"+ your perception multiplier = {num} \n"
                    )

                if num >= 10: # if rolled higher than 10 meet spamton
                    fastPrint(
                        "You notice looking at the table theirs a small "
                        "white spike protruding from behind the table and "
                        "decide to approach"
                        )
                    fastPrint(
                        "\nYou make out the shape of what looks to be an odd "
                        "looking man with a protruding nose "
                        "\nHe sits there for a second before blurting out in "
                        "a robotic voice"
                        )
                    spamtonPrint(
                        "\nAHHHH A NEW [slime] WHY BE THE [Little Sponge] WHO "
                        "HATES ITS [$4.99] LIFE WHEN YOU CAN BE A [BIG "
                        "SHOT!!!]. "
                        "\nWANNA BE A [[BIG SHOT?!?!]]"
                        )
                    questionPrint(" [Y/n]") # want to be a big shot

                    answer = input("\n").strip().lower()

                   # get to see his silly strings regardless of what you choose
                    if answer == "y" or answer == "n": 
                        spamtonPrint(
                            "I KNEW YOU DIDN'T WANT TO BE [the little slime] "
                            "YOU ARE NOW GRAB THIS BY THE [silly strings]"
                            )
                        questionOptionPrint(
                            "\nWanna grab it by the silly strings?"
                            )
                        questionPrint(" [Y/n]")

                        answer = input("\n").strip().lower() 
                        # grab by silly stings?

                        if answer == "y": # give item suspicious lever
                            fastPrint(
                                "you pull the silly string he's laid out on "
                                "the table and notice a lever attached to the "
                                "end of it. You take the lever and thank him "
                                "uncertainly"
                                )
                            itemPrint("\n+ 1 Suspicious Lever")
                            # add to inventory
                            player_items.append ("suspicious lever") 
                            spamtonPrint(
                                "\nNO PROBLEM COME BACK FOR MORE [[Hyperlink "
                                "Blocked]]"
                                )
                            approach = 0 # return to town
                            pluey_visits = 1 # increase pluey visits by one 

                        # return to town without increasing visits
                        if answer == "n": 
                            spamtonPrint(
                                "YOU WANT IT. YOU WANT [[Hyperlink Blocked]], "
                                "DON'T YOU."
                                )
                            fastPrint(
                                "\nYour not sure and decide to leg it back to "
                                "town hoping it isnt chasing you"
                                )
                            approach = 0

                    else: # return to town
                        fastPrint(
                            "Your not sure and decide to leg it back to town "
                            "hoping it isn't chasing you"
                            )
                        approach = 0

                else: # return to town
                    fastPrint(
                        "You don't notice anything and decide to head back to "
                        "the town square "
                        )
                    approach = 0

            elif answer == 3: # try to use items in inventory
                approach = 0

                for item in player_items: # print item list
                    print("-", item)

                # input item
                answer = input("Which do you choose? ").strip().lower()

                if answer in player_items: # if item valid print cant use it
                    normalPrint("You can't use that here")

                else: # if item not valid print error
                    errorPrint(f"you don't have {answer}")

            else: # if input not one of three 
                errorPrint("err: invalid input")

        # If its their 2nd time in pluey
        elif pluey_visits == 1:
            fastPrint(
                "Your in pluey still confused from the last time you "
                "were here"
                )
            questionPrint( # action options
                "\n1) leave and come back later"
                "\n2) inspect gap "
                "\n3) items"
                )
            
            answer = int(input("\n")) # what do you do

            if  answer == 1: # return to town square
                fastPrint(
                    "you leave and decide to head back to the town square "
                    )
                approach = 0

            elif answer == 2: # inspect gap
                print("you roll a die to see if you notice anything\n")
                with console.status(
                    "[violet]rolling...[/violet]", spinner="dots"
                    ):
                    time.sleep(1)
                num = d20(perception_mult)
                subTitlePrint(
                    f"you rolled: {num - perception_mult} "
                    f"+ your perception multiplier = {num}\n"
                    )
                
                if num >= 10:
                    moneyPrint("you think the space looks like it could house "
                        "some sort of switch\n"
                        )
                    approach = 3

                else:
                    fastPrint("you don't have a clue :/")
                    approach = 3

            elif answer == 3: # try use items in inventory
                for item in player_items:
                    print("-", item)
                answer = input("Which do you choose? ").strip().lower()

                if answer in player_items:

                    if answer == ("suspicious lever"):
                        fastPrint(
                            "You insert the lever into the slip gap and pull "
                            "it down "
                            "\nThe room lights up and you now see the "
                            "room a bit better you take a better look at the "
                            "man behind the counter. "
                            "\nHe has paper white skin and luminescent yellow, "
                            "pink glasses resting upon a long sharp nose "
                            "about a foot long"
                            )
                        spamtonPrint(
                            "\nHEY      EVERY      !! IT'S ME!!! EV3RY  BUDDY "
                            " 'S FAVORITE [[Number 1 Rated Salesman1997]] "
                            "SPAMT SPAMTON G. SPAMTON!! WOAH!! IF IT ISN T "
                            "A... ADVEN TUR UR RRR! HEY-HE Y HEY!!!"
                            "\nWELL HAVE I GOT A [[Specil Deals]] FOR LONELY "
                            "[[Hearts]] LIKE YOU"
                            )
                        questionOptionPrint(
                            "\nWant to see Spamtons [[specil Deals]] "
                            )
                        questionPrint("[Y/n]")

                        answer = input("\n").strip().lower()

                        if answer == "y":
                            open_shop()
                            pluey_visits = 2

                        elif answer == "n":
                            normalPrint(
                                "It was probably for the best you left you "
                                "thought, pondering to yourself as you wander "
                                "back to the town"
                                )
                            approach = 0
                            pluey_visits = 2

                        else: 
                            errorPrint("err: invalid input")
                            
                    else:
                        normalPrint("You can't use that here")

                else:
                    errorPrint(f"you don't have {answer}")

            else: # error
                errorPrint("err: invalid input")

        # If its their third time in pluey
        elif pluey_visits == 2:
            fastPrint(
                "You enter pluey again its much brighter than last time but "
                "no cleaner and spamton looks like he hasn't moved since"
                )
            spamtonPrint(
                "\nHEY      EVERY      !! IT'S ME!!! EV3RY  BUDDY  'S "
                "FAVORITE [[Number 1 Rated Salesman1997]] SPAMT SPAMTON G. "
                "SPAMTON!! WOAH!! IF IT ISN T YYOU AGA IN! HEY-HE Y HEY!!! "
                "WELLLLCOME BA B BB ACK"
                "\nWELL HAVE I GOT A [[Specil Deals]] FOR LONELY [[Hearts]] "
                "LIKE YOURS"
                )
            questionOptionPrint("\nWant to see Spamtons [[specil Deals]] ")
            questionPrint("[Y/n]")

            answer = input("\n").strip().lower() # ask what you want to do

            if answer == "y": # open shop
                open_shop()

            elif answer == "n": # return to town
                NormalPrint("It was probably for the best you left you "
                "thought, pondering to yourself as you wander back to the town"
                )
                approach = 0
                


#Imma just break the loop if u die :/
GameEndPrint("YOU DIED")
