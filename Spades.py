import random, time, sys

def spadesdrawtable(table, playerscores):
    print('|̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅| player 1 score: '+str(playerscores[0]))
    print('|          '+table[0]+'          | player 2 score: '+str(playerscores[1]))
    print('|                       | player 3 score: '+str(playerscores[2]))
    print('|                       | player 4 score: '+str(playerscores[3]))
    print('|                       |')
    print('| '+table[3]+'              '+table[1]+'  |')
    print('|                       |')
    print('|                       |')
    print('|                       |')
    print('|          '+table[2]+'          |')
    print('|_______________________|')

def spadesplayer1start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores):
    if len(player1hand) == 0:
        endspades(playerscores)
    table = ['   ','   ','   ','   ']
    print("Player 1 Starts")
    playernumber = 1
    spadeschoosestartingcard(player1hand, playernumber, table, spadesbroken)
    spadesdrawtable(table, playerscores)
    player1hand.remove(table[0])
    spltcard = list(table[0])
    startingsuit = spltcard[2]
    time.sleep(2)
    plays = 1
    spadesplayer2turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer2start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores):
    if len(player2hand) == 0:
        endspades(playerscores)
    table = ['   ','   ','   ','   ']
    print("Player 2 Starts")
    playernumber = 2
    spadeschoosestartingcard(player2hand, playernumber, table, spadesbroken)
    spadesdrawtable(table, playerscores)
    player2hand.remove(table[1])
    spltcard = list(table[1])
    startingsuit = spltcard[2]
    time.sleep(2)
    plays = 1
    spadesplayer3turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer3start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores):
    if len(player3hand) == 0:
        endspades(playerscores)
    table = ['   ','   ','   ','   ']
    print('Choose A Card To Lead Off With')
    print('Spades Broken: '+str(spadesbroken))
    print(player3hand)
    done = False
    while True:
        while True:
            startcard = input('>>')
            try:
                startcard = int(startcard) - 1
            except:
                print('A Number Please')
            if startcard in range(0, len(player3hand)):
                pass
            else:
                print('Choose One Of The Cards')
                break
            try:
                del hand
            except:
                pass
            hand = player3hand
            playernumber = 3 - 1
            extractedhand = []
            for y in range(0, len(hand)):
                toadd = list(hand[y])
                extractedhand.append(toadd[0])
                extractedhand.append(toadd[1])
                extractedhand.append(toadd[2])
            possiblehand = []
            possiblesuits = ['♥','♦','♣']
            if spadesbroken == True:
                if '♠' in possiblesuits:
                    pass
                else:
                    possiblesuits.append('♠')
            x = 0
            for z in range(0, len(extractedhand)):
                if extractedhand[x] in possiblesuits:
                    combined = (extractedhand[x-2]+extractedhand[x-1]+extractedhand[x])
                    possiblehand.append(combined)
                x += 1
            if player3hand[startcard] in possiblehand:
                table[2] = str(player3hand[startcard])
                lstcard = list(player3hand[startcard])
                startingsuit = lstcard[2]
                del player3hand[startcard]
                done = True
                break
            else:
                print('That Is An Ileagle Card')
        if done == True:
            break
    spadesdrawtable(table, playerscores)
    spltcard = list(table[2])
    startingsuit = spltcard[2]
    time.sleep(2)
    plays = 1
    spadesplayer4turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer4start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores):
    if len(player4hand) == 0:
        endspades(playerscores)
    table = ['   ','   ','   ','   ']
    print("Player 4 Starts")
    playernumber = 4
    spadeschoosestartingcard(player4hand, playernumber, table, spadesbroken)
    spadesdrawtable(table, playerscores)
    player4hand.remove(table[3])
    spltcard = list(table[3])
    startingsuit = spltcard[2]
    time.sleep(2)
    plays = 1
    spadesplayer1turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer1turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores):
    print("Player 1's Turn")
    playernumber = 1
    spadesreadboard(table[3], player1hand, playernumber, table, startingsuit, spadesbroken)
    spadesdrawtable(table, playerscores)
    player1hand.remove(str(table[0]))
    time.sleep(2)
    if plays == 3:
        spadesdetermine(table, playerscores, spadesbroken, startingsuit, player1hand, player2hand, player3hand, player4hand)
    else:
        plays += 1
        spadesplayer2turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer2turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores):
    print("Player 2's Turn")
    playernumber = 2
    spadesreadboard(table[0], player2hand, playernumber, table, startingsuit, spadesbroken)
    spadesdrawtable(table, playerscores)
    player2hand.remove(str(table[1]))
    time.sleep(2)
    if plays == 3:
        spadesdetermine(table, playerscores, spadesbroken, startingsuit, player1hand, player2hand, player3hand, player4hand)
    else:
        plays += 1
        spadesplayer3turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer3turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores):
    done = False
    print("Player 3's Turn")
    print('Spades Broken: '+str(spadesbroken))
    print('Your Hand:')
    print(player3hand)
    print('Choose Card Based On Placement Number Like The 5th Card Will Be 5')
    Done = False
    while True:
        while True:
            play = input('>>')
            try:
                play = int(play)
                play -= 1
            except:
                print('Please Type A Number')
                break
            if play in range(0,13):
                pass
            else:
                print('A Legal Number Please')
                break
                    
            base = table[1]
            base = list(base)
            follow = startingsuit
            maximum = len(player3hand)
            extractedhand = []
            for y in range(0,(maximum)):
                toadd = list(player3hand[y])
                extractedhand.append(toadd[0])
                extractedhand.append(toadd[1])
                extractedhand.append(toadd[2])
            possiblehand = []
            x = 0
            for z in range(0, (len(extractedhand))):
                if extractedhand[x] == follow:
                    combined = (extractedhand[x-2]+extractedhand[x-1]+extractedhand[x])
                    possiblehand.append(combined)
                x += 1
            if player3hand[play] in possiblehand:
                table[2] = player3hand[play]
                del player3hand[play]
                done = True
                break
            elif len(possiblehand) == 0:
                table[2] = player3hand[play]
                del player3hand[play]
                spadecheck = list(table[2])
                if '♠' in spadecheck:
                    spadesbroken = True
                    print('SPADES BROKEN')
                done = True
                break
            else:
                print('That Card Is Not A Legal Play')
                break
        if done == True:
            break
    spadesdrawtable(table, playerscores)
    time.sleep(2)
    if plays == 3:
        spadesdetermine(table, playerscores, spadesbroken, startingsuit, player1hand, player2hand, player3hand, player4hand)
    else:
        plays += 1
        spadesplayer4turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesplayer4turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores):
    print("Player 4's Turn")
    playernumber = 4
    spadesreadboard(table[2], player4hand, playernumber, table, startingsuit, spadesbroken)
    spadesdrawtable(table, playerscores)
    player4hand.remove(str(table[3]))
    time.sleep(2)
    if plays == 3:
        spadesdetermine(table, playerscores, spadesbroken, startingsuit, player1hand, player2hand, player3hand, player4hand)
    else:
        plays += 1
        spadesplayer1turn(player1hand, player2hand, player3hand, player4hand, table, plays, startingsuit, spadesbroken, playerscores)

