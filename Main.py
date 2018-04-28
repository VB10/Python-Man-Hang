import os
import DeathHuman
import Service

maxCount = len(DeathHuman.images)
tryCount = 0
findWorld = ''
empty = ''
def num(s):
    try:
        int(s)
        return num(input('Bir kelime girin : '))
    except ValueError:
        return s.lower()

#listede ki _ yerini değiştirip kelimeleri ekleme
def changeIndex(index,string,new):
    listString = list(string)
    listString[index*2]= new
    return ''.join(listString)
def endGame():
    try:
        end = int(input('Devam mı ? (evet 1 hayır 0) : '))
        if end == 1:
            return False
        else:
            print('Oyun biter.')
            return True
        
    except ValueError:
        print('Oyun biter.')
        return True      
def newGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    #mac os X
    findWorld = Service.get('worldlist')
    print('Hello Welcome Man Hang :) \n')
    empty= ''
    # gelen kelimeyi saklıyoruz
    for letter in findWorld:
        empty += "_ "
    print(empty)  
    tryCount = 0
    while True :
        # klavyeden sayı girmeyi engelleme
        numberCheck = True
        world = num(input('Bir kelime girin : '))
        # kelime kontrol varmı yokmu 
        result = findWorld.find(world)
        if result != -1:   
            for number in range(0,len(findWorld)):
                if findWorld[number] == world:
                    # empty.index = world+' '
                    empty = changeIndex(number,empty,world)
                else :
                    continue                
        else :
            print(DeathHuman.images[tryCount])
            tryCount += 1
        print(empty)
        if tryCount+1 == maxCount :
            if endGame():
                exit()
            else:
                newGame()
        if empty.find('_') == -1  :
            if endGame():
                exit()
            else:
                newGame()
newGame()

   
    