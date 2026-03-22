# Motion Time Calculator(rover)

## What this program do
This program helps you figure out how long it takes to travel from one point to another in a straight line.  
You give it:
- The starting point (origin coordinates)
- The ending point (destination coordinates)
- Your starting speed
- How quickly you accelerate
- The fastest speed you can reach

It then calculates:
1. The distance between the two points.
2. How long it takes to reach your top speed.
3. How much distance is left once you’re at top speed.
4. The total time needed to cover the journey.

---

## way of using it
1. Run the program.
2. Enter the origin coordinates 
3. Enter the destination coordinates
4. Enter your starting speed ,zero if start from initial
5. Enter your acceleration 
6. Enter your maximum speed 

The program will then print:
- The distance between the points.
- The total time required to travel that distance.

---

## important things
- If the destination is close, you might reach it before hitting your top speed. The program handles that case too.
- Make sure acceleration is greater than zero, otherwise the math won’t work.
- The output is in each seconds for time and unit meters  for distance.

---

## constraints(condition checking)
- Add checks for invalid inputs (like negative speeds).
- Format the output to show fewer decimal places.
- Handle special cases like zero acceleration more gracefully.







