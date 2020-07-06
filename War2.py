import random, time, os, sys

def war2drawtable(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements):
    print('|̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅|')
    print('|  '+lives[0]+'   ['+str(len(enemybackup[0]))+']   '+lives[1]+'   ['+str(len(enemybackup[1]))+']   '+lives[2]+'  |')
    print('|                               |')
    print('|  '+enemystacks[0][0]+'   '+enemystacks[1][0]+'   '+enemystacks[2][0]+'   '+enemystacks[3][0]+'   '+enemystacks[4][0]+'  |')
    print('|  ['+str(len(enemystacks[0])-1)+']   ['+str(len(enemystacks[1])-1)+']   ['+str(len(enemystacks[2])-1)+']   ['+str(len(enemystacks[3])-1)+']   ['+str(len(enemystacks[4])-1)+']  |')
    print('|                               |')
    print('|                               |')
    print('|  '+replacements[2]+'                     '+replacements[3]+'  |')
    print('|                               |')
    print('|                               |')
    print('|  ['+str(len(playerstacks[0])-1)+']   ['+str(len(playerstacks[1])-1)+']   ['+str(len(playerstacks[2])-1)+']   ['+str(len(playerstacks[3])-1)+']   ['+str(len(playerstacks[4])-1)+']  |')
    print('|  '+playerstacks[0][0]+'   '+playerstacks[1][0]+'   '+playerstacks[2][0]+'   '+playerstacks[3][0]+'   '+playerstacks[4][0]+'  |')
    print('|                               |')
    print('|  '+lives[3]+'   ['+str(len(playerbackup[0]))+']   '+lives[4]+'   ['+str(len(playerbackup[1]))+']   '+lives[5]+'  |')
    print('|_______________________________|')

def playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced):
    if playerstamina == 0:
        print('\nENEMY TURN\n')
        time.sleep(0.5)
        enemystamina = 3
        enemyturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    war2drawtable(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements)
    print('\nChoose A Move')
    print('\n1. Attack')
    if replaced == False:
        print('2. Replace A Card\n')
    else:
        print('\n')
    while True:
        while True:
            x = input('>>')
            try:
                x = int(x)
            except:
                print('A Number Only')
                break
            if x == 1:
                playerstamina -= 1
                playerattack(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
            elif (replaced == False) and (x == 2):
                replaced = True
                playerstamina -= 1
                playerreplace(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
            else:
                if replaced:
                    print('1 Only')
                else:
                    print('Either 1 or 2')
                break

def playerreplace(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced):
    print('Select One Of Your Warriors To Replace')
    print('(By The Placement Number)')
    warlist = []
    for x in range(0,5):
        warlist.append(playerstacks[x][0])
    warlist = (warlist[0]+' '+warlist[1]+' '+warlist[2]+' '+warlist[3]+' '+warlist[4])
    print('Warriors -> '+warlist+'\n')
    while True:
        done = False
        while True:
            x = input('>>')
            try:
                x = int(x)
            except:
                print('A Number Only')
                break
            if (x > 5) or (x < 1):
                print('Only A Number From 1 To 5')
                break
            else:
                sel = x-1
                done = True
                break
        if done:
            break
    if replacements[2] == replacements[3] == '[@]':
        print('Which Replacement Card?')
        print('1. Left')
        print('2. Right\n')
        while True:
            done = False
            x = input('>>')
            try:
                x = int(x)
                if x in range(1,3):
                    done = True
                    break
                else:
                    print('A Number Only')
                    pass
            except:
                print('A Number Only')
                pass
        if done == True:
            x = str(x)
            if True:
                if int(x) == 1:
                    replacements[2] = '   '
                    playerstacks[sel][0] = replacements[0]
                    print('Replacing...')
                    time.sleep(0.5)
                    playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
                elif int(x) == 2:
                    replacements[3] = '   '
                    playerstacks[sel][0] = replacements[1]
                    print('Replacing...')
                    time.sleep(0.5)
                    playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    elif replacements[2] != '   ':
        print('Taking Left Replacement Card')
        time.sleep(0.5)
        replacements[2] = '   '
        playerstacks[sel][0] = replacements[0]
        print('Replacing...')
        time.sleep(0.5)
        playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    elif replacements[3] != '   ':
        print('Taking Right Replacement Card')
        time.sleep(0.5)
        replacements[3] = '   '
        playerstacks[sel][0] = replacements[1]
        print('Replacing...')
        time.sleep(0.5)
        playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)

def playerattack(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced):
    print('\nChoos Your Target...')
    while True:
        cont = False
        while True:
            x = input('>>')
            try:
                x = int(x)
            except:
                print('A Number Only')
                break
            if x in range(1,6):
                print('Attacking Enemy '+str(x))
                cont = True
                target = x-1
                break
            else:
                print('One Of The Options')
                break
        if cont:
            break
    print('Rolling Dice...')
    time.sleep(2)
    dices = ['[1]','[2]','[3]','[4]','[5]','[6]']
    x1 = random.choice(dices)
    x2 = random.choice(dices)
    print('You Rolled -> '+x1,x2)
    time.sleep(1)
    total = int(x1[1])+int(x2[1])
    clone = enemystacks[target][0]
    warriors = ['1','2','3','4','5','6','7','8','9']
    letters = ['K','Q','J']
    if clone[1] in warriors:
        if total >= int(clone[1]):
            print('Beat It!!')
            del enemystacks[target][0]
            time.sleep(0.5)
        else:
            print('Attack Failed!')
            time.sleep(0.5)
    elif clone[0] + clone[1] == '10':
        if total >= 10:
            print('Beat It!!')
            del enemystacks[target][0]
            time.sleep(0.5)
        else:
            print('Attack Failed!')
            time.sleep(0.5)
    elif clone[1] == 'A':
        if x1 == x2:
            print('Beat It!!')
            del enemystacks[target][0]
            time.sleep(0.5)
        else:
            print('Atack Failed!')
            time.sleep(0.5)
    elif clone[1] in letters:
        if x1 == x2:
            print('You Took One Of The Enemies Lives!!!!')
            enemystacks[target][0] = '   '
            lifecount[1] -= 1
            time.sleep(0.5)
        else:
            print('Attack Failed!')
            time.sleep(0.5)
    elif clone[1] == ' ':
        print('Attacking Open Space!')
        if not blownup:
            if total == 12:
                print('Boom You Beat It!!!!')
                print('Enemy Lost One Random Life')
                time.sleep(0.5)
                lifecount[1] -= 1
                while True:
                    done = False
                    while True:
                        x = random.randint(0,2)
                        if lives[x] != '   ':
                            lives[x] = '   '
                            done = True
                            break
                    if done:
                        break
                blownup = True
            else:
                print('Attack Failed!')
                time.sleep(0.5)
        else:
            print('You Already Did This Atack')
            time.sleep(0.5)
            playerattack(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    for r in range(0,5):
        if enemystacks[r][0] == '   ':
            if len(enemybackup[0])+len(enemybackup[1]) == 0:
                if (r == 0) and (lives[0] != '   '):
                    enemystacks[r][0] = lives[0]
                    lives[0] = '   '
                elif (r == 2) and (lives[1] != '   '):
                    enemystacks[r][0] = lives[1]
                    lives[1] = '   '
                elif (r == 4) and (lives[2] != '   '):
                    enemystacks[r][0] = lives[2]
                    lives[2] = '   '
            else:
                print('Enemy Uses A Replacement')
                if (len(enemybackup[0]) != 0) and (len(enemybackup[1]) != 0):
                    rint = random.randint(0,1)
                    enemystacks[r][0] = enemybackup[rint][0]
                    del enemybackup[rint][0]
                elif len(enemybackup[0]) != 0:
                    enemystacks[r][0] = enemybackup[0][0]
                    del enemybackup[0][0]
                else:
                    enemystacks[r][0] = enemybackup[1][0]
                    del enemybackup[1][0]
                enemystacks[r].append('   ')
                time.sleep(0.5)
    if lifecount[1] == 0:
        endwar2(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
            
    playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)

def enemyturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced):
    if enemystamina == 0:
        print('\nPLAYER TURN\n')
        time.sleep(0.5)
        playerstamina = 3
        playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    time.sleep(1)
    war2drawtable(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements)
    enemystamina -= 1
    lownums = ['2','3','4','5']
    dicenums = [1,2,3,4,5,6]
    if enemyreplaced == False:
        done = False
        for num in range(0, 5):
            if enemystacks[num][0][1] in lownums:
                enemyreplaced = True
                print('ENEMY USES REPLACEMENT CARD')
                while True:
                    x = random.randint(2,3)
                    if replacements != '   ':
                        enemystacks[num][0] = replacements[x-2]
                        replacements[x] = '   '
                        done = True
                        break
                if done:
                    time.sleep(1)
                    enemyturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    print('\nENEMY IS ATTACKING\n')
    time.sleep(1)
    playerwarriors = []
    livestoattack = []
    fatals = ['K','J','Q']
    knightstoattack = []
    temp = []
    oddout = [1,3]
    for num in range(0,5):
        playerwarriors.append([playerstacks[num][0][1], num])
    for num in range(0,5):
        if playerwarriors[num][0] == '0':
            playerwarriors[num][0] = '10'
        elif playerwarriors[num][0] in fatals:
            livestoattack.append([playerwarriors[num][0], num])
        elif playerwarriors[num][0] == 'A':
            knightstoattack.append([playerwarriors[num][0], num])
    knightscopy = []
    if len(playerbackup[0]) + len(playerbackup[1]) == 0:
        for num in range(0,len(knightstoattack)):
            if knightstoattack[num][1] in oddout:
                pass
            else:
                knightscopy.append(knightstoattack[num])
        knightstoattack = knightscopy
    for num in range(0,5):
        if len(playerbackup[0]) + len(playerbackup[1]) == 0:
            if (num == 1) or (num == 3):
                pass
            else:
                try:
                    temp.append([int(playerwarriors[num][0]),num])
                except:
                    pass
        else:
            try:
                temp.append([int(playerwarriors[num][0]),num])
            except:
                pass
    attacked = False
    if len(livestoattack) != 0:
        print('\nENEMY IS ATTACKING THE LIFE '+playerstacks[livestoattack[0][1]][0]+'\n')
        time.sleep(0.5)
        dienums = [1,2,3,4,5,6]
        print('\nENEMY IS ROLLING THE DICE\n')
        time.sleep(1)
        x1 = random.choice(dicenums)
        x2 = random.choice(dicenums)
        print('\nTHE ENEMY ROLLED -> ['+str(x1)+'] ['+str(x2)+']\n')
        time.sleep(0.5)
        if x1 == x2:
            print('\nATTACK SUCCESSFUL\n')
            time.sleep(0.5)
            playerstacks[livestoattack[0][1]][0] = '   '
            lifecount[0] -= 1
        else:
            print('\nATTACK UNSUCCESSFUL\n')
        attacked = True
    elif len(knightstoattack) != 0:
        x = random.randint(0,4)
        if x == 1:
            print('\nENEMY IS ATTACKING '+playerstacks[knightstoattack[0][1]][0]+'\n')
            time.sleep(0.5)
            dicenums = [1,2,3,4,5,6]
            print('\nENEMY IS ROLLING THE DICE\n')
            time.sleep(1)
            x1 = random.choice(dicenums)
            x2 = random.choice(dicenums)
            print('\nTHE ENEMY ROLLED -> ['+str(x1)+'] ['+str(x2)+']\n')
            time.sleep(0.5)
            if x1 == x2:
                print('\nATTACK SUCCESSFUL\n')
                time.sleep(0.5)
                del playerstacks[knightstoattack[0][1]][0]
                attacked = True
            else:
                print('\nATTACK UNSUCCESSFUL\n')
                time.sleep(0.5)
                attacked = True
    if (not attacked) and (len(temp) != 0):
        playerwarriors = temp
        toattack = min(playerwarriors)
        print('\nENEMY SELECTED '+playerstacks[toattack[1]][0]+'\n')
        time.sleep(0.5)
        dienums = [1,2,3,4,5,6]
        print('\nENEMY IS ROLLING THE DICE\n')
        time.sleep(1)
        x1 = random.choice(dienums)
        x2 = random.choice(dienums)
        print('\nTHE ENEMY ROLLED -> ['+str(x1)+'] ['+str(x2)+']\n')
        time.sleep(0.5)
        total = (x1+x2)
        if total >= toattack[0]:
            print('\nATTACK SUCCESSFUL\n')
            time.sleep(0.5)
            del playerstacks[toattack[1]][0]
        else:
            print('\nATTACK UNSUCCESSFUL\n')
            time.sleep(0.5)
        attacked = True
    elif len(knightstoattack) != 0 and not attacked:
        x = random.randint(0,4)
        if x != -1:
            print('\nENEMY IS ATTACKING '+playerstacks[knightstoattack[0][1]][0]+'\n')
            time.sleep(0.5)
            dicenums = [1,2,3,4,5,6]
            print('\nENEMY IS ROLLING THE DICE\n')
            time.sleep(1)
            x1 = random.choice(dicenums)
            x2 = random.choice(dicenums)
            print('\nTHE ENEMY ROLLED -> ['+str(x1)+'] ['+str(x2)+']\n')
            time.sleep(0.5)
            if x1 == x2:
                print('\nATTACK SUCCESSFUL\n')
                time.sleep(0.5)
                del playerstacks[knightstoattack[0][1]][0]
                attacked = True
            else:
                print('\nATTACK UNSUCCESSFUL\n')
                time.sleep(0.5)
                attacked = True
    for r in range(0,5):
        if playerstacks[r][0] == '   ':
            leftgood = rightgood = False
            if len(playerbackup[0])+len(playerbackup[1]) != 0:
                if len(playerbackup[0]) != 0:
                    leftgood = True
                if len(playerbackup[1]) != 0:
                    rightgood = True
                print('Which Replacement Side Would You Like To Use?')
                lefttemp = leftgood
                righttemp = rightgood
                for x in range(1,3):
                    if lefttemp:
                        print(str(x)+'. Left Side')
                        lefttemp = False
                    elif righttemp:
                        print(str(x)+'. Right Side')
                        righttemp = False
                print('\n')
                while True:
                    allgood = False
                    while True:
                        choose = input('>>')
                        try:
                            x = int(choose)
                        except:
                            print('A Number Only')
                            break
                        if (x == 1) and (leftgood == True):
                            choice = 0
                            pass
                        elif (x == 1) and (rightgood == True):
                            choice = 1
                            pass
                        elif (x == 2) and ((leftgood == True) and (rightgood == True)):
                            choice = 1
                            pass
                        else:
                            print('1 or Possibly 2 Only')
                            break
                        print('\nPLAYER USES A REPLACEMENT\n')
                        time.sleep(0.5)
                        playerstacks[r][0] = playerbackup[choice][0]
                        del playerbackup[choice][0]
                        playerstacks[r].append('   ')
                        time.sleep(0.5)
                        allgood = True
                        break
                    if allgood:
                        break
            else:
                if r == 0:
                    playerstacks[r][0] = lives[3]
                    lives[3] = '   '
                elif r == 2:
                    playerstacks[r][0] = lives[4]
                    lives[4] = '   '
                elif r == 4:
                    playerstacks[r][0] = lives[5]
                    lives[5] = '   '
    if lifecount[0] == 0:
        endwar2(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)

    enemyturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)

