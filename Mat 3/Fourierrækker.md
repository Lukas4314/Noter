Givet en periodisk funktion f(x), så som en trigonomisk funktioner eller en firkant puls eller andet. Den behøver ikke være differentiable. Men så vil man beskrive den ved hjælp af sinus og cosinus funktioner.

Ideen er at man ved hjælp af sinus og cosinus funktioner danner en funktion som ligger omkring den originale periodiske funktion. Man kan så summere flere forskellige sinus eller cosinusfunktioner sammen med forskellige frekvenser og amplituder for at få det til at passe bedre.

Man kan beskrive en fourierrække som:
$$f(x) =a_{0}+ \sum_{n=1}^{\infty}(a_{n}\cos nx+ b_{n}\sin nx)$$
for mere præcise funktioner kan man blive ved med at lægge flere led til i sin originale funktion og funktionen herover beskriver rækken som indeholder uendelig mange led med.
Fordelen ved dette er at f(x) er differentiable over det hele nu.
Men vi mangler stadig vores konstanter som indgår i rækken og dem kan man finde med denne metode som Euler har lavet:

$$\begin{align*}
a_{0}&= \frac {1} {2\pi} \int_{-\pi}^{\pi}f(x) dx\\
a_{n}&=   \frac {1} {\pi} \int_{-\pi}^{\pi}f(x) \cdot \cos(nx) dx\\
b_{n}&=   \frac {1} {\pi} \int_{-\pi}^{\pi}f(x) \cdot \sin(nx) dx\\
\end{align*}$$
her kan man også forestille sig at $a_{0}$ er gennemsnitshøjden for den periodiske funktion 
her integrerer man fra $-\pi$ til $\pi$, men det er kun hvis man har en funktion af en periode på 2 pi.

### Beregning af pi med Fourierrækker
Hvis man laver en Fourierrække på en firkant puls med amplitude 1 og periode på 2 pi hvor skiftet mellem -1 og 1 er ved x=0 får men en rækker som hedder:
$$f(x)= \frac {4} {\pi}\cdot(\sin(x)+ \frac{1}{3}sin(3x)+ \frac{1}{5}\sin(5x) ...)$$
her vil man så undersøge hvad $f(\frac{\pi}{2})$ i forhold til vores firkant puls er svaret 1 og i forhold til vores fourierrække er svaret:
$$f(\frac{\pi}{2})=1= \frac {4} {\pi} \cdot (1- \frac{1}{3}+ \frac{1}{5}- \frac{1}{7}...)$$
man kan med andre ord beregne pi ved at isolerer det i denne ligning


### Fourierrækker med vilkårlige perioder
Fourierækker med en vilkårlig periode kan findes som:
$$f(x)= a_{0}+ \sum_{n=1}^{\infty}(a_{n}cos( \frac {n \pi} {L}x)+ b_{n}\sin( \frac {n \pi} {L}x))$$
her er $L= \frac{p}{2}$ hvor p var perioden
$$\begin{align*}
a_{0}&=  \frac{1}{2L} \int_{-L}^{L}f(x) dx\\
	a_{n}&= \frac{1}{L} \int_{-L}^{L}f(x) \cdot \cos( \frac {n \pi} {L}x )\space dx\\
b_{n}&= \frac{1}{L} \int_{-L}^{L}f(x) \cdot \sin( \frac {n \pi} {L}x )\space dx
\end{align*}$$
her er det igen ligesom tidligere bare med vilkårlige perioder. Det tidligere var derfor bare et special tilfælde af det her

## Lige og ulige funktioner

### Lige funktioner
lige funktioner er funktioner man kan spejle om y aksen, så som cos(x)
Hvis man har en funktion som er lige får man en fourierrække af cosinuser og ingen sinuser.
med andre ord så er $b_{n}=0$
### Ulige funktioner
Ulige funktioner er når $-f(-x) = f(x)$ 
dette kan fx være sinusfunktioner
Hvis man har en ulige funktioner og gerne vil finde dens fourierrække så er både $a_{0}=0$ og $a_{n}=0$ hvilket gør arbejdet en del nemmere


Hvis en funktion er lige eller ulige er der også smartere måde at man kan finde fourrier rækken på som kan ses her:
![[Pasted image 20250224122222.png]]



### Half-range expansion

hvis man har en funktion hvor man er interesseret i den fra området 0 til L, kan man forestille sig at den er periodiske og lave den ulige, altså ved at tegne resten af den hvis dette er tilfældet. Man kan nu finde fourierrækken som vil passe i området mellem 0 og L men resten af den vil ikke kunne bruges fordi det er noget man har "opdigtet".
se eventuelt på billedet herunder:
![[Pasted image 20250217131632.png]]


### Gibbs phenomenon
dette er at Fourierrækker tæt på hvor der er et spring fordi den originale funktion ikke er kontinuer, afviger den mere. og det er uanset hvor mange led man tilføjer



## Forced oscillation
Hvis man har en differentialligning som hedder:
$$my''+cy'+ky = r(t)$$
her kan man komme ud for at r(t) er en periodisk funktion, men ikke er differentiable eller kontinuer og man kan derfor ikke løse den som man normalt ville gøre.
Man kan dog i stedet finde fourierrækken til sin funktion og så kan man løse differentialligningen for alle n, ved at holde den som variable
#### Eksempel 
![[Pasted image 20250217134332.png|500]]
![[Pasted image 20250217134403.png|500]]
Eventuelt lige gennemgå det lidt mere....

