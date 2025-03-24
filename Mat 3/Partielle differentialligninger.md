En partiel differentialligning er en differentialligning hvor den afledte af 2 forskellige variabler indgår
dette kan en funktion $u(x, t)$ hvor x er en position og t er tiden. Den kan se sådan her ud:
$$
\frac{\partial u}{\partial t}=c^{2} \frac {\partial^{2}u} {\partial^{2}x}
$$
denne kaldes også den en dimensionale varmeledningsligning, som beskriver hvordan varmen gennem en stang som er isoleret bevæger sig, hvor t er tiden, og x er afstanden ned i stangen




### Andenordens partial differentialligning
Generelt ser de sådan her ud:
$$A \frac {\partial^{2}u} {\partial^{2}x}+B\frac {\partial^{2}u} {\partial x \partial y}+C \frac {\partial^{2}u} {\partial^{2}y}+f(x, y, u, \frac {\partial u} {\partial x}, \frac {\partial u} {\partial y})=0$$
der findes så 3 forskellige former for ligninger hvor vi har at:
$$\cases{B^{2}-4AC < 0 & Ellliptisk\\
B^{2}-4AC = 0 & Parabolsk\\
B^{2}-4AC > 0 & Hyperbolsk}$$

### Eksempel på løsning med seperation af variable
$$2x \frac {\partial z} {\partial x} - 3y \frac {\partial z} {\partial y}=0$$
hvor $z=z(x,y)$

