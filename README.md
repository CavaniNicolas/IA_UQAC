# AI projects as part of a UQAC course

## MansionCleaner

Goal is to implement a cleaning robot for a mansion.
The agent will evolve in a matrix in which dirt and jewels are generated randomly.
The robot has to clean dirt, pickup jewels and be the most efficient as possible.
Every action cost him energy and reduces his performance, he also gets a penalty if he sucks a jewel with dirt instead of picking it up first.
Viewing the mansion in order to re generate his list of actions to perform also costs him energy.
Depending on his performance, the robot is able to adapt the maximum number of actions he will do before looking at the entire mansion again. This allows him to detect more frequently newly added dirt and jewels if he needs it.
Four search algorithms were implemented and can be passed to the robot for him to choose his actions.
- non informed search :
  - Bread-First Search
  - Depth-First Search
- informed search :
  - Greedy search
  - A*
  
  ![appScreenshot](https://github.com/CavaniNicolas/IA_UQAC/blob/main/MansionCleaner/doc/appScreenshot.PNG)
