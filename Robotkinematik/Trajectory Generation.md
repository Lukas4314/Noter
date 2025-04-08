trajectory generation is generating a path to move in a line from one point to another.
is is therefore not setting the angles for the joint to a specifik, but actually you need to define every small step for a linear path and takes speed, constrains and so on into account.
![[Pasted image 20250408102943.png]]
The offline is basically making the robot Discretize the path into small steps.

### Different spaces
there are different spaces, either cartesian or joint spaces. Cartesian spaces are linear movement, and joint spaces are often curved because the shortest distance in joint spaces are the ones where the joints have to move as little as possible, and therefore does a curve.




### Velocity profiles
moving from one place to a different place, can be done in a lot of different ways depending of how much and when you accelerate and deaccelerate.
![[Pasted image 20250408103513.png]]

When traveling in a trapezoidal profile, there is multiple ways to define this way
![[Pasted image 20250408103716.png]]
depending on what is needed, if it is total time, max acceleeration or something else, this can be calculated the whole trajectory

![[Pasted image 20250408104641.png]]
this is just simple physics.


The trapezoidal has theoretically infinite jerk which is the derivative of acceleration which is bad, and harms the gears. Therefore you might use a polynomium instead:
![[Pasted image 20250408105951.png]]
Now to achieve a, b and c we set up some constrains:
![[Pasted image 20250408110035.png]]
this makes it possible to get what is wanted for the polynomium and we can now use this velocity profile instead, which has constant jerk.
We can also get higher polynomium order for smoother jerk like, 5'th order polynomiums
![[Pasted image 20250408110207.png]]


for multiple joints, it is done separately since this is for a single joint, but to make it easier to calculate it can be combined into vectors:
![[Pasted image 20250408110432.png]]



All of this is for joints spaces, meaning we wont get a linear movement anymore.



### Linear trajectories through multiple points
If we want to move between multiple points, we can use trapezoidal if we want to stop at the middle point, or we can use polynomium if we want a continuos movement.
![[Pasted image 20250408111015.png]]
