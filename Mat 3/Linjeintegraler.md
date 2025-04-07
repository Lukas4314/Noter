Normalt når man vil finde arealet under en kurve f(x) mellem a og b finder man det som:
$$A = \int_{a}^{b}f(x) dx$$

ved linjeintegraler har man et vektor felt $\vec{F}$ og så har vi en linje som bevæger sig igennem dette felt, $$\vec{r}(t)$$ og vi også et lille linjestykke $d \vec{r}$, og her finder man så integralet som:
$$\int_{a}^{b}\vec{F} \cdot d \vec{r}$$
her er a og b enderne på linjen, og $\vec{F}$ er vektorfeltet.
Hvis vores linje er en cirkel, altså $\vec{r}(t)$ så laver man en cirkel på integraller som:
$$\oint_{a}^{b}\vec{F} \cdot d\vec{r}$$
normalt kan man finde et arbejde som:
$$A = \vec{F} \cdot d \vec{s}$$
Det som linje integralet derfor er, er egentlig arbejdet som skal bruges på at trække en genstand igennem et felt. hvilket giver mening fordi hvis vektorfeltet, peger samme vej som linjen, og man prikker dem, så giver det 0, og der skal derfor ikke bruges noget arbejde.

Hvis man fx, har et tyngdefelt, som peger ned, og man gerne vil finde arbejdet som skal bruges på at løftet et objekt op, mod tyngdekraften så vil arbejdet være:
$$A = \oint_{a}^{b}\vec{F} \cdot d \vec{r}=E_{pot}=mgh$$
er behøves, a og b ikke være overfor hinanden, og der er lige meget om man tager en kæmpe omvej for at komme fra a til b, fordi arbejdet vil så være det samme.

### How to use
hvis vi har en linje i det 3 dimensionale og udtrykker den som parameterfremstilling:
$$\vec{r}(t) = \begin{pmatrix}x(t) \\ y(t) \\ z(t)\end{pmatrix}$$
her vil vores $d \vec{r}$ blive:
$$d \vec{r}=\begin{pmatrix}dx(t) \\ dy(t) \\ dz(t)\end{pmatrix}$$
vi kan så skrive dette om så det bliver:
$$\frac {d \vec{r}(t)} {dt} \cdot dt = \vec{r}'(t) dt$$
her får vi så vores integral over arbejdet til at være:
$$\int_{a}^{b}\vec{F} \cdot \vec{r}'dt$$
og dette kan så udregnes, ved først at prikke de 2 vektorer sammen, og derefter integrerer i forhold til dt

