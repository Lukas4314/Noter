
## prikprodukt af en vektor kan findes som:
$$\vec{a} \cdot \vec{b} = a_{1} \cdot b_{1}+ a_{2}\cdot b_{2}....$$
## krydsproduktet af en vektor kan findes som:
$$\vec{a} \times \vec{b}= \begin{pmatrix}a_{2}\cdot b_{3}-a_{3} \cdot b_{2} \\ -\left (a_{1}\cdot b_{3}-a_{3} \cdot b_{1} \right ) \\ a_{1}\cdot b_{2}-a_{2} \cdot b_{1}\end{pmatrix}$$
dette giver en vektor som er vinkelret ind på begge vektorer med retning som kan findes med højrehåndsreglen:
![[Pasted image 20241209121741.png]]



## vinklen mellem 2 vektorer kan findes som:
$$cos(v)= \frac {\vec{a} \cdot \vec{b}} {|\vec{a}| \cdot |\vec{b}|}$$
eller:
$$|\vec{a} \times \vec{b}|=|\vec{a}| \cdot |\vec{b}| \cdot sin(\theta)$$

## Projektering af vektor ind på en anden:
$$\vec{a_{\vec{b}}}= \frac {\vec{a} \cdot \vec{b}} {|\vec{b}|^{2}}\cdot \vec{b}$$
her er vektoren a projekteret ind på vektoren b

i Henriks slides stod det som:
![[Pasted image 20241209121606.png|300]]





## Mindste afstand mellem punkt og linje 2D:
$$dist(p,l)= \frac {|ax_{1}+b-y_{1}|} {\sqrt{a^{2}+1}}$$
her er P et punkt i 2D og l er en linje af formen y=ax+b

## Afstand mellem et punkt og en linje

Givet et punkt $P(x_{0},y_{0},z_{0})$ og en linje l, som er defineret ved:

- Et punkt $A(x_{1},y_{1},z_{1})$ på linjen, og
- En retningsvektor $\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}$

Afstanden d fra P til l er givet ved:

$$d= \frac {|\vec{AP}\times \vec{v}}{|\vec{v}|}$$
her er AP vektoren fra A til P



## Afstand mellem punkt og plan
givet en plan på normalform: $$ax+by+cz+d=0$$
findes afstanden som:
$$d= \frac {| ax_{0}+by_{0}+cz_{0}+d |} {\sqrt{a^{2}+b^{2}+c^{2}}}$$
her er det er punkt med koordinaterne: $P(x_{0},y_{0},z_{0})$ 


## Afstand mellem 2 linjer
hvis man har 2 linjer med parameterfremstillinger:
$$\begin{align*}
l_{1}=\vec{a_{1}}+t \cdot r_{1}\\
l_{2}=\vec{a_{2}}+t \cdot r_{2}
\end{align*}$$
findes den mindste afstand mellem dem som:
$$d= \frac {| (\vec{a_{2}}-\vec{a_{1}}) \cdot (\vec{r_{1}} \times \vec{r_{2}}) |} {|\vec{r_{1}} \times \vec{r_{2}}|}$$
