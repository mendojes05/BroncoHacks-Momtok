# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    player_name = ""
    sia_points = 0
    komp_points = 0
    komp_locked = False
    sia_locked = False
    komp_finished = False
    sia_finished = False
define p = Character("[player_name]")
# define pt = Character("[player_name] *thinking*", what_style="italics")
define cs = Character("Komp Sy")
define cis = Character("Sia Yes")

# The game starts here.

label start:

    scene bg main_room
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    "This is me, I'm just your average CPP student working on this Hackathon"

    $ player_name = renpy.input("Wait, but what was my name?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Billy Bronco"
  
    p "Ah of course. My name is [player_name]!"
    p "How silly of me to forget my own name!"


    p "Now that I'm here I gotta find myself a team."
    p "I should go talk to someone."

    "You look around the room and your eyes fall on two people on opposite sides of the room."
    
    show cis default left
    show cs default right

    p "Who should I talk to?"

    menu:
        "The person the right.":
            hide cis default left
            jump CS
        "The person on the left.":
            hide cs default right
            jump CIS



label CS:
    show cs default
    p "Hey my name is [player_name]!"

    cs "Konnichiwa! My name is Komp Sy-chan."
    cs "I'm a computer science major, or as I like to call myself, a super hacker or just call me when your code breaks."
    cs "The word hackers originally meant “skilled programmer you know"
    cs "Are you looking to join my super sugoi team of hackers?"

    menu:
        "{i}Strike a pose{/i} \"YES, I am!\"":
            cs "Sugoi! I knew I sensed main character energy from you."
            $komp_points += 1
        "Why are you talking like that?":
            $komp_points += -1
            cs "W-What do you mean? This is how all elite hackers talk!"
            cs "You're just not used to the culture yet. You'll get there, kouhai~"
            cs "Anyway, you in or nah? We've got algorithms to wrangle and a hackathon to win."
            menu:
                "Say yes":
                    "Uhh... sure I guess."
                "Just Leave":
                    $komp_locked = True
                    jump CStoCIS
    cs "But not so fast! You gotta pass our test first!"
    p "Huh? What test?"
    cs "Not anyone can just join our super team"
    cs "First question: light mode or dark mode?"
    menu:
        "Dark Mode":
            $komp_points += 1
            p "Dark mode, obviously."
            cs "A classic choice. You'll fit right in with the night coders."
        "Light mode":
            $komp_points += -1
            p "Light mode."
            cs "Ew. Gross."
    cs "Anyways, last question. What kinda games do  you play?"
    menu:
        "Soulslike":
            $komp_points += 2
            p "I'm a big soulslike enjoyer."
            cs "Ah a man of taste I see."
        "FPS":
            $komp_points += 1
            p "I mainly play FPS games."
            cs "A bit basic but ok."
        "I don't play games":
            $komp_points += -2
            p "I don't really play any games."
            cs "Oh…"
    if komp_points >= 2:
        cs "HMMMM... okay okay, you've got some rizz. Consider urself soft-accepted into Team 1337~"
        cs "When the cyber battle royale drops, just ping me. I'll add u to the Discord"
    else:
        $komp_locked = True
        cs "Ummm… yeahhh no offense but that was kinda mid "
        cs "You're giving background-NPC energy rn... but it's okay, we all start off as boring normies."

label CStoCIS:
    hide cs default
    $ komp_finished = True
    if sia_finished == True:
        jump TheChoice
    if komp_locked == True:
        p "Well that was weird. Probably not gonna end up on their team."
    else:
        p "Well that's one team I could join."
    p "I should go talk to that other person"
    jump CIS
            

    
label CIS:
    show cis default
    p "Hey, my name is [player_name]!"

    cis "Hello, my name is Sia Yes. 3rd Year CIS major."
    cis "Would you like to connect with me on LinkedIn?"

    menu:
        "Sure, let's connect!":
            $sia_points += 1
            cis "Perfect! With your connection, I'll finally be at 500+ on LinkedIn."
            cis "Now I can unlock my personal brand potential!"

        "Uhh, I'm not much of a networker.":
            cis "Oh… ok. Well, networking is the number one way to land a job these days… but good luck!"
            
    # Dialogue continues regardless of choice
    cis "I'm currently recruiting for a highly motivated entry-level hackathon participant —"
    cis "— preferably with 3 to 5 years of experience in every programming language."
    cis "Would you like to join my hackathon team of change makers, thought leaders, and innovators?"

    menu:
        "{i}I guess I can stick around.{/i}":
            p "I like your funny words, strange person"
            cis "Now that's the type of initiative that I like to see!"
        "{i}Big words. Scared. Must leave.{/i}":
            $sia_locked = True
            p "Uhhh no thanks, bye!"
            jump CIStoCS
    cis "Before we proceed, I just have some screening questions to assess team synergy."
    cis "If you were a SaaS solution pivoting into a blockchain ecosystem during Q3, how would you leverage synergy to disrupt legacy pain points?"
    menu:
            "Easy. I'd initiate a multi-cloud paradigm shift, then leverage KPI-driven microservices to maximize stakeholder buy-in.":
                $sia_points += 1
                cis "Wow… that was so dreamy."
                p "Pardon?"
                cis "Uh, nothing! I was just, uh, thinking about my stock portfolio."
            "I'm not a SaaS solution. I'm a person!":
                $sia_points += -1
                cis "I see..."
            "I don't think I have all of those qualifications…":
                cis "That's okay. Imposter syndrome is common in high-performance environments."
                cis "Here at Team Synergy, we believe in scaling *potential*."

    # Dialogue after first question

    cis "Finally, I have one last screening question to assess your fit."
    cis "Why should we choose you to be on our hackathon team?"

    menu:
        "Because I've survived three group projects, two tech interviews, and one emotional breakdown — all before midterms.":
            $sia_points += 1
            cis "Resilient. Gritty. Mentally cloud-native. Impressive."
        "Because no one else wanted to be on your team.":
            cis "That's… statistically accurate. But I admire your honesty."
        "No thanks. I think I've had enough disruption for one day.":
            cis "Suit yourself. The world's not going to innovate itself, you know."
            cis "But hey — if you change your mind, my DMs are always open for professionally relevant inquiries."
            $sia_locked = True
            jump CIStoCS
    if sia_points >= 2:
        cis "You're in... on a 3-day probationary unpaid trial basis."
        cis "Just let me know if you wanna join my team."
    else:
        $sia_locked = True
        cis "I don't think this may not be a match."
        cis "Unfortunately, we've decided to move forward with more qualified candidates."


label CIStoCS:
    hide cis default
    $ sia_finished = True
    if komp_finished == True:
        jump TheChoice
    if sia_locked == True:
        p "Well that was weird. Probably not gonna end up on their team."
    else:
        p "Well that's one team I could join."
    p "I should go talk to that other person"
    jump CS


label TheChoice:
    p "Ok now that I've talked to some people. I need to choose."
    menu:
        "Komp Sy" if komp_locked == False:
            jump CS_end

        "Sia Yes" if sia_locked == False:
            jump CIS_end

        "Both Komp Sy and Sia Yes" if komp_points == 4 and sia_points == 3:
            jump true_end

        "No team":
            jump Bad_end

label Bad_end:
    "Unfortunately you need a team to compete in the hackathon."
    "You were forced to drop out from the competition and were escorted out by security."
    "You could hear some people whispering about you as you walked out."
    "{i}Wow what a loser. They're not even skilled socially to find a team {/i}"
    "{i}There goes that normie. True NPC.{/i}"
    return

label CIS_end:
    show cis default
    cis "Welcome aboard! We will be starting your onboarding process shortly."
    return

label CS_end:
    show cs default
    cs "So happy to have you as my nakama!"
    return

label true_end:
    show cis default left
    show cs default right

    cis "Wait, you want BOTH of us on your team?"
    cs "Erm, yeah. That wouldn't be very based."
    cis "I concur. I do not sense good synergy between our teams."

    cs "Komp Sy-chan doesn't believe in synergy. I believe in the power of nakama and neural nets!"
    cis "That's not even a certified Scrum value."

    cs "You wouldn't understand my workflow. It's inspired by shōnen character arcs and machine learning pipelines."
    cis "That sounds… extremely unscalable."

    cs "And your LinkedIn posts sound like they were generated by ChatGPT with a caffeine addiction!"
    cis "Thank you. I actually take that as a compliment."

    p "Okay, okay! Let's all calm down. This is supposed to be a hackathon team, not a Crunchyroll vs. Crunchbase battle."
    p "Look. I know you two are basically operating in different programming dimensions..."
    p "But together, we could create something... no one would understand. Or be ready for."
    p "And isn't that what innovation is all about?"

    cs "Hmm... fine. But only if I get to be Lead Otaku Engineer."
    cis "Only if I get to be Chief Synergy Strategist."

    p "Deal. You can both have wildly unnecessary titles."
    p "We'll be a team of chaos, cringe, and maybe… code."

    cs "Kawaii~ I'm uploading our team logo to the shared Google Drive folder! It's a catgirl inside a QR code!"
    cis "And I've already drafted a 6-part thought leadership series about our journey on Medium."

    p "This is either going to be a groundbreaking innovation… or a total disaster."

    cs "Yattaaa!! Hackathon power-up sequence initiated!"
    cis "Let's circle back, align, and execute with maximum ROI."

    p "Let's go, Team \'Agile Anime Alliance\'!"

    # Cue dramatic music and screen fade
    "And thus, a team unlike any other was born."
    "Fueled by buzzwords, anime, and blind ambition..."

    "They didn't end up winning the hackathon."
    "But at least they had a good time."

    "True Ending Unlocked: *Synergy Unleashed*"
    return
