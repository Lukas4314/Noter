### Lineær approksimation
definitionen for en lineariseringen af en funktion f(x) om punktet x=a er givet ved:
$$L(x)=f(a)+f'(a)(x-a)$$
### Fejlvurdering af linear approksimation
Frejlen E er den sande værdi - den approksimeret værdi altså:
$$E(x)=f(x)=L(x)$$
men vi kender jo ikke f(x) da hvis vi kendte denne og kunne udregne denne var der ingen grund til at lave en linearisering vi har derved en sætning:
hvis $f''(x)$ eksisterer for vores interval som indeholder a og x, så eksisterer der et punkt s mellem a og x således at 
$$E(x)= \frac{f''(s)}{2}(x-a)^{2}$$
her kender vi dog ikke s, men vi regner derfor worst case scenario hvor vi undersøger hvor stor f''(s) kan blive.
man kan derfor skrive det op:
$$|E(x)|\leq \frac {|f''(s_{max})|} {2}(x-a)^{2}$$
her er s_max den s værdi hvor f''(x) bliver størst numerisk set og man skal derfor undersøge hvor den man får det største resultat numerisk inde for det givne interval dog.
en måde at gøre dette systematisk er ved at differentiere den og sætte den lig med 0 og så derefter undersøge om der er løsninger inde for intervallet og hvis der ikke er så regne det i endepunkterne af intervallet.
man kan nu undersøge fortegnet af den fejl som man finder.
hvis man kigger på fejludtrykket igen:
$$E(x)= \frac {f''(s)} {2}(x-a)^{2}$$
her ved vi at (x-a)^2 ikke kan blive negativt og vi er derfor nødt til at kigge på f''(x) i stedet for i vores givne interval for at bestemme om der er positivt eller negativt
efter dette er gjort kan man så kigge sige at ens interval ligger på:
$$[L(x)+E_{approx}(x);L(x)]$$
her skal man altid runde intervallet af til det største interval

## Hvorfor dette gælder (langt bevis):
hvis vi kigger på vores fejludtryk igen:
$$\begin{align*}
E(x)=f(x)-L(x)\\
E(X)=f(x)-f(a)-f'(a)x+f'(a)a\\
E'(x)=f'(x)-f'(a)
\end{align*}$$
ud fra dette kan vi bruge den generaliserede middelværdisætning:
$$\frac {f(b)-f(a)} {g(b)-g(a)}= \frac {f'(c)} {g'(c)}$$
$$c \in [a,b]$$

dette kan så anvendes på 
$$f(x)=E(x) \land g(x)=(x-a)^{2}$$
i intervallet
$$[a,t]$$
ud fra den generaliserede middelværdisætning kan vi så skrive:
$$\frac {E(t)-E(a)} {g(t)-g(a)}= \frac {E'(c)} {g'(c)}$$
$$\frac {E(t)-E(a)} {(t-a)^{2}-(a-a)^{2}}=\frac {f'(c)-f'(a)} {2(c-a)}$$
$$\frac {E(t)-0} {(t-a)^{2}}=\frac{1}{2} \frac {f'(x)-f'(a)} {c-a}$$
her har vi så middelværdisætningen som siger:
$$f'(s)= \frac {f(c)-f(a)} {c-a}$$
hvor$$s \in \space ]a,c[$$
og dette kan vi så indsætte
$$\begin{align*}
\frac {E(t)} {(t-a)^{2}}&= \frac{1}{2}f''(s)\\
E(t)&= \frac {f''(s)} {2}(t-a)^{2}
\end{align*}$$
her har vi
$$s \in \space ]a, c[$$
vi har fra tidligere at 
$$c \in [a, t]$$
hvilket betyder at:
$$ s \in \space ]a, t[$$
og dette er så worst case




# Taylorpolynomier
et n'te grads Taylor polynomium udviklet om x=a er givet som:
$$P_{n}(x)=f(a)+ \frac {f'(a)} {1!}(x-a)^{1}+ \frac {f''(a)} {2!}(x-a)+...... \frac {f^{n}(a)} {n!}(x-a)^{n}$$
ud fra dette har vi Taylors sætning
hvis $f^{n+1}(t)$ eksisterer fro alle t i et interval indeholdende a og x, og hvis $p_{n}$ er et n'te grads taylorpolynomium for f(x) omkring x=a, så er $f(x)=P_{n}(x)+E_{n}(x)$ når 
$$E_{n}(x) = \frac {f^{n+1}(s)} {(n+1)!}(x-a)^{n+1}$$
hvor 
$$ s \in \space ]a, x[$$
