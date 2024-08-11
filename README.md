Mariam Machaidze's internship projects and working progress.

overall task: I am given a NxN grid of resistors. One of the resistors inside the grid is broken. I have to find which one is broken based on values on perimeter of the grid.
- task 1: make a data for perimeter of the grid.
- task 2: figure out which resistor is broken.



to do:
 - If the resistor broke in the inside, it means one of the resistors can be RV01. I want to see what happens in this case.
 - Finish making recursion

30 July:
 - checking 4 possible inside broken resistors in example of 4x4 grid. 
 - Steps to check codes:
 1. saving_voltage_data.py - change variable broken to any of these: V11, H11, V12, H21.
 2. after running the code the data will be downloaded to the path that was chosen in the code
 3. making perimeter - upload the data by changing variables beginning and ending
 4. after running the code new data will be downloaded to the path that was chosen in the code
 5. finalizing recursion - upload the data by changing the path and run
 6. The output meanings - 0 - H11, 1 - V12, 2 - H21, 3 - V11
 - These 4 examples are working!
 - I am starting working on considering that connection resistor to be broken. (I'm gonna continue this tomorrow too)

28 July:
 - I am working on finilizing recurion solution.
   - First, I need to finish making good looking data. file - making perimeter. - finished this.
   - I made partially working recursion model. It still needs improvment.
     1. consider connection resistor to be broken.
     2. consider n > 4 higher grid
     3. returning answer looking like HV11.

26 July:
 - I figured out how to make recursion of the even-noded-side grid.

