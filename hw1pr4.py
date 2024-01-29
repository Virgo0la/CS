# CHOOSE YOUR OWN ADVENTURE

#  **** An if, elif, and else control structure (with exactly one elif) *****
#  **** An if, elif, elif, ... and else control structure (with at least two elifs) ****
#  **** An if, else control structure (with zero elifs) *****
#  **** An if, elif, ... control structure (with one or more elifs but no trailing else at all) ****
#  **** An if control structure (with no trailing elif nor trailing else at all) ****

# RUlES: You must spell things correctly. If you don't you will trigger the else statement. 

begin = input('would you like to choose your own adventure? (yes/no)')

while begin == "yes": 
    print("You're sitting at home wathcing tv. You hear your stomach growl, so natuarally you head into the kitchen.") 
    print("You check the fridge and there is nothing but ketchup. Despite the time being 2:37 am,")
    print("do you go to the local bodega or eat the bottle of ketchup?")
    a1 = input('walk to bodega or eat ketchup? ')
   
    if a1 == 'bodega':
     print("The walk to the bodega is 5 minutes faster if you chose to go through the dark alley, do you? ")
    else:
     print("you ate the entire bottle of ketchup, including the plastic which cut through your organs as you slept. you're dead. THE END")
     break 
   
    a2 = input("yes or no?" )
    if a2 == "yes":
      print("You walk down the dark alley listening to squeaks of rats, as you begin to see the light on the other side,")
      print("you fall through sewage drain. You land on your back harshly but you don't feel it.")
      print("You go to stand on your feet but you can't move anything below your neck. YOU'RE PARALYZED!")
      print ("You lie on your back for what seems like another lifetime. Suddenly your surrounded by humansized turtles wearing headbands.")
      print("They pick you up and bring you back to their hideout. They give you a headband and ask you to fight alongside them.")
      print("You are now a paralyzed mutant ninja. ")
      break
    else:
      print("It's took longer but your finally make it to the bodega. You scan the isles quickly and settle for a pack of ramen.") 
      print("As the bodega cat rings you up, the local crackhead corners you asking for a dollar. Do you?")
   
    a3 = input('yes or no')
    if a3 == 'yes':
      print('You reach into your pocket and hand over a dollar. They thank you and head out of the shop.')
      print('You take your ramen and make it home. As you eat your subpar snack and cry into the broth wondering where you went wrong in life. THE END ')
      break
    else:
      print('The crackhead sticks you with a needle and runs off. The bodega cat asks you if you are alright but the world begins to melt.') 
      print("Everything is changing colors but the world couldnt be any clearer now.")
      print('You remember why you moved to New York in the first place...to become an actor.')
      print("[FADE TO BLACK] FIVE YEARS LATER...") 
      print('youre up on stage at the oscars hosting. Do you tell a G.I Jane joke?')
      
    a4 = input("yes or no?")
    if a4 == "yes":
     print("You tell the joke which causes Will Smith to come up on stage. Do you run away?")
    else:
      print("The night ends well and you go home to your mansion. You're wealthy and famous and live a long life. THE END")
      break
    a5 = input("yes, no, dodge")
    if a5 == 'yes':
      print("You run off camera and towards backstage. Days later your all over tv and magazines. Several memes have been made about you.")
      print("You'll never be respected in Hollywood again. Loser.")
      break
    elif a5 == 'dodge':
      print("You dodge Will Smiths attack, do you return one or let security remove him from stage.")
    else:
      print("You let Will Smith slap you and the crowd is in shock. You shake it off and continue your poorly scripted oscars set.") 
      print("Luckily the public supports you. You're wealthy and famous and live a long life. THE END. ")
      break
    a6 = input("return or security")
    if a6 == "return":
      print("You strike Will Smith on the stage of the oscars. You are obviously much less famous then him. Security tackles you on stage and turn you over to the police.")
      print("You end up in a cold cell block. You're moved to a federal prison ans spend the rest of your life there. THE END.")
    elif a6 == "security":
      print("Security tackles Will Smith and hauls him off the stage. With all the rukus, you forget your lines.")
      print("Do you make a semi-racist joke, do you make a misogynistic joke, do you make a Rosie o'Donald joke, or do you wrap up your set? ")
    a7 = input("racist, misogynistic, Rosie, or end? ")
    if a7 == "racist":
      print('what were you thinking? You killed your career. Racist.')
      break
    elif a7 == "misogynistic":
      print("You killed you career. Asshole")
      break
    elif a7 == "Rosie":
      print("You killed your career. But Donald Trump offered you a job to be his assistant. You're forced to take it because your blacklisted everywhere.") 
      print("Unfortnatly he framed you for tax evasion, money laundering, racketeering,")
      print("conspiracy to attempt forgery, and several other federal crimes. You die in prison. THE END.")
      break
    else:
      print("You end your set ubruptly. Luckily the public supports you. You're wealthy and famous and live a long life. THE END.  ")
      break 

if begin == "no":
  print('ok')
     