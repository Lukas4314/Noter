vektorer kan skrives som:
$$\vec{a}=(a_{1}, a_{2}, a_{3})=a_{1} \vec{i}+ a_{2}\vec{j}+a_{3}\vec{k}= \begin{pmatrix}a_{1} \\ a_{2} \\ a_{3}\end{pmatrix}$$

### prikproduktet
dette findes ved at summere produktet af elementer i 2 vektorerne:
$$\begin{pmatrix}a_{1} \\ a_{2} \\ a_{3}\end{pmatrix} \cdot \begin{pmatrix}b_{1} \\ b_{2} \\ b_{3}\end{pmatrix}=a_{1} \cdot b_{1}+a_{2} \cdot b_{2}+ a_{3} \cdot b_{3}$$
dette kan bruges hvis et legeme har bevæget sit en strækning $\vec{s}$ hvor den er blevet udsat for en kraft $\vec{F}$ kan arbejdes findes:
$$Arbejde = \vec{F} \cdot \vec{s}$$
det kan også ses i fohold til matricer, hvor man har 2 matricer man gerne vil prikke sammen:
$$m_{1}\cdot m_{2} = m_{1}^{T}\cdot m_{2}$$
her skal det ses som at matricerne begge er søjle vektorer altså, 3 x n

### Krydsprodukt
her kan det findes som:
$$\vec{a} \times \vec{b}=\det \begin{pmatrix}\vec{i} & \vec{j} & \vec{k}  \\ a_{1} & a_{2}  & a_{3} \\ b_{1} & b_{2} & b_{3}\end{pmatrix}$$
når man kryds 2 vektorer får man derved også en vektor som altid er vinkelret ind på de 2 vektorer. 


### Gradienten
Gradienten beskriver hvordan noget hælder i et punkt.
hvis der findes en funktion $f(x, y)$ kan gradienten findes som:
$$\nabla f= \begin{pmatrix} \frac {\partial f} {\partial x} \\ \frac {\partial f} {\partial y}\end{pmatrix}$$
En anden ting er at gradienten altid står vinkelret, ind på niveaukurver eller flader.
hvilket betyder at man egentlig godt kan finde normalvektoren til sin flade som kommer ud af $f(x, y)$.

Hvis man fx har en funktion som hedder:
$$f(x, y) = z$$
kan man skrive det om sådan at det bliver:
$$g(x, y, z)=f(x, y)-z=0$$
her kan man så finde normalvektoren til denne flade som:
$$\nabla f= \begin{pmatrix} \frac {\partial g} {\partial x} \\ \frac {\partial g} { \partial y} \\ \frac {\partial g} {\partial z}\end{pmatrix}$$
## Kædereglen eksempel
vi har her funktionen:
$$w= x^{2}-y^{2}$$
hvor:
$$\begin{align*}
x&= r \cdot \cos(\theta)\\
y&= r \cdot \sin(\theta)
\end{align*}$$
her har vi så kædereglen som siger:
$$\frac {\partial w} {\partial r}=\frac {\partial w} {\partial x} \cdot \frac {\partial x} {\partial r}+ \frac {\partial w} {\partial y} \cdot \frac {\partial y} {\partial r}$$
i vores eksempel får vi så:
$$\frac {\partial w} {\partial r}= 2x \cdot \cos(\theta) - 2y \cdot \sin(\theta)$$
vi får derved også af kædereglen at:
$$\frac {\partial w} {\partial \theta}=\frac {\partial w} {\partial x} \cdot \frac {\partial x} {\partial \theta}+ \frac {\partial w} {\partial y} \cdot \frac {\partial y} {\partial \theta}$$
og derved:
$$\frac {\partial w} {\partial \theta}=-2x \cdot r \cdot \sin(\theta)-2y \cdot r \cdot \cos(\theta)$$
og sådan kan man blive ved.

Man kan også bare tage den hårde ved og differentier det hele på en gang, altså:
$$w= (r \cdot \cos(\theta))^{2}- \left (r \cdot \sin(\theta) \right )^{2}$$
og så herfra bare differentierer i forhold til r og $\theta$

## Hældning i bestemt retning
hvis man nu har en flade f(x, y) og man er intereserret i en hælding i et bestemt punkt, kan det findes som:
$$D_{P,\vec{v}} =\nabla f \cdot \frac {\vec{v}} {|\vec{v}|}$$
## Vektorfelt

hvis man fx har et vektor felt som kan så sådan her ud:
$$\vec{v}= (-y, x)$$
og man har et punkt $p = (1, 1)$ vil punktet i vektorfeltet bliver til:
$$p(1, 1) => \vec{v}=(-1, 1)$$
dette vektorfelt, er egentlig en rotation fordi punktet (-1, 1) bliver til  (-1, -1) osv. altså den kører i ring
man indsætter derfor bare sine punkter ind på x og y plads.
