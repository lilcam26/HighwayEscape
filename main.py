import pygame
import os
import time
import random


WIN = pygame.display.set_mode((900,500))
car = pygame.transform.scale((pygame.image.load(os.path.join("assets", "car.png"))), (73, 140))
traffic = (pygame.image.load(os.path.join("assets", "enemy1.png")))
cop = pygame.transform.scale(pygame.image.load(os.path.join("assets", "police.png")), (85, 160))

class BG():
    def __init__(self):
        self.y = 0
        self.view = pygame.image.load(os.path.join("assets", "BG.png"))

class Driver():

    def __init__(self):

        self.viewList = [220, 400, 580]
        self.index = 0
        self.x = self.viewList[self.index]
        self.y = 250
        self.view = car

    def switchLanes(self, LR):
        self.LR = LR

        if self.LR == True:
            if self.index < 2:
                self.index += 1


        if self.LR == False:
            if self.index > 0:
                self.index -= 1

class Enemy():

    def __init__(self, x, speed):
        self.WIDTH = 87
        self.HEIGHT = 158
        self.x = x
        self.y = -158
        self.speed = speed
        self.view = traffic

class Cop():
    def __init__(self):
        self.x = 407
        self.y = 500
        self.speed = 1.2
        self.distance = 5000
        self.view = cop


def Lane(testLane, traffic):
    testlanehere = testLane
    for i in traffic[testlanehere]:
        if i.y < 3:
            if testlanehere < 3:
                testlanehere += 1
            else:
                testlanehere = 1
            break
    else:
        return testlanehere

    for i in traffic[testlanehere]:
        if i.y < 3:
            if testlanehere < 3:
                testlanehere += 1
            else:
                testlanehere = 1
            break
    else:
        return testlanehere


    return 0






