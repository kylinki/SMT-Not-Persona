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
                    "Congrats! Your innards romanced Oni!"
                    return
                "Of course Onii-chan! You look kawaii as fuck":
                    o "URUSAI! URUSAI! URUSAI!"
                    o "I'M NOT INTO THAT LOVEY DOVEY SWEET TALK SHIT!"
                    jump oniBad

label oniBad:
    o ":'("
    "You made Oni sad"
    scene bg blacked
    stop music
    "Oni ran away to cry..."
    jump chaosBad

label girimekhala:
    scene bg chaos
    show demon girimekhala
    g "MAMUDOON! *pawoo*"
    "..."
    "You lucked out!"
    g "MAMUDOON! *pawoo*"
    "..."
    "You lucked out again!"
    "...but you're not feeling so lucky anymore"
    menu:
        "What will you do?"
        "Punch the stupid elephant":
            "You threw a weak punch"
            "*BAM*"
            "Stupid, you impaled your own face!"
            "FATALITY!"
            jump giriBad
        "Show off your junk":
            m "*unzips*"
            g "So that's your elephant trunk huh"
            g "Or what you humans call a 'junk'"
            menu:
                g "HOW DO YOU EVEN BREATHE THRU IT?"
                "I can't cuz Mara sits on it ;)":
                    g "It's cute"
                    g "BUT LOL IS IT MINISCULE!"
                    g "YOU REALLY THINK MASTER MARA WOULD SIT THERE?"
                    g "HECK YOU EVEN THINK HE'D FEEL ANYTHING?"
                    jump giriBad
                "It breathes fire":
                    g "Kay kid, I know you're bullshitting"
                    g "Perhaps I'll Mamudoon just to see you squeal and dance again ;)"
                    m "No wait, Giri. Let's do something else"
                    g "Oooh?"
                    m "Like..."
                    m "Let's go somewhere Arkansas and start a bar brawl"
                    m "It'll be especially fun with all the inbred rednecks"
                    g "Mhmm"
                    m "Then I go to kiss you!"
                    g "!!-"
                    m "Then I publicly suck your trunk or something..."
                    m "They'll be shocked and pissed at our gay furry making out shit"
                    g "So you're a chaos freak"
                    m "Exactly!"
                    g "Free trunkjobs for me, just do it outside there too kay? <3"
                    hide demon girimekhala
                    show good girimekhala
                    "Congrats! Your innards romanced Girimekhala!"
                    return



label giriBad:
    g "*snort* *pawoo*"
    "You made Girimekhala laugh"
    scene bg blacked
    stop music
    "Girimekhala strolled away..."
    jump chaosBad

label chaosBad:
    "The other demons skull fucked and blood orgy'd your innards"
    "Chaos - Bad End"
    return

label pixie:
    scene bg neutral
    show demon pixie
    pi "I've never seen a human like you before..."
    pi "You look kinda flabby and weak"
    m "..."
    menu:
        pi "What? Why are you looking at me like that?"
        "I hear you can become an Uber Pixie":
            pi "I ALREADY AM UBER PIXIE!"
            pi "You suggesting I don't look like it?"
            pi "Pfft lumping me with those level 1 caterpie pixies"
        "Aww you cute I just want to pet you!":
            pi "Yaay thank you!"
            pi "I get that a lot"
            m "Can you cast Megidoloan on this lake?"
            menu:
                pi "Sure but um why?"
                "It's funny to see you try and fail":
                    pi "Excuse me?"
                    m "Because you never have enough MP!"
                    pi "..."
                    pi "You seem like an honest person"
                    pi "I like that..."
                    pi "And you called me funny...well"
                    pi "I'm Pixie the Fairy. I'm sure we'll be the best of friends!"
                    m "Lol okay fusion fodder"
                    hide demon pixie
                    show good pixie
                    "Congrats! Your innards romanced Pixie!"
                    return
                "So we can kill all the perverts in the world":
                    pi "I know you're a pervert yourself, human"
                    m "Not to you of course"
                    jump pixieBad


label pixieBad:
    "You offended Pixie"
    scene bg blacked
    stop music
    "Pixie fluttered away..."
    jump neutralBad


label setanta:
    scene bg neutral
    show demon setanta
    menu:
        s "H-hey.... uhm.."
        "Hey Cum Chulainn":
            s "I'm sorry??"
            m "I called you Cum Chulainn, it's your more popular name"
            menu:
                s "W-who?? H-how do you know??"
                "I'm your father":
                    s "INCEST PORN IS GROSS!"
                    s "EWWEY!"
                    jump setantaBad
                "I watch your adult videos":
                    s "Y-you're a fan? So you must like me!"
                    s "Let's shoot an porno together"
                    s "Like..."
                    s "Kiss my shaft!"
                    s "Or..."
                    s "RAWRR I'M A SCARY STEGOSAURUS!!"
                    hide demon setanta
                    show good setanta
                    "Congrats! Your innards romanced Setanta!"
                    return

        "Spill it, boy toy":
            s "I'm n-not really used to this.."
            s "Hey yo, did you know y-you're ...fought for?"
            "*crickets*"
            m "That was goddamn awful bruh"
            s "S-sorry, let me try again.."
            s "You must be a pillow because I want to hug you tight..."
            s "Just like my hands..."
            s "Wrapped around that dog's neck..."
            "Setanta notices your not-so-subtle discomfort"
            s "NO NO PRETEND I DIDN'T SAY THAT!!"
            s "...UGGG I ALWAYS MESS UP!"
            jump setantaBad

label setantaBad:
    s ":'("
    "You made Setanta sad"
    scene bg blacked
    stop music
    "Setanta ran away crying like a pathetic NEET..."
    jump neutralBad

label neutralBad:
    "The other demons roast marshmallow'd your innards"
    "Neutral - Bad End"
    return

label angel:
    scene bg law
    show demon angel
    an "Hey Sugar, what brings you here?"
    m "I want to lick your fingers"
    an "Ahhh so your innards want to romance me!"
    an "If so, what are you going to do with me?"
    an "aside from finger-licking"
    menu:
        "How will you respond?"
        "Spoil you with gifts and treat you nicely like the angel you are":
            an "That's it?"
            jump angelBad
        "I don't do nice. Expect consensual domestic abuse":
            an "Ooooh dangerous, you sound fun"
            menu:
                an "Will butt plugs be involved?"
                "Of course! You'd look sexy with one":
                    an "ANYTHING UP THE BUTT IS A SIN!"
                    an "ESPECIALLY WHEN IT'S NOT A CHURCH PASTOR'S!"
                    an "That being said"
                    an "You lack a pedophile priest's sexpertise"
                    an "CUZ YOU"
                    jump angelBad
                "No":
                    an "Ahhh so you know the Lord's words!"
                    m "Sure"
                    m "Or maybe I just have better, more exciting ideas"
                    an "Ooh? Like what?"
                    m "Like chaining and whipping you in the church basement"
                    m "...only if you consent of course"
                    an "Sexy. I do"
                    an "What are we waiting for?"
                    an "It's a Sunday, and Bible study is in session!"
                    hide demon angel
                    show good angel
                    "Congrats! Your innards romanced Angel!"
                    return


label angelBad:
    an "BORINGGG!"
    scene bg blacked
    stop music
    "Angel left disappointed..."
    jump lawBad

label lawBad:
    "The other demons donated your innards to hungry orphans"
    "Praise YHVH! Law - Bad End"
    return



