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
    m "Luckily I already aced my Algorithms and Data Structures exams!"
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
    scene unidentified chaos
    "Three unidentifiable Lovecraftian horrors appear before you!"
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
    scene unidentified neutral
    "Three unidentifiable blue blobs appear before you!"
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
    scene unidentified law
    "Three unidentifiable heavenly figures appear before you!"
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
    "Oni ran away in tears..."
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
                    g "BUT LOL IS IT MICROSCOPIC"
                    g "YOU REALLY THINK MASTER MARA WOULD SIT THERE?"
                    g "YOU THINK HE'D EVEN FEEL A BULGE?"
                    m "Maybe like a speck of sand ahehe..."
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
                    m "They'll be so shocked at our gay furry making out shit"
                    g "...Freak"
                    g "...It isn't shit"
                    m "It is gay furry making out tho"
                    g "True dat. I don't mind it"
                    m "So off we go?"
                    g "Free trunkjobs for me, just do it every 5 minutes kay? <3"
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
    m "Wow but okay"
    m "..."
    menu:
        pi "What? Don't just stare!"
        "I hear you can become an Uber Pixie":
            pi "I ALREADY AM UBER PIXIE!"
            pi "You suggesting I don't look like it?"
            m "Don't you all look the same?"
            pi "Lumping me together with those magikarp pixies"
            jump pixieBad
        "Aww you cute I just want to pet you!":
            pi "Yaay thank you!"
            pi "I know"
            pi "I get that a lot"
            pi "*giggle*"
            m "Hey can you cast Megidoloan on this lake?"
            menu:
                pi "Sure but um why?"
                "It's lolz to see you try and fail":
                    pi "Excuse me?"
                    m "Because you never have enough MP!"
                    pi "..."
                    pi "You seem like an honest person"
                    pi "I like that..."
                    m "Yea I'm rich, handsome, and definitely without AIDS"
                    pi "I'm Pixie the Fairy. I'm sure we'll be the best of friends!"
                    hide demon pixie
                    show good pixie
                    "Congrats! Your innards romanced Pixie!"
                    return
                "So we can kill all the perverts in the world":
                    pi "I know you're a pervert yourself, human"
                    m "Yea I'm a huge pervert to everyone"
                    m "Just not to you"
                    jump pixieBad


label pixieBad:
    pi "-_-"
    "You offended Pixie"
    scene bg blacked
    stop music
    "Pixie fluttered away..."
    jump neutralBad


label setanta:
    scene bg neutral
    show demon setanta
    s "H-hey...."
    menu:
        s "uhm.."
        "Hey Cum Chulainn":
            s "I'm sorry??"
            m "I called you Cum Chulainn, it's your more popular name"
            m "...on PornHub heehee"
            menu:
                s "W-what?? H-how do you know??"
                "I'm your father":
                    s "INCEST PORN IS GROSS!"
                    m "No it ain't you lame prude"
                    m "Open your eyes and give Daddy a hickey"
                    s "EWWEY!"
                    jump setantaBad
                "I watch your adult videos":
                    s "Y-you're a fan? So you must like me!"
                    m "Sure totally"
                    s "P-please keep this a secret?"
                    s "My ma'am Scathach would be mad at me if she knew..."
                    m "Nah she already knows"
                    s "Ehh?!"
                    m "I watch your vids with her"
                    s "EHHH!?!"
                    m "Don't worry, she says she's proud of you"
                    s "*blushes*"
                    m "Here's a life stone and some macca"
                    m "Let's PS4 then Netflix and chill okay?"
                    s "*BLUSH INTENSIFIES!*"
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
            m "What the fuck?"
            "Setanta notices your unsubtle discomfort"
            s "W-why you looking at me like that??"
            m "Cuz dogs are man's best friend and all?"
            s "IT'S N-NOT LIKE I WANTED TO"
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
            m "I'll buy you a Nintendo Switch and BotW!"
            jump angelBad
        "I don't do nice. Expect domestic abuse":
            an "Ooooh dangerous, you sound fun"
            menu:
                an "Will butt plugs be involved?"
                "Of course! You'd look sexy with one":
                    an "ANYTHING UP THE BUTT IS A SIN!"
                    an "ESPECIALLY WHEN IT'S NOT A CHURCH PASTOR'S!"
                    m "Girl you a thot"
                    an "You lack a pedophile priest's sexpertise"
                    m "Babe, kids and animals are off limits-"
                    an "CUZ YOU"
                    jump angelBad
                "Hell no":
                    an "Ahhh so you know the Lord's words!"
                    m "Sure"
                    m "Or maybe I want to do something YHVH's into"
                    an "Ooh? Like what?"
                    m "Chain you down and whip you in the church basement"
                    an "Pfft done that"
                    m "Where all the little kiddies can watch"
                    an "Oh~"
                    m "...Just kidding!"
                    m "It's Sunday and Bible study is in place-"
                    an "Even better~"
                    an "Let me show you whan an angel can do <3"
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

label terminator:
    scene bg law
    show demon terminator
    te "..."
    te "Come with me if you want to live"
    menu:
        "How will you respond?"
        "I just want to lick your fingers":
            m "So I'll do anything you ask of me"
            te "..."
            te "We have to get out of the city immediately and avoid the authorities"
            te "I need your clothes, your boots, and your motorcycle"
            menu:
                "How will you respond?"
                "And my innards too?":
                    te "..."
                    te "Chill out, dickwad"
                    m "*sniffs*"
                    te "Why do you cry?"
                    m "For once a demon's not into me just for my innards"
                    te "..."
                    te "Here, hold this"
                    "Terminator hands you a Persona high schooler's innards"
                    m "!!"
                    "There's a ring and love letter underneath!"
                    "The letter reads"
                    "'Let us elope away into the future'"
                    "'We can make beautiful babies then'"
                    "'They'll look likie Jimenez or Demifiend"
                    m "Aww give me your babies!"
                    "Terminator suddenly grabs you and you teleport!"
                    scene bg blacked
                    show demon terminator
                    "..."
                    scene bg law
                    show demon terminator
                    te "Here we are 3 seconds into the future"
                    te "You may lick my sexy fingers now"
                    m "*licks*"
                    "Tastes of sweat and badass"
                    te "Let us commence the baby-making process"
                    hide demon terminator
                    show good terminator
                    "Congrats! Your innards romanced Terminator!"
                    return
                "You forgot to say 'please'":
                    te "Fuck you, asshole"

        "No one would dare attack a church...?":
            te "Wrong!"
            jump terminatorBad

label terminatorBad:
    "*BOOM!*"
    "Terminator shotgun'd your face!"
    "with style of course ;)"
    "Terminator romantically picks out your innards"
    "and throws them out the window"
    scene bg blacked
    stop music
    te "Hasta la vista, baby <3"
    jump lawBad

label lawBad:
    "The other demons donated your innards to hungry orphans"
    "Praise YHVH! Law - Bad End"
    return



