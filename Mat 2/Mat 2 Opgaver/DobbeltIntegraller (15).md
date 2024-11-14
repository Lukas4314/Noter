# 1.13
$$\iint_{R}dA$$
Where R is the rectangle $-1 \leq x \leq 3,\space \space  -4\leq y \leq 1$
dette er bare en kasse med højden 1 hvilket betyder at vi kan finde dobbeltintegrallet som:
$$1 \cdot (3-(-1) \cdot (1-(-4))=20$$
# 1.14
$$\iint_{D}(x+3) dA$$
where D is the half disk $0 \leq y \leq \sqrt{4-x^{2}}$
vi kan her bare dele integrallet op
$$\iint_{D}x dA+\iint_{D}3dA $$
eftersom vi har med en halvskive at gøre som ligger langs x akse er den ligeså meget negativt som den er positivt og egentlig bare spejlvendt i y aksen hvilket også gør at når x er negativt bliver integrallet det negative af det hvor x er positivt med samme værdi altså:
$$\iint_{D}x dA=0$$
og vi kan nu finde det andet integral ved at finde at finde arealet af vores halvcirkel
$$\begin{align*}
y &\leq \sqrt{4-x^{2}}\\
y^{2} &\leq  4-x^{2}\\
x^{2}+y^{2}&= 4
\end{align*}$$
vi har derved en halvcirkel med radius på 2 og kan finde arealet af den som
$$\begin{align*}
A&= \pi \cdot r^{2} \cdot \frac{1}{2}\\
A&= \pi \cdot 2^{2} \cdot \frac{1}{2}\\
A&= 2 \pi
\end{align*}$$
vi kan nu indsætte dette ind i vores dobbeltintegral
$$\begin{align*}
\iint_{D}x dA+\iint_{D}3dA\\
0+3 \cdot 2\pi &= 6 \pi
\end{align*} $$
# 2.1
$$\int_{0}^{1}dx \int_{0}^{x}(xy+y^{2})dy$$
vi kigger her først på det indre integral hvor vi bare skal differentierer i forhold til y
$$\begin{align*}
\int_{0}^{1}dx \int_{0}^{x}(xy+y^{2})dy\\
\int_{0}^{1} \left (\left. \frac{1}{2}xy^{2}+ \frac{1}{3}y^{3} \right)\right|^{y=x}_{y=0}   \space dx\\
\int^{1}_{0} \frac{1}{2} x^{3}+ \frac{1}{3}x^{3} dx\\
\int^{1}_{0} \frac{5}{6}x^{3} dx\\
\left. \frac{5}{6}\cdot \frac{1}{4}x^{4} \right |_{x=0}^{x=1}\\
\left. \frac{5}{24}x^{4} \right |_{x=0}^{x=1}&= \frac{5}{24}\\

\end{align*}$$
# 2.3
$$\int^{\pi}_{0}dx \int^{x}_{-x}cos(y) \space dy$$
$$\begin{align*}
\int_{0}^{\pi} \left.sin(y) \right|^{y=x}_{y=-x}   \space dx\\
\int_{0}^{\pi} sin(x)-sin(-x)   \space dx\\
\end{align*}$$
eftersom at $sin(-x)=-sin(x)$ får vi 0 inde i integrallet

$$\begin{align*}
\int_{0}^{\pi} 0 \space dx=0
\end{align*}$$
# 2.5
$$\iint_{R}\left (x^{2}+y^{2} \right )dA$$
where R is the rectangle $0 \leq x \leq a$ and $0 \leq y \leq b$ 
$$\begin{align*}
\int_{0}^{a} dx \int_{0}^{b}\left (x^{2}+y^{2} \right )dy\\
\int_{0}^{a} bx^{2}+\frac{1}{3}b^{3} \space dx\\
\frac{1}{3}a^{3}b+ \frac{1}{3}ab^{3}
\end{align*}$$

# 2.9
$$\iint_{R}xy^{2}dA$$
where R is the finite region in the first quadrant bounded by the curves $y=x^{2}$ and $x=y^{2}$
vi skal først finde ud af hvornår disse kurver rammer hinanden og det kan vi gøre ved at lave begge til en funktion af x
$$\begin{align*}
x=y^{2}\\
y=\sqrt{x}
\end{align*}$$
nu kan vi så sætte dem lig med hinanden
$$\sqrt{x}=x^{2}$$
dette sker kun i 2 tilfælde $x=0 \lor x=1$ 
vi har derfor vores område, fordi at mellem 0 og 1 kan vi skrive at $x^{2} \leq y \leq \sqrt{x}$

$$\begin{align*}
\int_{0}^{1}dx \int_{x^{2}}^{\sqrt{x}} xy^{2} \space dy\\
\int_{0}^{1} \left. \frac{1}{3}xy^{3} \right |_{y=x^{2}}^{y=\sqrt{x}}\space dx\\
\int_{0}^{1} \frac{1}{3}x (x^{1,5}-x^{6}) \space dx\\
\frac{1}{3} \cdot \int_{0}^{1} x^{2,5}-x^{7} \space dx\\
\frac{1}{3} \cdot \int_{0}^{1} x^{2,5}-x^{7} \space dx\\
\frac{1}{3} \cdot \left (\left. \frac{x^{2}}{3,5}- \frac{x^{8}}{8} \right |_{0}^{1} \right )\\
\frac{1}{3} \cdot \left (\frac{1}{3,5}- \frac{1}{8} \right )\\
\frac{1}{3} \cdot \left (\frac{16}{56}- \frac{7}{56} \right )\\
\frac{1}{3} \cdot \frac{9}{56} &= \frac{3}{56}
\end{align*}$$
# 2.10
$$\iint_{D}x \cdot \cos(y)  dA$$
where D is the finite region in the first quadrant bounded by the coordinate axes and the function $y=1-x^{2}$ 
her skal vi først finde hvor den skærer vores akser altså vores funktion ved at sætte x og y til at være 0. dette giver $y=1$ og $x=1$ for at den modsatte er 0
vi vælger her først at integrerer i forhold til y fra 0 af til $1-x^2$
$$\begin{align*}
\int_{0}^{1}dx \int_{0}^{1-x^{2}}x \cdot cos(y) \space dy\\
\int_{0}^{1} \left. x \cdot sin(y) \right |_{0}^{1-x^{2}}   \space dx\\
\int_{0}^{1} x(sin(1-x^{2})-sin(0)) \space dx\\
\int_{0}^{1} x \cdot sin(1-x^{2}) \space dx\\
\end{align*}$$
her vælger jeg at substituere $u=x^{2}$ hvilket medfører at $dx=\frac{du}{2x}$ 
$$\begin{align*}
\int_{x=0}^{x=1} x \cdot sin(1-u) \cdot \frac{du}{2x}\\
 \frac{1}{2}\cdot \int_{x=0}^{x=1} sin(1-u)  du\\
 \frac{1}{2}\cdot \left. (cos(1-u)) \right |_{x=0}^{x=1}\\
\end{align*}$$
her indsættes så $u=x^{2}$

$$\begin{align*}
 \frac{1}{2}\cdot \left. (cos(1-x^{2})) \right |_{x=0}^{x=1}\\
\frac{1}{2}\cdot \left ( \cos(1-1)-cos(1-0)   \right )\\
 \frac{1}{2}\cdot \left ( \cos(0)-cos(1)   \right )\\
 \frac{1}{2}\cdot \left ( 1-cos(1)   \right )&= - \frac{cos(1)+1}{2}
\end{align*}$$

# 2.14
$$\iint_{T} \frac{xy}{1+x^{4}}dA$$
where T is the triangle with vertecies (0, 0), (0,1) and (1, 1)
vi har her med en trekant at gøre som går langs x aksen og følger linjen y=x hvor områder er området under denne linje fra x=0 til x=1, vi vælger her at integrerer i forhold til y først da det er en hel del nemmere når vi senere så skal integrerer i forhold til x
$$\begin{align*}
\int_{0}^{1}dx \int_{0}^{x} \frac{xy}{1+x^{4}} dy\\
\int_{0}^{1} \left. \frac{x}{1+x^{4}}y^{2}\cdot \frac{1}{2} \right |_{0}^{x}  \space dx \\
\frac{1}{2}\cdot \int_{0}^{1} \frac{x^{3}}{1+x^{4}}  \space dx \\
\end{align*}$$
vi kan her substituerer $1+x^{4}=u$ og man kan nu se hvorfor vi skulle interegrere i forhold til y først
vi kommer frem til at $dx=\frac{du}{4x^{3}}$ 
$$\begin{align*}
\frac{1}{2}\cdot \int_{x=0}^{x=1} \frac{x^{3}}{u} \cdot \frac{du}{4x^{3}} \\
\frac{1}{8}\cdot \int_{x=0}^{x=1} \frac{1}{u} \cdot du \\
\frac{1}{8}\cdot \left. ln(u) \right |_{x=0}^{x=1} \\
\frac{1}{8}\cdot \left. ln(1+x^{4}) \right |_{x=0}^{x=1} \\
\frac{1}{8} \cdot \left (ln(2)-ln(1) \right )\\
\frac{1}{8} \cdot ln(2)
\end{align*}$$
# 2.21
find the volume of
Under $z=1-x^2-y^{2}$ and above the region $x \geq 0 \land y \geq 0 \land x+y \leq 1$
vi skal her først finde vores område og vi kan egentlig bare skrive det som at det er området mellem akserne i første kvadrant og under linjen $y=-x +1$ fordi at denne linje sikrer at $x+y \leq 1$ og eftersom vi kun kigger i først kvadrant kigger skærer den  x og y aksen når y=0 og x=0 hvilket betyder at vi ikke kan finde den der længere
$$\iint_{D}1-x^{2}-y^{2} \space dA$$
$$\begin{align*}
\int_{0}^{1}dx \int_{0}^{-x+1}1-x^{2}-y^{2} \space dy\\
\int_{0}^{1} \left. y-yx^{2}- \frac{y^{3}}{3} \right |_{y=0}^{y=-x+1} \space dx  \\
\int_{0}^{1} -x+1-x^{2}+x^{3}- \frac{\left (-x+1 \right )^{3}}{3} \space dx  \\
\int_{0}^{1} 1-x-x^{2}+x^{3}- \frac{-x^{3}+3x^{2}-3x+1}{3} \space dx  \\
\frac{1}{3} \cdot \int_{0}^{1} 3-3x-3x^{2}+3x^{3} +x^{3}-3x^{2}+3x-1\space dx  \\
\frac{1}{3} \cdot \int_{0}^{1} 2-6x^{2}+4x^{3}\space dx  \\
\frac{1}{3} \cdot \left (  \left. 2x-2x^{3}+ x^{4} \right |_{x=0}^{x=1}  \right )  \\
\frac{1}{3} \cdot \left (  2-2+ 1  \right )&= \frac{1}{3}
\end{align*}$$

# 2.23
Find the volume of
Under the surface $z=\frac{1}{x+y}$ and bounded by the region in the xy plane $x=1 \land x=2 \land y=0 \land y=x$ 

dette giver en trekant et nyt sted som vi kan finde
$$\iint_{D} \frac{1}{x+y} dA$$
hvor D er området
$$\begin{align*}
\int_{1}^{2}dx \int_{0}^{x} \frac{1}{x+y} dy\\
\int_{1}^{2} \left. ln(x+y) \right |_{y=0}^{y=x} \space dx\\
\int_{1}^{2} ln(2x)-ln(x) \space dx\\
\int_{1}^{2} ln \left (\frac{2x}{x} \right ) \space dx\\\\
\int_{1}^{2} ln (2) \space dx=ln(2)
\end{align*}$$
# 3.1
$$\iint_{Q}e^{-x-y} dA$$
where Q is the first quadrant og the xy plane
her er området uendelig altså vi kigger på området mellem $x=0 \land x=\infty \land y=0 \land y=\infty$
dette kan vi så skrive op som vores grænser
$$\begin{align*}
\iint_{Q}e^{-x-y} dA\\
\int_{0}^{\infty}dx \int_{0}^{\infty}e^{-x-y}dy\\
\int_{0}^{\infty} \left. -e^{-x-y} \right |_{y=0}^{y=\infty}  \space dx \\
\int_{0}^{\infty}  -e^{-x-\infty} \space dx \\
\int_{0}^{\infty}  -e^{-x}\cdot e^{-\infty} \space dx \\
\int_{0}^{\infty}  -e^{-x}\cdot 0 \space dx=0
\end{align*}$$
