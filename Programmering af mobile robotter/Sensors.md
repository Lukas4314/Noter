Forskellige sensorer

Afstandsmåler findes der forskellige former som fx. ultrasonic distance sensor og burger princippet ToF som står for time og flight
en anden form er en lidar som står for Light Detection and ranging som også måler og sender ud men rotere og derfor får data rundt om sig selv.

Andre sensorer er Orientation sensors som indeholder accelerometer gyroskop og magnetometer som er et compass. man kombinerer ofte disse sensorer for at få dem til at spille sammen og få mere præcision som man kalder for en IMU som står for inertial measurement unit.

Der findes også GNSS som står for global navigation satelite systems som er GPS men det er primært kun i europa eller USA vi bruger GPS hvor andre lande bruger andre systemer stort set virker ligeledes og som også er GNSS

## Kategorier af sensorer

### Internal VS external
Internal er indre måler på robotten som fx temperatur på robotten eller måler af strømen af robotten eller accelerometer eller lignende, altså de måler ting på robotten hvor data er uafhængig af hvor den er
external er målinger af omgivelserne



### Local vs global
locale som er monteres på robotten som fx kamera eller lignende
globale er ting som er monteret på omgivelserne som fx GNSS

### Active and passive
de aktiver sensorer er nødt til at sende noget ud for at kunne måle noget som fx afstandssensoren som sender noget ud for at kunne måle det.
Passive er ting som fx accelerometer eller lignende som bare måler.

## Data fra Sensorer
de kan måle forskellige alle sensorer

### Binær sensorer
binære sensorer kan er dem som enten er sande eller falske som fx en knap

### Analog sensorer
Det er sensorer som en variable men kontinuer strøm
dette kan fx være potentiometer eller LDR

### Digital sensors
konvertere analog signaler til digitale, dette betyder at der ikke behøves at bruge ADC til at få data og vi kan derved bare bruge en eller anden form for kommunikation som I2C eller lignende 


## ADC
det står for analog to digital converter
der er mange forskellige men det vigtigste begreber er Sampling rate som er hvor ofte man sampler opgivet i en frekvens ofte. Resolution er den anden og fortæller hvor præcist den kan måle og er ofte opgivet i bits så fx 1 bit kan den ikke vær sandt eller falsk hvilker gør at vores analog værdi enten bliver til 1 eller 0, men de typiske værdier er 8 bit til 16 bit som kan give enten 256 værdier eller 65xxx værdier
ved ADC er der et hav af forskellige fejl hvor 2 af dem er vær at nævne som er:
Quantization error som er jo lavere resolution jo værre er vores målinger da det ikke er særlig præcist og forskellige spændinger kan blive målt til det samme fordi resolutionen ikke er høj nok og der kan derfor ikke kendes forskel på dem.

den anden er Aliasing som er at væres sampling rate skal være stor nok til at måle ordentligt
der er derfor laves en regel som er Nyquist theorem som siger at vores sample rate skal være større end 2 gange den højeste frekvens af det som vi vil måle altså:
$$
f_{s}>=f_{max}
$$
der er lidt ligesom et hjul som kører hurtigt rundt og så ligner det lidt at det kører baglens
vi kommer til at høre mere i fremtiden med signalbehandling

for en pico findes der 5 forskellige ADC men nr 3 og 4 kan ikke bruges da de bruges af picoen i forvejen som derfor anbefales der ikke dette.
ADC er 12 bit og svinger fra 0-4095
