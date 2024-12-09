Man finde stamfunktionen til en funktion så som funktionen:
$$\int\frac{1}{\sqrt{1-x^{2}}}dx=\arcsin(x)+k$$
hvis man skal finde et integral med grænser på er notationen som Henrik bruger:
 $$\int^5_{2}(x^{3}+\cos(x))dx=[\frac{1}{4}x^4+sin(x)]^{x=5}_{x=2}$$

## Regneregler for bestemte integraler
$$\int^{a}_{a}f(x) \space dx=0$$
$$\int^{b}_{a}f(x) \space dx = F(b)-F(a)$$
$$\int^{b}_{a}A \cdot f(x)+B \cdot g(x)=A(F(b)-F(a))+B(G(b)-G(a))$$
$$\int^{c}_{a}f(x) \space dx=\int_{a}^{b}f(x) \space dx+\int_{b}^{c}f(x) \space dx$$

hvis at f(-x) = -f(x) så som sin(x)
$$\int_{-a}^{a}f(x) \space dx=0$$

hvis en funktion er lige som betyder at $f(-x)=f(x)$ så som $f(x)=x^{2}$ så gælder:
$$\int_{-a}^{a}f(x) \space dx = 2 \cdot \int_{0}^{a}f(x) \space dx$$

$$\int^{b}_{a}f(x) \space dx = \int^{b}_{a}f(t) \space dt$$


## Substitutionsmetoden
den kan bruges hvis man ved at man skal integrere en funktion og ved at svaret giver en sammendst funktion.
det man først gør at man substituere noget sådan at man får et nyt integral
et eksempel:
$$\int t \cdot sin(t^{2}) \space dt$$
her substituere vi så $t^{2}$
$$u=t^{2}$$
her differentiere vi så i  forhold til t på begge sider
$$\frac{du}{dx}=2t$$
her isolerer vi så dx
$$dx=\frac{du}{2t}$$
dette kan vi så indsætte ind igen
$$\int t \cdot sin(u) \frac{du}{2t}$$
her går t ud med t
$$\frac{1}{2} \cdot \int sin(u) \space du$$
dette kan vi integrere
$$\frac{1}{2} \cdot (-cos(u)+k_{1})=- \frac{1}{2} \cdot cos(u)+k_{2}$$
årsagen til at k_1 bliver til k_2 er fordi den bliver ganget med 1/2 før og det gør den ikke nu og det er derved en anden konstant
nu kan vi så indsætte t ind igen for
$$- \frac{1}{2} \cdot \cos(t^{2})+k_{2}$$
og vi har dermed integreret det og fået en sammensat funktion


### Substitutionsmetoden med grænser
hvis der er grænser på dit integral skal man være opmærksom på når man integrer med grænser
et eksempel:
$$\int^{x=4}_{x=0}x*sin(x^{2}) \space dx$$
hvis man så substituerer $u=x^{2}$ skal man huske at gøre det ved sine grænser også sådan at integralet bliver:
$$\int ^{u=17}_{u=1}x*sin(u) \space dx$$
man kan nu forsætte som man gjorde før hvis det er nødvendigt.



## bevis for substitutionsmetoden
hvis vi har en sammensat funktion hvor vi kan bruge kædereglen så som:
$$\frac{d}{dx} \space f(g(x))=f'(g(x)*g'(x))$$
hvis vi så integrerer på begge sider:
$$f(g(x))=\int f'(g(x)) \cdot g'(x) \space dx$$
vi lader nu være $u=g(x)$ og $\frac{du}{dx}=g'(x)$ sådan at $g'(x) \cdot dx = du$
$$f(u)=\int f'(u) \cdot du=f(u))=f(g(x)))$$

## Partiel integration
hvis man har et integral og man ved at svaret er 2 funktioner ganget på hinanden kan man blandt andet bruge partiel integration
hvis man har et integral som hedder:
$$\int x \cdot e^{x} \space dx$$
så kan man kalde 
(tjek op på det senere)


### Baggrund for partiel integration
man kan bruge produktreglen til at vise at man kan bruge partiel integration
hvis vi først skriver produktreglen op:
$$\frac{d}{dx}( f(x) \cdot g(x))=f'(x) \cdot g(x) + f(x) \cdot g'(x)$$
hvis vi så integrererbegge sider får vi:
$$f(x) \cdot g(x)=\int f'(x) \cdot g(x) \space dx+ \int f(x) \cdot g'(x) \space dx$$
hvis vi så bytter lidt rundt så bliver det til:
$$-\int f'(x) \cdot g(x) \space dx= \int f(x) \cdot g'(x) \space dx-f(x) \cdot g(x)$$
her ganger vi så begge sider med -1
$$\int f'(x) \cdot g(x) \space dx = f(x) \cdot g(x)-\int f(x) \cdot g'(x) \space dx$$
her kan vi så kalde $f'(x)=h(x)$
og vi får derved:
$$\int h(x) \cdot g(x) \space dx = H(x) \cdot g(x)-\int H(x) \cdot g'(x) \space dx$$

## Middelværdien af en funktion
hvis f er integrabel på intervallet $[a, b]$, så er middelværdien af f på $[a, b]$ givet som:
$$\overline{f}= \frac {1} {b-a} \int_{a}^{b}f(x) dx$$
