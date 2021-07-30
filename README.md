# AI_Virtual-painter

In this project,some of our online class instructure will use external board.So i created virtual painter in our system screen.[Eiether use white or black or on screen board] 

# Use case

In a pandamic situation,all of our school childerns study all subjects in online mode.Some of Instructors teach without blackboard feels uncomfortable to explaining concepts.
All of instructors will not able to buy any external board to explain our concepts.So,i worked and try to reduce this issue,with help of OpenCv and mediapipe,I create an virtual black or white or in screen mode and with help of finger you able to draw it in various colors.

# Requirements

        pip install opencv-python
        pip install mediapipe
        
# How its work

* To create a paint logo with same of you system display resolution you want working on it.
* Add and fit the painter logo top of our screen.I create a logo in : https://www.canva.com/
* First,with help of mediapipe to detect and track a hand model.
* By using hand landmark image to set two classes , one is used for drawing mode and another is used for changing colours or erasing.
* If you want use white board or black board or on screen board.

