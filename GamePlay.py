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
                        
def Game () :
        # Define some colours
        # Colours are defined using RGB values
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        PURPLE = (174, 20, 188)
        BROWN = (70, 31, 10)

        screenW = 1400
        screenH = 785

        # Check if staff placed or not
        active = True

        # Timer of when you need to spawn enemies
        spawnTime = 0
        waveSpeed = 0
        
        # Check if first wave has passed
        passedFirstWave = False

        pressedE = False

        # A cooldown event and boolean to see it's state
        cooldownEvent = pygame.USEREVENT
        cooled = True

        killCount = 0

        # This loop will continue until the user exits the game
        carryOn = True
        clock = pygame.time.Clock ()

        # Open a new window
        # The window is defined as (width, height), measured in pixels
        size = (screenW, screenH)
        screen = pygame.display.set_mode (size)
        pygame.display.set_caption("Demon Staff")

        
        pygame.mouse.set_visible (False)
        hitMarker = pygame.image.load ('hitMarker.png')
        hitMarker = pygame.transform.scale(hitMarker, (50, 50))
        hitMarkerRect = hitMarker.get_rect ()

        # - Create some tutorial text on the floor of the game
        demonFont = pygame.font.Font('DemonsAndDarlings.ttf', 64)
        demonFont2 = pygame.font.Font ('DemonsAndDarlings.ttf',48)
        # W
        wText = demonFont.render('W', True, RED)
        wTextRect = wText.get_rect()
        wTextRect.center = (screenW/2, screenH/3)
        # S 
        sText = demonFont.render('S', True, RED)
        sTextRect = sText.get_rect()
        sTextRect.center = (screenW/2, screenH * 3/4)
        # A
        aText = demonFont.render('A', True, RED)
        aTextRect = aText.get_rect()
        aTextRect.center = (screenW/4, screenH/2)
        # D
        dText = demonFont.render('D', True, RED)
        dTextRect = dText.get_rect()
        dTextRect.center = (screenW * 3/4, screenH/2)
        # The press e buttom
        eText = demonFont.render('', True, RED)
        eTextRect = eText.get_rect()
        # SpaceBar tutorial text
        devilText = demonFont2.render('Get close...', True, PURPLE)
        devilTextRect = devilText.get_rect ()
        devilTextRect.center = (200, 450)

        devil2Text = demonFont2.render('and hold that staff...', True, PURPLE)
        devil2TextRect = devil2Text.get_rect ()
        devil2TextRect.center = (500, 550)

        devil3Text = demonFont2.render('do it with Spacebar!', True, PURPLE)
        devil3TextRect = devil3Text.get_rect ()
        devil3TextRect.center = (screenW//2.7, 625)
        
        # The text to tell how many killed
        killText = demonFont.render ('Slain: ', True, RED)
        killTextRect = killText.get_rect ()
        killTextRect.center = (80, 110)
        # The text counter for the killed
        killCountText = demonFont.render (str(killCount), True, RED)
        killCountTextRect = killCountText.get_rect ()
        killCountTextRect.center = (180, 110)

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
        staff.rect.center = (screenW/8, screenH-160)

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


        #---------Main Program Loop----------
        while carryOn:

                spawnTime += 1
                hitMarkerRect.center = pygame.mouse.get_pos ()

                # --- Main event loop ---
                for event in pygame.event.get(): # Player did something
                        if event.type == pygame.QUIT: # Player clicked close button
                                carryOn = False
                        elif event.type == cooldownEvent : # Off cooldown
                                cooled = True
                                pygame.time.set_timer (cooldownEvent, 0)

                # - WASD controls
                keys = pygame.key.get_pressed ()
                
                # - WASD controls
                if keys [pygame.K_a] :
                        player.moveLeft (5)
                        aText = demonFont.render ('', True, BLACK)
                if keys [pygame.K_d] :
                        player.moveRight (5)
                        dText = demonFont.render ('', True, BLACK)
                if keys [pygame.K_w] :
                        player.moveUp (5)
                        wText = demonFont.render ('', True, BLACK)
                if keys [pygame.K_s] :
                        player.moveDown (5)
                        sText = demonFont.render ('', True, BLACK)

                
                # --- Game logic goes here
                spriteList.update ()

                # List to know what to check for collision between enemies and player
                hurtList = pygame.sprite.spritecollide (player, enemyList , False, pygame.sprite.collide_mask)
                pickUpList = pygame.sprite.spritecollide (player, itemList, False, pygame.sprite.collide_mask)

                # - Moves staff when presing and holding space
                for item in pickUpList :
                        
                        if keys [pygame.K_SPACE] :
                                item.moveWithPlayer (player)
                                staffAOE.kill ()
                                
                                devilText = demonFont2.render('', False, RED)
                                devil2Text = demonFont2.render('', False, RED)
                                devil3Text = demonFont2.render('', False, RED)
                                
                                active = False # Makes so can't use magic

                        else :
                                staffAOE.updateAOE (staff)
                                staffAOE.add (objectList)
                                staffAOE.add (spriteList)
                                
                                active = True # When placed down again, can use magic again

                # - Creates random amount of enemies in random locations
                if spawnTime == 1000 - waveSpeed :
                        
                        amount = 0
                        
                        if passedFirstWave == False :
                                amount = 1
                                print ("how many:", amount)
                        else :
                                amount = random.randint (1, 6)
                                print ("how many:", amount-1)
                                
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
                        waveSpeed += 5
                        passedFirstWave = True
                        
                elif waveSpeed == 1000 :
                        print ("Your free!")
                
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
                x1, y1 = player.rect.center
                x2, y2 = staffAOE.rect.center

                # Find the distance between player and AOE
                AOEDistance = math.hypot (x1 - x2, y1 - y2)
                if AOEDistance < staffAOE.radius and active == True :

                        eText = demonFont.render('Press E', True, RED)
                        eTextRect.center = (player.rect.x, player.rect.y - 70)

                        if pressedE == True :
                                eText = demonFont.render('', False, RED)

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

                                        eText = demonFont.render('', False, RED)

                                        cooled = False
                                        pressedE = True

                                        # Start cooldown timer
                                        pygame.time.set_timer (cooldownEvent, 3000)
                                        
                else :
                        eText = demonFont.render('', False, RED)
                        
                # Check for every fireball projectile
                for fireball in projectileList :
                        # Creates a collision list for enemies
                        enemyKillList = pygame.sprite.spritecollide (fireball, enemyList, False, pygame.sprite.collide_mask)
                        enemyKilled = 0
                        # When hits enemy, removes fireball enemies
                        for badboi in enemyKillList :
                                badboi.health -= 1
                                print (badboi.health)

                                projectileList.remove (fireBall)
                                spriteList.remove (fireBall)

                                if badboi.health <= 0 :
                                        badboi.kill ()
                                        killCount += 1

                        # When goes off screen, remove fireball
                        if fireball.rect.x < 0 or fireball.rect.x > screenW or fireball.rect.y < 0 or fireball.rect.y > screenH :
                                fireball.kill ()

                # --- Draw code goes here

                # - Clear the screen to white
                screen.fill(BROWN)

                # Queue different shapes and lines to be drawn
                # - Draw all sprites
                spriteList.draw (screen)
                
                # - Devil's writing
                screen.blit (wText, wTextRect)
                screen.blit (sText, sTextRect)
                screen.blit (aText, aTextRect)
                screen.blit (dText, dTextRect)
                screen.blit (eText, eTextRect)
                screen.blit (killText, killTextRect)
                screen.blit (killCountText, killCountTextRect)
                screen.blit (devilText, devilTextRect)
                screen.blit (devil2Text, devil2TextRect)
                screen.blit (devil3Text, devil3TextRect)
                screen.blit (hitMarker, hitMarkerRect)

                killCountText = demonFont.render (str(killCount), True, RED)

                # - Health Bar
                pygame.draw.rect (screen, BLACK, [5, 5, 200 + 10, 60], 10)
                pygame.draw.rect (screen, GREEN, [10, 10, player.health * 50, 50])

                # Update the screen with queued shapes
                pygame.display.flip()

                # --- Limit to 60 frames per second
                clock.tick(60)

        # Once the main program loop is exited, stop the game engine
        pygame.quit()
