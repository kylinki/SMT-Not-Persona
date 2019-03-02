# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character('Me', color="#c8ffc8")
define p = Character('Professor', color="#c8ffc8")

define j = Character('Alice', color="#110eed")
define n = Character('Angel', color="#c8ffc8")
define n = Character('Girimekhala', color="#D16587")
define j = Character('Jack Frost', color="#110eed")
define n = Character('Moh Shuvuu', color="#c8ffc8")
define n = Character('Oni', color="#D16587")
define j = Character('Pixie', color="#110eed")
define n = Character('Setanta', color="#c8ffc8")
define n = Character('Terminator', color="#D16587")
define n = Character('Titania', color="#D16587")

label start:
    play music "school.mp3"
    scene bg meadow
    m "It's finals seasons oof"
    m "Fortunately I already aced my Calc 4 and Algorithms exams!"
    m "Easy peasy cuz r/IAmVerySmart"
    m "Today's exam is my last final but also my weakest subject"
    m "How To Be Friendly or Likeable 101"

    menu:
        m "Guess I'm gonna..."
        "try my best!":
            jump notChaos
        "ditch it. This is a stupid, useless class":
            stop music
            scene bg blacked
            "You blacked out!"
            jump chaos

label notChaos:
    scene bg uni
    m "The exam starts in literally 3 seconds, uh oh"
    m "...I shouldn't have bought Persona 5 Racing right beforehand" 

    menu:
        m "Guess I'll..."
        "try to make it! There's literally 1 second left!":
            jump notNeutral
        "sneak into the opposite gender's bathroom and question my life decisions":
            stop music
            scene bg blacked
            "You blacked out!"
            jump neutral

label notNeutral:
    scene bg lecturehall
    m "I somehow impossibly made it! Now I can bomb the final"
    p "You may begin the test!"
    m "Let's see, first question"

    menu:
        "1) Which is the friendlier, more likeable subreddit?"
        "r/Persona5. I love cumming on Joker figurines":
            stop music
            scene bg blacked
            "A mysterious force killed you"
            "Pathetic End"
            return

        "r/Megaten. I love not cumming on Joker figurines":
            stop music
            scene bg blacked
            "You blacked out!"
            jump law

label chaos:
    play music "date.mp3"
    scene bg chaos
    m "..."
    m "What dafuq just happened"
    m "Am I up King Lucifer's asshole?"
    "Three unidentifiable Lovecraftian horrors appear before you!"
    scene unidentified chaos
    "They all emit a powerful aura"
    m "Hot, I want them to spank me so hard!"
    m "...and reject gods of course"

    menu:
        "Which one will you approach first?"
        "left Lovecraftian horror":
            jump oni
        "middle Lovecraftian horror":
            jump girimekhala
        "right Lovecraftian horror":
            jump alice

    return

label neutral:
    play music "date.mp3"
    scene bg neutral
    m "..."
    m "oof what happened"
    m "Well there certainly aren't any opposite gender bathrooms here"
    "Three unidentifiable blue blobs appear before you!"
    scene unidentified neutral
    "They all emit a lewd aura"
    "...not actually. You're just a pervert"

    menu:
        "Which one will you approach first?"
        "left blue blob":
            jump pixie
        "middle blue blob":
            jump titania
        "right blue blob":
            jump setanta

    return

label law:
    play music "date.mp3"
    scene bg law
    m "..."
    m "How did I arrive here?"
    m "Is this up Lord YHVH's one of infinite nostrils?"
    "Three unidentifiable heavenly figures appear before you!"
    scene unidentified law
    "They all emit a peaceful aura"
    m "Holy moly, I want to lick their fingers and praise YHVH"

    menu:
        "Which one will you approach first?"
        "left heavenly figure":
            jump angel
        "middle heavenly figure":
            jump terminator
        "right heavenly figure":
            jump mohShuvuu

    return