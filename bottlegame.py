#!/usr/bin/env python3

'''Cozmo bottle game

Cozmo spins in a random mode to play "spin the bottle game with truth or dare" with your friends
'''

import time
import random
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id


def cozmo_program(robot: cozmo.robot.Robot):

    time.sleep(10)

    while(True):


        # Tell the head motor up to face the players
        robot.move_head(5)
        time.sleep(0.5)

        #Random seed
        random.seed()

        #Random values
        randomtime=random.uniform(2,15) #Random time
        randomspeed=random.randint(100,500) #Random speed of the motors
        randomturn=random.randint(-1,1) #Turn direction

        #Cozmo lights setup
        cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip

        if cube1 is not None:
            cube1.set_lights(cozmo.lights.green_light)
        else:
            cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

        #The game won't start until someone tap the cube
        cube1.wait_for_tap()

        #Set the light to green again to indicate that Cozmo is ready for another turn
        cube1.set_lights(cozmo.lights.red_light)

        #After the tap we can print the random values
        print("Random time: "+str(randomtime)+" seconds")
        print("Random speed: "+str(randomspeed)+" mm/s")

        if randomturn>=0:
            randomturn=1
            print("AntiClockwise")
        else:
            randomturn=-1
            print("Clockwise")


        robot.drive_wheels(-randomspeed*randomturn, randomspeed*randomturn,duration=randomtime)

        #robot.say_text("I'm dizzy!",in_parallel=False,play_excited_animation=False).wait_for_completed()

        robot.say_text("Truth or dare?",in_parallel=False,play_excited_animation=False).wait_for_completed()
        robot.play_anim(name="id_poked_giggle").wait_for_completed()

        #Flash the cube to indicate that Cozmo has choose
        cube1.set_lights(cozmo.lights.green_light)
        time.sleep(0.250)
        cube1.set_lights(cozmo.lights.blue_light)
        time.sleep(0.250)
        cube1.set_lights(cozmo.lights.green_light)
        time.sleep(0.250)
        cube1.set_lights(cozmo.lights.blue_light)
        time.sleep(0.250)

        #Set the light to green again to indicate that Cozmo is ready for another turn
        cube1.set_lights(cozmo.lights.green_light)

cozmo.run_program(cozmo_program)