def spadesreadboard(str1, str2, str3, table, startingsuit, spadesbroken):
    try:
        del follow
    except:
        pass
    try:
        del hand
        del base
        del possibase
    except:
        pass
    playernumber = str3 - 1           
    possibase = []
    for y in range(0, len(table)):
        listedtable = list(table[y])
        if listedtable[2] == startingsuit:
            if listedtable[1] == 'J':
                listedtable[0] = '1'
                listedtable[1] = '1'
            elif listedtable[1] == 'Q':
                listedtable[0] = '1'
                listedtable[1] = '2'
            elif listedtable[1] == 'K':
                listedtable[0] = '1'
                listedtable[1] = '3'
            elif listedtable[1] == 'A':
                listedtable[0] = '1'
                listedtable[1] = '4'
            combined = (listedtable[0]+listedtable[1]+listedtable[2])
            possibase.append(combined)
    hand = str2
    highbase = list(max(possibase))
    allgood = True
    for x in range(0, len(table)):
        listedtable = list(table[x])
        if listedtable[2] == '♠':
            allgood = False
    if allgood == True:
        prevnumber = int(highbase[0]+highbase[1])
    else:
        prevnumber = 15
    follow = highbase[2]
    maximum = len(hand)
    extractedhand = []
    for y in range(0,(maximum)):
        toadd = list(hand[y])
        extractedhand.append(toadd[0])
        extractedhand.append(toadd[1])
        extractedhand.append(toadd[2])
    possiblehand = []
    x = 0
    for z in range(0, (len(extractedhand))):
        if extractedhand[x] == follow:
            combined = (extractedhand[x-2]+extractedhand[x-1]+extractedhand[x])
            possiblehand.append(combined)
        x += 1
    if len(possiblehand) != 0:
        possiblebrokendown = []
        for xy in range(0, len(possiblehand)):
            tobeadded = list(possiblehand[xy])
            possiblebrokendown.append(tobeadded[0])
            possiblebrokendown.append(tobeadded[1])
            possiblebrokendown.append(tobeadded[2])
        x = 0
        tocombine = []
        possiblenumbers = []
        for yz in range(0, len(possiblebrokendown)):
            if (yz+1)%3==0:
                pass
            else:
                if x == 0:
                    tocombine.append(possiblebrokendown[yz])
                    x = 1
                elif x == 1:
                    tocombine.append(possiblebrokendown[yz])
                    if tocombine[1] == 'J':
                        tocombine[1] = '1'
                        tocombine[0] = '1'
                    elif tocombine[1] == 'Q':
                        tocombine[1] = '2'
                        tocombine[0] = '1'
                    elif tocombine[1] == 'K':
                        tocombine[1] = '3'
                        tocombine[0] = '1' 
                    elif tocombine[1] == 'A':
                        tocombine[1] = '4'
                        tocombine[0] = '1'
                    possiblenumbers.append(int(tocombine[0]+tocombine[1]))
                    tocombine = []
                    x = 0
        bigger = False
        for xyz in range(0, len(possiblenumbers)):
            if possiblenumbers[xyz] > prevnumber:
                bigger = True
        if bigger == True:
            table[playernumber] = max(possiblehand)
        elif bigger != True:
            table[playernumber] = min(possiblehand)
    else:
        spadeshand = []
        for zy in range(0, (len(extractedhand))):
            if extractedhand[zy] == '♠':
                combined = (extractedhand[zy-2]+extractedhand[zy-1]+extractedhand[zy])
                spadeshand.append(combined)
        if len(spadeshand) != 0:
            table[playernumber] = min(spadeshand)
            if spadesbroken == False:
                print('SPADES BROKEN')
                spadesbroken = True
        else:
            table[playernumber] = min(hand)

