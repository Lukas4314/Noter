LVTTL er en standard for transistorer inde i picoen som fx, dette betyder at der ikke må indsættes mere end 3,3 V og mindre end 0 V
den siger også at alle spændinger som er mindre end 0,8 V skal opfattes som logisk 0.
ydermere siger standarden også at en spænding som er større end 2.0 V skal den opfattes som logisk høj. Alt i mellem disse spændinger er unikt fra chip til chip og det er derfor en garanti.
ofte er skelnet på 1,2 V men der er ingen garanti på hvad den læser det som. desuden er grænsen i praktisk hård hvilket betyder at det ikke er tilfældigt, men forskellig fra chip til chip, men som sagt ofte omkring 1,2 V. små ændringer skyldes, produktionsfejl, varme, alderdom eller noget andet.

På outputs lover den i stedet at give minimum 2,4 V og maximum 0,4 V for henholdsvis højt og lav hvilket er smart fordi hvis du skal sætte dem sammen er det meget vigtigt der ikke er et spændingsfald igennem ledningen på et output som resulterer i at et input på en anden IC ikke sikkert vil fange det som høj, men eftersom er er 0,4 V forskel mellem 2,4 V og 2 V kan der være et spændingsfald på 0,4 V fra en IC til en anden hvor den stadig vil fanges som høj



## VTTL
VTTL er ligesom LVTTL men er i stedet lavet til 5V i forhold til LVTTL som er til 3,3 V
