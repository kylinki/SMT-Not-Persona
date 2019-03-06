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
    m "How To Be A Decent Human Being 101"

    menu:
        m "Guess I'm gonna..."
        "try my best!":
            jump notChaos
        "ditch it. What a stupid, useless class":
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
    m "Let's see, first question..."

    if persistent.aliceGood and persistent.angelGood and persistent.girimekhalaGood and persistent.mohShuvuuGood and persistent.oniGood and persistent.pixieGood and persistent.setantaGood and persistent.terminatorGood and persistent.titaniaGood:

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

            "r/Megaten. I love cumming on Demifiend figurines":
                stop music
                scene bg blacked
                "You blacked out!"
                jump law

            "Zone out":
                m "...wish I was home browsing r/CummingOnFigurines now mhmm"
                "Professor-senpai tapped your shoulder!"
                p "We need to talk"
                "Professor-senpai suddenly grabs you!"
                stop music
                scene bg blacked
                "and you teleport!!"
                jump trueEnd

    else:
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

            "r/Megaten. I love cumming on Demifiend figurines":
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
    "Three unidentifiable heavenly beings appear before you!"
    "They all emit a peaceful aura"
    m "Holy moly, I want to lick their fingers and praise YHVH"

    menu:
        "Which one will you approach?"
        "left heavenly being":
            jump angel
        "middle heavenly being":
            jump terminator
        "right heavenly being":
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
            o "NYAA~"
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
                    $ persistent.oniGood = True
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
                    g "Jelly"
                    g "I wish mine could Agidyne mice and hamsters"
                    g "Just think of all the delicious hamster kebobs I'd eat!"
                    g "Cuz fuck rats"
                    m "..."
                    "Better change topic quick before Giri realizes you're bullshitting"
                    m "*blush*"
                    g "...What's up? Something on your mind?"
                    m "Hmm uhhhh"
                    m "I'd like to kiss you"
                    g "!!-"
                    m "And give you a trunkjob"
                    g "...Freak"
                    g "You into gay furry shit"
                    m "Damn right I am"
                    g "Kay just checking"
                    m "I just want to be your personal sex slave bruh"
                    g "!!!!"
                    "Giri's trunk went stiff!"
                    g "Those were the most beautiful words I've ever heard!"
                    m "Damn right Daddy Dumbo"
                    "And that's how Dumbo sequel got made"
                    "Featuring Dante from the Devil May Cry Series"
                    hide demon girimekhala
                    show good girimekhala
                    "Congrats! Your innards romanced Girimekhala!"
                    $ persistent.girimekhalaGood = True
                    return

label giriBad:
    g "*snort* *pawoo*"
    "You made Girimekhala laugh"
    scene bg blacked
    stop music
    "Girimekhala strolled away..."
    jump chaosBad

label alice:
    scene bg chaos
    show demon alice
    al "*giggle*"
    al "You want to play with me?"
    menu:
        "How will you respond?"
        "Like play SMT Nocturne?":
            al "You clearly know what I mean :'("
            m "No lil girl don't cry!"
            al "Waaaaaaah!!! :'("
            m "LIL GIRL"
            m "...YOU MAY SLICE ME UP!"
            al "*giggle* That's better"
            al "I wasn't actually crying silly ;)"
            al "But it's only fun when humans beg for their lives"
            menu:
                "How will you respond?"
                "I am no fun":
                    al "True you aren't"
                    m  "...horse bollocks"
                    al "Oh I know what'd be fun!~"
                    al "Let's exit Lucifer's asshole"
                    al "And make use of our second amendment rights~! <3"
                    m "What-"
                    al "We'll shoot up all the Persona 4 and 5 characters"
                    al "It'll be so wicked fun yaay~"
                    m "You a crazy, psycho loli"
                    menu:
                        "What will you do?"
                        "Stop her and save everyone":
                            al "HAHAHAHAHA!"
                            al "You adorable human~"
                            jump aliceBad
                        "I'll just watch you, like mukbang":
                            al "Fine by me"
                            al "*light giggle*"
                            al "AHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAAHA\
                            AHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAAHA\
                            AHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAAHA\
                            AHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHAHA!!!!!!!<3"
                            m "Sure"
                            m "Uhhh just do meth instead"
                            hide demon alice
                            show good alice
                            "Congrats! Your innards romanced Alice!"
                            $ persistent.aliceGood = True
                            return

                "...Please don't kill me?":
                    al "Yaaay! Just like that~!"
                    jump aliceBad

        "Short, little girls are sooooo cute!":
            m "Only in the teddy bear kinda way of course"
            al "I'm not your fucking teddy bear"
            al "You're ugly and look like an incel"
            jump aliceBad

