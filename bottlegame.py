#!/usr/bin/env python3

'''Cozmo bottle game

Cozmo spins in a random mode to play bottle game with other people
'''

import time
import random
import cozmo



def cozmo_program(robot: cozmo.robot.Robot):

    #Random seed
    random.seed()

    # Tell the head motor to start lowering the head (at 5 radians per second)
    robot.move_head(5)
    time.sleep(0.5)

    # Tell Cozmo to drive the left wheel at 25 mmps (millimeters per second),
    # and the right wheel at 50 mmps (so Cozmo will drive Forwards while also
    # turning to the left


    #Random values
    randomtime=random.uniform(2,15) #Random time
    randomspeed=random.randint(100,500) #Random speed of the motors
    randomturn=random.randint(-1,1) #Turn direction

    if randomturn>=0:
        randomturn=1
    else:
        randormturn=-1
    
    print("Random time: "+str(randomtime)+" seconds")
    print("Random speed: "+str(randomspeed)+" mm/s") 

    robot.drive_wheels(-randomspeed*randomturn, randomspeed*randomturn)

    # wait for 3 seconds (the head, lift and wheels will move while we wait)


    time.sleep(randomtime)

'''
    # Tell the head motor to start raising the head (at 5 radians per second)
    robot.move_head(5)
    # Tell the lift motor to start raising the lift (at 5 radians per second)
    robot.move_lift(5)
    # Tell Cozmo to drive the left wheel at 50 mmps (millimeters per second),
    # and the right wheel at -50 mmps (so Cozmo will turn in-place to the right)
    robot.drive_wheels(50, -50)

    # wait for 3 seconds (the head, lift and wheels will move while we wait)
    time.sleep(3)

'''
cozmo.run_program(cozmo_program)
