# ignore this just makes sure it runs on school computers (you can also run these on
# school computers; if you double click the python file they open in terminal and will 
# run properly with full colour and stuff idrk why )
import subprocess
subprocess.run(["pip", "install", "pygame", "rich", "progress", "playsound3"])


#  Imports :)
import random, time, pygame, progress, threading, playsound3 # probably wont need threading
from rich.console import Console
from progress.spinner import Spinner
from rich import print
console = Console()


#Music - fades in music and looks badass while doing it  
with console.status("[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"):
    pygame.init
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load("music/rudebuster_boss.mp3")
    pygame.mixer.music.play(loops=-1, fade_ms=5000)#
    time.sleep(1)


# stray variable cos needed in cool words
skip = False


# Cool Text - prints text letter by letter with diffrent colours and speeds
def type(words):
    letters = list(words)
    for letter in letters:
        print (letter, end="", flush=True)
        if skip == False:
            time.sleep(0.06)


def item_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[yellow3]{letter}[/yellow3]", end="")
        if skip == False:
            time.sleep(0.06)


def hint_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[orange3]{letter}[/orange3]", end="")
        if skip == False:
            time.sleep(0.06)


def fast_type(words):
    letters = list(words)
    for letter in letters:
        print (letter, end="", flush=True)
        if skip == False:
            time.sleep(0.015)


def question_options_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[green4]{letter}[/green4]", end="")
        if skip == False:
            time.sleep(0.06)


def question_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[spring_green3]{letter}[/spring_green3]", end="")
        if skip == False:
            time.sleep(0.08)


def title_type(title):
    letters = list(title)
    for letter in letters:
        console.print ( \
f"[underline bold purple]{letter}[/underline bold purple]", end="")
        if skip == False:
            time.sleep(0.1)


def subtitle_type(title):
    letters = list(title)
    for letter in letters:
        console.print (f"[deep_sky_blue1]{letter}[/deep_sky_blue1]", end="")
        if skip == False:
            time.sleep(0.1)


def error_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[red3]{letter}[/red3]", end="")
        if skip == False:
            time.sleep(0.1)


def damage_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[bright_red]{letter}[/bright_red]", end="")
        if skip == False:
            time.sleep(0.1)


def spamton_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[sky_blue2]{letter}[/sky_blue2]", end="")
        if skip == False:
            rand = random.randint(1,30)
            if rand > 29:
                time.sleep(0.4)
            else:
                time.sleep(0.02)


def game_end_type(words):
    letters = list(words)
    for letter in letters:
        console.print (f"[red]{letter}[/red]", end="")
        time.sleep(0.7)
         

fast_type("Do you want the text to print instantly or do the really epic cool" \
" printing where it types it out slowly and is only for cool people? ")
question_options_type("\nReally cool epic text? ")
question_type("[Y/n]")
answer = input("\n").lower().strip()

if answer == ("y"):
    type("ty :)")

elif answer == ("n"):
    error_type("aww :(")
    time.sleep(0.5)
    skip = True

else:
    error_type("error assuming you want the epic text mwuhahahaha")


# Variables
alive = True
character_chosen = False
player_stats = {
"health": 1, 
"strength": 0, 
"charisma": 0, 
"dexterity": 0, 
"intelligence": 0
}
player_items = ["stick"]
player_weapons = {}
money = 250
in_shop = False

question_options_type("\nDo you want to display diffrent character and their stats/weapons ")
question_type("[Y/n]")
answer = input("\n").lower().strip()

if  answer == ("y"):
# Display characters and their items/stats
    type("\nChoose one of these four adventurers\n")
# Warrior
    title_type("\nWarrior")
    fast_type("\nWarrior have considerable streangth and defense making them the \
    \neasiest to play while still being powerfull with a fairly even \
    \nstat distribution")
    subtitle_type("\n\nStats")
    fast_type("\nStrength - 16 Charisma - 14 Dexterity - 12 Perception - 14 " \
    "Health - 130")
    subtitle_type("\n\nWeapons")
    fast_type("\nLongsword\nDagger")
