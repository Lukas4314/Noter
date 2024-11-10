---
~
---
## Opgave 1

### A)
Løs de 2 ligninger herunder vha. Gauss elimination
$$\begin{align*}
5x+3y&= 12\\
2x+5y&= 1
\end{align*}$$
vi skriver det på udvidet matrix form for koefficienterne
$$
\left[
\begin{array}{cc|c}
5 & 3& 12 \\
2 & 5& 1 \\
\end{array}
\right]
$$
Nu kan vi lægger rækkerne sammen og trække dem fra hinanden indtil vi har det på reduceret row echelon form

$R_{1}-2 \cdot R_{2} \to R_{1}$ 
$$\left[
\begin{array}{cc|c}
1 & -7& 10 \\
2 & 5& 1 \\
\end{array}
\right]$$
$R_{2}-2 \cdot R_{1} \to R_{2}$
$$\left[
\begin{array}{cc|c}
1 & -7& 10 \\
0 & 19& -19 \\
\end{array}
\right]$$
$\frac{R_{2}}{19} \to R_{2}$
$$\left[
\begin{array}{cc|c}
1 & -7& 10 \\
0 & 1& -1 \\
\end{array}
\right]$$
$R_{1}+7 \cdot R_{2} \to R_{1}$
$$\left[
\begin{array}{cc|c}
1 & 0& 3 \\
0 & 1& -1 \\
\end{array}
\right]$$
vi kan her aflæse på vores koefficient matrix at $x=3$ og $y=-1$

### B)
Beregn værdien af udtrykket herunder:
$$\begin{pmatrix}5 & -1 \\ 3 & 2\end{pmatrix} \cdot \begin{pmatrix}2 & 3 \\ 3 & 2\end{pmatrix}$$
vi skal her bare gange 2 matrixer sammen, hvilket giver en ny matrix
$$\begin{pmatrix}5 \cdot 2+(-1) \cdot 3 & 5 \cdot 3+(-1) \cdot2  \\ 3 \cdot2+2 \cdot3 & 3 \cdot 3+2 \cdot 2\end{pmatrix}$$
nu skal vi bare reducere denne matrix
$$\begin{pmatrix}7 & 13 \\ 12 & 13\end{pmatrix}$$
og vi har dermed fundet svaret som er $\begin{pmatrix}7 & 13 \\ 12 & 13\end{pmatrix}$

