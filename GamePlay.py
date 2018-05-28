# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

def Game () :
    # Pygame Template File
    # adapted from http://www.101computing.net/getting-started-with-pygame/

from GameClasses import Player
from GameClasses import StaffAOE
from GameClasses import Staff
from GameClasses import Enemy
from GameClasses import FireBall
<<<<<<< HEAD
    # Import the pygame library and initialise the game engine
    import pygame, math

pygame.init()
    from GameClasses import Player
    from GameClasses import StaffAOE
    from GameClasses import Staff
    from GameClasses import Enemy
    from GameClasses import FireBall
=======

pygame.init()
>>>>>>> parent of 1d89312... going to make game func

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (174, 20, 188)

# Open a new window
# The window is defined as (width, height), measured in pixels
<<<<<<< HEAD
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
=======

screenW = 1400
screenH = 785
>>>>>>> parent of 1d89312... going to make game func

size = (screenW, screenH)
screen = pygame.display.set_mode (size)
pygame.display.set_caption("Demon Staff")
<<<<<<< HEAD
    screenW = 1400
    screenH = 785
=======
>>>>>>> parent of 1d89312... going to make game func

# Create lists
spriteList = pygame.sprite.Group ()
enemyList = pygame.sprite.Group ()
objectList = pygame.sprite.Group ()
projectileList = pygame.sprite.Group ()
itemList = pygame.sprite.Group ()
<<<<<<< HEAD
    size = (screenW, screenH)
    screen = pygame.display.set_mode (size)
    pygame.display.set_caption("Demon Staff")
=======
>>>>>>> parent of 1d89312... going to make game func

