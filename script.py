import datetime

date = datetime.datetime.now()

hour = date.hour ,date.minute

if hour <= (9,45) :
    
    print ("Ce n'est pas encore la pause")

if hour >= (9,46) :

    if hour <= (10,14) :
        
        print ("C'est bientôt la pause")

if hour >= (10,15) :

    if hour <= (10,29) :

        print("C'est LA PAUSEEE")

if hour >= (10,30) :

    print("La pause est fini")