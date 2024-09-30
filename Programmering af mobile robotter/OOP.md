## Key concepts
Klassen er skabelonen, og objektet er selve objektet.
Encapsulation er at variabler er private samt funktioner sådan at andre klasser ikke har adgang til det
Abstraction er når man kun definere det mest nødvendige for klasserne og så senere kan definere noget specifikt ved inheritance eller andet.
polymorphism er når forskellige klasser kan have de samme metoder og derfor kan en funktion kaldes for alle disse klasser selvom de er forskellige. som fx med at starte en bil er der forskellige klasser til forskellige biler men de har alle sammen en funktion som hedder start bil.

## Self
self er en parameter som er en pointer til objektet og dette parameter kan selv blive passed ind til funktionen. Self skal også være det første argument, men når man kalder en funktion behøves man ikke give det som argument.
den bruger ofte self til at have en reference til sit eget objekt og sine egne variabler da i en funktion kender den ikke til variabler som objekterne har medmindre der er igennem self som er blevet passed som argument.

## init 
init er Constructer og derved det første som bliver kaldt når et objekt bliver lavet.