#####################################################################################################
def game():
    RUN = True
    bg = BG()
    bg2 = BG()
    bg2.y = bg.y - 500
    player = Driver()
    cop = Cop()
    laneXDict = {1:220}
    laneXDict[2] = 400
    laneXDict[3] = 580
    speedDict = {580: 4}
    speedDict[400] =  6
    speedDict[220] = 5
    speed = 0
    atLine = 0
    speedBehind = 0
    bgSpeed = 10


    finishLine = 4900
    finishLineSub = 1

    lane1 = []
    lane2 = []
    lane3 = []

    traffic = {1 : lane1}
    traffic[2] = lane2
    traffic[3] = lane3

    trafficTotal = []

    caught = False
    behindCar = False
    move_left = False
    move_right = False
    forward = False
    back = False
    bF = False              #false if back / true if forward
    crashed = False




    while RUN:
        pygame.time.Clock().tick(60)

        if caught == False:


            cop.distance -= cop.speed
            if speed < 0:
                finishLineSub = -(speed)
            else:
                finishLineSub = 1


            if finishLine < 500:
                if len(trafficTotal) < 8:
                    atLine = 0
                    for i in trafficTotal:
                        if i.y < 184 :
                            atLine += 1

                    if atLine < 2:
                        prob = random.randint(0, 10000)
                        if prob > 9800:
                            randLane = random.randint(1, 3)
                            lane = Lane(randLane, traffic)
                            if lane > 0:
                                whichLane = laneXDict[lane]
                                newCar = Enemy(whichLane, speedDict[whichLane])
                                traffic[randLane].append(newCar)
                                trafficTotal.append(newCar)

            elif finishLine < 1000:
                if len(trafficTotal) < 7:
                    atLine = 0
                    for i in trafficTotal:
                        if i.y < 184:
                            atLine += 1

                    if atLine < 2:
                        prob = random.randint(0, 10000)
                        if prob > 9800:
                            randLane = random.randint(1, 3)
                            lane = Lane(randLane, traffic)
                            if lane > 0:
                                whichLane = laneXDict[lane]
                                newCar = Enemy(whichLane, speedDict[whichLane])
                                traffic[randLane].append(newCar)
                                trafficTotal.append(newCar)

            elif finishLine < 3000:
                if len(trafficTotal) < 5:
                    atLine = 0
                    for i in trafficTotal:
                        if i.y < 184:
                            atLine += 1

                    if atLine < 2:
                        prob = random.randint(0, 10000)
                        if prob > 9800:
                            randLane = random.randint(1, 3)
                            lane = Lane(randLane, traffic)
                            if lane > 0:
                                whichLane = laneXDict[lane]
                                newCar = Enemy(whichLane, speedDict[whichLane])
                                traffic[randLane].append(newCar)
                                trafficTotal.append(newCar)
            else:
                if len(trafficTotal) < 4:
                    atLine = 0
                    for i in trafficTotal:
                        if i.y < 184:
                            atLine += 1

                    if atLine < 2:
                        prob = random.randint(0, 10000)
                        if prob > 9800:
                            randLane = random.randint(1, 3)
                            lane = Lane(randLane, traffic)
                            if lane > 0:
                                whichLane = laneXDict[lane]
                                newCar = Enemy(whichLane, speedDict[whichLane])
                                traffic[randLane].append(newCar)
                                trafficTotal.append(newCar)




            if len(trafficTotal) > 1:
                for i in range(0, len(trafficTotal) - 1):
                    if trafficTotal[i].y - 2 > 500:
                        trafficTotal.pop(i)
            else:
                for i in range(0, len(trafficTotal)):
                    if trafficTotal[i].y - 2 > 500:
                        trafficTotal.pop(i)




            ###Move shit on screen
            for i in trafficTotal:
                    i.y += i.speed
            if crashed == False:
                bg2.y += 13
                bg.y += 13
                if bg.y > 500:
                    bg.y = bg2.y - 500
                if bg2.y > 500:
                    bg2.y = bg.y - 500





            #activating the method to change its lane index
            if move_left:
                    player.switchLanes(False)
                    move_left = False
            if move_right:
                    player.switchLanes(True)
                    move_right = False

           # move Player
            for i in trafficTotal:
                if player.x == i.x and i.y - 140 < player.y < i.y + 160:
                    behindCar = True
                    speedBehind = i.speed
                    break
                elif i.y - 120 < player.y < i.y + 145 and i.x - 60 < player.x < i.x +40:
                    behindCar = False
                    crashed = True
                    speedBehind = 0
                    break
            else:
                behindCar = False


            #if the key toggles are on it changes the speed that is acting on the car in the next lines
            if forward:
                if bF == False:
                    speed = 0
                    bF = True
                speed -= 1
                forward = False
            if back:
                if bF == True:
                    speed = 0
                    bF = False
                speed += 1
                back = False

            if crashed == False:
                if behindCar:
                    player.y += speedBehind
                    if player.y > 500:
                        RUN = False
                else:
                    if 360 > player.y > 3:
                        player.y += speed
                    else:
                        if player.y > 350:
                            player.y = 350
                if player.x > player.viewList[player.index]:
                    player.x -= 15
                if player.x < player.viewList[player.index]:
                    player.x += 15
            else:
                if player.y > 20:
                    player.y -= 1

                if player.index > 1:
                    if player.x < 810:
                        player.x +=5
                else:
                    if player.x > 2:
                        player.x -=10



            if crashed:
                player.view = pygame.transform.rotate(player.view, 5)
                bg2.y += 4
                bg.y += 4
                if bg.y > 500:
                    bg.y = bg2.y - 500
                if bg2.y > 500:
                    bg2.y = bg.y - 500



            finishLine -= finishLineSub

            if finishLine < 0:
                print( "you win")
                break


            if cop.distance < finishLine:
                caught = True
                player.index = 2
        else:
            for i in trafficTotal:
                if i.y < 500:
                    i.y += 8
            if player.y > 150:
                player.y -= 2
            if len(trafficTotal) > 0:
                for i in range(0, len(trafficTotal) - 1):
                    if trafficTotal[i].y < 498:
                        break
                else:
                    if player.x < player.viewList[player.index]:
                        player.x += 15


            if bg.y > 500:
                bg.y = bg2.y - 500
            if bg2.y > 500:
                bg2.y = bg.y - 500
            if bgSpeed > 0:
                bg2.y += bgSpeed
                bg.y += bgSpeed
                bgSpeed -= .1





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_UP:
                    forward = True
                if event.key == pygame.K_DOWN:
                    back = True




        WIN.blit(bg.view, (0, bg.y))
        WIN.blit(bg2.view, (0, bg2.y))

        for i in trafficTotal:
            WIN.blit(i.view, (i.x, i.y))
        WIN.blit(player.view, (player.x, player.y))
        pygame.display.update()
        print(len(trafficTotal))




game()

