
### Eksamensopgave februar 2021

Opgave 2
Betragt funktionen 
$$f(x,y)=e^{x+2y} \cdot sin(xy)$$
a)
bestem gradienten af funktionen i punktet $(\frac{\pi}{2},1)$ 
$$\nabla f(x, y)=\begin{pmatrix}\frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y}\end{pmatrix}$$
$$\frac{\partial f}{\partial x}=e^{x+2y} \cdot sin(xy)+e^{x+2y} \cdot y \cdot cos(xy)$$
$$\frac{\partial f}{\partial y}=2e^{x+2y} \cdot sin(xy)+e^{x+2y} \cdot x \cdot cos(xy)$$
vi kan her indsætte ind i punkterne
$$\begin{align*}
\frac{\partial f}{\partial x}&= e^{\frac{\pi}{2}+2} \cdot sin(\frac{\pi}{2})+e^{\frac{\pi}{2}+2} \cdot cos\left(\frac{\pi}{2}\right)\\

\frac{\partial f}{\partial x}&= e^{\frac{\pi}{2}+2}\\
\end{align*}$$
$$\begin{align*}
\frac{\partial f}{\partial y}&= 2e^{\frac{\pi}{2}+2} \cdot sin(\frac{\pi}{2})+e^{x+2} \cdot \frac{\pi}{2} \cdot cos(\frac{\pi}{2})\\\\
\frac{\partial f}{\partial y}&= 2e^{\frac{\pi}{2}+2}
\end{align*}$$
vi kan nu opskrive gradienten
$$\nabla f(x, y)=\begin{pmatrix}e^{\frac{\pi}{2}+2} \\ 2e^{\frac{\pi}{2}+2}\end{pmatrix}$$
b)

bestem normalvektoren n til overfladen $z=f(x, y)$ i punktet $(\frac{\pi}{2},1)$ 
vi kan her bruge formlen
$$\vec{n}=\begin{pmatrix}f_{1}(a,b) \\ f_{2}(a,b)  \\ -1\end{pmatrix}$$
vi kender allerede værdien af de partielle afledte i punktet $(\frac{\pi}{2}, 1)$ og vi kan derfor bare indsætte dette
$$\vec{n}=\begin{pmatrix}e^{\frac{\pi}{2}+2} \\ 2e^{\frac{\pi}{2}+2}  \\ -1\end{pmatrix}$$
vi har derved normalvektor til grafen i punktet $(\frac{\pi}{2},1)$

c)
bestem tangentplanens ligning i punktet $(\frac{\pi}{2},1 )$
formlen for en plan kan findes som:
$$z=f(a,b)+f_{1}(a,b) \cdot (x-a) + f_{2}(a,b) \cdot (y-b)$$
vi kender her det hele bortset fra $f(a,b)$ som i vores tilfælde er $f(\frac{\pi}{2},1)$
$$\begin{align*}
f(x,y)&= e^{x+2y} \cdot sin(xy)\\
f(\frac{\pi}{2},1)&= e^{\frac{\pi}{2}+2} \cdot sin(\frac{\pi}{2})\\
f(\frac{\pi}{2},1)&=e^{\frac{\pi}{2}+2}
\end{align*}$$
vi kan nu indsætte dette ind i formlen for planen
$$z=e^{\frac{\pi}{2}+2}+e^{\frac{\pi}{2}+2} \cdot (x-\frac{\pi}{2}) + 2 \cdot e^{\frac{\pi}{2}+2} \cdot (y-1)$$
dette kan så reduceres
$$\begin{align*}
z&= e^{\frac{\pi}{2}+2} \cdot (1+x- \frac{\pi}{2}+2(y-1))\\
z&= e^{\frac{\pi}{2}+2} \cdot (x+2y-\frac{\pi+2}{2})\\
\end{align*}$$




