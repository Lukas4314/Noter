
i en matrix på 2x2 størrelse som matrixen her under:
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$ er determinanten a*d-c*b

på større matrixer som fx 3x3 med denne matrix
$$A=\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}$$
findes determinanten som 
$$det(A)=a*\begin{vmatrix}
e & f \\
h & i
\end{vmatrix}-b*\begin{vmatrix}
d & f \\
g & i
\end{vmatrix}+c*\begin{vmatrix}
d & e \\
g & g \\ 
\end{vmatrix}$$
den fulde måde at finde determinanten af en matrix er ved:
$$D=\sum\limits^n_{j=1}(-1)^{(j+k)}*D_{jk}*a_{jk}$$
eller for vilkårligt j i stedet for et vilkårligt k

$$D=\sum\limits^n_{k=1}(-1)^{(j+k)}*D_{jk}*a_{jk}$$
D_jk er determinanten uden række j og søjle k og a_jk er element i matrix A
ligesom tidligere hvor vi havde $$det(A)=a*\begin{vmatrix}
e & f \\
h & i
\end{vmatrix}-b*\begin{vmatrix}
d & f \\
g & i
\end{vmatrix}+c*\begin{vmatrix}
d & e \\
g & g \\ 
\end{vmatrix}$$ fulgte vi her første række
kort sagt så det man gør er at man vælger en række eller kolonne, så sætter man så -1 opløftet i række + søjle nr. hvor man så efter ganger det med elementet i den række og søjle man er nået til og ganger med determinanten at den matrix der vil stå hvis man fjernede den række og søjle
 i eksemplet igen fulgte vi første række og havde først -1 opløftet i 1+1 hvilket giver 1 og ganger det med elementet i rækken og kolonnen som var a og ganger det med Determinanten af matrixen når vi havde fjernet række og søjlen som vi var nået til. det fortsætter vi så med for resten af rækken som vi valgte. man kan vælge lige hvilket søjle eller række som man vil, og det er en fordel at vælge en som indeholder mange 0 fordi man så ganger med 0

Determinanten kan bruges til at afgøre [[Antal løsninger af Matrix|antallet af løsninger]]fordi hvis
## determinanten lig med 0
$$det(A)=0$$
betyder det at der findes 0 eller uendelig mange løsninger fordi nogle variabler er lig afhængige af hinanden. Determinanten lig med 0 betyder også at
$$rang(A)\neq rang(Ã)$$
## determinanten ikke lig med 0
hvis A er en nxn matrix er 
$$rang(A)=n$$
hvis 
$$det(A)\neq 0$$
og der findes kun 1 løsning



## Rækkeoperationer af en matrix
hvis der byttes rundt på rækker så skifter man fortegnet for determinanten

hvis man lægger en række til en anden række sker der ikke noget med determinanten

hvis man ganger en række med en konstant k som er forskellig med 0 så for hvis
$$D*k$$
alt dette gælder også for søjler ligesom med rækker

alt dette kan bruges til at gøre det nemmere at finde determinanten af enkelte matricer hvis man fx har nogle meget store matricer men man kan lækker rækker til så man får en række eller kolonne kun bestående af 0


## Regneregler for determinanten

$$det(c*A)=c^n*det(A)$$
her er n antallet af rækker og eftersom man når man ganger en række med en konstant så skal man så bliver determinanten konstanten større
$$det(A^T)=det(A)$$


lad B være nxn matrix
$$det(A*B)=det(A)*det(B)=det(B)*det(A)=det(B*A)$$
