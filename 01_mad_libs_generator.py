print("Welcome in Mad Libs Generator!")
run = True
while(run):
    story = int(input("Choose one story(1-2-3): "))
    print("Now insert the following words")
    print('-------------------------------')
    
    if story == 1:
        animal = input("Please insert a animal name: ")
        profession = input("Please insert a profession name: ")
        cloth = input("Please insert a cloth name: ")
        thing = input("Please insert a thing name: ")
        name = input("Please insert a name: ")
        place = input("Please insert a place name: ")
        verb = input("Please insert a verb: ")
        food = input("Please insert a food name: ")
        print('-------------------------------')
        print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animal + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + thing + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')
        run = False
    elif story == 2:
        adjective = input("Please insert a adjective: ")
        color = input("Please insert a color name: ")
        thing = input("Please insert a thing name: ")
        place = input("Please insert a place name: ")
        person = input("Please insert a person name: ")
        adjective2 = input("Please insert a second adjective: ")
        insect = input("Please insert a insect name: ")
        food = input("Please insert a food name: ")
        verb = input("Please insert a verb: ")
        print('-------------------------------')
        print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjective2+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')
        run = False
    elif story == 3:
        person = input("Please insert a person name: ")
        color = input("Please insert a color name: ")
        foods = input("Please insert a food name: ")
        adjective = input("Please insert a adjective: ")
        thing = input("Please insert a thing name: ")
        place = input("Please insert a place name: ")
        verb = input("Please insert a verb: ")
        adverb = input("Please insert a adverb: ")
        food = input("Please insert a food name: ")
        thing2 = input("Please insert a second thing name: ")
        print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+thing2+' pies!.') 
        run = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
