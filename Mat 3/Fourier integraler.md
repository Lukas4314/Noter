Hvis man har en periodisk firkant puls med perioden 2L, og laver en fourier række af den hvor man lader L være en variable ender man med at a_n vil afhænge af L og vil komme til at hede:
$$a_{n}= \frac{2}{L} \cdot \frac {2 \sin( \frac {n \pi} {L})} { \frac {n \pi} {L}}$$

her bliver a_n mindre jo større L bliver. og hvis man lader L gå mod uendelig går a_n mod 0.
Hvis vi så kigger på en periodisk funktion med perioden 2L kan den skrives med fourier rækken:
$$f_{L}(x)=a_{0}+ \sum_{n=1}^{\infty}(a_{n} \cdot \cos(w_{n}x)+b_{n} \cdot \sin(w_{n}x))$$
hvor:
$$w_{n}= \frac {n \pi} {L}$$
og man lader L gå mod uendligt og regner fourer rækken finder man:
![[Pasted image 20250224123917.png]]
her er v i f(v) osv er variablen i den originale funktion af en eller anden grund, således at man ender med en funktion som er afhængig af x. altså hvis man har en periodisk funktion som er afhængig af x bytter man den ud så den er afhængig af v, således at sin fourier række kan være afhængig af x, (tjek lige op på det i bogen)


## Endeligt fourier integral:
det endelige fourier integral er egentlig bare det vi har på billedet her:
![[Pasted image 20250224123917.png]]



### Fourier transformation
hvis det her over i billedet indsættes ind i en funktion og man bruger eulers formel altså $e^{ix}=\cos(x) + i \cdot \sin(x)$
her vil man så få:
$$f(x) = \frac{1}{2\pi} \cdot \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(v) \cdot e^{iw(x-v)}dvdw$$
dette kan så bliver til:
$$f(x)= \frac {1} {\sqrt{2\pi }} \cdot \int_{-\infty}^{\infty} \frac {1} {\sqrt{2\pi } } \int_{-\infty}^{\infty} f(v) \cdot e^{-iwv} dv e^{iwx}dw$$
her kan man så kigge lidt på laplace transformation hvor vi har at:
$$\mathscr{L}=\int_{0}^{\infty}e^{-st}f(t) dt$$
her har vi så fourier transformationer hvor:
$$\mathscr{F}= \frac {1} {\sqrt{2\pi}}\int_{\infty}^{\infty}e^{-iwx}f(v) dw$$
dette kan man så slå op og indsætte ind i sit integral. En tabel kan findes på side 534-536 over forskellige fourier transformationer, som man så senere kan bruge i sit integrale for at gøre det nemmere.
Det er egentlige bare en masse integraler som er regnet på forhånd sådan man slipper for at regne hele sit dobbeltintegral



### Dirichlet’s discontinous factor
dette er:
$$\int_{0}^{\infty} \frac {\cos(\omega x) \cdot \sin(\omega)} {\omega} d \omega=\cases{\frac{\pi}{2} & if 0 <= x < 1,\\ \frac{\pi}{4} & if x=1,\\ 0 & if x>1}$$