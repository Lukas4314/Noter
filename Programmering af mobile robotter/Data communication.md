Når man skal sende data er der forskellige måder at gøre det på.

en måde er at gøre det parallelt hvilket betyder at hver bit har en lednings og dette er meget hurtigt men kræver mange ledninger
en anden måde at gøre det på med serial kommunikation hvor bits bliver sendt 1 efter en, men dette er dog langsommere, men kræver langt mindre ledninger

ud over dette kan man kommunikerer synkront hvilket betyder at der er en fælles klokke som bestemmer hvor hurtigt man kan kommunikere, men ligeledes findes der også en asynkron måde at kommunikerer hvor der ikke er nogen klokke.
eksempler på dette er at I2C er synkron fordi der er en klokke. en asynkron måde at kommunikere på kan være emails, txt beskeder eller andet hvor der ikke er nogen klokke, men i stedet bare sender og læser


## Duplex
dette betyder at man kan modtage eller sender beskeder samtidigt
ud over dette er der noget som hedder full duplex hvilket betyder at man kan sende og skrive samtidig på forskellige ledninger. Der findes også half duplex hvor der kun kan sendes eller skrives på 1 ledning.

## Simplex
Her er data kun sendt 1 vej


## Protocol
en protocol er egentlig bare en fælles forståelse af hvordan dataene som bliver sendt eller modtaget skal forstås.



# I2C
Dette er en 2 wired synkron protocol. De 2 ledninger hedder SDA og SCL som er henholdsvis data og klokken
Den har en master slave arkitektur
den kan have 128 forskellige enheder fordi at deres adresser er 7 bit hvilket betyder at der kan forbindes 127 andre forskellige udover masterens adresse.
Når kommunikationen skal starte så er alle linjer sat høj, masteren vælger så at sætte datalinjen lav og derefter sætte klokken lav og på den måde er de alle synkroniseret op til masterens klokke
efter dette følger der 7 bits som er adressen på slaven som den gerne vil snakke med
når der skal sendes data over kan den enkelte bit ikke ændres så længde at klokken er høj, dette betyder at når klokken går lav vil ens bit ændrer sig til den næste i rækken og når den så går højt igen vil man så kunne måle sin næste bit
efter vores 7 adresse bit så følger der et read/write bit som er om man vil måle eller skrive til sin I2C, efter dette sender slaven så et acknowledgement bit som er høj hvis slaven har forstået det
efter dette bliver der så sendt 8 bit data efterfulgt af en acknowledgement hver gang. efter man har sendt alt sit data går klokken så høj samt datalinjen hvilket gør at slaverne venter på at den næste master sætter klokken lav og tager styringen igen.



# SPI 
SPI er four wire full duplex synkron kommunikation mellem 1 master og en eller mange slaves
den første ledning er CS som er chipselect, hvilket betyder at der kører 1 linje fra masteren til slaves og dette medfører også at der skal være en linje pr slave hvilket resulterer i mange ledninger hvis der er mange slaves
den næste ledning er SCLK som er klok linjen
efter det har vi vores 2 linjer som bliver brugt til transmit og receiver og de hedder MOSI og MISO som står for master out slave in og master in slave out.
Når der skal kommunikeres over SPI skal man starte med at sætte sin CS lav for at sige man gerne vil snakke med den enkelte slave. efter dette begynder den at sende klokken ud for at synkroniserer kommunikationen gennem masteren. Hastigheden på klokken har ikke nogen standard men man vil ofte gå op til MHz. ud over dette har man også en klokke polaritet som er defineret alt efter hvordan ens klokke starter, altså om den skal læse når klokken går lav eller når den går høj. Dette er beskrevet som CPOL hvor CPHA 0 er når den går høj skal den læse og CPHA 1 læser den når den går lav. denne konfiguration bliver kaldt for CPOL. 
(ikke sikker på det med CPOL og CPHA)

efter dette kan man sender beskeder over MOSI og modtage beskeder på MISO, der bliver ydermere ofte sendt 8 bits ad gangen. 


# UART
UART er en 2 wire full duplex asynkron serial kommunikation
med UART har vi en receiver og transmitter linje som hedder RX og TX, men her skal man huske at kryds dem så at transmit bliver sat til receiver på det man vil kommunikere sammen med.
I UART er vores hastighed opgivet i Baud-rate som fortæller hvor hurtigt vi kommunikerer vores data og det er står for bits per second. 
Framestrukturen er at når vi ikke sender noget så er TX hold højt or når man så vil sende noget trækker man den lav for så at sende sit data i  enten 7, 8 eller 9 bits. efter dette har man mulighed for at lave et parity check med en ekstra bit hvor at hvis man har et lige tal så skal parity bit sættes til 0 eller ulig skal det sættes til 1, dette betyder at hvis der er en bit som fejler vil man ikke få det lige eller ulige tal man forventer. det der menes når man tjekker om en der er lige eller ulige sine bits er at man lægger det sammen sådan at 0110 = 2 altså lige og 111=3 altså ulige