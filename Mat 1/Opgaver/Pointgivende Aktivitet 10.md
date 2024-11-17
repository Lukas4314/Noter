
## Opgave 8
Omskriv det komplekse tal $z=1+ \sqrt{3}j$ til formen $z=re^{j \theta}$
vi skal her omskrive et kartesisk tal til polær form
vi kan starte med at finde r som kan gøres ved hjælp af pythagoras sætning
$$\begin{align*}
r&= \sqrt{1^{2}+ \sqrt{3}^{2}}\\
r &= \sqrt{1+3}\\
r=\sqrt{4}\\
r=2
\end{align*}$$
efter vi har fundet r skal vi finde vinklen og til dette kan vi bruge inverse tangent
$$\begin{align*}
\theta &= tan^{-1}\left (\frac{\sqrt{3}}{1} \right )\\
\theta &= tan^{-1} \left (\sqrt{3} \right )=\frac{\pi}{3}\\
\end{align*}$$
vi har nu fundet længden og vinklen og kan derfor opskrive det på polært form
$$z=2e^{j \cdot \frac{\pi}{3}}$$

## Opgave 9
Find den generelle løsning y(x) til differentialligningen:
$$\frac{dy}{dx}=6yx-3y$$
vi starter her med at faktorisere y på højre siden
$$\frac{dy}{dx}=y(6x-3)$$
efter dette kan vi bruge separation af variable til løse denne differentialligning
$$\frac{1}{y} dy=(6x-3)dx$$
vi kan nu integrerer på begge sider
$$\begin{align*}
\int \frac{1}{y}dy&= \int6x-3 \space dx\\
ln(y)&= 3x^{2}-3x +k_{1}
\end{align*}$$
nu kan vi så bare isolerer y
$$\begin{align*}
y=e^{3x^{2}-3x+k_{1}}\\
y=e^{3x^{2}-3x} \cdot e^{k_{1}}
\end{align*}$$
her kan vi så kalde $e^{k_{1}}$ for en ny konstant altså $k_{2}$ og vi får derved løsning 
$$y=e^{3x^{2}-3x} \cdot k_{2}$$
vi har derved en løsning til differentialligningen: $\frac{dy}{dx}=6yx-3y$ som er $y(x)=e^{3x^{2}-3x} \cdot k_{2}$

