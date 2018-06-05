# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame, sys, math, random
pygame.init()

from GameClasses import Player
from GameClasses import StaffAOE
from GameClasses import Staff
from GameClasses import Enemy
from GameClasses import FireBall
from GameClasses import EnemySpawner

##def paused():
##
##        pause = True
##        quitgame = pygame.quit()
##        
##        screenW = 1400
##        screenH = 785
##        size = (screenW, screenH)
##        screen = pygame.display.set_mode(size)
##
##        BLACK = (0, 0, 0)
##        WHITE = (255, 255, 255)
##        GREEN = (0, 255, 0)
##        BRIGHT_GREEN = (0, 200, 0)
##        RED = (255, 0, 0)
##        BRIGHT_RED = (200, 0, 0)
##        PURPLE = (174, 20, 188)
##
##        fontTitle = pygame.font.Font('freesansbold.ttf',32)
##        textSurfaceTitle = fontTitle.render('Pause', True, BLACK) 
##        textRectTitle = textSurfaceTitle.get_rect()
##        textRectTitle.center = ((screenW/2),(screenH/2))
##        screen.blit(textSurfaceTitle, textRectTitle)
##        button = screen.blit
##        while pause:
##                for event in pygame.event.get():
##                        if event.type == pygame.QUIT:
##                                pygame.quit()
##                button("Continue",150,450,100,50,GREEN,BRIGHT_GREEN, pause == False)
##                button("Quit",550,450,100,50,RED,BRIGHT_RED,quitgame)
##
##                pygame.display.update()

                        

