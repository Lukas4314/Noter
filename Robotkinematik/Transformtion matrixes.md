A tranformation matrix is a matrix by the size of 4x4 and its values are:
$$T=\begin{pmatrix}{}^{A}_{B}R_{3x3} & {}^{A}P_{B_{org}} \\ w^{T} & s\end{pmatrix}$$
here R is the rotation matrix, P is the translation matrix, and w^t is the shearing factor, and s is the scale factor. This combined is called a transformation matrix which bassicly can be used with a single point in frame A to transform it into frame B with B's rotation and position and everything else.
when having a point it consist of 3 values so to be able to multiply the 2, the point last value should be the scaling factor like this:
$${}^{B}p=\begin{pmatrix}x \\ y \\ z \\ s\end{pmatrix}$$
this makes it possible to multiply the 2 matrixes.
in our case in this course the sheering and scale would always be 0 for the shearing and 1 for the scale.
Like rotation matrices the transformation matrices can be multiplied and combined the same way as rotation matrices.

## Example
lets say you only have a rotation matrix, or a translation matrix, the transformation matrix would be:
$$T=\begin{pmatrix}1 & 0 & 0 & x \\ 0 & 1 & 0 & y \\ 0 & 0 & 1 & z \\ 0 & 0 & 0 & 1\end{pmatrix}$$
$$T=\begin{pmatrix}a & b & c & 0 \\ d & e & f & 0 \\ g & h & i & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$
the first matrix is only consisting of translation
the second matrix is only the rotationmatrix



## Homogenous coordinates


