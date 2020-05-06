# Jetpack-Joyride
Python game emulating the famous Android game Jetpack-Joyride

## Usage Instructions
### Running the game

 `git clone https://github.com/Vikr-182/Jetpack-Joyride/`
 
 `cd Jetpack-Joyride`
 
 `python3 game.py`
 
 ### Keyboard controls
 
 | Key | Use | 
 |-----|-----|
 |  `w`  | Up |
 |  `a`  | Left |
 |  `d`  | Right |
 |  `s`  | Down |
 |  `(space)`  | Activate Shield |
 |  `x`  | Shoot bullets |
 |  `l`  | Activate Dragon |
 |  `q`  | Quit |
 

### Additional Libraries

- Colorama
To install the library, type the command - 

`pip3 install colorama`
- Numpy
To install the library, type the command - 

`pip3 install numpy`
Recommended to be played in Ubuntu v12.0 or higher having `aplay` builtin for better effects.
 

## File stucture 

![Structure](../images/drawing.jpg)


   Legend - 
   
   
 | Figure | Type| 
 |-----|-----|
 |  ![Parent Class](../images/parent.jpg)  | Parent Class |
 |  ![Inherited Class](../images/inherited.jpg)  | Inherited Class |
 |  ![Object](../images/object.jpg)  | Object (Instance) |
 
 ## Mission
 Din is a mandalorian living in the post-empire era. He is one of the last remaining members of his clan
in the galaxy and is currently on a mission for the Guild. He needs to rescue The Child, who strikingly
resembles Master Yoda, a legendary Jedi grandmaster. But there are lots of enemies and obstacles in
his way, trying to prevent Din from saving Baby Yoda. Din is wearing classic mandalorian armour and
has a jetpack as well as a blaster with unlimited bullets. You've got to help him ght his way through
and rescue Baby Yoda.

 ## Characters 
 
 ### Din 
- Contains 10 lives initially 
- Has unlimited bullets
- Also has a pet dragon who it can call anytime to help him on his mission !! 

### Boss
- Appears at last
- Continously throws ice-balls at the player
- Has 100 lives

### Dragon
- Has only 1 live
- Can only traverse in the y-direction 

## Additional Details

#### -Firebeams
 - Oriented at 0,45,90,135 and 180 degrees.
 - Din can shoot down any of the beams with it's bullets.
 - Randomly placed on the board
 
 #### -Magnet
 - Attracts Din in the x direction
 - Can only be dis-activated when Din over-rides it.
 
 #### -Shield
 - Appears around when pressed the space key.****
 - Lasts for  10 seconds, requires 60 seconds cool up time.
 
 #### -Speed Bost
 - Can be collected on the way.
 - Will speed up the game by 3x.
 