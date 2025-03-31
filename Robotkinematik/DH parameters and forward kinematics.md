Forward kinematics is used to calculate how a movement joint of a robot effects the end result for the robot. Like moving the base of the robot rotates the whole robot and the end part of the rotate can be calculated by having the transformation matrix of each joint.

## 2R Planar
this means we have 2 revolute joint which moves in a plane, which is basically the example showed in the image here:
![[Pasted image 20250311083739.png]]
we can here calculate the position (x, y) by having an additional frame in the last joint
the result can then be calculated as:
![[Pasted image 20250311084646.png]]
the second frames origin are at the same position as the (x, y) meaning if we want to calculate the (x, y) in the first frame we have to multiply ${}^{0}_{2}T$ with the point ${}^{2}P=\begin{pmatrix}0 \\ 0 \end{pmatrix}$
because the (x, y) point is in the origin of frame 2, and if we want to get the point in frame 0, we have to multiply the point with the transformation matrix.
we just need to remember to add the 1 as the scale for the point to be able to multiply them together so the point is:
$${}^{2}P=\begin{pmatrix}0 \\ 0 \\ s\end{pmatrix}$$


Another way of achieving the tranformation matrix is this:
![[Pasted image 20250311085150.png]]
we now have a different way of getting to the same result. The individuelle transforms are easier to understand this way.

### Parameters for a robot
we want a standardized way on how joints and links are set, and frames. We therefore have the DH parameters, but there is also a way called Modified DH which is another way to set the parameters. There is of course a bunch more, but these are the two we would use, and mainly the modified DH parameters.

To understand this you need to understand the different types of joint which needs different amount of specification to define which way a joint points.
For DH parameters, we say that every type of joint can be decomposed of a revolute joint or a prismatic. Prismatic joint is the joint to go forward and backwards and revolute describes a rotation.


## Links
Link are the connection between 2 links which allows relative motion
When there is a link between 2 join they must have relationship between some of the links:
![[Pasted image 20250311092406.png]]
The skew where the 90 degree angle is are when the axes are closest to each other, for visuallising you need to remember it is in 3D, and therefore the distance on the sketch above. It is also the line which is perpendicular to both axes

These links can be described by 2 parameters:
![[Pasted image 20250311092439.png]]
and also:
![[Pasted image 20250311092513.png]]

this can all be assembled into an table and used to describe the relationship between joints.
![[Pasted image 20250311092612.png]]
here the joint before is called joint i-1 and the next joint is called i, and so on.
The meaning of everything is:
$\alpha_{i-1}$ is the rotation around the x axis
$a_{i-1}$ is the distance between the links at the point of interest where they are perpendicular for skew axis and different for other axis which is explained earlier
$d_{i}$ this is the distance for the point of interest to the joint along its z axis
$\theta_{i}$ this is the rotation around the z axis
also check earlier images and so on.




If we then have these value in place, we then need to place frame for alle the joints, and the systematically way of doing this is:
![[Pasted image 20250311092825.png]]
this is how frame are supposed to be placed, and what way the direction of the frames axes needs to be. This example are only for skew axes, because the line between was defined as the perpendicular axes, where as parallel axes has infinite many perpendicular, and intersecting axis which means it is a point.

When having intersecting axis, the X axis is placed perpendicular to the 2 axis, mening it is possible to find it using the cross product. 

When the lines are parallel the origin of the frame is set to minimize the distance $d_{i-1}$ or meaning $d_{i-1}=0$

for the first link and the last link, you do not have a next link or a earlier link which means to set the frame on the first link the frame should just be the same as the reference frame or main frame.
And the last frame should the same as the second last frame.

### Recipe for placing the frames
![[Pasted image 20250311094209.png]]




## Difference between modified and standard
![[Pasted image 20250311094334.png]]
the difference are basically on how the frame is rotated based on the link or the earlier link

### Example
![[Pasted image 20250311101608.png]]
here is the filled table for the robot.


## From DH parameters to transformmatrix
To get a transformation matrix we first have to rotate around the x axis $\alpha_{i-1}$ degrees and then translate it along the x axis for $a_{i-1}$ amount, and the translate it $d_{i}$ along the z axis, and then rotate it around the z axis for $\theta_{i}$ and all in all you will get a transformation matrix looking like this:
![[Pasted image 20250311104722.png]]


This can then be chained together for all joints, which then could be used to for calculate the end based on the variables for the joints
