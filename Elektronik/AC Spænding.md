(Anbealer til at læse Impedans noten når man når dertil i noten her da de hænger meget sammen)
grafen over veksel spænding er en sinus funktion hvilket også er den som er tegnet på symbolet for vekselspænding. det behøver ikke at være en sinus funktion som en vekselspænding laver men det er stadig symbolet fordi den spænding man har i stikkontakten er med en sinus funktion.
dette betyder også at en firkant signal egentlig også er en vekselspænding fordi den veksler
desuden behøver spændingen heller ikke være periodisk for at det er en vekselspænding.
Kort sagt kan man sige at alle spændinger som ikke er konstante med tiden er vekselspænding.
en anden grund til at man ofte bruger sinus formede spændinger til vekselspænding er fordi at man i teorien kan lave alle former for vekselspænding ved summen af sinus spændinger og man kan derfor udtrykke alle vekselspændinger ved hjælp af sinus spændinger og kan derfor nøjes med at arbejde med sinus spændinger og teorien bag dette.

en måde at gøre dette på er med at starte med funktionen:
$$f(t)=sin(2 \pi *f *t)$$
hvis man så lægger endnu et led til som hedder
$$f(t)=sin(2 \pi *f *t)+\frac{1}{3}sin(2\pi*3*f*t)$$
dette vil så ligne mere en firkant puls og man kan derved lave en firkant puls ud fra vekselspænding.
man kan forsøge at tegne graferne hvis det er i MATLAB eller andet for bevis

### Sinusoide funktioner
det er funktioner som minder om sinus på formen som fx cosinus.
de kan blandt andet beskrives som
$$f(x)=U_{max} \cdot cos(\omega \cdot t \cdot \phi)$$
man bruger ofte cosinus da det har fordelen at hvis t er 0 og phi også er 0 så giver det startspændingen. Desuden kan man også måle perioden på toppen af funktionerne eller som
$$T=\frac{2\pi}{\omega}$$
her er T perioden
Desuden er omega i radianer pr sekund da det er nemmere i forhold til matematik da vi jo har med en trigonometrisk funktion. Man skal huske at omega er vinkelhastigheden og ikke frekvensen hvor vinkelhastigheden er frekvensen ganget med 2 pi altså:
$$\omega=2\pi \cdot f$$
Sinusoider kan også beskrives med komplekse tal hvor
$$\begin{align*}
r&= U_{max}\\
\theta&= \omega \cdot t + \phi
\end{align*}$$
og dette medfører
$$e^{j \cdot \theta}=cos(\theta)+\sin(\theta) \cdot j$$
se blandt andet [[Komplekse tal]]

En af årsagerne til at vi hellere vil have det på kompleks form i stedet for at "arbejde" igennem med cosinus til spændingen er når man har flere spændinger i samme kredsløb eller andet så er det svært at addere dem eller gange dem hvis man skal det i forhold til Kirchhoff eller noget. men ved at skrive det på kompleks form bliver det en hel del nemmere at arbejde med. Mere præcist kalder man det for en vektor i det komplekse plan som hedder [[phasor]] på engelsk
ved at skrive det med phasors kan man blandt andet reducrer ting som dette:
![[Pasted image 20241024100712.png]]
på den måde kan man reducerer et langt udtryk af cosinusfunktioner til noget simpelt


ud fra dette kan vi også skrive sinioder som
$$U_{max} \cdot e^{j \cdot (\omega \cdot t + \phi)}$$
dette er dog kun en model hvor det der sker i virkeligheden er egentlig kun de reelle del som blandt andet kan skrives som
$$Re(U_{max} \cdot e^{j \cdot (\omega \cdot t + \phi)})=U_{max} \cdot \cos(\omega \cdot t + \phi)$$
vi har derfor 2 måder at definere vores vekselspænding på 2 måder som er den samme sinusoide hvor den ene er en cosinus funktion og den anden er et kompleks tal

dette kan man så bruge når man regner på kredsløb med vekselstrøm. hvis man fx har en modstand i et kredsløb med en vekselspænding vil strømmen også varierer med tiden og er faktisk også en sinusoide og kan derfor både beskrives med en trigonometrisk funktion eller som et kompleks tal
man kan så beskrive det med en phasor som:
$$U(t)=U_{max}\angle \theta$$
her er det dog vigtigt at bemærke at U max er spændingen over det man måler på og er altså ikke spændingen på spændingskilden, med mindre man måler på spændingskilden selvfølgelig

strømmen i de her tilfælde kan man også beskrive som kompleks tal men her skal den faseforskydes med 90 grader hvilket betyder at hvis vi kigger på et tidspunkt så vil det have en vinkel, hvor man så skal lægge 90 grader oveni den vinkel og så kigge på den reelle del af det komplekse tal som man har for strømmen. formlen for det har jeg ikke her


### Note to self omkring forelæsningen den 23/10
årsagen til forvirringen omkring Anders' forelæsning omkring rotation og kigge fra gulvet stammer højst sandsynligt fra at vi arbejdede med en kondensator hvilket gjorde at den impedans var et kompleks tal og det var det som han mente med at den var roteret 90 grader



### Spændingsdeler med Vekselstrøm (AC)
når man arbejder med en spændingsdeler og har vekselstrøm virker det fuldstændig ligesom med en spændingsdeler for DC men her skal man dog regne med dens [[Impedans]]. dette betyder dog også at hvis man har en serieforbindelse hen over nogle komponenter men man kan finde impedansen af alle komponenter er det meget lige til at regne både strømmen og spændingen hen over en af komponenterne. Ohms lov virker også på impedanser til at beregne strømstyrken


### Reducering af kredsløb med AC
når man har lyst til at reducere et kredsløb som står som vekselstrøm er der nogle steps man kan gøre sig
først skrive man de komponenter op som impedanser da man skal regne med deres impedans for at reducerer det. 
efter dette skiver man sin spændingskilde op som en phasor da det også skal bruges til at regne videre, det er her også vigtigt at alle ens spændingskilder har samme frekvens
efter dette kan man regne det ligesom hvis det var et kredsløb med jævnstrøm hvor alle regler gælder så som Kirchhoff eller erstatningsmodstande.
