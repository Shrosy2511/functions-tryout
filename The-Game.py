npcText1 = """
help help is anyone there can someone please help me!

"""
npcText2 = """
aaaagh my leg it hurts! 
you look at the wound and see that the leg is not critically wounded.

"""



lose1 = """
u slowly walk away while the man is crying for help
u walk towards some bushes and get jumped by a pack of wolfs that eat you alive
U LOSE!

"""
lose2 = """
you walk away while the man is crying for u to help him.
you went back home without any remorse to tend your wounds and get some rest.
a few months go by, u hear a knock on the door.
the man that u left to die was rescued and came back for revenge and murders u in cold blood.
U LOSE!
"""
lose3 = """
you run away while the wolf is slaughtering the man.
while u run away u trip and fall over a branch.
u stand back up noticing that the sword penetrated your body u slowly fall to the ground and die
U LOSE!
"""



win1 = """
you rip a piece of cloth from your shirt to cut off the bloodstream so the wounded man doesnt die.
you slowly lift up the wounded man.
after 30 minutes u find a village u ask the villagers for help and they bring the man to the hospital where he gets treated.
after a couple days the man is all healthy again.
the man comes up to you and the man tells he is the king of the village he thanks you and gives u a big reward of 100 gold coins
U WIN! 
"""




text1 = """
ohw thank god that you found me i thought i was going to die
there is a pack of wolfs close by can you please save me from them
my sword is next to that tree quickly grab it before the wolfs come back!

"""
text2 = """
the wolfs appear, they vividly run towards you to attack
one wolf jumps right at you another wolf attacks you from behind
striking your back leaving a bloody claw mark.

"""
text3 = """
the wolfs appear they run at you with murderous intend
one wolf comes from your right and one comes from your left
u dodge the first attack and are ready to punch.

"""
text4 = """
u strike the wolf in front of you u killing it in one big swoop
the wolf in your back engages pushing you on the ground, you're holding him of with your sword
the wolf is trying to bite you in your neck with all your might you push the wolf of of you
the wolf rushes towards the wounded man craving the taste of blood.

"""
text5 = """
u make a spinning slash to the wolf behind of you killing it in one blow
the other wolf trembled with fear and ran away.
u walk up to the man and ask him if everything is alright.

"""
text6 = """
u run towards the wolf as fast as you can to save the wounded man, the wolf is faster and bites the man in his leg
u get to the wolf and stab it right into its heart.

"""



import sys, time, os

for c in npcText1:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

scene1 = input('do you wish to help yes/no ')

if scene1 == 'yes':
    for c in text1:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    scene2 = input('will you grab the sword or fight with your bare hands answer sword/hands ')
else:
    for c in lose1:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

if scene2 == 'sword':
    for c in text2:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    scene3 = input('do you strike the wolf in front of you or behind you answer front/behind ')
    if scene3 == 'front':
        for c in text4:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
        scene4 = input('do you run away or try to save the man run/fight ')
        if scene4 == 'fight':
            for c in text6:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.05)
            scene5 = input('do you bring the man to the nearest village to get him medical help or do you let him die? rescue/abandon ')
            if scene5 == 'rescue':
                for c in win1:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(0.05)
            elif scene5 == 'abandon':
                for c in lose2:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(0.05)                
        elif scene4 == 'run':
            for c in lose3:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.05)

    elif scene3 == 'behind':
        for c in text5:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
elif scene2 == 'hands':
    for c in text3:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    scene5 = input('do you strike the right wolf or the left wolf answer right/left ')