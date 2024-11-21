Grænseværdier bruges blandt andet til når man skal differentierer noget hvor man har definitionen for differentialregning:
$$\lim_{h \to 0} \left ( \frac{f(x+h)-f(x)}{h} \right )=f'(x)$$
ud fra dette kan man udlede mange af definitionerne for funktioner differentieret som fx:
$$\frac{d}{dx}x^{2}=2x$$
hvis man indsætter $x^{2}$ ind på $\lim_{h \to 0} \left ( \frac{f(x+h)-f(x)}{h} \right )=f'(x)$ vil man få 2x


#### Hvornår eksisterer grænseværdier
![[Pasted image 20241121103721.png|500]]
![[Pasted image 20241121103730.png|500]]

## Kapløb mellem funktioner
der er hvor hurtigt noget vokser, inde for software bruges O() notaton som er hvor hurtigt noget er og hvordan det skalerer med antallet af ting som algoritmen skal bruges på
det er relevant hvor man har grænseværdier som vokser mod det uendelige som fx udtrykket:
$$\lim_{x \to \infty} \left ( \frac{2x^{2}-x+3}{3x^{2}+5}  \right )$$
her kan man så forlænge brøkken med $\frac{1}{x^{2}}$ og man vil så få:
$$\lim_{x \to \infty} \left ( \frac{2- \frac{1}{x} + \frac{3}{x^{2}} }{3+ \frac{5}{x^{2}} }  \right )$$
her kan man så indsætte at x går mod uendelig og så vil meget af det gå mod 0 og man vil få:
$$\lim_{x \to \infty} \frac{2}{3}$$
forskellige funktioner vokser med forskellige hastigheder og et overblik over hvilke som vokser hurtigst kan ses her:
![[Pasted image 20241121111855.png|500]]


# L'Hoptials regel 
L'hopitals regel kan bruges når vi skal finde grænseværdien.
den kan kun bruges når vi har at:
$$\begin{align*}
\lim_{x \to a} \frac{f(x)}{g(x)}\\
\frac{f(a)}{g(a)}&= \frac{\infty}{\infty} \lor \frac{0}{0}
\end{align*}$$
det man så kan gøre er at man kan sige:
$$\lim_{x \to a} \frac{f(x)}{g(x)}=\lim_{x \to a} \frac{f'(x)}{g'(x)}$$
her kan man så få et resultat som man eventuelt kan bruge eller arbejde videre med
et eksempel på sådan en funktion er:
$$\lim_{x \to 1} \frac{sin(\pi x)}{x^{2}-1}$$
her hvis der indsættes $x=1$ vil man få $\frac{0}{0}$ og man kan derfor differentierer tæller og nævner og få
$$\lim_{x \to 1} \frac{cos(\pi x) \pi}{2x}$$
her kan vi så godt indsætte $x=1$ og dermed kan vi løse denne

## L'hopital med linearisering
en anden måde at finde grænseværdier som normalt ikke kan findes er ved at linearisering tæller og nævner
altså hvis man har en funktion:
$$\begin{gather*}
f(x)\\
f_{L}= f(a)+f'(a) \cdot (x-a)
\end{gather*}$$
her er a x værdien man vil lineariserer omkring
dette er også det som ender med L'hopitals regel 