label aliceBad:
    al "Die for me!"
    scene bg blacked
    stop music
    "Alice knifed you to shreds..."
    jump chaosBad

label chaosBad:
    "The other demons skull fucked and blood orgy'd your innards"
    "One more noob rejected! Chaos - Bad End"
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
            m "Talk about overconfidence"
            m "You're the friggin SMT equivalent of caterpie"
            pi "W-what!?"
            m "Then..."
            m "Can you cast Megidoloan on this lake?"
            menu:
                pi "Sure but um why?"
                "It's lolz to see you try and fail":
                    pi "Excuse me?"
                    m "Because you never have enough MP!"
                    pi "..."
                    pi "You seem like an honest person"
                    pi "I like that..."
                    m "Yea I'm rich, handsome, and definitely without AIDS"
                    pi "I'm Pixie the Fairy. I'm sure we'll be the best of friends-"
                    m "Yadi yada whatever"
                    m "Waifu fusion fodder"
                    pi "-_-"
                    hide demon pixie
                    show good pixie
                    "Congrats! Your innards romanced Pixie!"
                    $ persistent.pixieGood = True
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

label titania:
    scene bg neutral
    show demon titania
    ti "La la la.. La la..."
    ti "How truly beautiful am I, queen of the fairies?"
    ti "It's such a great honor to be queen that it almost brings me to tears..."
    ti "...Hey you!"
    m "M-me?"
    menu:
        ti "Are you ready?"
        "I am damn ready":
            m "For Persona 5 port on Switch!"
            "Titania gave a disgusted look"
            "The mood is awkward..."
            ti "More like Persona 5 Time to Stop"
            m "..."
            jump titaniaBad

        "My body is ready!":
            ti "Fantastisch!"
            "Titania lifts up her skirt to reveal something HUGE"
            ti "You can do wonders with fairy magic, you know? ;)"
            m "*gulp*"
            menu:
                ti "May I test it on you?"
                "Hell no":
                    ti "That is too bad"
                    ti "I'll just use Jack Frost instead"
                    m "...Can I watch"
                    jump titaniaBad
                "I just want to find some opposite gender's bathrooms":
                    m "Then you may get freaky with me there"
                    ti "There are none. This lake is the only bathroom for all"
                    m "Well shite"
                    ti "You may peeping tom all you'd like, we demons don't care"
                    m ":D"
                    ti "But first, let's get freaky"
                    m "Excite...I'm so depraved"
                    ti "I'm gonna ram my Sugar Key so far up your ass...La la..."
                    scene bg blacked
                    "Hours later..."
                    "(Demons are different from humans, ya know?)"
                    scene bg neutral
                    show demon titania
                    ti "Thank you, used cloth. I've filled you up with 2 years worth"
                    m "My lady, your Sugar Key is beyond out of this world!"
                    ti "Thank you, not even Oberon can take it"
                    ti "...Hmm"
                    ti "I think I'll just leave him for you instead"
                    ti "You're my used cloth bitch now"
                    m "Funnnn"
                    hide demon titania
                    show good titania
                    "Congrats! Your innards romanced Titania!"
                    $ persistent.titaniaGood = True
                    return

