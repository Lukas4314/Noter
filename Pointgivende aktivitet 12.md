
## Opgave 1
bestem værdien af intergrallerne 
$$\int_{0}^{5}x^{-0,9}dx$$
$$\int_{5}^{\infty}x^{-0.9}dx$$
vi starter her med at kigge på integrallet $\int_{0}^{5}x^{0,9}dx$
$$\begin{align*}
\int_{0}^{5}x^{-0,9}dx\\
\left. 10x^{0,1} \right |_{0}^{5}\\
10 \cdot 5^{0,1}-10 \cdot 0^{0,1}&= 11,746
\end{align*}$$
vi kan nu kigge på det andet integral
$$\int_{5}^{\infty}x^{-0,9}dx$$
vi opskriver det her som en grænseværdi i stedet for et uendeligt integral
$$\lim_{R \to \infty}\int_{5}^{R}x^{-0,9}dx$$
vi kan her bare integrerer det ligesom før
$$\begin{align*}
\lim_{R \to \infty} \left ( \left. 10x^{-0,1} \right |_{5}^{R} \right )\\
\lim_{R \to \infty} \left (10 \cdot R^{0,1}-10 \cdot5^{0,1} \right )
\end{align*}$$
hvis her sætter uendelig ind på R plads vil det give $\infty^{0,1}$ hvilket vil være uendeligt og vi kan derfor skrive svaret som:
$$\int_{5}^{\infty}x^{-0,9}dx=\infty$$
