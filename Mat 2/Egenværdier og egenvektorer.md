vi skal løse et problem som hedder
$$(A-\lambda \cdot I)\vec{x}=\vec{0}$$
hvor$$\vec{x} \neq0 $$
egenværdien er så
$$det(A - \lambda \cdot I)=0$$
hvor lambda er egenværdien som man skal finde i ligningen herover
for hver egenværdi findes der en egenvektor vec(x)
$$(A-\lambda \cdot I) \cdot \vec{x} = \vec{0}$$
denne ligning herover skal man så løse i forhold til vec(x) for at finde egenvektoren
for nxn matrix findes mindst 1 egenværdi og maks n egenvektor

## eksempel
$$A=\begin{pmatrix}-5 & 2 \\ 2 & -2\end{pmatrix}$$
$$det(A-\lambda \cdot \lambda)=0$$
$$\begin{align*}
A-\lambda \cdot I&= \begin{pmatrix}-5 & 2 \\ 2 & -2\end{pmatrix}-\lambda \cdot\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}\\\\

&= \begin{pmatrix}-5-\lambda & 2\\
2 & -2-\lambda\end{pmatrix}\\
\end{align*}$$
$$
\begin{align*}
det\begin{pmatrix}-5-\lambda & 2\\
2 & -2-\lambda\end{pmatrix} &= 0\\
(-5-\lambda) \cdot(-2-\lambda)-4&= 0\\
\lambda^2+7\lambda+6=0
\end{align*}
$$
dette løses og bliver til
$$\lambda=-1$$
$$\lambda=-6$$
dette her er derved egenværdierne altså lambda
disse 2 indsættes derefter ind i ligningen
$$(A-\lambda \cdot I)\vec{x}=\vec{0}$$
man kan nu finde vektor x, i dette eksempel hvor man bruger -1 som egenværdi er der ikke 1 løsning men uendelige da det ene element i vektoren afhænger af det andet. Det samme gør man også for den anden egenværdi og man får også 2 elementer i en vektor som afhænger af hinanden
vektoren x har dog altid den samme retning når man har løst den med en af egenværdierne hvilket også betyder at dine 2 elementer for din vektorer altid kan findes ved den anden ganget med en skalar


## Hvad man kan bruge det til
det kan bruges til at bestemme "spredning" eller retning af en "BLOB" eller datapunkter
hvis man har en hel del punkter som har en retning hvor den går en retning, og man så har et middelpunkt midt i punkterne. så vil den primære retning være den vej hvor punkter mest bevæger sig hen i forhold til middelpunktet. den vektorer er den største egenværdi
![[Pasted image 20241004100321.png]]
fx i dette her billede så er der nogle punkter og den primære retning vil være op mod højre, den vil så også have en sekunder retning som er vinkelret på den primære og er den vektor som kommer ved den mindste egenværdi
punnkter vil være i en matrix som har 2 søjler og n rækker alt efter hvor mange punkter man har
middelværdien vil være 1 vektor som tager gennemsnittet af alle x som x og y som y
hvis vi kalder u for vektoren som er middelværdien
kan vi finde afvigelsen som
$$B=X-h \cdot (\vec{u})^T$$
Her er X datapunkter i en matrix og vec(u) er gennemsnittet i en vektor med 2 rækker og 1 søjle og h er 
$$h=\begin{pmatrix}1 \\ 1 \\ 1 \\ osv\end{pmatrix}$$
hvor den har n rækker og er af størrelsen nx1
dette er det samme som at trække gennemsnittet fra alle punkter og gemme det i B

efter dette skal vi regne vores [[Covarians matrix]]
dette er
$$C=\frac{1}{n-1}\cdot B^{T}\cdot B$$
her indeholder B reelle tal og er matrixen fra før
nu skal vi så bestemme egenværdier til C
og ud fra dette kan vi finde 2 vektorer hvor den største egenværdi giver vektoren som har samme retning som "hoved aksen" fra billedet tidligere var det op mod højre, og den mindste egenværdi er derfor mindst spredning som også er vinkelret ind på den anden vektor

hvis vi så gemmer vores 2 vektorer i en variable W
$$W=\begin{pmatrix}\vec{v_{1}} & \vec{v_{2}}\end{pmatrix}$$
så er 
$$T=B \cdot W$$
dette projicere data ind på dataspredning (ikke helt sikker på hvad dette betyder)

