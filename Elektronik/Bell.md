Bell er en skala som bliver brugt til at udtrykke lydstyrke primært.
årsagen til at denne blev lavet er fordi menneskers hørelse ikke er lineært men i stedet logaritmisk, formlen for bell skalaen er:
$$Bell=log_{10}\left(\frac{p_{out}}{p_{in}}\right)$$
i forhold til elektronik og spænding kan effekten findes som:
$$P=R*I^{2}$$
eller
$$P=\frac{U^{2}}{R}$$
hvis dette så indsættes ind i vores bell formel fra før får vi
$$\begin{align*}
Bell&= log_{10}\left(\frac{p_{out}}{p_{in}}\right)\\
Bell&= {log}_{10}\left(\frac{U_{out}^{2}}{U_{in}^{2}}\right)\\
Bell&= 2*{log}_{10}\left(\frac{U_{out}}{U_{in}}\right)
\end{align*}$$
hvis nu dette skal bruges i forhold til gain i en spændingsdeler kan det findes som:
$$\begin{align*}
G&= \frac{U_{out}}{U_{in}}\\
Bell&= 2 \cdot log_{10}(G)
\end{align*}$$
hvis man så vil have det som decibel skal man selvfølgelig bare gange dette med 10 eftersom at Deci betyder 1 tiende del
$$dB= 20 \cdot log_{10}(G)$$

dette kan så også bruges som en måde at skrive et tal på som fx:
$$\frac{1}{2}=20*log_{10}\left(\frac{1}{2}\right)=-6 \cdot dB$$

## Neper
en Neper er en enhed ligesom decibel og her er det defineret som:
$$N_{p}=ln(G)$$
den bliver dog aldrig brugt selvom den er smartere fordi den bruger den naturlige logaritme