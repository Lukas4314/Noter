står for pulse width modulation

Det er en klasse i Machine library.


### duty cycle
Duty cycle er hvor lang tid vi har PWM signallet høj,
der er også forskel på hvor høj frekvens man har om hvor hurtigt den skal skifte. Der er også mulighed for at man kan høre skiftene hvis man har en for lav frekvens.

## for RP2040
der er i alt 8 individuelle PWM slices som giver et total på 16 kanaler.
det fungerer på RP2040 ved at man har en counter på 16 bit (65535) som tæller op og en counter compare (CC) og så længe ens kinder er under grænsen sætter man pinen høj og lav ellers.


## frekvens for PWM
i princippet ligegyldigt medmindre det larmer, eller hvis der er en chip som ikke kan holde til for høj frekvens

