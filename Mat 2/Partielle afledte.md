Når man skal finde den partielle afledte så skal man lade f(x, y) være en funktion så er de partielle afledte givet ved:
$$\frac{\partial f}{\partial x}=\lim_{h \to 0} \frac{f(x+h,y)-f(x,y)}{h}$$
$$\frac{\partial f}{\partial y}=\lim_{h \to 0} \frac{f(x,y+h)-f(x,y)}{h}$$
det som det egentlig betyder er at når man skal tage den partielle i forhold til en af dem så skal kun opfatte det man differentierer til som en variable og alt andet som konstanter, dette medfører desuden også at alle normalle regneregler for differentiering virker

## Værdier for partielle afledte
når man skriver det  op skriver man det som
$$\frac{\partial z}{\partial x}|_{(a,b)}=\frac{\partial f}{\partial x}|_{(a,b)}=f_{1}(a,b)=f_{x}(a,b)$$
det er forskellige måder at skrive det på

et eksempel
vi skal her differentierer funktionen $f(x,y)=e^{xy}*cos(x+y))$ 
$$\frac{\partial f}{\partial x}=y \cdot e^{xy} \cdot \cos(x+y)+e^{xy} \cdot (-sin(x+y))$$
det samme kan man så gøre for $\frac{\partial f}{\partial y}$
hvis man så vil tage det til et punkt skal man så bare indsætte det ind i stedet for x og y med syntaxen $\frac{\partial f}{\partial x}|_{(a,b)}$ eller en af de andre som det blev sat lig med tidligere
dette vil så give hældningen i punktet (a, b) i henholdsvis x og y retningen alt efter hvilken man taget den partielle afledte af


## Tangentplan og normaler
en tangentplan er en plan som tangerer sin funktion i et punkt.
ligesom når man snakker om en tangent når man differentier i forhold til 1 variable så får man en plan når man differentier en funktion med 2 variable
når man skal finde sin plan skal man bruge en normalvektor på planen og den kan man finde ved bruge 2 retningsvektorer som man kan danne ud fra sine partielle Afledte
$$\vec{n}=\begin{pmatrix}0 \\ 1 \\ f_{2}(a,b)\end{pmatrix}\times \begin{pmatrix}1 \\ 0 \\ f_{2}(a,b)\end{pmatrix}=\begin{pmatrix}f_{1}(a,b) \\ f_{2}(a,b)  \\ -1\end{pmatrix}$$
når man så skal finde sin ligning for sin tangentplan kan finde den som:
$$z=f(a,b)+f_{1}(a,b) \cdot (x-a) + f_{2}(a,b) \cdot (y-b)$$
her skal er $f_{1}(a,b)$ egentlig bare vores først element i vores normalvektor og det samme med $f_{2}(a,b)$

### normal linjen
man beskriver normallinjen som:
$$\frac{x-a}{f_{1}(a,b)}=\frac{y-b}{f_{2}(a,b)}=\frac{z-f(a,b)}{-1}$$
dette er 3 krav som skal være opfyld for linjen men vi kan ikke lave en forskrift for linjen men vi kan lave en parameter fremstilling til at finde en linje som går gennem punkter og er vinkelret på planen
vi kan derfor ikke bruge en forskrift til linjen særlig meget da man alternativt bare ville lave en parameterfremstilling til normalvektoren
hvis man får opgaven om at man skal finde normallinjen skal man bare indsætte det ind i formlen og så skal man egentlig bare reducerer mest mulig og så

## Kædereglen
kædereglen kan bruges når vi skal differentierer en funktion med 2 variable, og det gør det nemmere
![[Pasted image 20241101095153.png]]her er det skrevet op hvordan reglen er samt et eksempel hvor man har funktionen

## Gradienten
definitionen for gradienten er:
$$\nabla f(x,y)=grad \space f(x,y)=\begin{pmatrix}\frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y}\end{pmatrix}$$
den er sagt med ord en vektor som er vinkelret ind på en niveaukurver hvilket betyder at det er en vektor som peger i den retning hvor funktionen vokser mest

## Den retningsafledede
det fortæller noget om hvor meget noget vokser i en bestem retning og findes som:
$$D_{\frac{\vec{v}}{|\vec{v}|}}\space f(a,b)=\frac{\vec{v}}{|\vec{v}|} \cdot \nabla f(a,b)$$
her er $\vec{v}$ den retning som man er interesseret i at finde hældningen
og for en enhedsvektor hedder den:
$$D_{\vec{u}}\space f(a,b)=\vec{u} \cdot \nabla f(a,b)$$
men det er kun i specielle tilfælde hvor vi kigger på en enhedsvektor
