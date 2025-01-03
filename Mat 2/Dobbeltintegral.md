dobbeltintegraller bruges til at finde arealet under en funktion af 2 variable
notationen for double integrallet kan skrives som:
$$V=\iint _{D}f(x,y) dA$$
hvor vi har at
$$\iint_{D}dA=areal(D)$$
dette er fordi der er nogen funktion hvilket betyder at vores volumen er flad eller er arealet
dette gælder dog kun når:
f(x,y) er defineret på et lukket begrænset område D hvor randen skal bestå af endelige antal kurver med endelige længder, samt at f skal være kontinuert
dette betyder at randen skal også være defineret i vores område og begrænset betyder at det kan ligge i en cirkel med endelig radius.
dette er dog bare en formel måde at beskrive det på og vi kommer ikke til at arbejde med andre funktioner end det. Hvis en funktion opfylder disse krav kan vi sige at f er integrabel på f

## Egenskaber
1)
hvis arealet er 0 bliver integrallet 0
$$\iint_{D}f(x,y)dA=0$$
hvis D ikke har noget areal 

2)


$$\iint_{D}1 dA=area(D)$$
fordi vi får et areal med højden 1

3)
vi kan bruge samme regneregler ligesom med almindelige integraler, altså at konstanter ganget på kan sættes udenfor og 2 led som lægges sammen kan vi lave 2 integraler

4)
$$|\iint_{D}f(x, y) dA|\leq \iint_{D}|f(x,y)| dA$$


## Eksempel

$$I=\iint(sin(x)+4)dA$$
integreret på området:
$$x^{2}+y^{2}\leq 1$$
$$I=\iint sin(x) dA+4 \cdot \iint dA$$
vi ved her fordi vi integrerer på et område som er en cirkel med centrum i (0, 0) bliver sin(x) 0 fordi der er lige meget positivt og negativt
og eftersom det danner en cirkel på arealet være $2^{2}\pi=4\pi$
$$I=0+4 \pi=4 \pi$$

dette her var ved hjælp af integration by inspection hvilket er fordi at vi egentlig bare kigger på integrallet og løser det på den måde

## Beregning af dobbeltintegraller
et område kan ses ned på et xy plan og kan egentlig beskrives som arealet mellem 2 funktioner som er mellem 2 punkter
dette er så at man kalder den for y-simpel fordi området er starter og slutter ved 2 x værdier hvor y også stopper
hvis man så kigger ind fra siden så vil man se en linje hvor integrallet af den linje er området under x værdien hvor hvis man så flytter sin x vil man få et areal et andet sted. hvis man så ganger det med dx vil man få volumner som man så kan integrerer op. kig på tegningen her:
![[Pasted image 20241108085255.png|500]]
her kommer der også frem til at
$$\iint_{D}f(x,y) dA =\int^{b}_{x=a}A(x)dx=\int^{b}_{a}\left (\int^{d(x)}_{c(x)}f(x,y)dy \right)dx$$
dette er dog kun når det er y simpel som ses på tegningen betyder at den stopper brat ved en x værdi

modsat hvis man har et integral som er x simpelt kan det findes som:
![[Pasted image 20241108085908.png|500]]
her kan integrallet findes som
$$\iint_{D}f(x, y)dA=\int ^{d}_{c}A(x) dy=\int^{d}_{c}\left (\int^{b(x)}_{a(x)}f(x,y) dx \right)dy$$
## Eksempel
$$f(x,y)=4x+5$$
området er så $y=-\frac{x}{2}+1$ som også er $x=-2y+2$
fra x=0 til x=2
hvilket betyder at den er y simpel
$$
\iint_{D}f(x,y) dA = \int^{b}_{a}\left (\int^{d(x)}_{c(x)}f(x,y)dy \right)
$$
![[Pasted image 20241108092459.png|700]]
et bedre billede findes inde på MEGA som skal indsættes

## Uegentlige integraler
hvis enten D er ubegrænset eller f(x, y) er ubegrænset på D er det et uegentligt integral
vi kigger her kun på når $f(x, y) \geq 0$

vi starter her med at kigge på et eksempel
$$I=\iint_{D} \frac{1}{xy}dA$$
vi finder her området til at være arelaet mellem funktionerne
$$y=x$$
$$y=x^{2}$$
og kigger på området fra x=0 til x=1
hvis man så gør ligesom før finder man frem til at volumen går mod positivt uendelig hvilket gir mening fordi man har punktet (0, 0)
et andet godt eksempel er:
![[Pasted image 20241114212649.png|500]]


# Middelværdi
arealet som man kigger på her er lukket og begrænset og vores funktion er kontinuert i dette område
ud fra dette må alle værdier som vi kan få beskrives som:
$$f(x_{1},y_{2})\leq f(x, y) \leq f(x_{2}, y_{2})$$
her er punktet f(x1, y1) det mindste funktionsværdi som findes i vores område og $f(x_{2},y_{2})$ er et maksimum
man kan så integrerer på det i forhold til arealet
se billedet herunder:
![[Pasted image 20241108094506.png| 500]]
her definerer vi så $\frac{1}{A}\iint_{D}f(x,y) dA$ som middelværdien
og fordi at funktionen er kontinuert må der findes et punkt i vores areal som er vores middelværdi
![[Pasted image 20241114213022.png]]
dette giver mening når man tænker på gennemsitter


## dobbeltintegral i polære koordinater
hvis vi har et område D i kartesiske koordinater og et område R som er i polære koordinater
![[Pasted image 20241108095626.png| 700]]

## Eksempel med variable skift

![[Pasted image 20241108101758.png|700]]
bedre billede findes på MEGA

![[Pasted image 20241108102009.png|700]]
