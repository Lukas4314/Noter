dette er differentialligningen af typen
$$ay''+by'+cy=0$$
## Løsningsmetode:
der opstilles først karakterligningnen:
$$ar^{2}+br+c=0$$
diskrimanten kan så findes som:
$$D=b^{2}-4ac$$
dette handler om hvormange løsningerne der er og hvordan de er dæmpet

D>0
her er det overdæmpet og løsningen er:
$$y(t)=A \cdot e^{r_{1}t}+Be^{r_{2}t}$$
D=0
her det kritisk dæmpet
$$y(t)=A \cdot e^{rt}+Bte^{rt}$$
D<0
her er det underdæmpet
$$y(t)=A \cdot e^{kt} \cdot cos( \omega t)+B \cdot e^{kt} \cdot cos(\omega t)$$
## Inhomogene tilfælde
her er at højre siden ikke lig med 0 altså 
$$ay''+by'+cy \neq 0$$
og dette kan fx være:
$$ay''+by'+cy=f(t)$$

## Eksempel
$$y''+4y=sin(t)$$
vi prøver her at gætte på en funktion af typen:
$$y_{p}(t)=A \cdot sin(t)+B \cdot cos(t)$$
og vi får dermed:
$$y_{p}''=-A \cdot sin(t)- B \cdot cos(t)$$
vi kan er indsætte det ind i differentialligningen
$$-A \cdot sin(t)- B \cdot cos(t)+4 \cdot (A \cdot sin(t)+B \cdot cos(t))=sin(t)$$
dette kan så reduceres:
$$3A \cdot sin(t) + 3B \cdot cos(t)=sin(t)$$
vi ser her at en løsning til dette er:
$$\begin{align*}
B&= 0\\
A&= \frac{1}{3}
\end{align*}$$
og vi får derfor en løsning som hedder:
$$y_{p}(t)= \frac{1}{3} \cdot sin(t)$$
