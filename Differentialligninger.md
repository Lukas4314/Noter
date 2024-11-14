
### Ordner af differential ligninger
en første orden differential ligning er en lignign hvor med at vi har den første afledte er er en funktion af den ikke afledte altså:
$$y'=k \cdot y$$
dette er førsteordens fordi vi kun har den første orden
den generelle form for en første ordens differentialligning er:
$$\frac{dy}{dx}=h(x, y)$$
her er h(x, y) en hvilken som helst funktion hvor x og y kan indgå


en anden ordens differentialligning kan være:
$$y''=y$$
osv. for ordnerne

### General løsning
en general løsning er en løsning som ofte er givet ved noget hvor der så også er en ukendt konstant som kommer fra integration. Dette gør at vi ikke kan løse det specifikke tilfælde for vores differentialligning og vi derfor har brug for en begyndelses værdi for at få en specifik løsning.


## Metoder for løsning af differentialligninger

### Separable differentialligninger
dette er differentialligninger hvor man har at:
$$\frac{dy}{dx}=f(x) \cdot g(y)$$
altså 2 funktioner hvor den ene kun afhænger af x og den anden kun afhænger af y fordi her kan man så få alt som afhænger af x på en ene side og alt der afhænger af y på den anden side. altså man kan skrive det om som:
$$\frac{1}{g(x)}dy=f(x) dx$$
her kan man så integrerer på begge sider og isolerer y og så har man løst sit integral men man skal dog huske sin integrationskonstant



## Lineær første ordens differentialligning
dette er en differentialligning med formen:
$$\frac{dy}{dx}+p(x) \cdot y=q(x)$$
med denne findes der også en general løsning
hvis q(x) = 0 kan den løses med separation af variable og den landles for homogen 
hvis den ikke er homogen og derfor er inhomogen kan den løses på en anden måde
man starter først med at gang en funktion på begge sider som er afhængig af x
$$\begin{align*}
\frac{dy}{dx}+p(x) \cdot y=q(x)\\
\gamma(x) \cdot \frac{dy}{dx}+\gamma(x) \cdot p(x) \cdot y=\gamma(x) \cdot q(x)
\end{align*}$$
nu ønsker vi så at venstresiden kan skrives som
$$\frac{d}{dx}(\gamma(x) \cdot y)=\gamma'(x) \cdot y + \gamma(x) \cdot \frac{dy}{dx}$$
ud fra disse 2 udtryk kan vi skrive at:
$$\begin{align*}
\gamma'(x) \cdot y=\gamma(x) \cdot p(x) \cdot y\\
\gamma'(x)=\gamma(x) \cdot p(x)
\end{align*}$$
ud fra dette kan vi så skrive
$$\begin{align*}
\frac{1}{\gamma(x)} \frac{dy}{dx}=p(x)\\
\int \frac{1}{\gamma(x)} dy=\int p(x) dx\\
ln(\gamma)=P(x)\\
\gamma(x)=e^{\int p(x) dx}
\end{align*}$$
nu kan vi så skrive differentialligningens om vi startede med som:
$$\frac{d}{dx}(\gamma(x) \cdot y)=\gamma(x) \cdot q(x)$$
vi kan nu integrerer på begge sider:
$$\gamma(x) \cdot y= \int \gamma(x) \cdot q(x) dx$$
nu kan vi så isolere gamma
$$y=\int \gamma(x) \cdot q(x) dx \space \cdot \frac{1}{\gamma(x)}$$
vi husker nu at $\gamma(x)=e^{\int p(x) dx}=e^{P(x)}$
og vi kan nu indsætte dette
$$y=\int e^{P(x)} \cdot q(x) dx \space \cdot \frac{1}{e^{P(x)}}$$
rigtigt se vil der have været integrationskonstanter som vi skulle have med men hvis vi kigger på dem altså:
$$\begin{align*}
y=\int e^{P(x)+k} \cdot q(x) dx \space \cdot \frac{1}{e^{P(x)+k}}
\end{align*}$$
her vil $e^{P(x)+k}=e^{k} \cdot e^{P(x)}$
$$\begin{align*}
y=\int e^{k}\cdot e^{P(x)} \cdot q(x) dx \space \cdot \frac{1}{e^{P(x) \cdot e^{k}}}
\end{align*}$$

fordi e^k er en konstant kan vi sætte den udenfor integrationen og vi kan den går så ud med den anden
$$\begin{align*}
y=\int e^{k}\cdot e^{P(x)} \cdot q(x) dx \space \cdot \frac{1}{e^{P(x) \cdot e^{k}}}\\
y=e^{k}\cdot \int  e^{P(x)} \cdot q(x) dx \space \cdot \frac{1}{e^{P(x) \cdot e^{k}}}\\
y=\int e^{P(x)} \cdot q(x) dx \space \cdot \frac{1}{e^{P(x)}}
\end{align*}$$
