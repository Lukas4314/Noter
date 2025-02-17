
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
