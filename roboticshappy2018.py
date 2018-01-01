#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World

Make Cozmo say 'Hello World' in this simple Cozmo SDK example program.
'''

import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

import time

def cozmo_program(robot: cozmo.robot.Robot):


    time.sleep(10)

    #Cozmo lights setup
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    if cube1 is not None:
        cube1.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")




    robot.say_text("Hello Makers!").wait_for_completed()
    print("Playing Animation 3:")
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin, in_parallel=False).wait_for_completed()
    robot.say_text("This year has been AWESOME and full of SAV").wait_for_completed()
    robot.play_anim(name="id_poked_giggle").wait_for_completed()
    cube1.set_lights(cozmo.lights.green_light)
    cube2.set_lights(cozmo.lights.blue_light)
    cube3.set_lights(cozmo.lights.red_light)
    #robot.say_text("We wish you a happy new year!",in_parallel=True)#.wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin, in_parallel=False).wait_for_completed()
    robot.say_text("Me and Julian wish you a happy new year!",in_parallel=False,play_excited_animation=False).wait_for_completed()
    robot.say_text("Let's make!",in_parallel=False,play_excited_animation=True).wait_for_completed()



    #Animation lists
    #coz = robot.wait_for_robot()
    #print("All animations = %s" % coz.anim_names)

    
    #CodeLabPartyTime

    # Keep the lights on for 10 seconds until the program exits
    #time.sleep(10)


    
cozmo.run_program(cozmo_program)
