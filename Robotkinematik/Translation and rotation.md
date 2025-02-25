
### Types of joints
#### Revolute:
on rotation in one angle

#### Prismatic:
linear movement

#### Cylindrical:
linear movement but with a twist

#### Spherical:
like a ball socket

#### Planar:
movement on a plane

#### Screw joint
like a screw where rotation becomes linear movement


### Degrees of freedom (DoF)
DoF is the number of variables needed to define a specific position of every joint.



### Robot workspace
the area where the robot can reach and is restrained by the structure of the robot and the design.



### Notation 
![[Pasted image 20250211091024.png]]
Notation vary depending on who is using it and there is not one notation everyone uses

### Translation
a translation is a vector used to move point to get a new point 
![[Pasted image 20250211091251.png|600]]
a translation can both be viewed as a point moving of the reference frame moving in the opposite direction
A translation is different in different frames, meaning a translation have some values in one frame, but some other values in another frames, but viewed from a common frame the translation is the same. meaning moving a point in one frame with a translation is result in the same as moving the same point in a different frame because the point would have different values according to the frame, and the translation would also have different values but would be the same translation in different frames.


### Rotating frames
when rotating something it can be set up as a matrix as:
![[Pasted image 20250211093603.png|600]]
The notation here is that the result is how you rotate A to B since the A is on top 

#### Rotation with angles
When rotating a set amount of degrees the result can be find using trigonometri.
The result of doing this would be:
![[Pasted image 20250211094656.png]]
when rotatin around the z axis

### Rotation matrices properties
![[Pasted image 20250211094813.png]]

### Using the rotation matrix
it is possible to use the rotation matrix to rotate a point. if a rotation matrix called $^{A}_{B} R$ and having a point in B frame it is possible to multiply the point with the matrix to rotate it, a set amount of degrees depending on the rotation matrix. It is important now that if you have a point in frame B the rotation matrix has to be $^{A}_{B} R$ and not $^{B}_{A} R$



### Combining rotation matrices
if you have an rotation matrix ${}^{A}_{B}R$ and a matrix called ${}^{B}_{C}R$ we can get the matrix called:
$${}^{A}_{C}R={}^{A}_{B}R \cdot {}^{B}_{C}R$$

This can be used if you have a frame you want to rate in a complex way, you can first make multiple rotation matrix, to rotate it into the desired position meaning, you make one rotation making it a new frame but not the desired but a frame which is closer, and then keep doing that and finally multiply all the rotation matrices togeter to end up with one roation matrix which can be used make the whole rotation.


# Orientation 
in contrast to position where position is measured in real numbers orientation is measured in degrees and therefore spheres and circles SO(3). 
Orientation describes an state where a rotation performs an action to rate something. it is the same with position and translation when talking about positions and placement.


### Angle-Set Conventions
angle set conventions are a familiy consisting of auler angles and fixed angles.
the diffrence between euler and fixed angles is that fixed angles are still where euler angles moves and the angles are therefore in relative to the what it is describing.
![[Pasted image 20250225091504.png]]

therefore the meaning of the rotation of the euler angles depends on earlier rotations around its axis. like if the plane rotate around the yaw and then rotate around the roll the absolute rotation direction changes. you can also say that euler angles only works in local frames where the frame follows whatever we are rotating, and the frame rotates too.

the syntax for the difference is an ' for the euler angles like: $R_{x´y´z´}$ where the ´ means the angles are changing which makes sense for euler angles. the fixed angles, are the same without the ´.

### Euler angles
when using euler angles to rotate something, just like mentioned earlier in rotation multiple times. a combination of rotations, can be multiplied to get a final rotation matrix to achieve any rotation. the rotation should be multiplied in the way which makes sense meaning the first rotation should be multiplied with the second rotation which then should be multiplied with the next and so on.

### Fixed angles
Here the rotation is around a fixed frame meaning the rotation is not the same as euler angles. Doing it this way when doing multiple rotations to achieve a specific rotation, you have to multiply the rotation matrix in the reversed order. meaning the last rotation you did needs to be multiplied with the second last rotation last time, which then needs to be multiplied with the third last rotation last time and so on.


### Gimbal lock
the gimbal lock is a problem which appears when 2 axis aligns like the picture below:
![[Pasted image 20250225100610.png]]
if a plane steers up, it at some time reach a point where i has to rotate 180 degrees instant for it to always be upside down which is the problem.
There is 2 sides of this problem, the first is the mechanical problem where you get a problem because you have to move very fast.
the second problem is the mathematical problem which appears because the axis align and you therefore lose a degree of freedom.
## From rotation matrix to fixed angles
when having an rotation matrix you can find the fixed rotation which is the result
it can be calculated from this:
![[Pasted image 20250225101719.png]]![[Pasted image 20250225101726.png]]
![[Pasted image 20250225101740.png]]
