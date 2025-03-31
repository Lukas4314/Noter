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



Hvis man har en roterende skive som roterer mod uret med vinkelhastigheden $\omega$ kan dette beskrive som et vektorfelt af formen:
$$\vec{r} =- y \cdot \vec{i}+x \cdot  \vec{j}$$
hvis man så ganger  dette med $\omega$ som er  vinkelhastigheden får man et hastighedsfelt:
$$\vec{v} = \omega \cdot \left (-y \cdot \vec{i} + x \cdot \vec{j}\right )$$
### Divergens af et vektorfelt
Hvis man har et vektorfelt $\vec{v}$ skal man for at finde divergens:
$$div \space \vec{v}= \nabla \cdot \vec{v}$$
her er $\nabla$ gradienten
dette kan så omskrives til:
$$div \space \vec{v} = \frac {\partial v_{1}} {\partial x}+ \frac {\partial v_{2}} {\partial y}+ \frac {\partial v_{3}} {\partial z}$$
hvis vi så har et vektorfelt:
$$\vec{v}=\begin{pmatrix}v_{1} \\ v_{2} \\ v_{3}\end{pmatrix}$$
#### Ikke sikker på hvad man bruger det her til:
sætter man så et kontrol element ind, som er en uendelig lille kasse ind og udregner volumen flow igennem af hver af de 6 sider på kassen.
kassen har størrelserne: $$dx, dy, dz$$
hastigheden af ting som løber igennem kassen hvor den er orienteret rigtigt er arealet, altså dx gange med flowraten langs x aksen retning altså $v_{1}$ osv.
desuden antages det at vektorfeltet er solenoidal, hvilket betyde at der ikke må være en kilde, eller "afløb" altså at der bliver tilføjet eller fjernet noget inde i kassen.

igennem denne kasse er der så et volumenflow $Q = v \cdot A$ her er A arealet.
Dette er egentlig bare arealet af de forskellige flader, ganger med vektorfeltet i denne samme retning.

Hvis man så har en strømlinje som på forskellige tidspunkter har samme vektorfelt, og derved samme strømninger kalder man strømlinjen for steady state.

### Eksempler
vi har her vektorfeltet:
$$\vec{v} = \omega \cdot\begin{pmatrix}-y \\ x\end{pmatrix}$$
som er en rotation mod uret. på en skive.
og vi har ikke nogen divergens i dette felt:
$$div \space \vec{v} = \frac {d} {dx} (-y) + \frac{d}{dy}(x)=0$$
har vi derimod et vektorfelt som hedder:
$$\vec{v} = \begin{pmatrix}x \\ 0\end{pmatrix}$$
så vil vi have en divergens på 1:
$$div \space \vec{v} =  \frac {d} {dx}(x) + \frac {d} {dy}(0)    = 1$$

fordi at partiklerne accelerer jo længere man kommer ud af x aksen.

hvis vi så har et punkt i dette vektorfelt: $P = (c_{1}, c_{2}, c_{3})$
hvor vi har at punktet er der ved $t=0$ og vi gerne vil vide hvor der er ved $t=1$ 
her har vi at hastigheden som partiklen bevæger sig med er v og er ændring i strækningen over tiden:
$$\begin{align*}
v &= \frac {ds} {dt}\\
ds&= v \cdot dt\\
s &= \int v dt
\end{align*}$$
dette betyder at vi kan finde punktet det har bevæget sig som:
$$x = c_{1}+ \Delta x=c_{1}+ \int vdt$$
og eftersom at $v_{1}= x$ fra vores vektorfelt har vi at:
$$c_{1}+ \Delta x = c_{1}+ \int x dt$$
eftersom at alt dette skulle være lig med x fra starten kan vi differentierer i forhold til t 
$$\frac{d}{dt}x=\frac{d}{dt} \left (c_{1}+ \int x dt \right )$$
$$\frac{dx}{dt}= x$$
og dette kan så omskrives

$$dt = \frac{1}{x} dx$$
dette kan så indsættes
$$c_{1}+ \Delta x = c_{1}+ \int \frac{1}{x}dx$$
dette kan så integres og laves noget mere med og så ender man med:
$$\vec{r}(t) = \begin{pmatrix}c_{1}\cdot e^{t} \\ c_{2} \\ c_{3}\end{pmatrix}$$
tror ikke det er skrevet rigtigt op her men se billedet her af hans gennemgang:



### Parameterfremstilling
#### Cirkel
Hvis man fx har en cirkel med radius 2 og formlen:
$$x^{2}+y^{2}=2^{2}$$
så vil parameterfremstillingen se sådan her ud:
$$\vec{r}(t)=2 \cdot \begin{pmatrix}\cos(t) \\ \sin(t)\end{pmatrix}$$


