Laplace transformationer kan bruges til at løse lineære ordinære differentielligninger med begyndelsesbetingelser altså ODE med begyndelsesbetingelser eller IVP (initial valuation problems)
De differentialligninger man ofte bruger dette til er når variablen er tiden.

Det man så gør er at man har en differentiel ligning hvor domænet er tiden, laver man sin differentielligning om til at være i s domænet i stedet for og dette skulle så gøre det nemmere fordi man ofte når noget som er mere algebraisk altså der er mere noget med at flytte rundt på nogle ligninger og når man så har gjort det laver man en invers Laplace transformation og så har man sin løsning til differentialligningen

### Definition
hvis man har en funktion som afhænger af tiden $f(t)$ og $t \geq0$ så har man at:
$$F(s)=L(f)=\int_{0}^{\infty}f(t)e^{-st}dt$$
her er notationen også at når man finder Laplace transformationen af en funktion er det med det store bogstav i stedet hvor den afhænger af s i stedet for t
Den inverse Laplace transformation kan man finde som:
$$f(t)=L^{-1}(F(s))$$

### Simpel eksempel
vi har her funktionen:
$$f(t)=1$$
$$
\begin{align*}
L(f)&= \int_{0}^{\infty}1 \cdot e^{-st}dt\\
&=  \left. - \frac{1}{s}e^{-st} \right |_{0}^{\infty}\\
&=  \frac{1}{s}
\end{align*}
$$

Rigtig syntax er egentlig at vi ikke kan have et integral som er opløftet i uendelig og der derfor i stedet skal stå
$$\lim_{t \to \infty}\int_{0}^{T}f(t)dt$$

### Regneregel med linearitet
$$L(a \cdot f(t)+b \cdot g(t))=a \cdot L(f)+ b \cdot L(g)$$
et eksempel på dette kan være funktionen $L(2+t)=2L(1)+L(t)$ 
$$\begin{align*}
L(2+t)&= \int_{0}^{\infty}2e^{-st}dt+\int_{0}^{\infty}te^{-st}dt\\
&= \frac{2}{s}+ \frac{1}{s^{2}}
\end{align*}$$
### Tabel over Laplace transformation
![[Pasted image 20241122084116.png|500]]


### Random sætning
vi har her en funktion $f(t)$ som har en Laplace transformation $F(s)$ som eksisterer for $s > k$   så er:
$$L(e^{at}f(t))=F(s-a)$$
hvor vi har at $s-a>k$
så har vi derved også at:
$$L^{-1}(F(s-a))=e^{at}f(t)$$
her er k en konstant

### Sætning om eksistens for Laplace transformation "Growth restriction"
vi kigger her på $f(t)$ som vi gerne vil transformerer hvor $f(t)$ er stykvis og $t \geq 0$ 
så har vi at 
$$|f(t)|\leq M \cdot e^{kt}$$
hvis Laplace transformationen findes, her er K og M konstanter, og her har vi at $s>k$ 
et eksempel på en funktion som ikke går er 
$$f(t)=e^{t^{2}}$$
dette skal ikke forveksles med $f(t)=(e^{t})^{2}=e^{2t}$