# Rouge
    title_type("\n\nRouge")
    fast_type("\nRouge has low strength and health but with high damage making" \
    "\nthem a difficult Character to play but powerful")
    subtitle_type("\n\nStats")
    fast_type("\nStrength - 16 Charisma - 12 Dexterity - 18 Perception - 16 " \
    "Health - 70")
    subtitle_type("\n\nWeapons")
    fast_type("\nKatar\nDagger")
# Barbarian
    title_type("\n\nBarbarian")
    fast_type("\nWith their high damage and low health the barbarian is a glass" \
    "\ncannon dealing high damage but with little in ways of defense")
    subtitle_type("\n\nStats")
    fast_type("\nStrength - 20 Charisma - 10 Dexterity - 12 Perception - 12 " \
    "Health - 100")
    subtitle_type("\n\nWeapons")
    fast_type("\nBattle axe\nHatchet")
# Paladin
    title_type("\n\nPaladin")
    fast_type("\nPaladin has high defense and decent offense making it a powerful" \
    "\ncombatant matched with good charisma although stleath will be" \
    "\noff the table for the most part")
    subtitle_type("\n\nStats")
    fast_type("\nStrength - 14 Charisma - 18 Dexterity - 6 Perception - 14 " \
    "Health - 160")
    subtitle_type("\n\nWeapons")
    fast_type("\nShort sword\nShield")
elif answer == ("n"):
    subtitle_type("\nskipped..")
else:
    error_type("error skiping anyway :)")

# Choose character
subtitle_type("\n\nEnter a number to choose")
question_options_type("\n1) Warrior \n2) Rouge \n3) Barbarian \n4) Paladin\n")

def character_select(number, character):
    global character_chosen
    global your_character

    if answer == number:
        question_type(f"You Choose {character}? [Y/n]")
        check = input("\n").strip().lower()

        if check == "y":
            type(f"Your class is now {character}\n")
            character_chosen = True
            your_character = character

        elif check == "n":
            pass

        else:
            error_type("error :/\n")

while character_chosen == False:
    question_type("which do you choose")
    answer = int(input("\n"))
    character_select(1, "Warrior")
    character_select(2, "Rouge")
    character_select(3, "Barbarian")
    character_select(4, "Paladin")

# Dice - functions for each dice if called return random number between 1 and d_ + mult
def d2(mult):
    num = random.randint(1,2) + mult
    return num


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
if your_character == "Warrior":
   player_stats.update({
    "health": 130,
    "strength": 16,
    "charisma": 14,
    "dexterity": 12,
    "perception": 14 })
   player_weapons.update({
       "main": ("longsword", d8),
       "secondary": ("dagger", d4)
   })

elif your_character == "Rouge":
    player_stats.update({
    "health": 70,
    "strength": 16,
    "charisma": 12,
    "dexterity": 18,
    "perception": 16 })
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
    "perception": 12 })
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
    "perception": 14 })
    player_weapons.update({
       "main": ("short sword", d6),
       "secondary": ("shield", d4)
   })
    
else:
    error_type("huh? you shouldn't be here :/")
    exit()
#print(player_weapons["main"] [1] (0) )

# Change music - shows loading screen while music fades out and fades in
with console.status("[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"):
   time.sleep(1)

# Title - just words innit
title_type("welcome to BOBLIN\n\n")

# Opening
fast_type("You approach  the town you'd been looking for the past 3 years it " \
"is an adventuring town built around the main landmark the great orouborus " \
"dungeon a seemingly endless maze with one grand door large enough to " \
"allow thousands of adventurers to enter and exit at the same time. Although " \
"being called a dungeon it spans into the sky as far as the eye can see and is " \
"said to house the gods at the top although no ones ever made it that far " \
"you look around and also see a tavern named grillbys for meals and resting "
"and a run down shop with a sign that says Pluey? You have no idea what " \
"that means and decide to ignore it for now and continue to the town square")


