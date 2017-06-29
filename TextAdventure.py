
gameOn = True

while gameOn:
    print ("It is the beginning of senior year. The choices that you make this year will significantly impact your future, whether you know it or not")
    print ("Your friend invites you to a party tonight, but keep in mind that you have college applications due in a week and you have not started yet")
    print ("Will you go to the party or will you stay at home? That is a decision you will have to make")
    print ("1. You decide to go to the party ")
    print ("2. You decide to stay home and work on apps ")
    option = int(input("Enter 1 or 2:"))
    if not option:
        exit()

    if option == 1:
        print ("You arrive at the party and are having a blast. An hour into the party you start getting missed calls from your mother ")
        print ("What are you going to do?")
        print ("1. It is senior year; you decide to stay and make new friends ")
        print ("2. You go home and work on apps")
        decision1 = int(input("Enter 1 or 2:"))

        if decision1 == 1:
            print ("It is getting late and you decided it is time to leave. As you make your way to the door, you see your high school crush approach you ")
            print ("What are you going to do?")
            print ("1. You decide he is not worth it and that YOU ARE AN INDEPENDENT WOMAN! SO YOU LEFT")
            print ("2. You stay and hang out with your crush")
            decision2 = int(input("Enter 1 or 2:"))
            if decision2 == 1:
                    print ("Life is great and you end up at a decent college: ")
            if decision2 == 2:
                    print ("10 minutes later your mother shows up to shut down the party ")
        elif decision1 == 2:
                print ("You end up at a decent college")
    elif option == 2:
            print ("You decide to stay home and start on your college applications")
            print ("It has been hours since you started. What are you going to do?")
            print ("1. Stay up for 1 more hour to finish up the apps")
            print ("2. Go to sleep")
            decision3 = int(input("Enter 1 or 2:"))
            if decision3 == 1:
                    print ("You get into a very good college and start a life of your own")
            elif decision3 == 2:
                    print ("You get into a decent college and live life")
    answer = input ("Do you want to play yes/no? ")
    if answer == "yes":
        gameOn = True
    else:
        gameOn = False

print ("Game Over!")
