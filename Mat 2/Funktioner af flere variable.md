---
~
---
Definition:
en funktion a n reelle variable er en regels om tildeler et unikt reelt tal f(x_0, x_1 ... x_n) til hvert punkt (x_0, x_1 ... x_n) for en def. mængde Dm(f)  (delmængde af R^n) som på engelsk hedder domain, og mængden af reelle tal fra f(x_0, x_1 ... x_n) kaldes for værdimængden og på engelsk kaldes dette for range

## Niveaukurver
niveaukurver er tegninger hvor man har en enten en variable eller f(x) til at være noget specielt og så tegner man dem hvor man har forskellige værdier for f(x_0 ...)
et eksempel kan være 
$$f(x,y)=x^{2}+y^{2}$$
hvor man så ville sætte $$f(x,y)=2$$
og tegne den funktion som er en cirkel og det kan man så gøre for forskellige værdier og derved laver man niveaukurver



Niveaukurver kan også bruges til at afbilde funktioner som er 4 dimensionale fordi at niveaukurver kommer til at være i en dimension mindre altså i dette tilfælde i 3D


## Grænseværdier af funktion af flere variable
Hvis en funktion f(x, y) nærmer sig en grænseværdi L når punktet (x, y) nærmer sig punktet (a, b) skriver vi $$
\lim_{(x,y)->(a,b)}f(x, y) = L
$$
hvis alle punkter i "omegnen" af (a, b) måske på nær (a, b) tilhører definitionsmængden af f(x, y)
dette betyder alle punkter omkring punktet som ikke selv er defineret og ikke tilhører definitionsmængden 

#### Def 2
grænseværdien
$$\lim_{(x, y)->(a, b)}f(x,y) = L$$
givet af
a) enhver omegn af (a, b) indeholder punkter i definitionsmængden for f(x, y) forskellige fra punktet (a, b) hvilket betyder at (a, b) ikke behøves være i definitionsmængden 
b) for et hvert positivt tal epsilon eksisterer der et positivt tal delta = delta(epsilon) således at 
$$|f(x, y) -L| <\epsilon$$
er sandt når (x, y) er i definitionsmængden for f og opfylder
$$0<\sqrt{(x-a)^{2}+(y-b)^{2}}< \delta$$
den sidste formel altså den med kvadrat rod er egentlig en cirkelskive rundt om punktet. denne radius vil vi så gerne have ti at være så lille som muligt, altså at den skal være mindre end epsilon. Epsilon og delta afhænger af hinanden men vi ved ikke hvordan de afhænger af hinanden og det er denne sammenhæng som vi skal finde.
rent praktisk (tror) jeg ikke der er en fremgangsmåde herover men kig her i eksemplet herunder hvis det er:

Eksempel:
$$\lim_{(x, y)->(0, 0)}\frac{2xy}{x^{2}+y^{2}}$$
definitionsmængden er alle x og y på nær (0, 0)
vi lader nu (x, y)->(0,0) langs linjen y=x fordi denne linje går nemlig hen mod punktet (0, 0)
hvis vi så tager vores funktionsværdi
$$f(x, y)=\frac{2xy}{x^{2}+y^{2}}$$
ved y=x får vi
$$
f(x, y)=\frac{2x^{2}}{2x^{2}}=1
$$
her kan vi så kigge på udtrykket igen hvor x går mod 0 og dette er fordi at vores linje siger at x=y og hvis x går mod 0 kommer y også til at gå mod 0
$$\lim_{x->0}1=1$$
vi har derfor grænseværdien men i eksemplet herover havde vi fulgt en linje som hed x=y hvis man gør samme fremgransmåde men følger y=x^2 vil man få et svar på 0, dette betyder at grænseværdien afhænger af "vejen" hen til punktet og der derfor ikke eksister en grænseværdi
dette kan lidt sammenlignes med 1/x hvor alt efter hvilket side man kommer fra på grafen får man enten -uendelig eller +uendelig



Eksempel 2:
$$
f(x, y)=\frac{x^{2}*y}{x^{2}+y^{2}}
$$
$$
\lim_{(x,y)->(0,0)}f(x, y)=0
$$
her er det opgivet at grænseværdien muligvis er 0
vi skal her opfylde 2 betingelser:
$$0<\sqrt{(x-a)^{2}+(y-b)^{2}}< \delta$$
 epsilon kan her ikke være 0 fordi f(x, y) er ikke defineret i grænseværdien.
eftersom vi har fået opgivet at en mulig grænseværdi er 0 kan vi indsætte dette og at vi kigger på punktet (0, 0)
$$|f(x, y) -0| <\epsilon$$
$$0<\sqrt{(x-0)^{2}+(y-0)^{2}}< \delta$$
og ud fra dette får vi
$$|\frac{x^{2} \cdot y}{x^{2}+y^{2}}| <\epsilon$$
$$0<\sqrt{x^{2}+y^{2}}< \delta$$
her får vi så "en god ide" hvor vi siger at $x^{2}\leq x^{2}+y^{2}$   
$$\begin{align*}
x^{2} \leq  x^{2}+y^{2}\\
\frac{x^{2}}{x^{2}+y^{2}}\leq  1\\
\end{align*}$$

dette kan så indsættes ind i tidligere ligning
$$|\frac{x^{2}}{x^{2}+y^{2}} \cdot y |<=1 \cdot |y|$$
eftersom vi her har at |y| = sqrt(y^2) og vores tidligere udtryk skal være mindre en det tidligere kan vi lægge hvad som helst positivt til dette og det vil stadig være sandt og vi kan derfor skrive
$$|\frac{x^{2}}{x^{2}+y^{2}} \cdot y |<=1 \cdot |y|<=\sqrt{y^{2}+x^{2}}$$
vi nu fra tidligere at sqrt(x^2+y^2) skal være mindre end delta og derfor får vi
$$|\frac{x^{2}}{x^{2}+y^{2}} \cdot y |<=1 \cdot |y|<=\sqrt{y^{2}+x^{2}}<\delta$$
her fjerner vi så nogen mellemled sådan der står
$$|\frac{x^{2}}{x^{2}+y^{2}} \cdot y |<\delta$$
eftersom et af kravende var at
$$
|f(x, y) -L|<\epsilon
$$
og vi ved at 
$$
|f(x, y)-L| = |\frac{x^{2}}{x^{2}+y^{2}} \cdot y |
$$
kan vi indsætte dette og få
$$
|\frac{x^{2}}{x^{2}+y^{2}} \cdot y |<\epsilon
$$
og det kan vi sammenligne med tidligere hvor vi havde
$$
|\frac{x^{2}}{x^{2}+y^{2}} \cdot y |<\delta
$$
eftersom vi skulle finde en sammenhæng mellem delta og epsilon for at det passede med denne grænseværdi kan vi her lave sammenhængen delta lig med epsilon.
dette virkede kun fordi at vi allerede havde en ide til hvor grænseværdien lå, men alternativt skal man gøre ligesom i eksempel 1 får at få en ide til grænseværdien og så efter dette bruge samme fremgangsmåde for at tjekke om det faktisk er en løsning til grænseværdien