#Differentialligninger


# Eksponentiel vækst 
ved en eksponentiel vækst har vi at væksten kan beskrives som:
$$\frac{dy}{dx}=k \cdot y$$
den generelle løsning til denne differentialligning er:
$$y(x)=y_{0} \cdot e^{k \cdot x}$$

## Fordoblings og halveringskonstant
fordobling og halveringskonstanten kan findes som:
$$\begin{align*}
T_{f}&= \frac{ln(2)}{k}\\
T_{h}&= -\frac{ln(2)}{k}
\end{align*}$$
det kan udeledes ved at regne:
$$f(x+T)=2 \cdot f(x)$$
her skal så isoleres T når det indsættes ind i en eksponentiel funktion som vist herover som den generelle løsning til en eksponentiel vækst 





# Logistisk vækst
logistisk vækst har formen:
$$\frac{dy}{dt}=k \cdot y \cdot \left(1-\frac{y}{L}\right)$$
dette her er en vækst som vokser i forhold til hvor meget der er men når et maks på et tidspunkt som er L antal 
et eksempel kan være en dyreart som formerer sig men på et tidspunkt ikke har nok mad til at formerer sig og derfor når et maks antal L

### Løsning til logistisk vækst 
løsningen er givet ved 
$$y(t)=\frac{L \cdot y_{0}}{y_{0}+(L-y_{0}) \cdot e^{-kt}}$$
vi kan tjekke om grænsen passer ved at:
$$\lim_{t \to \infty}y(t)=L$$
hvis dette indsættes ind i udtrykker får vi at $e^{-kt}$ bliver til $\frac{1}{\infty}$ og vi har derved en brøk som hedder:
$$y(t)=\frac{L \cdot y_{0}}{y_{0}}$$
og dette giver så L hvilket er det som det skulle
## Bevis for løsning til logistisk vækst 
![[Pasted image 20241107111953.png|500]]
![[Pasted image 20241107112021.png|500]]
![[Pasted image 20241107112036.png|500]]
![[Pasted image 20241107112049.png|500]]
![[Pasted image 20241107112120.png|500]]
![[Pasted image 20241107112130.png|500]]
![[Pasted image 20241107112138.png|500]]


# Anden ordens differentialligninger
her har vi en ligning som hedder:
$$a \cdot y'' +b \cdot y' + c \cdot y = 0$$
![[Pasted image 20241107113045.png|500]]
![[Pasted image 20241107113101.png|500]]

man kan som altid forsøge at gætte på nogle løsninger
når man så har gjort det kan man indsætte det ind i ligningen og så skal det så selvfølgelig give 0
hvis man fx gætter på at
$$y(t)=e^{rt}$$
vil man få en ligning som hedder
$$e^{rt} \cdot (ar^{2}+br+c)=0$$
her skal enten $e^{rt}$ give 0 eller det andet hvor $e^{rt}$ ikke kan give 0 hvilket betyder at
$$ar^{2}+br+c=0$$
dette kan undersøges ved at finde diskriminanten
$$D=b^{2}-4ac$$
vi har her 3 tilfælde som kan forekomme når man forsøger med sin differentialligning og dette medfører at der er 3 forskellige løsningsformer der kommer an på hvilken differentialligning

tilfælde 1 $D>0$
her får vi 2 rødder og en løsning vil derfor være
$$y(t)=A \cdot e^{r_{1}t}+B \cdot t \cdot e^{r_{2}t}$$
Tilfælde 2 $D=0$
her har vi den generelle løsning som er:
$$y(t)=A \cdot e^{rt}+ B \cdot t \cdot e^{rt}$$
tilfælde 3 $D<0$
i dette tilfælde har vi kun komplekse rødder
her får vi løsningerne
$$r=\frac{-b}{2a}\pm i \cdot \frac{\sqrt{-D}}{2a}$$
læg her mærke til at der står plus minus den komplekse del
dette giver så en generel løsning som er
$$y(t)=A \cdot e^{kt} \cdot cos(\omega t)+B \cdot e^{kt} \cdot sin(\omega t)$$
her er $\omega = \frac{\sqrt{-D}}{2a}$ 
dette her giver er så en svingning da det kan beskrives med det komplekse plan og det giver derved 3 forskellige svinginger:
### Underdæmpet system
![[Pasted image 20241107114428.png|500]]
### Kritiskdæmpet system
![[Pasted image 20241107114438.png|500 ]]
### Overdæmpet system
![[Pasted image 20241107114449.png| 500]]

### Eksempel
![[Pasted image 20241107115118.png|500]]
![[Pasted image 20241107115129.png|500]]