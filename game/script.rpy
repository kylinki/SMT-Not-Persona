define m = Character('Me', color="#128412")
define p = Character('Professor-senpai', color="#110eed")

define al = Character('Alice', color="#d16587")
define an = Character('Angel', color="#d16587")
define g = Character('Girimekhala', color="#d16587")
define j = Character('Jack Frost', color="#110eed")
define mo = Character('Moh Shuvuu', color="#d16587")
define o = Character('Oni', color="#d16587")
define pi = Character('Pixie', color="#d16587")
define s = Character('Setanta', color="#d16587")
define te = Character('Terminator', color="#d16587")
define ti = Character('Titania', color="#d16587")

label start:
    play music "school.mp3"
    scene bg meadow
    m "It's finals seasons oof"
    m "Fortunately I already aced my Calc 4 and Algorithms exams!"
    m "Easy peasy cuz r/IAmVerySmart"
    m "Today's exam is my last final but also my worst subject"
    m "How To Be Nice 101"

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
    m "...I shouldn't have bought Persona 5 Racing right beforehand!" 

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
    m "I somehow impossibly made it!"
    m "Now I can bomb the final once Professor-senpai says-"
    "*gunshots*"
    p "YOU MAY BEGIN!"
    m "Oh"
    m "Let's see, first question"

    menu:
        "1) Which is the friendlier, more likeable sub?"
        "r/Persona5. I love cumming on Joker figurines":
            stop music
            scene bg blacked
            "A mysterious force killed you"
            "..."
            "Just kidding"
            "Professor-senpai strangled you to death"
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
    m "What dafuq just happened?"
    m "Am I up King Lucifer's asshole?"
    "Three unidentifiable Lovecraftian horrors appear before you!"
    scene unidentified chaos
    "They all emit a powerful aura"
    m "Hot, I want them to spank me hard!"
    m "...and reject gods of course"

    menu:
        "Which one will you approach?"
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
    m "Oof how did I get here?"
    m "Well there certainly aren't any opposite gender bathrooms here"
    "Three unidentifiable blue blobs appear before you!"
    scene unidentified neutral
    "They all emit a lewd aura"
    "...not actually. You're just a pervert"

    menu:
        "Which one will you approach?"
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
    m "Where am I?"
    m "Is this up Lord YHVH's one of infinite nostrils?"
    "Three unidentifiable heavenly figures appear before you!"
    scene unidentified law
    "They all emit a peaceful aura"
    m "Holy moly, I want to lick their fingers and praise YHVH"

    menu:
        "Which one will you approach?"
        "left heavenly figure":
            jump angel
        "middle heavenly figure":
            jump terminator
        "right heavenly figure":
            jump mohShuvuu

    return

label oni:
    scene bg chaos
    show demon oni
    o "FUCK OFF!"
    
    menu:
        "What will you do?"
        "Scram away":
            o "Nooooo I didn't actually mean it!"
            jump oniBad
        
        "NO YOU FUCK OFF!":
            o "Ah that's more like it!"
            o "Rule is by the strong!"
            o "..."
            o "...I'm actually a little tsundere ya know"
            o "...my kokoro is very different from my brutish appearance..."
            o "kya~"
            menu:
                o "Can't you tell by my Japanese schoolgirl-inspired outfit?"
                "So you're a crossdressing weeb pervert":
                    o "YES JUST LIKE THAT! I LIKE RUDE!"
                    o "My heart is going crazy doki doki around you..."
                    o "I've decided!"
                    o "You are to be my new kawaii sweetheart~"
                    o "cuz the last one didn't last long ;)"
                    "..."
                    "Onii-chan later spanked you so hard"
                    "with power, just the way you wanted"
                    o "*exhales deeply*"
                    o "Okay let's grab some burgers, my treat <3"
                    hide demon oni
                    show good oni
                    "Congrats! You got Onii-chan Good End!"
                    return
                "Of course Onii-chan! You look kawaii as fuck":
                    o "URUSAI! URUSAI! URUSAI!"
                    o "I'M NOT INTO THAT LOVEY DOVEY SWEET TALK SHIT!"
                    jump oniBad

label oniBad:
    o ":'("
    stop music
    "You made Oni sad"
    scene bg blacked
    "Oni ran away in tears"
    "The other demons blood orgy'd with your innards"
    "Oni Bad End"
    return