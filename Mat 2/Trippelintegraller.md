Sørg for at have styr på [[Dobbeltintegral]] først
trippelintegraller skrives ligesom dobbeltintegraller med med 3 integral tegn:
$$\iiint_{D}f(x, y, z) \space dV$$
i stedet for at integrerer over et areal som før integrerer vi nu over et volumen
her er $dV=dxdydz$
ligeledes som man gjorde med dobbeltintegraller hvor hvis man havde
$$\iint_{D}dA=areal(A)$$
så er:
$$\iiint_{D}dV=volumen(D)$$
et eksempel på hvor dette kam bruges er at man gerne vil finde en masse af et objekt men at densiteten af afhænger af hvilket punkt man befinder sig ved kan man finde det som:
$$\iiint_{S}\delta(x,y,z)dV$$
her er $\delta$ densiteten som afhænger af positionen

Når man skal beregne selve trippelintegrallet skal man egentlig bare gøre ligesom med dobbeltintegraller bare med en integration mere eller en iteration mere kan man også kalde det.

Eksempel:
$$\iiint_{T}y \space dV$$
T har punkterne: $(0, 0, 0), (1,0,0), (0,1,0), (0,0,1)$
vi har derved en form for pyramide som er væltet og som ligger op af de 3 planer og pager ud mod den positive del af alle akser (eventuelt tegn dem)
$$\int_{0}^{1}dx \int_{0}^{-x+1} dy \int_{0}^{1-x-y}y \space dz$$
dette kan så løses lige man gør når man finder dobbeltintegraller og man kommer så frem til
$$\iiint_{T}y \space dV = \frac{1}{24}$$

## Variabelskift
her kigger vi på $$\iiint_{D} f(x,y,z) dxdydz$$
vi kigger her på nogle nye variable $u, v, w$
vi kender også sammenhængen mellem u v og w
$$\begin{align*}
x(u,v,w)\\
y(u,v,w)\\
z(u,v,w)
\end{align*}$$
vi kigger nu på et nyt område som er beskrevet i u v w kordinater
$$\iiint_{S}f(x(u,v,w),y(u,v,w),z(u,v,w)| \frac{\partial(x,y,z)}{ \partial(u,v,w) } | dudvdw$$
vi introducerer her det som hedder jacobianten hvor vi har at:
![[Pasted image 20241115085146.png|500]]
### Specialtilfælde med cylinder koordinater
her har vi at sammenhængen mellem mellem variablerne er her:
$$\begin{align*}
x&= r \cos(\theta)\\
y &= r \sin(\theta)\\
z &= z
\end{align*}$$
hvis man plotter det og vinder ud af hvad man får dV til at være ved at kigge på en lille ændring i r, theta og z altså $dr, d \theta, dz$
vil man få en dV som er $dV=rdrd \theta dz$
her vil man så få at r er: $r=| \frac{\partial(x,y,z)}{ \partial(u,v,w) } |$  hvis man valgte at gøre det med jacobianten

### Specialtilfælde med sfæriske koordinater
her er forholdet mellem koordinaterne:
$$\begin{align*}
x&= R \sin(\phi) \cos(\theta)\\
y&= R \sin(\phi) \sin(\theta)\\
z&= R \cos(\phi)
\end{align*}$$
her kan man finde dV som:
$$dV=R^{2}\sin(\phi) \space dR \space d \phi \space d \theta$$



## Massemidtpunkt ved hjælp af trippelintegraller
man kan bruge trippelintegraller til at finde massemidtpunkter
vi har tidligere skrevet at:
$$m= \iiint_{R}\delta(x,y,z)dV$$
hvor delta var densiteten og m er massen
hvis man så vil finde massepunktet hvor densiteten afhænger hvorhenne i ens legeme man kigger kan det findes som:
$$\begin{align*}
\overline{x}= \frac{1}{m} \iiint_{R}x \delta(x,y,z) dV\\
\overline{y}= \frac{1}{m} \iiint_{R}y \delta(x,y,z) dV\\
\overline{z}= \frac{1}{m} \iiint_{R}z \delta(x,y,z) dV
\end{align*}$$
her finder man så massemidtpunktets koordinat 
her skal man så have styr på sine variabler fordi vi har x ,y eller z i integrallet som er i sfæriske koordinater eller andet og x skal derfor regnes om til de koordinater vi bruger så hvis det fx. var sfæriske ville man skulle indsætte $x= R \sin(\phi) \cos(\theta)$