#### Elipse
Hvis man fx har en ellipse i stedet, med formlen:
$$\frac{x^{2}}{a^{2}}+ \frac{y^{2}}{b^{2}}=1$$
her er parameterfremsillingen:
$$\vec{r}(t) = \begin{pmatrix}a \cdot \cos(t) \\ b \cdot \sin(t)\end{pmatrix}$$
her er a afstanden cirklen bevæger sig ud af x aksen, og b er afstanden ud af y aksen

#### Linje
hvis man har en linje i 3 dimensioner kan parameterfremstillingen findes, ved et punkt på linjen, og en retingsvektor. Punktet på linjen kan kaldes $\vec{a}$ og retiningsvektoren kan kaldes $\vec{b}$ og parameterfremstillingen bliver derfor:
$$\vec{r}(t) = \vec{a} + t \cdot \vec{b}$$
#### Helix
en helix er en spiral som snurer sig op af en cyllinder i 3 dimensioner
her bliver parameterfremstillingen:
$$\vec{r}(t)= \begin{pmatrix}a \cos(t) \\ b \sin(t) \\ ct\end{pmatrix}$$
en fjedre er fx en helix, og man kan se på parameterfremstillingen at det ca stemmer overens.

### Hastighedsvektoren

Hvis man nu har en linje som bevæger sig igennem det 3 dimensionale rum og har parameterfremstillingen $\vec{r}(t)$ kan hastighedsvektoren findes, ved at differentierer den i forhold til tiden, altså:
$$\vec{v} = \frac {d} {dt} \vec{r}(t)$$
hastighedsvektoren er også den som tangerer linjen.
Man kan derfor også finde enhedstangentvektoren som:
$$\vec{u} = \frac {\vec{v}} {|\vec{v}|}$$
### Eksempel
hvis vi har en elipse:
$$\frac{1}{4}x^{2}+ y^{2}=1$$
og vi gerne vil finde hastighedsvektoren i punktet: $P(\sqrt{2}, \frac{1}{\sqrt{2}})$ 
her skal vi først finde vores parameterfremstilling for en ellipse
$$\vec{r}(t) = \begin{pmatrix}2 \cos(t) \\ \sin(t)\end{pmatrix}$$
og ved at differentiere denne:
$$\vec{v}(t)=\begin{pmatrix}-2 \sin(t) \\ \cos(t)\end{pmatrix}$$
her skal vi så finde t og kan derfor opstille 2 ligninger:
$$\begin{align*}
\sqrt{2}&= 2 \cos(t)\\
\frac{1}{\sqrt{2}}&= \sin(t)
\end{align*}$$
det er her lige meget hvilken en vi løser da svaret bliver det samme:
$$\begin{align*}
t &=  \sin^{-1}( \frac{1}{\sqrt{2}})\\
t &=  \frac{\pi}{4}
\end{align*}$$hvis denne så indsættes ind i vores hastighedsvektor får vi:
$$\begin{align*}
\vec{v}\left (\frac{\pi}{4} \right )&= \begin{pmatrix}-2 \sin(\frac{\pi}{4}) \\ \cos(\frac{\pi}{4})\end{pmatrix}\\
\vec{v}\left (\frac{\pi}{4} \right )&= \begin{pmatrix}- \sqrt{2}\\
\frac {\sqrt{2}} {2}\end{pmatrix}
\end{align*}$$

### Rotation af vektorfelt (Curl)
på dansk bliver det bare kaldt for rotation og kan findes som:
$$Curl \space \vec{v} = \nabla \times \vec{v}$$
### Eksempler 
vi har her vektorfeltet:
$$\vec{v} =\omega \cdot \begin{pmatrix} -y \\ 0\end{pmatrix}$$
her får vi så:
$$\begin{align*}
Curl \space \vec{v} &= \nabla \times \vec{v}\\
Curl \space \vec{v} &= \begin{pmatrix}0\\
0\\
2 \omega\end{pmatrix}
\end{align*}$$


her har vi så vektorfeltet:
$$\vec{v} = \begin{pmatrix}yz \\ 3xz \\ z\end{pmatrix}$$
her får vi så curlen til at være:
$$\begin{align*}
Curl \space \vec{v} &= \nabla \times \vec{v}\\
Curl \space \vec{v} &= \begin{pmatrix} \frac{d}{dx}\\
\frac{d}{dy}\\
\frac{	d}{dz} \end{pmatrix} \times  \begin{pmatrix}yz \\ 3xz \\ z\end{pmatrix}\\
Curl \space \vec{v} &= \begin{pmatrix}0-3x\\
0-y\\
3z-z
\end{pmatrix}\\
Curl \space \vec{v} &= \begin{pmatrix}-3x\\
-y\\
2z\end{pmatrix}
\end{align*}$$