# Create the objects and sets properties
player = Player (GREEN, 50, 50, 100)
player.rect.center = (screenW//2, screenH//2)
<<<<<<< HEAD
    # Create lists
    spriteList = pygame.sprite.Group ()
    enemyList = pygame.sprite.Group ()
    objectList = pygame.sprite.Group ()
    projectileList = pygame.sprite.Group ()
    itemList = pygame.sprite.Group ()
=======
>>>>>>> parent of 1d89312... going to make game func

badBoi = Enemy (RED, 0, 0, 100, 4)
badBoi.rect.x = 1400
badBoi.rect.y = screenH/2
<<<<<<< HEAD
    # Create the objects and sets properties
    player = Player (GREEN, 50, 50, 100)
    player.rect.center = (screenW//2, screenH//2)
=======
>>>>>>> parent of 1d89312... going to make game func

staff = Staff (PURPLE, 0, 0)
staff.rect.x = screenW//3
staff.rect.y = screenH//2
<<<<<<< HEAD
    badBoi = Enemy (RED, 0, 0, 100, 4)
    badBoi.rect.x = 1400
    badBoi.rect.y = screenH/2
=======
>>>>>>> parent of 1d89312... going to make game func

staffAOE = StaffAOE (PURPLE, 400, 400, 400//2)
staffAOE.rect.x = staff.rect.x - 170
staffAOE.rect.y = staff.rect.y - 160
<<<<<<< HEAD
    staff = Staff (PURPLE, 0, 0)
    staff.rect.x = screenW//3
    staff.rect.y = screenH//2
=======
>>>>>>> parent of 1d89312... going to make game func

# Put objects into lists
spriteList.add (player)
spriteList.add (badBoi)
spriteList.add (staff)
spriteList.add (staffAOE)
<<<<<<< HEAD
    staffAOE = StaffAOE (PURPLE, 400, 400, 400//2)
    staffAOE.rect.x = staff.rect.x - 170
    staffAOE.rect.y = staff.rect.y - 160

enemyList.add (badBoi)
    # Put objects into lists
    spriteList.add (player)
    spriteList.add (badBoi)
    spriteList.add (staff)
    spriteList.add (staffAOE)

objectList.add (staff)
objectList.add (staffAOE)
    enemyList.add (badBoi)

itemList.add (staff)
itemList.add (staffAOE)
    objectList.add (staff)
    objectList.add (staffAOE)

# Check if staff placed or not
active = True
    itemList.add (staff)
    itemList.add (staffAOE)
=======

enemyList.add (badBoi)

objectList.add (staff)
objectList.add (staffAOE)

itemList.add (staff)
itemList.add (staffAOE)

# Check if staff placed or not
active = True
>>>>>>> parent of 1d89312... going to make game func

# A cooldown event and boolean to see it's state
cooldownEvent = pygame.USEREVENT
cooled = True
<<<<<<< HEAD
    # Check if staff placed or not
    active = True

# This loop will continue until the user exits the game
carryOn = True
    # A cooldown event and boolean to see it's state
    cooldownEvent = pygame.USEREVENT
    cooled = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock ()
    # This loop will continue until the user exits the game
    carryOn = True

#---------Main Program Loop----------
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock ()
=======

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock ()

#---------Main Program Loop----------
>>>>>>> parent of 1d89312... going to make game func

while carryOn:
    
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == cooldownEvent : # Off cooldown
            cooled = True
            pygame.time.set_timer (cooldownEvent, 0) 

    # - WASD controls
    keys = pygame.key.get_pressed ()
    if keys [pygame.K_a] :
        player.moveLeft (5)
    if keys [pygame.K_d] :
        player.moveRight (5)
    if keys [pygame.K_w] :
        player.moveUp (5)
    if keys [pygame.K_s] :
        player.moveDown (5)
<<<<<<< HEAD
    #---------Main Program Loop----------

    while carryOn:
=======
>>>>>>> parent of 1d89312... going to make game func
        
    # --- Game logic goes here
    spriteList.update ()

    # List to know what to check for collision between enemies and player
    hurtList = pygame.sprite.spritecollide (player, enemyList , False, pygame.sprite.collide_mask)
    pickUpList = pygame.sprite.spritecollide (player, itemList, False, pygame.sprite.collide_mask)

    # - Moves staff when presing and holding e
    for item in pickUpList :
        if keys [pygame.K_e] :
            item.moveWithPlayer (player)
            staffAOE.moveWithStaff (staff)
            staffAOE.kill ()
            active = False # Makes so can't use magic
        else :
            staffAOE.add (objectList)
            staffAOE.add (spriteList)
            active = True # When placed down again, can use magic again

    # - Enemies charge to player
    for enemy in enemyList :
        enemy.moveToPlayer (player)
           
    # - Does dmg when player toches enemy
    for bad in hurtList :
        player.health -= 25

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
<<<<<<< HEAD
            
    if distance < staffAOE.radius and active == True :
        # Checks pressed SpaceBar
        if keys [pygame.K_SPACE] :
        # --- Main event loop ---
        for event in pygame.event.get(): # Player did something
            if event.type == pygame.QUIT: # Player clicked close button
                carryOn = False
            elif event.type == cooldownEvent : # Off cooldown
                cooled = True
                pygame.time.set_timer (cooldownEvent, 0) 

        # - WASD controls
        keys = pygame.key.get_pressed ()
        if keys [pygame.K_a] :
            player.moveLeft (5)
        if keys [pygame.K_d] :
            player.moveRight (5)
        if keys [pygame.K_w] :
            player.moveUp (5)
        if keys [pygame.K_s] :
            player.moveDown (5)
            
=======
            
    if distance < staffAOE.radius and active == True :
        # Checks pressed SpaceBar
        if keys [pygame.K_SPACE] :
            
>>>>>>> parent of 1d89312... going to make game func
            #  - Cooldown portion,
            # based off: https://stackoverflow.com/questions/23368999/move-an-object-every-few-seconds-in-pygame?noredirect=1&lq=1
            if cooled:
                
                # Gets position of mouse
                pos = pygame.mouse.get_pos ()
                xMouse = pos[0]
                yMouse = pos[1]
<<<<<<< HEAD

                # Creates a "Fireball"
                fireBall = FireBall (player.rect.x, player.rect.y, xMouse, yMouse)
        # --- Game logic goes here
        spriteList.update ()

        # List to know what to check for collision between enemies and player
        hurtList = pygame.sprite.spritecollide (player, enemyList , False, pygame.sprite.collide_mask)
        pickUpList = pygame.sprite.spritecollide (player, itemList, False, pygame.sprite.collide_mask)

        # - Moves staff when presing and holding e
        for item in pickUpList :
            if keys [pygame.K_e] :
                item.moveWithPlayer (player)
                staffAOE.moveWithStaff (staff)
                staffAOE.kill ()
                active = False # Makes so can't use magic
            else :
                staffAOE.add (objectList)
                staffAOE.add (spriteList)
                active = True # When placed down again, can use magic again

        # - Enemies charge to player
        for enemy in enemyList :
            enemy.moveToPlayer (player)
               
        # - Does dmg when player toches enemy and knocks back
        for bad in hurtList :
            player.health -= 25

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

                # Add fireball to lists
                spriteList.add (fireBall)
                projectileList.add (fireBall)
        # - Blessing zone to allow player to use magic,
        # Code based off: https://stackoverflow.com/questions/34054248/pygame-circle-and-its-associated-rect-for-collision-detection
        
        #  Find pos of player and AOE
        x1 = player.rect.x
        y1 = player.rect.y
        x2, y2 = staffAOE.rect.center

                # Now on cooldown
                cooled = False
        # Find the distance between player and AOE
        distance = math.hypot (x1 - x2, y1 - y2)
                
                # Start cooldown timer
                pygame.time.set_timer (cooldownEvent, 3000)

    # Check for every fireball projectile
    for fireball in projectileList :

        # Creates a collision list for enemies 
       enemyKillList = pygame.sprite.spritecollide (fireball, enemyList, False)
      
        # When hits enemy, removes fireball enemies
       for badboi in enemyKillList :

           badboi.health -= 25
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
    spriteList.draw (screen)

    # - Health Bar 
    pygame.draw.rect (screen, BLACK, [5, 5, 210, 60], 10)
    pygame.draw.rect (screen, GREEN, [10, 10, player.health * 2, 50])

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

# Once the main program loop is exited, stop the game engine
pygame.quit()
        if distance < staffAOE.radius and active == True :
            # Checks pressed SpaceBar
            if keys [pygame.K_SPACE] :
=======

                # Creates a "Fireball"
                fireBall = FireBall (player.rect.x, player.rect.y, xMouse, yMouse)

                # Add fireball to lists
                spriteList.add (fireBall)
                projectileList.add (fireBall)

                # Now on cooldown
                cooled = False
>>>>>>> parent of 1d89312... going to make game func
                
                # Start cooldown timer
                pygame.time.set_timer (cooldownEvent, 3000)

    # Check for every fireball projectile
    for fireball in projectileList :

        # Creates a collision list for enemies 
       enemyKillList = pygame.sprite.spritecollide (fireball, enemyList, False)
      
        # When hits enemy, removes fireball enemies
       for badboi in enemyKillList :

           badboi.health -= 25
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
    spriteList.draw (screen)

    # - Health Bar 
    pygame.draw.rect (screen, BLACK, [5, 5, 210, 60], 10)
    pygame.draw.rect (screen, GREEN, [10, 10, player.health * 2, 50])

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

# Once the main program loop is exited, stop the game engine
pygame.quit()
