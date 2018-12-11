# RC-vision-car
this project aims to control a car so that it can move using signs ..
the main.py code is the one that detects the signs and moves the car but the command.py is needed as is has the functions that are used to control the arduino which in turn controls the motors.
the signs can be found in this project but changing them shouldn't be that hard as the color can be changed with changing the values of this part of the code:

 lower_blue = np.array([90,80,50])
 upper_blue = np.array([110,255,255])
 
 
 material list for the project :
 1-an RC car chassis
 2-raspberry pi 3 modelB
 3-PI camera (we used V1 but V2 or really any web cam should work)
 4-arduino uno (or any available arduino board )
 5- motor drivers (we used L298n but any one available should do the job)
 
 
 
 last we leave this video showing the project running using this code:https://www.youtube.com/watch?v=utAhb-LCONQ&feature=youtu.be
 
 
 as for the remaining scripts they are trials using openCV as :
 trial 2 is face detection on the Pi camera
 trials 3-4 are also face detection but using the dlib library 
 trials 4-6 are older versions of the command.py
 
 
 at last we thank this contribution as his work is essenstial to our work:https://github.com/nikgens/TankRobotProject/tree/master/signRecognition?fbclid=IwAR0tsNbo8MZ9ZEHTadfSWdGIeY_5Rd4q_1HxUwe70qC1POXjGsQDXNC2CkI