def endwar2(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced):
    print('END WAR\n')
    time.sleep(1)
    if lifecount[1] > lifecount[0]:
        print('The Winner Is The Enemy!!!\n')
        print('You Lost!!!!')
    else:
        print('The Winner Is The Player!!!\n')
        print('You Won!!!!')
    sys.exit()

def startwar2():
    cards = [' A♥',' 2♥',' 3♥',' 4♥',' 5♥',' 6♥',' 7♥',' 8♥',' 9♥','10♥',' A♦',' 2♦',' 3♦',' 4♦',' 5♦',' 6♦',' 7♦',' 8♦',' 9♦','10♦',' A♠',' 2♠',' 3♠',' 4♠',' 5♠',' 6♠',' 7♠',' 8♠',' 9♠','10♠',' A♣',' 2♣',' 3♣',' 4♣',' 5♣',' 6♣',' 7♣',' 8♣',' 9♣','10♣']
    lifecount = [3,3]
    blownup = False
    enemyreplaced = False
    replaced = False
    dice = [1,2,3,4,5,6]
    backup = [2,2,2,2]
    suits = ['♠','♣','♥','♦']
    backup = []
    replacements = []
    playerbackup = [[],[]]
    enemybackup = [[],[]]
    while True:
        count = 0
        while True:
            count += 1
            x = random.randint(0, len(cards)-1)
            replacements.append(cards[x])
            del cards[x]
            if count == 2:
                break
        replacements.append('[@]')
        replacements.append('[@]')
        x = random.randint(0, len(cards)-1)
        playerbackup[0].append(cards[x])
        del cards[x]
        x = random.randint(0, len(cards)-1)
        playerbackup[1].append(cards[x])
        del cards[x]
        x = random.randint(0, len(cards)-1)
        playerbackup[0].append(cards[x])
        del cards[x]
        x = random.randint(0, len(cards)-1)
        playerbackup[1].append(cards[x])
        del cards[x]

        x = random.randint(0, len(cards)-1)
        enemybackup[0].append(cards[x])
        del cards[x]
        x = random.randint(0, len(cards)-1)
        enemybackup[1].append(cards[x])
        del cards[x]
        x = random.randint(0, len(cards)-1)
        enemybackup[0].append(cards[x])
        del cards[x]
        x = random.randint(0, len(cards)-1)
        enemybackup[1].append(cards[x])
        del cards[x]
        break
    print('What Suit Would You Like To Have?')
    print('1. Spades')
    print('2. Clubs')
    print('3. Hearts')
    print('4. Diamonds\n')
    while True:
        while True:
            good = False
            x = input('>>')
            try:
                x = int(x)
            except:
                print('Type One Of The Numbers\n')
                break
            if x in range(1,5):
                print('You Chose -> '+suits[x-1])
                good = True
                break
            else:
                print('1, 2, 3, or 4\n')
                break
        if good:
            break
    playersuit = suits[x-1]
    del suits[x-1]
    enemysuit = random.choice(suits)
    print('Enemy -> '+enemysuit+'\n')
    lives = [' K'+enemysuit, ' Q'+enemysuit, ' J'+enemysuit, ' J'+playersuit, ' Q'+playersuit, ' K'+playersuit]
    backup = [2,2,2,2]
    playerstacks = [[],[],[],[],[]]
    enemystacks = [[],[],[],[],[]]
    x = -1
    for n in range(0, 15):
        x += 1
        num = random.randint(0, len(cards)-1)
        playerstacks[x].append(cards[num])
        del cards[num]
        num = random.randint(0, len(cards)-1)
        enemystacks[x].append(cards[num])
        del cards[num]
        if x == 4:
            x = -1
    x = -1
    while True:
        x += 1
        playerstacks[x].append('   ')
        enemystacks[x].append('   ')
        if x == 4:
            break
    print('\n\nRolling Die To Determine Starting Player\nPlayer -> 1-3\nEnemy -> 4-6\n')
    print('Rolling...')
    time.sleep(1)
    dienum = random.choice(dice)
    print(str(dienum)+'\n')
    playerstamina = enemystamina = 3
    if dienum < 4:
        print('Player Starts\n')
        time.sleep(1)
        playerturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)
    else:
        print('Enemy Starts\n')
        time.sleep(1)
        enemyturn(playerstacks, enemystacks, lives, enemybackup, playerbackup, replacements, replaced, lifecount, enemystamina, playerstamina, blownup, enemyreplaced)

startwar2()
