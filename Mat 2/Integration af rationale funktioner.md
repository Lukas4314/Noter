
når man skal lave integration af rationale funktioner så som:
$$\frac{P(x)}{{Q(x)}}$$
et eksempel på dette kan være $\int \frac{x^{2}+2x}{3x+4}dx$  

skal mam bruge partialbrøksopløsning:
$$\frac{P(x)}{{Q(x)}}=\frac{P_{1}(x)}{{Q_{1}(x)}}+\frac{P_{2}(x)}{{Q_{2}(x)}}...$$
Nu skal man så antage at P's grad er mindre end Q's grad 
her betyder grad at hvor meget der er opløftet i altså $grad(x^{2})=2$ og $grad(3)=0$ 

dette giver så nogle forskellige tilfælde hvor der er forskellige metoder til at løse det på
## Tilfælde 1:
$$Q(x)=(x-a_{1})(x-a_{2})...(x-a_{n})$$
dette betyder at Q(x) er kun bestående af lineære led
her skal man så også huske at man ofte kan gøre ting som:
$$x^{2}-x-2=(x-2)(x+1)$$

så bliver det før til:
$$\frac{P(x)}{Q(x)}=\frac{A_{1}}{x-a_{1}}+\frac{A_{2}}{x-a_{2}}...$$
Dette afhænger selvfølgelig af hvor mange led man ender med at få

En metode som man så kan bruge er at gange me nævneren
man kan gange med nævneren sådan at vi får
$$P(x)=Q(x) \cdot (\frac{A_{1}}{x-a_{1}}+\frac{A_{2}}{x-a_{2}}...)$$
eftersom at $Q(x)=(x-a_{1})(x-a_{2})...(x-a_{n})$ kan vi se at første led altid går ud med et andet led men at alle andre led bliver ganget på
altså:
$$P(x)=A_{1} \cdot (x-a_{2})(x-a_{3})...+A_{2} \cdot (x-a_{1})(x-a_{3})...$$

Efter man har gjort dette er der forskellige metoder til at finde A_1 og A_2 osv
Metode 1
sammenligner koefficenter til $x^{n},x^{-1}...x$ 
opskriv ligning med flere ubekendte og løser ligningen
dette betyder at man kigger siger at koefficienterne på den ene side af lighedstegnet skal være lig med koefficienterne på den modsatte side og på den måde kan man opskrive nogle ligninger for A_1 og A_2 osv og løse for dem


Metode 2
sæt $x=a_{1}$ og find $A_{1}$ 
sæt $x=a_{2}$ og find $A_{2}$
osv
Når man gør det giver nogle af leddene 0 hvilket gør det markant nemmere og på denne måde kan man finde frem til A_1 osv da det selvfølgelig skal gælde for alle x


## Eksempel med tilfælde 1:
$$R(x)=\frac{P(x)}{Q(x)}=\frac{6x+8}{x^{2}+3x+2}=\frac{6x+8}{(x+1)(x+2)}$$
her består vores nævner af lineære led
dette betyder at vi kan skrive:
$$\frac{6x+8}{(x+1)(x+2)}=\frac{A_{1}}{x+1}+\frac{A_{2}}{x+2}$$
så ganger vi med nævneren
$$6x+8=A_{1}(x+2)+A_{2}(x+1)$$
dette kan så blive til
$$6x+8=(A_{1}+A_{2})x+2A_{1}+A_{2}$$
Nu kan vi så opskrive 2 ligninger med 2 ubekendte:
$$\begin{align*}
A_{1}+A_{2}=6\\
2A_{1}+A_{2}=8
\end{align*}$$
dette kan så løses og så får man
$$A_{1}=2$$
$$A_{2}=4$$
dette betyder at 
$$R(x)=\frac{P(x)}{Q(x)}=\frac{6x+8}{x^{2}+3x+2}=\frac{A_{1}}{x+1}+\frac{A_{2}}{x+2}$$
$$R(x)=\frac{P(x)}{Q(x)}=\frac{6x+8}{x^{2}+3x+2}=\frac{2}{x+1}+\frac{4}{x+2}$$
og den er derved delt op 


## Tilfælde 2
her har vi
$$Q(x)=(x-a_{1})^{n}(x-a_{2})...$$
dette betyder at nævner har noget som er opløftet i noget og muligvis også har lineære led

dette medfører at vi får
$$\frac{P(x)}{Q(x)}=\frac{A_{1}}{(x-a_{1})^{n}}+\frac{B_{1}}{(x-a_{2})^{n-1}}...+\frac{Q_{1}}{x-a_{1}}...+\frac{A_{2}}{x-a_{2}}$$
Ikke helt sikker på det her med tilfælde 2 hvordan det adskiller sig. (tror mulligvis det har noget med at man skal kigge på forskellen i grad mellem tæller og nævner)

### Eksempel med tilfælde 2
$$\frac{2x+5}{(x+1)^{2}}=\frac{A_{1}}{(x+1)^{2}}+\frac{B_{1}}{x+1}$$
nu ganger vi så med nævner:
$$2x+5=A_{1}+B_{1}(x+1)$$
nu bruger vi så metode 2 og prøver at sætte $x=-1$
$$2 \cdot (-1)+5=A_{1}+B_{1}(-1+1)$$
$$3=A_{1}$$
nu prøver vi så at sætte $x=1$
$$2 \cdot 1+5=A_{1}+B_{1}(1+1)$$
$$7=A_{1}+2B_{1}$$
her indsætter vi så A1 fordi den kender vi 
$$7=3+2B_{1}$$
$$2B_{1}=4$$
$$B_{1}=2$$
og vi kan nu skrive det op som:
$$\frac{2x+5}{(x+1)^{2}}=\frac{3}{(x+1)^{2}}+\frac{2}{x+1}$$


## Tilfælde 3
i dette tilfælde har nævner komplekse rødder
led med $(ax^{2}+bx+c)^{n}$ hvor det ikke kan skrives som 2 led som bliver ganget med hinanden
fås led med:
$$\frac{A_{1}x+B_{1}}{(ax^{2}+bx+c)^{n}}+\frac{C_{1}x+D_{1}}{(ax^{2}+bx+c)^{n-1}}...$$



## Eksempel med tilfælde 3
$$R(x)=\frac{P(x)}{Q(x)}=\frac{3x^{2}+11x+14}{(x-4)(x^2+6x+13)}=\frac{A_{1}}{x-4}+\frac{A_{2}x+B_{2}}{x^{2}+6x+13}$$
her ganger vi så med nævneren
$$3x^{2}+11x+14=A_{1}(x^{2}+6x+13)+(A_{2} \cdot x+B_{2})(x-4)$$
her bruger vi så igen metode 2 hvor vi starter med at sætte $x=4$
$$3x^{2}+11 \cdot 4+14=A_{1}(4^{2}+6\cdot 4+13)+(A_{2} \cdot x+B_{2})(4-4)$$
dette bliver så til
$$A_{1}=2$$
nu kigger på vi på koeffiecienten foran x^2 hvor der står:
$$3=A_{1}+A_{2}$$
eftersom vi kender $A_{1}$ bliver dette til:
$$A_{2}=1$$
nu kigger vi så på konstnatledet:
$$14=13A_{1}-4B_{2}$$
ud fra dette kan vi så finde $B_{2}=3$
vi kan derved nu skrive det op
giver op så kig på dette billede:
![[Pasted image 20241101110110.png]]

anbefaler klart at se opgaverne [[Integration af rationelle funktioner (partialbrøker)]]