det kan så skrives op som:
$$\int_{a}^{b}(F_{1} \cdot x'+F_{2}\cdot y' + F_{3}\cdot z') dt$$
hvor at x, y, og z kom fra parameterfremstillingen af linjen.
### Eksempel i 2 dimensioner
vi har her et felt som er: 
$$\vec{F} = \begin{pmatrix}-y \\ -xy\end{pmatrix}$$
og en linje som går fra (1, 0) til (0, 1) i en bue, altså en kvartcirkel som kan skrives som:
$$\vec{r}(t) = \begin{pmatrix}\cos(t)  \\ \sin(t)\end{pmatrix}$$
for at vi kører mellem vores punkter, svarer det til at $0 \leq t \leq \frac{\pi}{2}$ 
vi får derfor vores integral som hedder:
$$\begin{align*}
A &=  \int_{0}^{\frac{\pi}{2}} \begin{pmatrix}-\sin(t) \\ - \cos(t)\end{pmatrix} \cdot \begin{pmatrix}-\sin(t)  \\ \cos(t)\end{pmatrix}dt\\
A &=  \int_{0}^{\frac{\pi}{2}} (\sin^{2}(t) - \cos^{2}(t) \cdot \sin(t)) dt
\end{align*}$$
dette integral skal så bare løses, og så ender man med at få:
$$A = \frac{\pi}{4} - \frac{1}{3}$$

### Eksempel i 3 dimension:
vi har her et felt:
$$\vec{F} = \begin{pmatrix}z \\ x \\ y\end{pmatrix}$$
og vi har en linje som hedder:
$$\vec{r}(t) = \begin{pmatrix}\cos(t) \\ \sin(t) \\ 3t\end{pmatrix}$$
og her der bevæger vi os en omgang, hvilket betyder: $0 \leq t \leq 2\pi$
vores integral bliver så her:
$$\int_{0}^{2\pi}\vec{F} \cdot \vec{r}'(t) dt$$
dette bliver så til:
$$\int_{0}^{2\pi}\begin{pmatrix}3t \\ \cos(t) \\ \sin(t)\end{pmatrix} \cdot \begin{pmatrix}-\sin(t) \\ \cos(t) \\ 3\end{pmatrix} dt$$
dette integral bliver så:
$$\int_{0}^{2\pi}(-3t \cdot \sin(t) + \cos^{2}(t)+ 3\sin(t)) dt$$
dette integral kan så løses ved det først led med partial integration, andet led, kan man slå op i bogen, og 3 led er lige ud af landevejen



### Konservativ felt
hvis en felt er konservativt afhænger linjeintegrallet kun af start og slutpunkt. altså at vejen fra, a til b er ligegyldig, bare man har det samme start og slutpunkt. Et linjeintegral, er uafhængigt af vejen hvis:
$$\vec{F} = \nabla f$$
Her er f en funktion som vi ikke kender fra start, men man så kan finde.
dette betyder så også:
$$\begin{pmatrix}F_{1} \\ F_{2} \\ F_{3}\end{pmatrix} = \begin{pmatrix} \frac {\partial f} {\partial x} \\  \frac {\partial f} {\partial y} \\ \frac {\partial f} {\partial z}\end{pmatrix}$$
hvis der findes en funktion f som opfyldet dette, kaldes 
$$\vec{F} \cdot d \vec{r} = F_{1}dx+F_{2}dy+F_{3}dz=df$$
Vi skal nu tjekke for om dette nu passer eller om det er exact, hvor vi har at:
$$\begin{align*}
\frac {\partial F_{1}} {\partial y}&= \frac {\partial F_{2}} {\partial x}\\
\frac {\partial F_{1}} {\partial z} &= \frac {\partial F_{3}} {\partial x}\\
\frac {\partial F_{2}} {\partial z} &= \frac {\partial F_{3}} {\partial y}
\end{align*}$$
en opgave omkring, dette kan så lyde, at man skal tjekke om dette er exact, og så kan man undersøge det, ved at tjekke disse herover igennem. Hvis man kommer frem til at der er opfyldt så vil er linjeintegrallet konservativt, og afhænger derfor ikke af vejen, fra a til b, men bare hvor a og b er. Sådan et felt kan fx være tyngdefeltet, som vil opfylde dette, da arbejder som skal bruges til at flyttet noget op er uafhængigt om hvilken vej man tager og det som afgør det er højden, som kan bevises med formlen for potentiel energi: $E_{pot}= mgh$ 


### Eksempel 
vi har her et linjeintegral som er:
$$\int_{c}2xyz^{2}dx+(x^{2}z^{2}+z \cos(yz))dy+(2x^{2}yz+y \cos
(yz))dz$$
her er den delt op så hvert led er F_1, F_2 og F_3 og c er linjen som vi følger. i stedet for a og b fordi vi er interesseret i at tjekke om den er konservativ, og vi derfor ikke behøves linje
vi tjekker så her om det er konservativt ved at indsætte det ind i formlerne fra tidligere:
$$\begin{align*}
\frac {\partial F_{1}} {\partial y}=2xz^{2} &= \frac {\partial F_{2}} {\partial x}= 2xz^{2} \\
\frac {\partial F_{1}} {\partial z} = 4xyz &= \frac {\partial F_{3}} {\partial x}=4xyz\\
\frac {\partial F_{2}} {\partial z} = 2x^{2}z+\cos(yz)-zy \sin(yz) &= \frac {\partial F_{3}} {\partial y}=2x^{2}z+\cos(yz)-zy \sin(yz)
\end{align*}$$
dette betyder så at den er exact, og vi kan derfor finde en funktion f som sagde:
$$\vec{F} = \nabla f$$
og
$$\begin{pmatrix}2xyz^{2} \\ x^{2}z^{2}+z \cos(yz) \\ 2x^{2}yz+y \cos(yz)\end{pmatrix} = \begin{pmatrix} \frac {\partial f} {\partial x} \\  \frac {\partial f} {\partial y} \\ \frac {\partial f} {\partial z}\end{pmatrix}$$
hvis vi her kigge på det første som siger:
$$\frac {\partial f} {\partial x} = 2xyz^{2}$$
kan det skrives om til:
$$f = x^{2}yz^{2}+g(y, z)$$
her er g(y, z) en funktion som kan være der som vi ikke kender
af den næste for vi:
$$\begin{align*}
\frac {\partial f} {\partial y}&= x^{2}z^{2}+z \cos(yz)\\
f &= x^{2}yz^{2}+\sin(yz)+h(z) 
\end{align*}$$
her har vi ledet fra første gang, som kommer med videre, og vi kan nu kigge på den sidste:
$$\begin{align*}
\frac {\partial f} {\partial z} &=  2x^{2}yz + y \cos(yz)\\
f &= x^{2}yz^{2}+\sin(yz)+k
\end{align*}$$
nu har vi så vores funktion og så kan vi skrive vores linjeintegral op som:
$$\int_{c}2xyz^{2}dx+(x^{2}z^{2}+z \cos(yz))dy+(2x^{2}yz+y \cos
(yz))dz=\int_{(0, 0, 1)}^{(1, \frac{\pi}{4}, 2)}df$$
og eftersom vi kender f kan vi regne dette ud nemmere:
$$\int_{(0, 0, 1)}^{(1, \frac{\pi}{4}, 2)}df=[x^{2}yz^{2}+\sin(yz)]_{(0, 0, 1)}^{(1, \frac{\pi}{4}, 2)}$$
dette kan så regnes ved at indsætte:
$$[x^{2}yz^{2}+\sin(yz)]_{(0, 0, 1)}^{(1, \frac{\pi}{4}, 2)}=1^{2} \cdot\frac{\pi}{4}\cdot 2^{2}+\sin( \frac{\pi}{4} \cdot 2)-(0 \cdot 0 \cdot 1^{2}+ \sin(0 \cdot 1))=\pi +1$$
vi har derfor nemmere regnet dette ud, ved at tjekke om den er konservativ, og vi har derfor ikke behøvet at bruge linjen, da den ikke er relevant
