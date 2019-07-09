The Gothon Game by Zed Shaw (Learn Python the Hard Way: A very simple introduction to the terryfing beautiful world of computers and code)

In Zed's above referred book exercise 43 is about basic object oriented analysis and design. In this chapter students are tasked to create a small Zork like game based on Zed's instruction. Point 4 in Study drills tweaks the task by challenging readers to:

"Go back to my description and analysis, then try to build a small combat system for the hero and the various Gothons he encounters."

The code in this folder is my answer to that challange. 

I have completed the original task too but I didn't build on top of that. For easy understanding I have used Zed's original solution he disclosed in his book. Through this anybody who is familiar with the problem and invested enough time into solving it should quickly get my points.

I have made the following amends.

1) Semantical hence less important changes: Zed didn't check on numeric inputs like the ones e.g. for the neutron bomb numeric lock or the number for selecting an escape pod. I've added that. Created own exception types for the above.

2) To be able to utilise a combat engine I have inserted a new PopUpRoom in his tightly woven texture of action scenes or rooms. This one comes after the LaserWeaponArmory. Recently it surely follows the armory as the next scene but you can adjust the chances to 50% by changing my code to this: return["the_bridge", "popup_room"][randint(0,1)]

3) PopUpRoom serves as spring board to the combat engine. 
The combat engine or battle engine as I called it can play any game you want. I have created a dice game as an example on which the duel between the Gothon and you (Blondy, sorry) or any other heros (you name them) will be decided. This will use two random numbers between 1 and 6 and adds them together mimicing the event when somebody is throwing two dice at once. The higher number wins.
You can create an infinite number of new games and call them from the PopUpRoom scene. 
My game is using a decorator structure because I am a) obsessed by them recently and b) through this the random number  generator can easily be replaced with any other function of your choice. 
You can use the same structure too. 
