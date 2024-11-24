## Opgave 1

$$\lim_{x \to -1}\left ( \frac {x^{3}+3x^{2}+2x} {x^{2}+4x +3} \right )$$
vi kan her ikke indsætte -1 på x plads fordi man så vil dividerer med 0
der faktorisere så i tælleren og nævneren:
$$
\begin{align*}
x^{3}+3x^{2}+2x &=x(x+1)(x+2)\\
x^{2}+4x+3&= (x+1)(x+3)
\end{align*}
$$
dette kan vi så indsætte ind i grænsen igen
$$\begin{align*}
\lim_{x \to -1} \left ( \frac {x \cancel{(x+1)}(x+2)} {\cancel{(x+1)}(x+3)} \right )\\
\lim_{x \to -1} \left ( \frac {x (x+2)} {x+3} \right )
\end{align*}$$
nu kan vi så indsætte -1 på x plads
$$
\begin{align*}
\lim_{x \to -1} \left ( \frac {x (x+2)} {x+3} \right )&=  \frac {-1(-1+2)} {-1+3}\\
&=  \frac {1-2)} {2}\\
&=- \frac {1} {2}
\end{align*}
$$
vi har derved at $$\lim_{x \to -1}\left ( \frac {x^{3}+3x^{2}+2x} {x^{2}+4x +3} \right )=- \frac{1}{2}$$