def spadeschoosestartingcard(str1, str2, table, spadesbroken):
    try:
        del hand
    except:
        pass
    hand = str1
    playernumber = str2 - 1
    extractedhand = []
    for y in range(0, len(hand)):
        toadd = list(hand[y])
        extractedhand.append(toadd[0])
        extractedhand.append(toadd[1])
        extractedhand.append(toadd[2])
    possiblehand = []
    possiblesuits = ['♥','♦','♣']
    if spadesbroken == True:
        if '♠' in possiblesuits:
            pass
        else:
            possiblesuits.append('♠')
    x = 0
    for z in range(0, len(extractedhand)):
        if extractedhand[x] in possiblesuits:
            combined = (extractedhand[x-2]+extractedhand[x-1]+extractedhand[x])
            possiblehand.append(combined)
        x += 1
    cardtoplay = random.randint(0, (len(possiblehand)-1))
    table[playernumber] = str(possiblehand[cardtoplay])
    splitcard = list(possiblehand[cardtoplay])
    startingsuit = splitcard[2]

def spadesdetermine(table, playerscores, spadesbroken, startingsuit, player1hand, player2hand, player3hand, player4hand):
    suits = ['♥','♦','♣','♠']
    extractedtable = []
    for x in range(0, len(table)):
        templist = list(table[x])
        extractedtable.append(templist[0])
        extractedtable.append(templist[1])
        extractedtable.append(templist[2])
        extractedtable.append(x+1)
    strongercards1 = []
    for x in range(0, len(extractedtable)):
        if extractedtable[x] == '♠':
            combined = (extractedtable[x-2]+extractedtable[x-1]+extractedtable[x])
            strongercards1.append(combined)
            strongercards1.append(extractedtable[x+1])
    for y in range(0, len(extractedtable)):
        if extractedtable[y] == 'A':
            extractedtable[y-1] = '1'
            extractedtable[y] = '4'
        elif extractedtable[y] == 'J':
            extractedtable[y-1] = '1'
            extractedtable[y] = '1'
        elif extractedtable[y] == 'Q':
            extractedtable[y-1] = '1'
            extractedtable[y] = '2'
        elif extractedtable[y] == 'K':
            extractedtable[y-1] = '1'
            extractedtable[y] = '3'
        if extractedtable[y] in suits and extractedtable[y] != startingsuit:
            extractedtable[y-1] = '0'
            extractedtable[y-2] = '0'
    if len(strongercards1) == 0:
        suits = ['♥','♦','♣','♠']
        reconstruct = []
        for y in range(0, len(extractedtable)):
            if extractedtable[y] in suits:
                combined = (extractedtable[y-2]+extractedtable[y-1]+extractedtable[y])
                reconstruct.append(combined)
        if reconstruct[0] == max(reconstruct):
            print('The Winner Of This Round Is Player 1')
            table = ['   ','   ','   ','   ']
            playerscores[0] = playerscores[0] + 1
            spadesplayer1start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
        elif reconstruct[1] == max(reconstruct):
            print('The Winner Of This Round Is Player 2')
            table = ['   ','   ','   ','   ']
            playerscores[1] = playerscores[1] + 1
            spadesplayer2start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
        elif reconstruct[2] == max(reconstruct):
            print('The Winner Of This Round Is Player 3')
            table = ['   ','   ','   ','   ']
            playerscores[2] = playerscores[2] + 1
            spadesplayer3start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
        elif reconstruct[3] == max(reconstruct):
            print('The Winner Of This Round Is Player 4')
            table = ['   ','   ','   ','   ']
            playerscores[3] = playerscores[3] + 1
            spadesplayer4start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
    else:
        playernumbers = []
        strongercards = []
        for y in range(0, len(strongercards1)):
            if y%2 != 0:
                playernumbers.append(strongercards1[y])
            else:
                strongercards.append(strongercards1[y])
        strongercardssaved = strongercards
        extractedcardssaved = []
        rebuild = []
        for y in range(0, len(strongercardssaved)):
            lengthoflist = list(strongercardssaved[y])
            extractedcardssaved.append(lengthoflist[0])
            extractedcardssaved.append(lengthoflist[1])
            extractedcardssaved.append(lengthoflist[2])
        for y in range(0, len(extractedcardssaved)):
            if extractedcardssaved[y] == 'A':
                extractedcardssaved[y-1] = '1'
                extractedcardssaved[y] = '4'
            elif extractedcardssaved[y] == 'J':
                extractedcardssaved[y-1] = '1'
                extractedcardssaved[y] = '1'
            elif extractedcardssaved[y] == 'Q':
                extractedcardssaved[y-1] = '1'
                extractedcardssaved[y] = '2'
            elif extractedcardssaved[y] == 'K':
                extractedcardssaved[y-1] = '1'
                extractedcardssaved[y] = '3'
        countnum = len(strongercardssaved)
        while countnum != 0:
            combined = (extractedcardssaved[0]+extractedcardssaved[1]+extractedcardssaved[2])
            rebuild.append(combined)
            del extractedcardssaved[2]
            del extractedcardssaved[1]
            del extractedcardssaved[0]
            countnum -= 1
        strongercards = rebuild
        for y in range(0, len(strongercards)):
            if strongercards[y] == max(strongercards):
                winner = playernumbers[y]
                if winner == 1:
                    print('The Winner Of This Round Is Player 1')
                    table = ['   ','   ','   ','   ']
                    playerscores[0] += 1
                    spadesbroken = True
                    spadesplayer1start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
                if winner == 2:
                    print('The Winner Of This Round Is Player 2')
                    table = ['   ','   ','   ','   ']
                    playerscores[1] += 1
                    spadesbroken = True
                    spadesplayer2start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
                if winner == 3:
                    print('The Winner Of This Round Is Player 3')
                    table = ['   ','   ','   ','   ']
                    playerscores[2] += 1
                    spadesbroken = True
                    spadesplayer3start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
                if winner == 4:
                    print('The Winner Of This Round Is Player 4')
                    table = ['   ','   ','   ','   ']
                    playerscores[3] += 1
                    spadesbroken = True
                    spadesplayer4start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)