## Laplace transformation af afledte funktioner
hvis vi skal Laplace transformerer funktionen $f'(t)$ får man svaret 
$$L(f'(t))=s L(f)-f(0)$$
hvis man har den dobbeltafledte så som:
$$L(f''(t))=s^{2}L(f)-sf(0)-f'(0)$$
generelt kan man skrive:
$$L(f^{(n)}(t))=S^{n}L(f)-s^{n-1}f(0)-s^{n-2}f'(0)-...f^{n-1}(0)$$

### Laplace transformation af integraller
vi kigger her igen  på en funktion $f(t)$ hvor  $t \geq0$ 
så har vi:
$$L(\int_{0}^{t}f(\tau)d \tau)=\frac{1}{s}F(s)$$



## Eksempel med løsning af differentialligning
vi har her differentialligningen:
$$y'(t)+y(t)=q \cdot e^{2t}$$
$$y(0)=3$$
vi Laplace transformerer hele ligningen
$$
\begin{align*}
L(y'+y)&= L(9 \cdot e^2t)\\
sY(s)-y(0)+Y(s)&= 9 \cdot \frac{1}{s-2}
\end{align*}
$$
nu skal vi så løse for $y(s)$
$$
\begin{align*}
sY(s)-y(0)+Y(s)&= 9 \cdot \frac{1}{s-2}\\
Y(s)(s+1)&= \frac{9}{s-2}+3= \frac {9+3(s-2)} {s-2}\\
Y(s)&= \frac {9+3s-6} {(s+1)(s-2)}= \frac {3(s+1)} {(s+1)(s-2)}=\frac{3}{s-2}\\
y(t)&= L^{-1}(Y(s))= 3e^{2t}
\end{align*}
$$
på denne måde er differentialligningen løst


## Eksempel 2 med løsning af differentialligning
$$y''(t)-y(t)=-t^{2}$$

$$\begin{align*}
L(y''-y)&= L(-t^{2})\\
s^{2}Y(s)-sY(0)-y'(0)-Y(s)&= - \frac{2}{s^{3}}\\
s^{2}Y(s)-s \cdot 2-0-Y(s)&= - \frac{2}{s^{3}}\\
Y(s) \cdot (s^{2}-1)&= - \frac{2}{s^{3}}+2s\\
Y(s)&= \frac {-2+2s^{4}} {s^{3}} \\
Y(s)&= \frac {-2+2s^{4}} {(s^{2}-1) \cdot s^{3}}\\
Y(s)&= \frac {2(s^{4}-1)} {(s^{2}-1)s^{3}}\\ 
Y(s)&= \frac {2(s^{2}+1)(s^{2}-1)} {(s^{2}-1)s^{3}}\\
Y(s)&= \frac {2(s^{2}+1)} {s^{3}}\\
Y(s)&= \frac{2s^{2}}{s^{3}}+ \frac{2}{s^{3}}\\
Y(s)&= \frac {2} {s} + \frac{2}{s^{3}}\\
y(t)&= L^{-1}(Y(s))\\
y(t)&= L^{-1}( \frac {2} {s} + \frac{2}{s^{3}} )\\
y(t)&= 2+t^{2}
\end{align*}$$



## Unit step (enhedsstep)
hvis man her har en funktion som er:
$$\begin{align*}
f(t)&= 1 &t>0\\
f(t)&= 0 & t<0 
\end{align*}$$
den kan også være beskrevet anderledes altså som:
$$
\begin{align*}
u(t-a)&= 0 & t<a\\
u(t-a) &= 1 & t>a
\end{align*}
$$


vi kigger her på om man kan Laplace transformerer denne
$$
\begin{align*}
L(u(t-a))&= \int_{0}^{\infty}u(t-a)e^{-st}dt\\
L(u(t-a))&= \frac{e^{-as}}{s}
\end{align*}
$$
man kan bruge unit step til at skubbe og tænde noget som fx med funktionen:
$$f(t) \cdot u(t-a)$$
her har vi en funktion $u(t-a)$ som er enten 1 eller 0 alt efter tiden og derfor nogle gange får vi 0 og andre gange får vi $f(t)$ 
dette kan så bruges til at beskrive mange forskellige funktioner som ikke nødvendigvis er 
differentiable i området 
hvis man fx har en funktion $f(x)=sin(x)$ som er 0 når $x<0 \lor x>\pi$ kan man beskrive den med et unit step altså:
$$f(x)=sin(x) \cdot u(t-\pi)$$ her er u enten 0 eller 1 alt efter om det er positivt det som står inde i parrentesen 



![[Pasted image 20241122094232.png|500]]


### Random Vigtig sætning 3

hvis vi har en funktion f(t) og en Laplace tranformation af denne $F(s)$ har vi
$$L(f(t-a)u(t-a)=e^{-as}F(s))$$
ikke helt sikker på hvad man kan bruge den til med noget med inverse Laplace transformation hvor det bliver nemmere eller noget idk.

#### Eksempel
$$\begin{align*}
L^{-1} \left (\frac {e^{-3s}} {s^{2}}  \right )=(t-3)u(t-3) \\
\end{align*}$$
her har vi at fra random sætning 3 at $a=3$ og $F(s)= \frac{1}{s^{2}}$ 


## Dirac delta 
her har vi en funktion:
$$\begin{align*}
f_{k}(t-a)&= \frac{1}{k} &a \leq t \leq a+k\\
f_{k}(t-a)&= 0 &ellers\\
\end{align*}$$
her definerer man så en delta $\delta(t-a)$ som grænseværdien for 
$$\lim_{k \to 0}f_{k}(t-a)$$
intervallet  kan bevæge sig på bliver mindre og mindre men selve funktionsværdien bliver større og større, se eventuelt [[Dirac Puls]] 
ud fra dette får vi at:
$$\begin{align*}
\delta(t-a)&= \infty &t=a\\
\delta(t-a)&= 0 &ellers\\
\end{align*}$$
her gælder det også at
$$\begin{align*}
\int_{0}^{\infty}\delta(t-a)dt=1
\end{align*} $$
der gælder også generelt
$$\int_{0}^{\infty}g(t) \delta(t-a)dt=g(a)$$
Her er g(a) er bare funktionsværdien i punktet

### Laplace transformation af Dirac delta
![[Pasted image 20241122100436.png|500]]



## Laplace transformationer Generelle formler
![[Pasted image 20241122100617.png|500]]
