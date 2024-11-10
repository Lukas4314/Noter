
# 6.2
#### 9)
$$
\int\frac{x^{2}}{x^{2}+x-2}dx
$$
fordi at graden af tælleren og nævneren har samme grad kan vi ikke opskrive en partial, medmindre vi ændrer dette
$$\frac{x^{2}}{x^{2}+x-2}=\frac{x^{2}+x-2-(x-2)}{x^{2}+x-2}$$
$$\frac{x^{2}}{x^{2}+x-2}=\frac{x^{2}+x-2}{x^{2}+x-2}+ \frac{-x+2}{x^{2}+x-2}$$
$$\frac{x^{2}}{x^{2}+x-2}=1+ \frac{-x+2}{x^{2}+x-2}$$
$$
\int\frac{x^{2}}{x^{2}+x-2}dx=\int 1+\frac{-x+2}{x^{2}+x-2}dx
$$
$$\int\frac{x^{2}}{x^{2}+x-2}dx=x+\int\frac{-x+2}{x^{2}+x-2}dx+k$$
nu har vi en at tælleren har en lavere grad end nævneren og vi kan derved opstille vores partialbrøk
$$\frac{-x+2}{x^{2}+x-2}=\frac{-x+2}{(x-1)(x+2)}$$
$$\frac{-x+2}{(x-1)(x+2)}=\frac{A_{1}}{x-1}+ \frac{A_{2}}{x+2}$$
her ganger vi så med nævneren på venstre side
$$-x+2=A_{1}(x+2)+A_{2}(x-1)$$
ud fra dette kan man så sætte x til at være -2 og 1 og så får man
$$\begin{align*}
A_{1}&= \frac{1}{3}\\
A_{2}&= -\frac{4}{3}
\end{align*}$$
$$\frac{-x+2}{(x-1)(x+2)}=\frac{\frac{1}{3}}{x-1}- \frac{\frac{4}{3}}{x+2}$$
nu kan vi så indsætte dette ind i det som vi havde tidligere
$$
\begin{align*}
\int\frac{x^{2}}{x^{2}+x-2}dx&= x+\int\frac{\frac{1}{3}}{x-1}- \frac{\frac{4}{3}}{x+2}dx+k\\
\int\frac{x^{2}}{x^{2}+x-2}dx&= x+\frac{\ln(x-1)}{3}+\frac{4\ln(x+2)}{3}+k
\end{align*}
$$


#### 11)

$$\int\frac{x-2}{x^{2}+x}dx$$
vi har her at tælleren er en lavere grad end nævneren
vi skal derfor nu bare skrive det om
$$\frac{x-2}{x^{2}+x}=\frac{x-2}{x(x+1)}$$
$$\frac{x-2}{x(x+1)}=\frac{A_{1}}{x}+ \frac{A_{2}}{x+1}$$
her ganger vi så med nævneren
$$x-2=A_{1}(x+1)+A_{2}x$$
her sætter vi så x til at være 0 og -1 for at finde A_1 og A_2
$$\begin{align*}
A_{1}&=-2\\
A_{2}&= 3
\end{align*}$$
$$\frac{x-2}{x(x+1)}=\frac{-2}{x}+ \frac{3}{x+1}$$
$$\int\frac{x-2}{x^{2}+x}dx=\int \frac{-2}{x}dx + \int \frac{3}{x+1}dx$$
$$\int\frac{x-2}{x^{2}+x}dx=-2\ln(x)+3\ln(x+1)+k$$


#### 13)
$$\int \frac{dx}{1-6x+9x^{2}}$$
her er vores tæller 2 grad mindre end nævneren
$$\frac{1}{1-6x+9x}=\frac{1}{(-3x+1)(-3x+1)}=\frac{1}{(-3x+1)^{2}}$$
nu skal vi bare opskrive partial brøken for dette
$$\frac{1}{(-3x+1)^{2}}=\frac{A_{1}}{(-3x+1)^{2}}+\frac{A_{2}}{-3x+1}$$
her ganger vi så med nævneren
$$1=A_{1}+A_{2}(-3x+1)$$
hvis vi her sætter $x=\frac{1}{3}$ får vi at $A_{1}=1$  og vi kommer egentlig frem til $A_{2}=0$ fordi der ikke skal være nogen x koefficient hvilket igen bare sender også tilbage, men vi kan løse den med substitution af variable i stedet for
$$\int \frac{1}{(-3x+1)^{2}}dx$$
her substituerer vi -3x+1
$$\begin{align*}
u=-3x+1\\
\frac{du}{dx}=-3\\
dx=-\frac{1}{3}du
\end{align*}$$
$$- \frac{1}{3}\int \frac{1}{u^{2}}du$$
dette integral kan vi dog bare løse
$$\begin{align*}
- \frac{1}{3} \cdot \left(-\frac{1}{u}\right)+k\\
\frac{1}{3u}+k
\end{align*}$$
nu kan vi så indsætte x ind igen i stedet for u
$$\begin{align*}
\frac{1}{3(-3x+1)}+k\\
-\frac{1}{9x-3}+k
\end{align*}$$
vi kan derved skrive at:

$$\int \frac{dx}{1-6x+9x^{2}}=-\frac{1}{9x-3}+k$$


#### 14)
$$\int \frac{x}{2+6x+9x^{2}}dx$$
her har nævneren kun komplekse rødder hvilket betyder at vi ikke kan faktorisere det fordi det ikke kan give 0 på nogen måde
vi vælger her i stedet at at skrive x som $x=\frac{1}{18} \cdot (18x+6- \frac{18}{3})$

$$\int \frac{18x+6- \frac{18}{3}}{18(2+6x+9x^{2})}dx$$
her deler vi det så op
$$\int \frac{18x+6}{18(2+6x+9x^{2})}dx - \int \frac{1}{3(2+6x+9x^{2})}dx$$
dette kan så reduceres
$$\frac{1}{3} \left( \int \frac{3x+1}{2+6x+9x^{2}}dx - \int \frac{1}{2+6x+9x^{2}}dx \right)$$
vi kan så substituere $2+6x+9x^{2}$ i begge integraler
magter ikke mere. spørg mulgivis prebben hvordan dette kan gøres smart eller noget