def endspades(playerscores):
    teamscores = [(playerscores[0]+playerscores[2]),(playerscores[1]+playerscores[3])]
    print('END OF MATCH')
    print('Player 1 And 3: '+str(playerscores[0]+playerscores[2]))
    print('Player 2 And 4: '+str(playerscores[1]+playerscores[3]))
    if teamscores[0] == max(teamscores):
        print('The Winners Are Player 1 And 3')
        sys.exit()
    if teamscores[1] == max(teamscores):
        print('The Winners Are Player 2 And 4')
        sys.exit()

def spadesstart():
    while True:
        while True:
            while True:
                goodtogo = False
                allgood = [False, False, False, False]
                spadesbroken = False
                playerscores = [0,0,0,0]
                table = ['   ','   ','   ','   ']
                cards = [' A♥',' 2♥',' 3♥',' 4♥',' 5♥',' 6♥',' 7♥',' 8♥',' 9♥','10♥',' J♥',' Q♥',' K♥',' A♦',' 2♦',' 3♦',' 4♦',' 5♦',' 6♦',' 7♦',' 8♦',' 9♦','10♦',' J♦',' Q♦',' K♦',' A♠',' 2♠',' 3♠',' 4♠',' 5♠',' 6♠',' 7♠',' 8♠',' 9♠','10♠',' J♠',' Q♠',' K♠',' A♣',' 2♣',' 3♣',' 4♣',' 5♣',' 6♣',' 7♣',' 8♣',' 9♣','10♣',' J♣',' Q♣',' K♣']
                player1hand = []
                player2hand = []
                player3hand = []
                player4hand = []
                x = 0
                while x != 13:
                    cardtodeal = random.randint(0, (len(cards)-1))
                    selected = cards[cardtodeal]
                    player1hand.append(selected)
                    del cards[cardtodeal]
                    cardtodeal = random.randint(0, (len(cards)-1))
                    selected = cards[cardtodeal]
                    player2hand.append(selected)
                    del cards[cardtodeal]
                    cardtodeal = random.randint(0, (len(cards)-1))
                    selected = cards[cardtodeal]
                    player3hand.append(selected)
                    del cards[cardtodeal]
                    cardtodeal = random.randint(0, (len(cards)-1))
                    selected = cards[cardtodeal]
                    player4hand.append(selected)
                    del cards[cardtodeal]
                    x += 1
                for x in range(0, len(player1hand)):
                    if '♠' in player1hand[x]:
                        allgood[0] = True
                for x in range(0, len(player2hand)):
                    if '♠' in player2hand[x]:
                        allgood[1] = True
                for x in range(0, len(player3hand)):
                    if '♠' in player3hand[x]:
                        allgood[2] = True
                for x in range(0, len(player4hand)):
                    if '♠' in player4hand[x]:
                        allgood[3] = True
                if False in allgood:
                    break
                else:
                    goodtogo = True
                    break
            if goodtogo == True:
                break
        if goodtogo == True:
            break
    spadesplayer1start(player1hand, player2hand, player3hand, player4hand, table, spadesbroken, playerscores)
spadesstart()