label titaniaBad:
    ti "Pfft"
    ti "Looks like our tea time is up"
    ti "I must return before my husband realizes I'm cheating"
    scene bg blacked
    stop music
    "Titania twirled away..."
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
                    m "Don't worry, she's proud of what she taught you"
                    s "*blushes*"
                    m "Here's a life stone and some macca"
                    m "T-thanks-"
                    m "and a SMT V release date"
                    s "*BLUSH INTENSIFIES!*"
                    m "OF NEVER!"
                    hide demon setanta
                    show good setanta
                    "Congrats! Your innards romanced Setanta!"
                    $ persistent.setantaGood = True
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
    "Your innards cut its own throat! Neutral - Bad End"
    return

label angel:
    scene bg law
    show demon angel
    an "Hey Sugar, what brings you here?"
    m "I want to lick your fingers"
    an "Ahhh so your innards want to romance me!"
    an "If so, what are you going to do with me?"
    menu:
        "How will you respond?"
        "Spoil you with gifts and treats like the angel you are":
            an "That's it?"
            m "I'll buy you a Nintendo Switch"
            an "*yawn*"
            m "and Breath of the Wild?"
            jump angelBad
        "I don't do nice. Expect domestic abuse":
            an "Ooooh dangerous, you sound fun"
            menu:
                an "Will butt plugs be involved?"
                "Of course! You'd look sexy with one":
                    an "ANYTHING UP THE BUTT IS A SIN!"
                    an "ESPECIALLY WHEN IT'S NOT A CHURCH PASTOR'S!"
                    m "Girl you a thot"
                    an "You lack a pedo priest's sexpertise"
                    m "Babe, I don't do kids or animals-"
                    an "CUZ YOU"
                    jump angelBad
                "Hell no":
                    an "Ahhh so you know the Lord's words!"
                    m "Sure"
                    m "Or maybe I want to do something YHVH would watch"
                    an "Ooh? Like what?"
                    m "Chain you down and whip you in the church basement"
                    an "Pfft done that"
                    m "Where all the little kiddies can watch"
                    an "Oh~"
                    m "...Just kidding!"
                    m "It's Sunday and Bible study is in place-"
                    an "Even better~"
                    m "W-What"
                    an "Let me show you whan an angel can do <3"
                    hide demon angel
                    show good angel
                    "Congrats! Your innards romanced Angel!"
                    $ persistent.angelGood = True
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
                    "Terminator hands you a Persona 4 high schooler's innards"
                    m "!!"
                    "There's a ring and love letter underneath!"
                    "The letter reads"
                    "'Let us elope away into the future'"
                    "'We can make beautiful babies then'"
                    "'They'll look like Jimenez or Demifiend'"
                    m "Aww give me your babies!"
                    "Terminator suddenly grabs you and you teleport!"
                    scene bg blacked
                    show demon terminator
                    "..."
                    "What feels like an eternity eventually passes..."
                    scene bg law
                    show demon terminator
                    te "Here we are"
                    te "0.5 seconds into the future"
                    te "You may lick my sexy fingers now"
                    m "*licks*"
                    "Tastes of sweat and badass"
                    te "Let us commence the baby-making process"
                    hide demon terminator
                    show good terminator
                    "Congrats! Your innards romanced Terminator!"
                    $ persistent.terminatorGood = True
                    return
                "You forgot to say 'please'":
                    te "Fuck you, asshole"

        "No one would dare attack a church...?":
            te "Wrong!"
            jump terminatorBad

label terminatorBad:
    "*BOOM!*"
    "Terminator shotgun'd your face!"
    "with Smokin' Sexy Style!! ;)"
    "Terminator romantically picks out your innards"
    "and throws them out the window"
    scene bg blacked
    stop music
    te "Hasta la vista, baby <3"
    jump lawBad

