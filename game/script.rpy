# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    player_name = ""
    sia_points = 0
    komp_points = 0
define p = Character("[player_name]")
define cs = Character("Komp Sy")
define cis = Character("Sia Yes")

# The game starts here.

label start:

    scene bg main_room
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
    show eileen happy

    "This is me, I'm just your average CPP student working on this Hackathon"

    $ player_name = renpy.input("Wait, but what was my name?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Billy Bronco"
    # define p = Character(player_name)

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
  
    p "Ah of course. My name is [player_name]!"
    p "How silly of me to forget my own name!"


    p "Now that I'm here I gotta find myself a team."
    p "I should go talk to someone."

    "You look around the room and your eyes fall on two people on oppsite sides of the room."

    p "Who should I talk to?"

    menu:
        "The person the right.":
            jump CS
        "The person on the left.":
            jump CIS



label CS:
    p "Hey my name is [player_name]!"

    cs "Hey"

    
label CIS:

    p "Hey my name is [player_name]!"

    cis "Hey"