måden man løse denne er ved seperation af variable.
Her håber man at man kan finde en løsning hvor $z=X(x) \cdot Y(y)$ altså en funktion for x og y som er ganget med hinanden, hvor $X=X(x)$ og $Y=Y(y)$
hvis dette kna lade sig gøre, betyder det at:
$$\frac {\partial z} {\partial x}=X' \cdot Y$$ og tilsvarende for Y
og ud fra dette kan man så substiturerer det ind i vores differentialligning
$$2x (X' \cdot Y) - 3y (X \cdot Y')=0$$
her kan man så sepererer x og y så man får:
$$2x X'Y=3yXY'$$
her kan man så dividerer med  X og Y
$$
2x \frac{X'}{X}=3y\frac{Y'}{Y}
$$
her har vi så at fordi at x ændrer sig betyder det ikke at y skal ændre, hvilket betyder at det må være lig med en konstant.
$$2x \frac {X'} {X}=k$$
og $$3y \frac {Y'} {Y}=k$$
disse 2 differentialligninger kan man så løse hver for sig, hvor vi husker at $X'= \frac {dX} {x}$ 
man ender så med:
$$\begin{align*}
X=x^{\frac{k}{2}} \cdot c\\
Y=y^{\frac{k}{3}} \cdot c
\end{align*}$$
vi har nu vores 2 funktioner hvor vi nu husker at vi ledte efter funktioner som opfyldte: $z=X(x) \cdot Y(y)$ hvilket vi nu har fundet og kan derfor skrive:
$$z=x^{\frac{k}{2}}\cdot y^{\frac{k}{3}} \cdot c_{1}\cdot c_{2}$$
her ganger vi konstanterne sammen og kalder dem for c
$$z=x^{\frac{k}{2}}\cdot y^{\frac{k}{3}} \cdot c$$
vi har derfor nu en løsning



## Bølgeligningen
Vi vil nu gerne løse ligningen:
$$u_{tt}=c^{2}u_{xx}$$
her betyder $u_{tt}$ at u er partial differentieret i forhold til t 2 gange.
denne ligning kalder man bølgeligning og kommer ud fra, at man har en streng som er udspændt en længe L og har et udsving u, altså en snor som er spændt ud og trukket ud som laver vibrationer hvor vibrationerne er udsvinget som ændrer sig.
i denne ligning er:
$$c^{2}= \frac {T} {m}$$
hvor T er trækkraften og m er massen per meter. Årsagen til at man kalder det c^2 er fordi at det er positivt så for at det altid bliver positivt gør man dette. eftersom trækkraften eller massen ikke kan være negativ.

Her satser man så på at man kan finde en løsning med seperation af variable. altså:
$$u= X(x) \cdot T(t)$$
vi får så også her at:
$$u_{xx}=X''(x) \cdot T(t)$$
og 
$$u_{tt}=X(x) \cdot T''(t)$$
her, ligesom tidligere substituerer vi
$$X(x) \cdot T''(t)=c^{2} \cdot X''(x) \cdot T(t)$$
her separerer vi så variablerne.
$$\frac{X''}{X}=\frac{1}{c^{2}}\frac{T''}{T}$$
her har vi igen separeret dem og de må derfor være lig med en konstant

$$\frac{X''}{X}=\frac{1}{c^{2}}\frac{T''}{T}=k$$
vi har derfor:
$$X''-kX=0$$
og 
$$\frac{1}{c^{2}}T''-kt=0$$
disse 2 andenordens differentialligninger skal nu løses, men der er 3 forskellige måder at løse andenordensdifferentialligninger alt efter hvilket fortegn k har, hvilket også betyder der er 3 forskellige løsninger her alt efter hvad k er
$$X(t)= \cases{c_{1}\cdot e^{px}+c_{2}e^{-px} & p*p=k>0\\
A_{1}\cos(px)+ A_{2}\sin(px) & -p*p=k<0\\
ax+b & k=0
}$$
her får man 3 løsninger, hvor den ene er eksponential, den anden er linæear og den sidste er trigonomisk, og eftersom at vi arbejeder med en streng som laver periodiske bevægelser arbejder vi kun videre med case 2 altså:
$$X(x)= A_{1}\cos(px)+ A_{2}\sin(px)$$
hvor $$k=-p^{2}$$
det samme gøres nu for T(t) og her finder man frem til:
$$T(t)= A_{3}\cos(pct) + A_{4}\sin(pct)$$
nu har vi så vores 2 funktioner og her husker vi at: $u= X(x) \cdot T(t)$ og vi får derfor at:
$$u(x, t)=(A_{1}\cos(pc) +A_{2}\sin(px)) \cdot (A_{3}\cos(pct)+A_{4}\sin(pct))$$
vi har her en løsning til vores ligning
måden man så finder vores 4 konstanter er ved at kigge på vores startbetingelser
eftersom at vores streng er spændt fast i enderne har vi at
$$u(0, t)=0$$
og 
$$u(L, t)=0$$
fordi den ikke kan svinge i enderne.
dette kan så indsættes ind i vores ligning:
$$\begin{align*}
u(0, t)=(A_{1}\cos(0) +A_{2}\sin(0)) \cdot (A_{3}\cos(pct)+A_{4}\sin(pct))&= 0\\
A_{1} \cdot (A_{3}\cos(pct)+A_{4}\sin(pct))&= 0\\
A_{1}&= 0
\end{align*}$$
nu har vi:

$$u(x, t)=A_{2}\sin(px) \cdot (A_{3}\cos(pct)+A_{4}\sin(pct))$$

nu kan vi så kigge på den anden startbetingelse
$$\begin{align*}
u(L, t)=A_{2}\sin(pL) \cdot (A_{3}\cos(pct)+A_{4}\sin(pct))&= 0\\
A_{2}\sin(pL) \cdot (A_{3}\cos(pct)+A_{4}\sin(pct))&= 0\\
\sin(pL)&= 0\\
pL&= n \pi\\
p&= \frac {n \pi} {L}
\end{align*}$$

her ser vi at A_2 ikke må være 0 og derfor kommer vi frem til dette.
dette betyder så at:
$$u(x, t)=A_{2}\sin(\frac {n \pi} {L}x) \cdot (A_{3}\cos(\frac {n \pi} {L}ct)+A_{4}\sin(\frac {n \pi} {L}ct))$$
det betyder så også at der er mange forskellige, alt efter hvad n, er og man kan derfor skrive det som:
$$u_{n}(x, t)=A_{2}\sin(\frac {n \pi} {L}x) \cdot (A_{3}\cos(\frac {n \pi} {L}ct)+A_{4}\sin(\frac {n \pi} {L}ct))$$
hvor frekvensen af det, afhænger af hvad man sætter n til at være. Det betyder også at det kun er bestemte frekvenser som den genererer og derfor kun bestemte toner man kan laver.
For at reducerer dette yderligere kigger man nu på nogle startbetingesler:
hastighed og position ved t=0
$$v= \frac {\partial u(x, 0)} {t}$$
$$u(x, 0)$$
her hvis man tager en streng ud og slipper kan man sige at hastigheden af strengen er 0, altså:
$$v= \frac {\partial u(x, 0)} {t}=0$$
dette kan så indsættes:
$$ \frac {\partial u} { \partial t}=A_{2} \cdot \sin(\frac {n \pi} {L}x) \cdot (-A_{3} \cdot \frac {n \pi} {L} c \cdot \sin(\frac {n \pi} {L}ct)+A_{4} \cdot \frac {n \pi} {L}c \cdot \cos(\frac {n \pi} {L}ct))$$
$$ \frac {\partial u(x, 0)} { \partial t}=A_{2}\sin(\frac {n \pi} {L}x) \cdot (A_{4})=0$$
$$A_{4}=0$$
her har vi fra tidligere at A_2 ikke måtte være 0. 
vi har nu vores nye svar som er:
$$u_{n}(x, t)=A_{2}\sin(\frac {n \pi} {L}x) \cdot \cos(\frac {n \pi} {L}ct)$$
her kan man så summere dette op for alle n.
$$u(x, t)= \sum_{n=1}^{\infty}A_{n}sin\left( \frac {n \pi} {L}x\right)\cdot \cos( \frac {n \pi c} {L}t)$$



nu kan man så kigge på hvordan strengen ser ud når vi starter, og det kan man kalde for f(x)
$$u(x, 0)=f(x)$$
her er f(x) en funktion som ikke nødvendigvis er differentiable, men den er kontinuer fordi strengen ikke er i stykker.
man kan derfor skrive:
$$u(x, 0)= \sum_{n=1}^{\infty}A_{n}sin\left( \frac {n \pi} {L}x\right)\cdot \cos( \frac {n \pi c} {L}\cdot 0)=f(x)$$
$$u(x, 0)= \sum_{n=1}^{\infty}A_{n}sin\left( \frac {n \pi} {L}x\right)=f(x)$$
her har vi så også fordi at dette er en fourierrække at:
$$A_{n}= \frac{2}{L} \cdot
 \int_{0}^{L}f(x) sin(\frac {n \pi} {L}x)dx$$
 her kan man så løse for alle A_n og man kan så derefter indsætte dette ind i sin formel igen, og så har man løse dette
$$u(x, t)= \sum_{n=1}^{\infty}A_{n}sin\left( \frac {n \pi} {L}x\right)\cdot \cos( \frac {n \pi c} {L}t)$$
man kan så videre lave det samme, med hvor den har starthastighed og eller startposition osv, hvor den som lige er blevet udledt er ved at man har en startposition, men ikke nogen start hastighed.

Hvis man havde haft andre startbetingelser, så som at hastigheden ikke var 0, men lig med en function d
$$ \frac {\partial u} {\partial t}(x, 0)=g(x)$$

og at startpositionen er 0
$$u(x, 0)=0$$
dette er altså det tilfælde hvor strengen er på 0 i starten men har en fart op eller ned igennem strengen.
her ender man med udtrykket som hedder:
$$

$$


# alt i alt
hvis hastigheden er 0 i starten er løsningen:
$$u(x, t)=\sum_{n=1}^{\infty}A_{n} \cdot \sin\left(\frac {n \pi} {L}x\right)\cdot \cos(\frac {n \pi c} {L}t)$$
hvor A_n kan findes som:
$$u(x, 0)= \sum_{n=1}^{\infty}A_{n}sin\left( \frac {n \pi} {L}x\right)=f(x)$$
som også betyder:
$$A_{n}= \frac{2}{L} \cdot
 \int_{0}^{L}f(x) sin(\frac {n \pi} {L}x)dx$$
 

her er f(x) start positionen af snoren

Hvis startpositionen er 0 men den har en hastighed g(x) er løsningen 
$$u(x, t)= \sum_{n=1}^{\infty}B_{n}\sin\left(\frac {n \pi } {L}x\right)\cdot \sin(\frac {n \pi c} {L}t )$$
hvor vi har at
$$B_{n}= \frac{2}{cn \pi} \int_{0}^{L}g(x) \cdot \sin( \frac {n \pi x} {L})dx$$
her er g(x) start hastigheden gennem snoren



## D'Alembert
en anden måde at løse denne bølgeligning er med D'Alembert som har løse den anderledes.
De løsninger vi lige har kigget på havde vi sinus ganget med cosinus og sinus ganget med cosinus, og dette kan skrives om med additionsformlerne (findes under en af alle trigonometri siderne), hvis der arbejdes videre med den ide og laves en masse mellemregninger jeg ikke gider ender man med dette:
hvis snoren ikke har nogen start hastighed men har en start position f(x) er løsningen:
$$u(x, t)= \frac{1}{2} \cdot (f(x+ct)+ f(x-ct)  )$$
en måde man så kan se dette på er ved at forestille sig snoren er i en bestemt position, kaldet f(x), når tiden går bliver u(x, t) forskudt, mod venstre og højre og det man så skal ende med, er altså gennemsnittet af disse 2 funktioner. Dette kan så beskrive snoren eftersom at tiden går. Det er også det som er beskrevet på figur 291 i bogen:
![[Pasted image 20250310130333.png]]
her ser man at den blive forskudt mod venstre og højre, og så gennemsnittet til højre

lad os nu sige at snoren både har en startposition og en starthastighed, så får man løsningen:
$$u(x, t)=\frac{1}{2} \cdot \left (f(x+ct)+ f(x-ct) \right )+ \frac{1}{2c} \cdot \int_{x-ct}^{x+ct}g(x) dx$$
her er f(x) startpositionen og g(t) er start hastihgeden




## En dimensional varmledningsligningen
Hvis der ses en stang hvor temperaturen er u(x, t) hvor x er hvor langt man bevæger sig ud af stangen, får man denne differentialligning:
$$ \frac {\partial u} {\partial t}= c^{2} \frac {\partial^{2}u} {\partial x^{2}}$$
som beskriver temperaturen igennem stangen x, til et tidspunkt t.
Det antages også at denne stang er fuldstændig isoleret.

#### Steady state situation
dette er hvis temperaturen er lineær ud af x aksen (dette sker når der er gået lang ) altså der kan fx. være 0 grader i starten og 20 grader i slutningen, så vil der være 10 grader halvvejs igennem stangen.

### Løsning af varmeledningsligningen
Ligesom med bølgeligningen kan denne differentialligning løses ved hjælp af bølgeligningen og vi gætter derfor på et svar som har formen:
$$u(x, t)=X(x) \cdot T(t)$$
vi får så her:
$$\begin{align*}
\frac {\partial u} {\partial x}&= X'(x) \cdot T(t)\\
\frac {\partial^{2}u} {\partial x^{2}}&= X''(x) \cdot T(t)\\
\frac {\partial u} {\partial t} &= X(x) \cdot T'(t)
\end{align*}$$
dette kan så indsættes ind i vores differentialligning:
$$X(x) \cdot T'(t)=c^{2} \cdot X''(x) \cdot T(t)$$
vi kan så her omskrive dette til:
$$\frac {X''(x)} {X(x)}=\frac {1} {c^{2}} \cdot \frac {T'(t)} {T(t)}$$
eftersom at x og t er uafhængige variable må dette være lig med en konstant
$$\frac {X''(x)} {X(x)}=\frac {1} {c^{2}} \cdot \frac {T'(t)} {T(t)}=k$$
vi har nu 2 differentialligninger:
$$\begin{align*}
\frac {X''(x)} {X(x)}&= k\\
\frac {1} {c^{2}} \cdot \frac {T'(t)} {T(t)} &= k
\end{align*}$$
dette kan så omskrives til:
$$\begin{align*}
X''(x)-k \cdot X(x)&= 0\\
T'(t) -kc^{2} \cdot T(t) &= 0
\end{align*}$$
her sættes $k=-p^{2}$ 
så vi får disse differentialligninger:
$$\begin{align*}
X''(x)+p^{2} \cdot X(x)&= 0\\
T'(t) + p^{2}c^{2} \cdot T(t) &= 0
\end{align*}$$
Hvis disse 2 differentialligninger løses og ganges sammen for at få vores svar:
$$u(x, t)=(A_{1}\cos(px)+A_{2}\sin(px)) \cdot e^{-(pc)^{2} \cdot t}$$
denne løsning giver tilsyneladende kun den relative ændring mellem 2 steady state situation. Dette betyder hvis man har 0 grader i den ene ende, og 20 i den anden som er i steady state, og så ændrer den første ende til 5 grader, kan man beskrive ændringen mellem den nuværende og når den når til sin nye steady state. Dette kan ses ved at $e^{-kt}$ bliver ganget på og når tiden vokser går dette mod 0 og derved bliver ændringen mindre, og mindre.

### varmeledningsligning med startbetingelse.
hvis temperaturen igennem en stang som u(x, 0) kan beskrives som en funktion f(x). altså start temperaturen. og Man derefter sætter enderne til at være 0 grader sådan at 
$$\begin{align*}
u(0, t)&= 0\\
u(L, t)&= 0
\end{align*}$$
her har vi igen en løsning hvor vi også kan skrive:
$$u(x, \infty)=0$$
og her kan vi bruge eksemplet fra før til at regne temperaturen, fordi den nye steady state er 0 grader over alt, og vi regner differencen som tidligere forklaret.
Vores startbetingelser fra før kan så indsættes ind i vores ligning:
$$\begin{align*}
u(0, t)&= (A_{1}\cos(0)+A_{2}\sin(0)) \cdot e^{-(pc)^{2} \cdot t}=0\\
u(0, t)&= A_{1} \cdot e^{-(pc)^{2} \cdot t}=0\\
A_{1}&= 0
\end{align*}$$
dette betyder vores svar ser sådan her ud:
$$u(x, t)=A_{2}\sin(px) \cdot e^{-(pc)^{2} \cdot t}$$
vi kigger på på den anden randbetingelse:
$$\begin{align*}
u(L, t)=A_{2}\sin(pL) \cdot e^{-(pc)^{2} \cdot t}&= 0\\
\end{align*}$$
eftersom at $A_{2}$ ikke kan være 0 da hele ligningen så giver 0 får vi at:
$$\begin{align*}
pL&= n \pi\\
p&= \frac {n \pi} {L}
\end{align*}$$
vi får derfor denne ligning:
$$u(x, t)=A \cdot \sin\left( \frac {n \pi} {L}x\right)\cdot e^{-(pc)^{2}t}$$
her findes der dog uendelig mange løsninger alt efter hvad n er, og vi får derfor svarene som:
$$u(x, t) = \sum_{n=1}^{\infty}A_{n}\cdot \sin( \frac {n \pi} {L}x) \cdot e^{-(pc)^{2}t}$$
vi kan nu også kigge på vores anden startbetingelse, altså start temperaturen:
$$u(x, 0)=\sum_{n=1}^{\infty}A_{n}\cdot \sin( \frac {n \pi} {L}x) \cdot e^{-(pc)^{2}t} = f(x)$$
vi har nu en sinus række som vi kan finde:
$$A_{n}= \frac{2}{L} \cdot \int_{0}^{L}f(x) \cdot \sin \left ( \frac {n \pi} {L}x \right ) dx$$
### Kort sagt
hvis der sættes en stang til at være 0 grader i begge ender og har start temperaturen f(x) igennem stangen kan temperaturen til et givent tidspunkt på en given position findes som:
$$u(x, t) = \sum_{n=1}^{\infty}A_{n}\cdot \sin( \frac {n \pi} {L}x) \cdot e^{-(pc)^{2}t}$$
hvor 
$$A_{n}= \frac{2}{L} \cdot \int_{0}^{L}f(x) \cdot \sin \left ( \frac {n \pi} {L}x \right ) dx$$
her er det givet at:
$$\begin{align*}
u(0, t)&= 0\\
u(L, t) &= 0\\
u(x, 0) &=  f(x)\\
p &= \frac {n \pi} {L}
\end{align*}$$



### Fuldstændig isoleret legeme
her har vi nu at enderne også er isoleret, hvilket betyder at enderne ikke er sat til en konstant, men faktisk også bliver opvarmet eller afkølet.
Her får vi:
$$\begin{align*}
\frac {\partial u(0, t)} {x}&= 0\\
\frac {\partial u(L, t)} {x}&= 0
\end{align*}$$
her kan samme fremgangsmåde som før bruges, og der ender man med en cosinus række i stedet for sinus (siger han)