label mohShuvuu:
    scene bg law
    show demon mohshuvuu
    mo "Hey there~ <3"
    "You feel uncomfortable, this is a lil girl"
    mo "Oh no need to be shy, I'm actually hundreds of years old~ <3"
    m "*glances around*"
    mo "And YHVH wouldn't have police up his nostrils"
    mo "*giggle*"
    menu:
        mo "What does love mean for you?"
        "Cuddling and spooning":
            mo "Yaaay same for me!"
            m "Let's try that out, can we? :D"
            mo "Kill two birds with one stone ;)"
            "Moh Shuvuu put her arms around you"
            mo "I'll be big spoon~ <3"
            jump mohBad
        "Lol I wouldn't know":
            mo "Of course, who'd date your lame innards ass-?"
            m "Love can't be described"
            mo "What?"
            m "Some people like to eat ass, that's love"
            m "Others like to gangbang at funerals, that's also love"
            "Moh Shuvuu gives you a disgusted look"
            mo "No wonder why YHVH abandoned you filthy humans"
            m "But it's the feeling! The deep interpersonal connections you get!"
            mo "Sounds gross and stupid but prove me wrong"
            menu:
                "What will you do?"
                "Give her your PS2":
                    mo "Dafuq is this"
                    m "It's called a PlayStation 2"
                    m "Cool people play games like Nocturne or Digital Devil Saga on it"
                    mo "Sure..."
                    m "Others also play Devil Summoner Raidou Kuzunoha on it"
                    mo "Kuzunoha...Raidou..?"
                    "You hand her over a copy of Raidou"
                    mo "He looks so...cool and dreamy"
                    mo "Just looking at him...makes me feel..."
                    mo "Warm inside...like hot coco"
                    m "Little bird chick, he's like your husbando"
                    m "There's no Platinum Games remake of it...yet"
                    m "But I hope you enjoy it anyway! *gentlemanly bows*"
                    mo "Awww I love it! Thank you so much mister! <3"
                    mo "*gives you a hug*"
                    m ":D"
                    mo "I can't wait to draw Raidou X Demifiend yaoi"
                    m "...fujoshi chick"
                    mo "with you DP'd! <3"
                    hide demon mohshuvuu
                    show good mohshuvuu
                    "Congrats! Your innards romanced Moh Shuvuu!"
                    $ persistent.mohShuvuuGood = True
                    return

                "Give her your PS4":
                    mo "Dafuq am I supposed to do with this?"
                    m "Umm play Fortnite and Persona 5?"
                    jump mohBad


label mohBad:
    "*CRACK!*"
    "Moh Shuvuu cracked your skull!"
    "*SLURP!*"
    "Moh Shuvuu sucked your brain out!"
    mo "Mhmm tasty-"
    mo "*coughs* *gags*"
    mo "Dafuq is this!?!"
    mo '*COUGHS!* *GAGS!* *SEIZURES!*'
    "Your brain tumor food poisoned Moh Shuvuu..."
    scene bg blacked
    stop music
    "Moh Shuvuu immediately got sent to loli hospital..."
    jump lawBad

label lawBad:
    "The other demons donated your innards to hungry orphans"
    "Praise YHVH! Law - Bad End"
    return

label trueEnd:
    scene bg true
    m "...This ain't school"
    m "Where am I?"
    "Professor-senpai stands before you"
    p "As you can perhaps tell, I am no human"
    m "*shivers*"
    m "Brrr is it cold here"
    p "Now I shall reveal to you my true form..."
    show demon jackfrost
    m "My love!!"
    play music "love.mp3"
    j "All the demons your innards romanced, along with YHVH and Lucifer..."
    j "I am special fused from that love, Ho!"
    m "*blush* Jack called me a ho~ *feels good*"
    j "Hee ho! I am Jack Frost Almighty!"
    j "All bends to my will!"
    hide demon jackfrost
    show good jackfrost
    m "Jack..."
    m "You are the sexiest motherfucker demon my innards have ever laid eyes on"
    j "Your mother, yep. Father too"
    m "...Is there a figurine of you? *indecent thoughts*"
    j "No, Ho!"
    m "Well shite"
    j "Worry not, Ho!"
    j "I got something better for you!"
    "Jack Frost Almighty is transforming!-"
    hide good jackfrost
    show true
    m "!!-"
    j "Hee Ho!"
    "Congrats! Your innards got SMT V!"
    m ":D :D :D :D :D :D"
    "You haven't realized yet you left your Switch at home"
    "TRUE END! <3"
    return
