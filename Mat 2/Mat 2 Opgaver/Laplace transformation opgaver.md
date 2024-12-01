
# 6.1
## 18

![[Pasted image 20241128104616.png]]
vi skal her finde Laplace transformationen af billedet herover
vi kan se at det er en lineær linje som har funktionsværdien k i når t er b, vi kan også se at den starter i (0,0) og kan derfor skrive funktionsværdien som:
$$f(t)=t \frac{k}{b}$$
$$\begin{align*}
L(f)=\int_{0} ^{\infty} f(t)e^{-st}dt\\
L(f)=\int_{0} ^{\infty} \frac{k}{b} te^{-st}dt
\end{align*}$$

$$\begin{align*}
L(f)&= \frac{k}{b} \left. \left [  - \frac{1}{s}e^{-st}\cdot t-\int - \frac{1}{s}e^{-st}dt   \right] \right |_{0}^{\infty}\\
L(f)&= \frac{k}{b} \left. \left [  - \frac{1}{s}e^{-st}\cdot t-\frac{1}{s^{2}}e^{-st}   \right] \right |_{0}^{\infty}\\
L(f)&= \frac{k}{b} \cdot \frac{1}{s^{2}}\\
L(f)&=  \frac{k}{bs^{2}}
\end{align*}$$
Dette er forket fordi man skulle tage den inverse laplace fra 0 til b og ikke uendelig da funktionen stopper ved b




## 32
Given F(s)=L(f) find the reverse laplace transformation
$$\begin{align*}
F(s)&= \frac {10} {2s+\sqrt{2}}\\
F(s)&= \frac{10}{2} \cdot \frac {1} {s+\sqrt{\frac{2}{4}}}
\end{align*}$$
her gør vi brug af at:
$$L(e^{at})= \frac{1}{s-a} $$
$$f(t)= \frac{10}{2} \cdot e^{-t \cdot \sqrt{0,5}}$$

## 34
find the inverse Laplace transformation:
$$ F(s)=\frac {20} {(s-1)(s+4)}$$
Vi skal her først opløse vores brøk i partial brøkker
vi har her en nævner som er af anden grad og en tæller som er af 0 grad og nævneren er kun af lineære led
$$\begin{align*}
\frac {20} {(s-1)(s+4)}&= \frac{A_{1}}{s-1}+ \frac{A_{2}}{s+4}\\
20&= A_{1}(s+4)+A_{2}(s-1)
\end{align*}$$
her sætter vi så $s=-4$ og $s=1$ 
$$\begin{align*}
20&= A_{2}(-4-1)\\
20&= A_{1}(1+4)
\end{align*}$$$$\begin{align*}
A_{2}&= -4\\
A_{1}&= 4
\end{align*}$$
dette giver os så vores partial brøkker
$$ F(s)=\frac {20} {(s-1)(s+4)}=\frac{4}{s-1} - \frac{4}{s+4}$$
nu kan vi så lave vores Laplace transformationer 
$$f(t)=4 e^{t}-4e^{-4t}$$
# 6.2

## 10
Solve the differential equation using Laplace transformation
$$\begin{align*}
y'+4y&= 0 & y(0)&= 2,8
\end{align*}$$
Vi Laplace transformerer på begge sider
$$\begin{align*}
L(y'+4y)&= L(0)\\
L(y')+4L(y)&= L(0)\\
sY(s)-y(0)+4Y(s)&= 0\\
sY(s)+4Y(s)&= y(0)\\
Y(s)(s+4)&= y(0)\\
Y(s)&= \frac {y(0)} {s+4}\\
Y(s)&= \frac {2,8} {s+4}\\
y(t)&= L^{-1}\left (\frac {2,8} {s+4} \right )\\
y(t)&= 2,8 \cdot e^{-4t}
\end{align*}$$

## 12
$$\begin{align*}
y''-y'-6y&= 0 &y(0)&= 6 &y'(0)=13
\end{align*}$$
gør her ligesom før i 10

$$\begin{align*}
L(y'')-L(y')-6L(y)&= L(0)\\
s^{2}Y(s)-sy(0)-y'(0)-(sY(s)-y(0))-6Y(s)&= 0\\
s^{2}Y(s)-6s-13-(sY(s)-6)-6Y(s)&= 0\\
s^{2}Y(s)-sY(s)-6Y(s)-6s&= 7\\
s^{2}Y(s)-sY(s)-6Y(s)&= 6s+7\\
Y(s) \cdot \left ( s^{2}-s-6 \right )&= 6s+7\\
Y(s) &= \frac {6s+7} {s^{2}-s-6}\\
Y(s) &= \frac {6s+7} {(s-3)(s+2)}\\
y(t) &= L^{-1}\left (\frac {6s+7} {(s-3)(s+2)} \right )
\end{align*}$$
vi skal her ud i at skrive det op som en partial brøk, hvilket er lige til fordi nævneren består kun af lineære led
$$\begin{align*}
\frac {6s+7} {(s-3)(s+2)}&= \frac{A_{1}}{s-3}+ \frac {A_{2}} {s+2}\\
6s+7&= A_{1}(s+2)+A_{2}(s-3)\\
6s+7&= A_{1}s+2A_{1}+A_{2}s-3A_{1}\\
6s+7 &= s(A_{1}+A_{2})+2A_{1}-3A_{1}
\end{align*}$$
her kan vi sammenligne koefficienter 
$$\begin{align*}
A_{1}+A_{2}=6\\
2A_{1}-3A_{1}=7
\end{align*}$$
vi kan her opstille en matrix
![[Laplace transformation opgaver 2024-11-28 21.04.37.excalidraw]]
ved ikke hvorfor det fucker så meget op men man skulle gerne nå frem til:
$$\begin{align*}
A_{1}&= 5\\
A_{2}&= 1
\end{align*}$$
$$\begin{align*}
\frac {6s} {(s-3)(s+2)}&= \frac{5 }{s-3}+ \frac {1} {s+2}\\
y(t) &= L^{-1}\left (\frac {6s} {(s-3)(s+2)} \right )\\
y(t) &= L^{-1}\left (  \frac{5 }{s-3}+ \frac {1} {s+2}\right )\\
y(t)&= 5 \cdot e^{3t}+e^{-2t}
\end{align*}$$




## 18

$$y''+9y=10e^{-t}$$
![[Laplace transformation opgaver 2024-11-28 21.17.04.excalidraw|5000]]
   
# 6.3

## 4

## 28

## 36


# 6.4
## 3