def Game () :
        # Define some colours
        # Colours are defined using RGB values
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        PURPLE = (174, 20, 188)

        screenW = 1400
        screenH = 785
        # Open a new window
        # The window is defined as (width, height), measured in pixels
        size = (screenW, screenH)
        screen = pygame.display.set_mode (size)
        pygame.display.set_caption("Demon Staff")

        # - Create some tutorial text on the floor of the game
        demonFont = pygame.font.Font('DemonsAndDarlings.ttf', 64)
        # W
        wText = demonFont.render('W', True, BLACK)
        wTextRect = wText.get_rect()
        wTextRect.center = (screenW/2, screenH/3)
        # S 
        sText = demonFont.render('S', True, BLACK)
        sTextRect = sText.get_rect()
        sTextRect.center = (screenW/2, screenH/1.5)
        # A
        aText = demonFont.render('A', True, BLACK)
        aTextRect = aText.get_rect()
        aTextRect.center = (screenW/4, screenH/2)
        # D
        dText = demonFont.render('D', True, BLACK)
        dTextRect = dText.get_rect()
        dTextRect.center = (screenW * 3/4, screenH/2)

        eText = demonFont.render('', True, BLACK)
        eTextRect = eText.get_rect()
        
        # Create lists
        spriteList = pygame.sprite.Group ()
        spawnerList = pygame.sprite.Group ()
        enemyList = pygame.sprite.Group ()
        objectList = pygame.sprite.Group ()
        projectileList = pygame.sprite.Group ()
        itemList = pygame.sprite.Group ()

        # Create the objects and sets properties
        player = Player (GREEN, 50, 50, 4)
        player.rect.center = (screenW//2, screenH//2)

        staff = Staff (PURPLE, 0, 0)
        staff.rect.center = (screenW//3, screenH//2)

        staffAOE = StaffAOE (PURPLE, 300, 300, 300//2)
        staffAOE.rect.center = staff.rect.center

        staffAOE = StaffAOE (PURPLE, 300, 300, 300//2)
        staffAOE.rect.center = staff.rect.center

        spawner = EnemySpawner (RED, 50, 50)
        spawner.rect.center = (-50, -50)

        spawner2 = EnemySpawner (RED, 50, 50)
        spawner2.rect.center = (1450, -50)

        spawner3 = EnemySpawner (RED, 50, 50)
        spawner3.rect.center = (-50, 835)

        spawner4 = EnemySpawner (RED, 50, 50)
        spawner4.rect.center = (1450, 835)

        spawnerList.add (spawner, spawner2, spawner3, spawner4)

        spriteList.add (player, staff, staffAOE, spawner, spawner2, spawner3, spawner4)
        objectList.add (staff, staffAOE)
        itemList.add (staff)

        # Check if staff placed or not
        active = True

        # Timer of when you need to spawn enemies
        spawnTime = 0
        # Check if first wave has passed
        passedFirstWave = 0

        # A cooldown event and boolean to see it's state
        cooldownEvent = pygame.USEREVENT
        cooled = True

        # This loop will continue until the user exits the game
        carryOn = True
        clock = pygame.time.Clock ()
        pause = False

        #---------Main Program Loop----------
        while carryOn:

                spawnTime += 1

                # --- Main event loop ---
                for event in pygame.event.get(): # Player did something
                        if event.type == pygame.QUIT: # Player clicked close button
                                carryOn = False
                        elif event.type == cooldownEvent : # Off cooldown
                                cooled = True
                                pygame.time.set_timer (cooldownEvent, 0)

                # - WASD controls
                keys = pygame.key.get_pressed ()

                #pause key
##                if event.type == pygame.KEYDOWN:
##                        if event.key == pygame.K_ESCAPE and pause == False:
##                                pause = True
##                        if event.key == pygame.K_ESCAPE and pause == True:
##                                pause == False

##                if pause == True:
##                        paused()

##                elif pause == False:
                
                # - WASD controls
                if keys [pygame.K_a] :
                        player.moveLeft (5)
                if keys [pygame.K_d] :
                        player.moveRight (5)
                if keys [pygame.K_w] :
                        player.moveUp (5)
                if keys [pygame.K_s] :
                        player.moveDown (5)
                

                # --- Game logic goes here
                spriteList.update ()

                # List to know what to check for collision between enemies and player
                hurtList = pygame.sprite.spritecollide (player, enemyList , False, pygame.sprite.collide_mask)
                pickUpList = pygame.sprite.spritecollide (player, itemList, False, pygame.sprite.collide_mask)

                # - Moves staff when presing and holding space
                for item in pickUpList :
                        
                        if keys [pygame.K_SPACE] :
                                item.moveWithPlayer (player)
                                staffAOE.updateAOE (staff)
                                staffAOE.kill ()
                                active = False # Makes so can't use magic

                        else :
                                staffAOE.updateAOE (staff)
                                staffAOE.add (objectList)
                                staffAOE.add (spriteList)
                                active = True # When placed down again, can use magic again

                # - Creates random amount of enemies in random locations
                if spawnTime == 1000 :
                        amount = 0
                        if passedFirstWave == 0 :
                                amount = 1
                                print ("how many:", amount)
                        else :
                                amount = random.randint (0, 5)
                                print ("how many:", amount)
                                
                        for badguy in range (amount) :
                        
                                badguy = Enemy (RED, 0, 0, 4, 3)
                        
                                corner = random.randint (1, 4)
                                if corner == 1 :
                                        badguy.rect.center = spawner.rect.center
                                if corner == 2 :
                                        badguy.rect.center = spawner2.rect.center
                                if corner == 3 :
                                        badguy.rect.center = spawner3.rect.center
                                if corner == 4 :
                                        badguy.rect.center = spawner4.rect.center
                                        
                                enemyList.add (badguy)
                                spriteList.add (badguy)
                        spawnTime = 0
                        passedFirstWave = 1 
                
                
                # - Enemies charge to player
                for enemy in enemyList :
                        enemy.moveToPlayer (player)

                # - Does dmg when player toches enemy
                for bad in hurtList :
                        player.health -= 1

                        if bad.rect.x > player.rect.x :
                                player.rect.x -= 100
                        if bad.rect.x < player.rect.x :
                                player.rect.x += 100
                        if bad.rect.y > player.rect.y :
                                player.rect.y -= 100
                        if bad.rect.y < player.rect.y :
                                player.rect.y += 100

                # - Ends game when player runs out of health
                if player.health <= 0 :
                        carryOn = False
                        print("GAME OVER!!!")

                # - Blessing zone to allow player to use magic,
                # Code based off: https://stackoverflow.com/questions/34054248/pygame-circle-and-its-associated-rect-for-collision-detection

                #  Find pos of player and AOE
                x1 = player.rect.x
                y1 = player.rect.y
                x2, y2 = staffAOE.rect.center

                # Find the distance between player and AOE
                distance = math.hypot (x1 - x2, y1 - y2)
                if distance < staffAOE.radius and active == True :

                        eText = demonFont.render('Press E', True, BLACK)
                        eTextRect.center = (player.rect.x, player.rect.y - 70)

                        # Checks pressed e
                        if keys [pygame.K_e] :
                                #  - Cooldown portion,
                                # based off: https://stackoverflow.com/questions/23368999/move-an-object-every-few-seconds-in-pygame?noredirect=1&lq=1
                                if cooled:

                                        # Gets position of mouse
                                        pos = pygame.mouse.get_pos ()
                                        xMouse = pos[0]
                                        yMouse = pos[1]

                                        # Creates a "Fireball"
                                        fireBall = FireBall (player.rect.x, player.rect.y, xMouse, yMouse)

                                        # Add fireball to lists
                                        spriteList.add (fireBall)
                                        projectileList.add (fireBall)

                                        cooled = False

                                        # Start cooldown timer
                                        pygame.time.set_timer (cooldownEvent, 3000)
                else :
                        eText = demonFont.render ("", True, BLACK)

                # Check for every fireball projectile
                for fireball in projectileList :
                        # Creates a collision list for enemies
                        enemyKillList = pygame.sprite.spritecollide (fireball, enemyList, False)

                        # When hits enemy, removes fireball enemies
                        for badboi in enemyKillList :
                                badboi.health -= 1
                                print (badboi.health)

                                projectileList.remove (fireBall)
                                spriteList.remove (fireBall)

                                if badboi.health <= 0 :
                                        badboi.kill ()
                                        

                        # When goes off screen, remove fireball
                        if fireball.rect.x < 0 or fireball.rect.x > screenW or fireball.rect.y < 0 or fireball.rect.y > screenH :
                                fireball.kill ()

                # --- Draw code goes here

                # - Clear the screen to white
                screen.fill(WHITE)

                # Queue different shapes and lines to be drawn
                # - Draw all sprites
                spriteList.draw (screen)
                
                # - Devil's writing
                screen.blit (wText, wTextRect)
                screen.blit (sText, sTextRect)
                screen.blit (aText, aTextRect)
                screen.blit (dText, dTextRect)
                screen.blit (eText, eTextRect)

                # - Health Bar
                pygame.draw.rect (screen, BLACK, [5, 5, 210, 60], 10)
                pygame.draw.rect (screen, GREEN, [10, 10, player.health * 50, 50])

                # Update the screen with queued shapes
                pygame.display.flip()

                # --- Limit to 60 frames per second
                clock.tick(60)

        # Once the main program loop is exited, stop the game engine
        pygame.quit()
