Lets say we have a point Q seen from frame B meaning it is: ${}^{B}Q$ the difference in position from the frame is the velocity, but if the frame moves according to another frame, frame A, the point seems to move from the B frame, meaning velocity is relative.
Velocity can be defined as:
$$^{B}V_{Q}=\frac{d}{dt}{}^{B}Q$$
but as mentioned, the velocity is relative, meaning there can be an velocity from another frame and is written as:
$$^{A}({}^{B}V_{Q})= \frac {{}^{A}d} {dt}{}^{B}Q(t)$$
we can therefore also write it as an rotation matrix, to make the velocity translate:
$$^{A}({}^{B}V_{Q})= {}^{A}_{B}R\space  {}^{B} V_{Q}$$
this only works, when the frames are not moving, since it only changes the direction, and therefore does not change the value of the velocity.

### Angular velocity
this describes, how a frame rotates relative to another frame, and is written out as:
$$^{A}\Omega_{B} \space \space \text{or} \space \space {}^{A}\omega_{B}$$
since a frame can rotate freely around a given axis, it is made up of an unit vector describing the axis of rotation and a magnitude describing speed
It is written out as:
$$\boldsymbol{\Omega} = \Omega \cdot \vec{u}$$
here the first omega is in bold, and the non bold omega has the unit $[\frac{rad}{s}]$

### Linear velocity
here we have an translation between 2 frames change over time.
Here we can get the velocity of a point in a reference frame as:
$$^{A}V_{Q}= {}^{A}V_{BORG}+ {}^{A}_{B}R \space {}^{B}V_{Q}$$
here we have the velocity of the point multiplied by the rotation of the frame so account for the point moving, and then we also have the frame moving taken into account.


### Rotational velocity
here we have an velocity which rotates relative to each other.
See the image:
![[Pasted image 20250408084105.png]]
here the bottom point is frame B, and the point does not have an velocity in frame B, because the frame is the only thing which moves.
the first equation is derrived using trigonometri, where $|Q|\sin(\theta)$ is the hypotheneuse, and when $\Delta Q$ is very small it can be seen as 90 degree triangle, because it is so small. therefore it is possible to use $\sin(\Omega \Delta t)$, on the image above it does not say sinus, but in the PowerPoint he showed is said sinus as:
$$|\Delta Q| = (|^{A}Q|\sin(\theta)) \cdot (\sin(|^{A}\Omega_{B}|\Delta t))$$
which is the hypotenuse multiplied by the sinus of the near katete.
And because the sin to a small angle is is the same $\sin(a) = a$ of a is very small is can be written as:
$$|\Delta Q| = (|^{A}Q|\sin(\theta)) \cdot (|^{A}\Omega_{B}|\Delta t)$$
because delta t is very small
Inigo then further derrived it to a crossproduct, which i did not see. But he ends up with:
$$^{A}V_{Q}= {}^{A}\Omega_{B} \times {}^{A}_{B}R \space{}^{B}Q$$
of if the point is in frame A:
$$^{A}V_{Q}= {}^{A}\Omega_{B} \times{}^{A}Q$$
## Combination of movement.
if everything moves it can be written as:
$$^{A}V_{Q}= {}^{A}V_{BORG}+ {}^{A}_{B}R \space {}^{B}V_{Q}+ {}^{A}\Omega_{B} \times  {}^{A}_{B}R \space {}^{B}Q$$
which takes into account the frame, which moves, in the first part, and then the point moving in frame B into account in the second part, and then the rotation in the last part.


### Rotation matrix over time
here we have a rotation matrix, which changes over time, and therefore makes an angular rotation.
We therefore describe an rotation matrix as:
$$R(t)$$
since rotation matricivies are othogonal:
$$R(t) \cdot R^{T}(t) = I$$
meaning its transpose is the same as the inverse.
we now take the differentiate both side in case of time and get this:
$$R'(t) R^{T}(t)+\left (R'(t)R^{T}(t) \right )^{T}=0$$
We now define S(t) as:
$$S(t) = R'(t)R^{T}(t)$$
and can then rewrite our equation:
$$S(t) + S^{T}(t)= 0$$
and this is a skew symmetric  matrix, which means: $S^{T}= -S$ and we can therefore rewrite this as:
$$R'(t) = S(t)R(t)$$
we can then relate skew symmetric matrices to angular velocities:
![[Pasted image 20250408093303.png]]
this is kinda equivalent to the angular rotation which was derrived earlier.

In practice i dont think we gonna need this and are just another proof of the angular velocities.
It is just another way to express angular velocity, and this time as a skew axis
### Other representation of angular  velocity
we can also represent angular velocity as euler angles, but it will not be used, since it does not make any sense when talking about velocities, since euler angles are rotations around axis, in a specifik order and by a specific amount.

## Velocity of links
![[Pasted image 20250408094910.png]]
1.
Since the rotation using DH parameters always revolves the z axis we can write it as:
$${}^{i+1}\omega_{i+1, \vec{\theta'}_{i+1}}= \theta'_{i+1} \cdot {}^{i+1}\vec{Z}_{i+1}  =\begin{pmatrix}0 \\ 0 \\ \vec{\theta'}_{i+1}\end{pmatrix}$$
here the syntax is the frame i+1, where the omega for the i+1 frame and the theta in the same frame, meaning $\omega_{i+1}$ is the speed for that frame specifik frame, and it is seen from the same frame meaning it can be written as, ${}^{i+1}\omega_{i+1}$ and the rotation it is doing is according to the change og thetas, in the same frame so $\theta'_{i+1}$ so to say the omega is rotating around the right one is:
${}^{i+1}\omega_{i+1, \vec{\theta'}_{i+1}}$

2.
$$^{i}\omega_{i+1} = {}^{i}\omega_{i}+ {}^{i}_{i+1}R \theta'_{i+1} {}^{i+1}\vec{Z}_{i+1}$$
here we have the angular velocity for the next frame equal to the angular velocity of the current frame summed with, the rotation for the next frame, along the z axis due to the how DH parameters specify how the frames needs to be put.

3.
$$^{i}v_{i+1}= {}^{i}_{i}v+{}^{i}\omega_{i} \times {}^{i}P_{i+1}$$
here we have the velocity for the next frame, is the velocity for the current frame, plus the cross product of the angular velocity and the vector to the next frame

4.
here the result from before is just multiplied with an rotation matrix, to rotate everything.
![[Pasted image 20250408101104.png]]



#### For prismatic joints
for prismatic joints it can be calculated as:
![[Pasted image 20250408102302.png]]