#Variables - change stats to multiplyers so i van just ad or take away them from dice rolls
strength_mult = int((player_stats["strength"] - 10) / 2)
charisma_mult = int((player_stats["charisma"] - 10) / 2)
dexterity_mult = int((player_stats["dexterity"] - 10) / 2)
perception_mult = int((player_stats["perception"] - 10) / 2)
dungeon_visits = 0
tavern_visits = 0
pluey_visits = 0
runs = 0


# MAIN GAME LOOP - keeps the game in a big loop so it doesnt end
while alive == True:
   print("") # <-- so console below removes this instead of important text
   with console.status("[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line"):
       pygame.mixer.music.fadeout(1000)
       pygame.mixer.music.load("music/field_of_hopes.mp3")
       pygame.mixer.music.play(loops=-1, fade_ms=2000)
       time.sleep(0.5)
   subtitle_type("\n\nChoose a number to travel : ")
   question_options_type("\n1) Approach orouborus dungeon \n2) Look in Grillbys\n" \
"3) Pluey?")
   question_type("\nWhere do you want to go?")
   approach = int(input("\n"))

   while approach == 1:
        print("") # <-- so console below removes this instead of important text
        with console.status("[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line", ):
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("music/vs_susie.mp3")
            pygame.mixer.music.play(loops=-1, fade_ms=1000)
            time.sleep(0.5)
        subtitle_type("\nas you approach the dungeon you decide it isnt finsihed yet and " \
        "pluey might have some [$DEAL$!] maybe")
        question_options_type("\nReturn to city center?")
        question_type("[Y/n]")
        answer = input("\n").strip().lower()

        if answer == "y":
            fast_type("as you walk back you think it might be for the best but maybe at a later " \
            "time *cough cough nudge nudge wink wink")
            approach = 0

        elif answer == "n":
            type("you decide to sit here and wait till the end of time maybe your enjoying the " \
            "music, maybe you areconvinced theres more but sadly i didnt have enough time " \
            "but plueys deffinetly really cool so maybe go there after re-loading this ??")
            while alive == True:
                pass
                time.sleep(1)

        else:
            error_type("oh no an error thats so sad well too bad you missed out on all the " \
            "dungeon content better luck next time")
            
            exit()

   while approach == 2:
        print("") # <-- so console below removes this instead of important text
        with console.status("[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line", ):
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("music/sans_shop.mp3")
            pygame.mixer.music.play(loops=-1, fade_ms=1000)
            time.sleep(0.5)

        subtitle_type("\nas you approach the tavern you decide it isnt finsihed yet and " \
        "pluey might have some $VALUES$ maybe")
        question_options_type("\nReturn to city center?")
        question_type("[Y/n]")
        answer = input("\n").strip().lower()

        if answer == "y":
            fast_type("as you walk back you think it might be for the best but maybe in a later " \
            "project *cough cough nudge nudge wink wink")
            approach = 0

        elif answer == "n":
            type("you decide to sit here and wait till the end of time maybe your enjoying the " \
            "music, maybe you are convinced theres more but sadly i didnt have enough time " \
            "but plueys deffinetly really cool so maybe go there after re-loading this ??")
            while alive == True:
                pass
                time.sleep(1)
        

        else:
            error_type("oh no an error thats so sad well too bad you missed out on all the " \
            "dungeon content better luck next time")
            exit()

   while approach == 3:
        print("") # <-- so console below removes this instead of important text
        with console.status("[dark_slate_gray1]loadin...[/dark_slate_gray1]", spinner="line", ):
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("music/spamton_meeting.mp3")
            pygame.mixer.music.play(loops=-1, fade_ms=1000)
            time.sleep(0.5)

        if pluey_visits == 0:
            fast_type("You stuble into pluey not sure what to expect. Its cold and " \
            "baren, the room is empty barring the rows of book shelves lining the outer " \
            "walls and single old oak desk centerd at the then end of the room. " \
            "it faces you but you can barely make out its shape as all that illuminates"  \
            "is the faint glow from the open door behind you.")
            subtitle_type("\n\nDo you want to leave or look closer?")
            question_options_type("\n1) leave and come back later " \
            "\n2) inspect table \n3) items")
            question_type("\nWhat do you do?")
            answer = int(input("\n"))

            if  answer == 1:
                damage_type("you attempt to leave")
                fast_type(" and remember you left the door wide open allowing you " \
                "to leave with ease you decide to head back to the town square ")
                approach = 0

            elif answer == 2:
                type("you roll a die to see if you notice anything\n")
                with console.status("[violet]rolling...[/violet]", spinner="dots", ):
                    time.sleep(1)

                num = d20(perception_mult)
                subtitle_type("you rolled: ")
                print((num - perception_mult), "+ your perception multiplier =", num)

                if num >= 10:
                    fast_type("\nYou notice looking at the table theirs a small " \
                    "white spike pertruding from behind the table and decide to approach")
                    fast_type("\nYou make out the shape of what looks to be an odd " \
                    "looking man with a protruding nose" \
                    "\nHe sits there for a second before blurting out in a robotic voice")
                    spamton_type("\nAHHHH A NEW [slime] WHY BE THE [Little Sponge] " \
                    "WHO HATES ITS [$4.99] LIFE WHEN YOU CAN BE A [BIG SHOT!!!]. " \
                    "\nWANNA BE A [[BIG SHOT?!?!]]")
                    question_type(" [Y/n]")
                    answer = input("\n").strip().lower()

                    if answer == "y" or answer == "n":
                        spamton_type("I KNEW YOU DIDNT WANT TO BE [the little slime] " \
                        "YOU ARE NOW GRAB THIS BY THE [silly strings]")
                        question_options_type("\nWanna grab it by the silly strings?")
                        question_type(" [Y/n]")
                        answer = input("\n").strip().lower()

                        if answer == ("y"):
                            fast_type("you pull the silly string he's layed out on the tabel and " \
                            "notice a lever attached to the end of it." \
                            "You take the lever and thank him uncertainly")
                            item_type("\n+ 1 Suspicious Lever")
                            player_items.append ("suspicious lever")
                            spamton_type("\nNO PROBLEM COME BACK FOR MORE [[Hyperlink " \
                            "Blocked]]")
                            approach = 0
                            pluey_visits = 1


                        if answer == ("n"):
                            spamton_type("YOU WANT IT. YOU WANT [[Hyperlink Blocked]], " \
                            "DON'T YOU.")
                            fast_type("\nYour not sure and decide to leg it back to town hoping " \
                            "it isnt chasing you")
                            approach = 0

                    else:
                        fast_type("Your not sure and decide to leg it back to town hoping " \
                        "it isnt chasing you")
                        approach = 0

                else: 
                    fast_type("You dont notice anything and decide to head back to " \
                    "the town square ")
                    approach = 0

            elif answer == 3:
                approach = 0
                for item in player_items:
                    print("-", item)
                answer = input("Which do you choose? ").strip().lower()

                if answer in player_items:
                    type("You can't use that here")

                else:
                    error_type("huh?")

            else:
                print("you dont have ", answer)

        elif pluey_visits == 1:
            fast_type("You return to pluey still confused from the last time you were here")
            question_type("\n1) leave and come back later \n2) inspect gap \n3) items")
            answer = int(input("\n"))

            if  answer == 1:
                fast_type("you leave and decide to head back to the town square ")
                approach = 0

            elif answer == 2:
                type("you roll a die to see if you notice anything\n")
                with console.status("[violet]rolling...[/violet]", spinner="dots", ):
                    time.sleep(1)
                num = d20(perception_mult)
                subtitle_type("you rolled: ")
                print((num - perception_mult), "+ your perception multiplier =", num)
                
                if num >= 10:
                    hint_type("you think the space looks like it could house some sort " \
                    "of switch\n")
                    approach = 3

                else:
                    fast_type("you dont have a clue :/")
                    approach = 3

            elif answer == 3:
                for item in player_items:
                    print("-", item)
                answer = input("Which do you choose? ").strip().lower()

                if answer in player_items:

                    if answer == ("suspicious lever"):
                        fast_type("You insert the lever into the slip gap and pull it down" \
                        "\nThe room lights up and you now see the room a bit better " \
                        "you take a better look at the man behind the counter." \
                        "\nHe has paper white skin and luminecent yellow, pink glasses " \
                        "resting upon a long sharp nose about a foot long")
                        spamton_type("\nHEY      EVERY      !! IT'S ME!!! EV3RY  BUDDY  'S " \
"FAVORITE [[Number 1 Rated Salesman1997]] SPAMT SPAMTON G. SPAMTON!! " \
"WOAH!! IF IT ISN T A... ADVEN TUR UR RRR! HEY-HE Y HEY!!!")
                        spamton_type("\nWELL HAVE I GOT A [[Specil Deals]] FOR LONELY " \
                        "[[Hearts]] LIKE YOU")
                        question_options_type("\nWant to see Spamtons [[specil Deals]] ")
                        question_type("[Y/n]")
                        answer = input("\n").strip().lower()

                        if answer == ("y"):
                            in_shop = True
                            spamton_type("AND I HAVE JUST. \nTHE THING. \nYOU NEED. " \
                            "\nTHAT'S [[BARGAIN$]].")
                            while in_shop == True:
                                title_type("\n\nS͠P̷A͜M̴T̛O͞N͢'͠S͡ ̵$$D͜E͜A̷L̡Z̸$$ ͝S͠H͘O̢}")
                                print("")
                            
                                if "broken sword" not in player_items:
                                    item_type("\nTHE BIG ONE  [D£ 100]")

                                if "frayed bowtie" not in player_items:
                                    item_type("\nBSHOT BOWTIE  [D£ 60]")
                                item_type("\nH.POISON  [D£ 30]")

                                if "silver key" not in player_items:
                                    item_type("\nSUPER KEY (ExTrEmE) [D£ 100]")

                                hint_type("\n\nYou Have D£ ")
                                print(f"[orange3]{money}[/orange3]", end="")
                                hint_type(" Kromer")

                                subtitle_type("\n\nwould you like to buy anything?")
                                question_options_type("\n1) Buy THE BIG ONE " \
    "\n2) Buy BSHOT BOWTIE \n3) Buy H.POISON \n4) SuperKEY " \
    "\n5) Decide not to buy anything and leave to the town square " )
                                question_type("[1->5]")
                                answer = int(input("\n"))

                                if answer == 1:

                                    if money >= 100 and "broken sword" not in player_items:
                                        subtitle_type("\nYou bought THE BIG ONE")
                                        item_type("\n- D£100")
                                        item_type("\n+ 1 broken sword")
                                        player_items.append("broken sword")
                                        money -= 100
                                    else:
                                        error_type("not enough money or already purchased")

                                elif answer == 2:

                                    if money >= 60 and "frayed bowtie" not in player_items:
                                        subtitle_type("\nYou bought BSHOT BOWTIE")
                                        item_type("\n- D£60")
                                        item_type("\n+ 1 frayed bowtie")
                                        player_items.append("frayed bowtie")
                                        money -= 60
                                    else:
                                        error_type("not enough money or already purchased")

                                elif answer == 3:

                                    if money >= 30:
                                        subtitle_type("\nYou bought H.POSION")
                                        item_type("\n- D£30")
                                        item_type("\n+ 1 health potion")
                                        player_items.append("health potion")
                                        money -= 30

                                elif answer == 4:

                                    if money >= 100 and "silver key" not in player_items:
                                        subtitle_type("\nYou bought SUPER KEY (ExTrEmE")
                                        item_type("\n- D£100")
                                        item_type("\n+ 1 silver key")
                                        player_items.append("silver key")
                                        money -= 100
                                    else:
                                        error_type("not enough money or already purchased")

                                elif answer == 5:
                                    pluey_visits = 2
                                    type("you wander back wondering what those wierd items did")
                                    in_shop = False
                                    approach = 0

                        elif answer == ("n"):
                            approach = 0
                            pluey_visits = 2
                            type("It was probably for the best you left you thought, pondering  " \
                            "to yourself as you wander back to the town")

                        else: 
                            error_type("huh? its y or n it cant be that hard")
                            
                    else:
                        type("You can't use that here")

                else:
                    error_type("huh?")

            else:
                print("you dont have ", answer)

        elif pluey_visits == 2:
            fast_type("You enter pluey again its much brighter than last time but " \
            "no cleaner and spamton looks like he hasn't moved since")
            spamton_type("\nHEY      EVERY      !! IT'S ME!!! EV3RY  BUDDY  'S " \
"FAVORITE [[Number 1 Rated Salesman1997]] SPAMT SPAMTON G. SPAMTON!! " \
"WOAH!! IF IT ISN T YYOU AGA IN! HEY-HE Y HEY!!! WELLLLCOME BA B BB ACK")
            spamton_type("\nWELL HAVE I GOT A [[Specil Deals]] FOR LONELY " \
            "[[Hearts]] LIKE YOURS")
            question_options_type("\nWant to see Spamtons [[specil Deals]] ")
            question_type("[Y/n]")
            answer = input("\n").strip().lower()

            if answer == ("y"):
                in_shop = True
                spamton_type("AND I HAVE JUST. \nTHE THING. \nYOU NEED. " \
                "\nTHAT'S [[BARGAIN$]].")
                while in_shop == True:
                    title_type("\n\nS͠P̷A͜M̴T̛O͞N͢'͠S͡ ̵$$D͜E͜A̷L̡Z̸$$ ͝S͠H͘O̢}")
                    print("")

                    if "broken sword" not in player_items:
                        item_type("\nTHE BIG ONE  [D£ 100]")

                    if "frayed bowtie" not in player_items:
                        item_type("\nBSHOT BOWTIE  [D£ 60]")
                    item_type("\nH.POISON  [D£ 30]")

                    if "silver key" not in player_items:
                        item_type("\nSUPER KEY (ExTrEmE) [D£ 100]")

                    hint_type("\n\nYou Have D£ ")
                    print(f"[orange3]{money}[/orange3]", end="")
                    hint_type(" Kromer")

                    subtitle_type("\n\nwould you like to buy anything?")
                    question_options_type("\n1) Buy THE BIG ONE " \
    "\n2) Buy BSHOT BOWTIE \n3) Buy H.POISON \n4) SuperKEY " \
    "\n5) Decide not to buy anything and leave to the town square " )
                    question_type("[1->5]")
                    answer = int(input("\n"))

                    if answer == 1:

                        if money >= 100 and "broken sword" not in player_items:
                            subtitle_type("\nYou bought THE BIG ONE")
                            item_type("\n- D£100")
                            item_type("\n+ 1 broken sword")
                            player_items.append("broken sword")
                            money -= 100
                        else:
                            error_type("not enough money or already purchased")

                    elif answer == 2:

                        if money >= 60 and "frayed bowtie" not in player_items:
                            subtitle_type("\nYou bought BSHOT BOWTIE")
                            item_type("\n- D£60")
                            item_type("\n+ 1 frayed bowtie")
                            player_items.append("frayed bowtie")
                            money -= 60
                        else:
                            error_type("not enough money or already purchased")

                    elif answer == 3:

                        if money >= 30:
                            subtitle_type("\nYou bought H.POSION")
                            item_type("\n- D£30")
                            item_type("\n+ 1 health potion")
                            player_items.append("health potion")
                            money -= 100
                        else:
                            error_type("not enough money")

                    elif answer == 4:

                        if money >= 100 and "silver key" not in player_items:
                            subtitle_type("\nYou bought SUPER KEY (ExTrEmE")
                            item_type("\n- D£100")
                            item_type("\n+ 1 silver key")
                            player_items.append("silver key")
                            money -= 100
                        else:
                            error_type("not enough money or already purchased")

                    elif answer == 5:
                        type("you wander back to the town center curious about the items")
                        in_shop = False
                        approach = 0
            elif answer == ("n"):
                approach = 0
                type("It was probably for the best you left you thought, pondering to " \
                "yourself as you wander back to the town")
                


#Imma just break the loop if u die :/
game_end_type("YOU DIED")
