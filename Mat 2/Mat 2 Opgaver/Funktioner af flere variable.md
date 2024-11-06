## 13.1
1)
specify the domain of the function $f(x, y)=\frac{x+y}{x-y}$
$$Dm(f)=R^{2}\space \backslash \{x=y\}$$
ved ikke helt med notationen

2)
specify the domain of the function $f(x, y)=\sqrt{xy}$
$$Dm(f)=R^{2}\space \backslash \{xy>=0\}$$

4)
specify the domain of the function $f(x, y)=\frac{xy}{x^{2}-y^{2}}$ 
$$Dm(f)=R^{2}\space \backslash \{x \neq \pm y\}$$

7)
specify the domain of the function $f(x, y)=ln(1+xy)$
$$Dm(f)=R^{2}\space \backslash \{xy \leq-1\}$$


19)
Sketch some of the level curves of the function $f(x,y)=x-y$
tegner det i matematika 
![[Pasted image 20241031194748.png|500]]
i dette her tilfælde $x-y=[0,5]$ med hop på 1
kommandoerne i Mathematica er:
Table\[x - y == n, {n, -5, 5}]
ContourPlot\[%, {x, -5, 5}, {y, 0, 5}, PlotLegends -> "Expressions"]


20)
Sketch some of the level curves of the function $f(x,y)=x^{2}+2y^{2}$
tegner det igen i Mathematica med samme fremgangsmåde
![[Pasted image 20241031194659.png|500]]

21)
Sketch some of the level curves of the function $f(x,y)=xy$
igen samme måde
![[Pasted image 20241031194924.png|500]]


## 13.2

1)
Evaluate the limit or explain why it does not exist 
$$\lim_{(x,y) \to (2,-1)}\space xy+x^2$$
her kan vi bare indsætte det
$$\lim_{(x,y) \to (2,-1)}\space xy+x^2=2 \cdot (-1)+2^{2}=2$$



3)
Evaluate the limit or explain why it does not exist 
$$\lim_{(x,y) \to (0,0)}\space \frac{x^{2}+y^{2}}{y}$$
vi prøver her at følge linjen $y=x$ og indsætter dette ind i stedet for
$$\lim_{(x) \to (0)}\space \frac{x^{2}+x^{2}}{x}$$
dette kan vi godt løse:
$$
\begin{align*}
\lim_{(x) \to (0)}\space \frac{x^{2}+x^{2}}{x}\\
\lim_{(x) \to (0)}\space \frac{2 \cdot x^{2}}{x}\\
\lim_{(x) \to (0)}\space 2x=0
\end{align*}
$$
hvis vi følger linjen $y=x$ får vi en grænseværdi på 0 men vi kan lige prøve at følge linjen $y=x^{2}$
$$\lim_{(x,y) \to (0,0)}\space \frac{x^{2}+x^{2^{2}}}{x^{2}}$$
dette kan vi så reducerer
$$\begin{align*}
\lim_{(x,y) \to (0,0)}\space \frac{x^{2}+x^{2^{2}}}{x^{2}}\\
\lim_{(x,y) \to (0,0)}\space \frac{x^{2}+x^{4}}{x^{2}}\\
\lim_{(x,y) \to (0,0)}\space 1+x^{2}=1
\end{align*}$$
vi får derfor 2 forskellige grænseværdier afhængigt af hvilken linje vi følger og der findes derfor ikke en grænseværdi for punktet (0, 0) til denne funktion

5)
Evaluate the limit or explain why it does not exist 
$$\lim_{(x,y) \to (1,\pi)}\space \frac{cos(xy)}{1-x-cos(y)}$$
vi kan ved den her bare regne den
$$\begin{align*}
\lim_{(x,y) \to (1,\pi)}\space \frac{cos(xy)}{1-x-cos(y)}\\
\frac{cos(1 \cdot \pi)}{1-1-cos(\pi)}\\
\frac{cos(\pi)}{-cos(\pi)}=-1
\end{align*}$$
vi har derved fundet grænseværdien til at være -1





7)
Evaluate the limit or explain why it does not exist 
$$\lim_{(x,y) \to (0,0)}\space \frac{y^{3}}{x^{2}+y^{2}}$$
vi kan her først forsøge at følge en linje og vi kan følge linjen $x^{2}=y^{2}$ 
$$\begin{align*}
\lim_{(x,y) \to (0,0)}\space \frac{y^{3}}{y^{2}+y^{2}}\\
\lim_{(x,y) \to (0,0)}\space \frac{y^{3}}{2 \cdot y^{2}}\\
\lim_{(x,y) \to (0,0)}\space \frac{y}{2}=0
\end{align*}$$
eftersom jeg ikke kan finde nogle linjer i hovedet som giver en anden grænseværdi bliver vi nødt til at tage det på den hårde måde hvor der er 2 ting som skal opfyldes
$$|f(x, y) -L| <\epsilon$$
her er L vores grænseværdi hvor vi har fået den til 0
$$|f(x, y)| <\epsilon$$
vi kan nu indsætte vores funktion
$$|\frac{y^{3}}{x^{2}+y^{2}}| <\epsilon$$

og vi skal også have opfyldt at
$$0<\sqrt{(x-a)^{2}+(y-b)^{2}}< \delta$$
her er (a, b) punktet som vi er interesseret i og i vores tilfælde er (0, 0)
$$0<\sqrt{x^{2}+y^{2}}< \delta$$
vi får her en god ide som siger at $y^{2}\leq y^{2}+x^{2}$ og dette medfører at 
$$\frac{y^{2}}{y^{2}+x^{2}}\leq 1$$
eftersom at $y^{2}+x^{2}$ ikke kan være negativt skal vi ikke tænke på dette tilfælde hvor man ellers skulle vende uligheden
dette kan vi så gange med |y| på begge sider for at få
$$\frac{y^{2}}{y^{2}+x^{2}} \cdot |y|\leq |y|$$
eftersom at selve brøken kun kan være positivt og |y| også altid er positivt kan vi skrive det som:
$$|\frac{y^{3}}{y^{2}+x^{2}}|\leq |y|$$
her har vi så også at den absolute værdi af y er det samme som $\sqrt{y^{2}}$ og det faktum at $x^{2} \geq 0$ kan vi skrive:
$$|y|\leq \sqrt{y^{2}+x^{2}}$$
dette kan vi så indsætte ind i vores ligning fra før
$$|\frac{y^{3}}{y^{2}+x^{2}}|\leq |y|\leq \sqrt{y^{2}+x^{2}}$$
fra tidligere havde vi defineret $\sqrt{x^{2}+y^{2}}< \delta$ og vi kan derfor indsætte dette
$$|\frac{y^{3}}{y^{2}+x^{2}}|\leq |y|\leq \sqrt{y^{2}+x^{2}}< \delta$$
her kan vi så fjerne nogle mellemled og få:
$$|\frac{y^{3}}{y^{2}+x^{2}}|< \delta$$
hvis vi så sammenligner med et af kravende fra tidligere:
$$|\frac{y^{3}}{x^{2}+y^{2}}| <\epsilon$$
her husker vi så at vi skulle finde en sammenhæng mellem epsilon og delta for at dette var grænseværdien og den kan vi finde som $\delta = \epsilon$ og så er kravende opfyldt og epsilon og delta afhænger af hinanden


