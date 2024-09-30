Tanken: vi kan ikke dividere med en matrix A
men vi kan finde den inverse matris dvs.
$$A^{-1}*A=I$$
eks:
$$A*\vec{x}=\vec{b}$$
$$A^{-1}*A*\vec{x}=A^{-1}*\vec{b}$$
$$I*\vec{x}=A^{-1}*\vec{b}
$$
$$\vec{x}=A^{-1}*\vec{b}$$

A^-1 findes kun hvis [[Determinant af Matrix]] ikke er lig med 0 hvilket betyder at A har fuld rang

med denne ligning kan vi finde den inverse matrix
$$A*A^{-1}=I$$
vi kan nemlig bare bruge gauss elimination på dette hvor vi har A som er vores matrix og når man tilføjer den udvidet del af matrixen så er det identitetsmatrixen

hvis man har flere matrixer ganget sammen som så til sidst ganget nogle ubekendte som skal løses som fx:
$$A*B*C*D*\vec{x}=\vec{b}$$
så skal man først gange med A^-1 og så efter B^-1 osv. hvor man til sidst får
$$\vec{x}=D^{-1}*C^{-1}*B^{-1}*A^{-1}*\vec{b}$$
hvis nu bare har
$$E*\vec{x}=\vec{b}$$
hvor 
$$E=A*B*C*D$$
så er svaret
$$\vec{x}=E^{-1}*\vec{b}$$
og hermed er
$$E^{-1}=D^{-1}*C^{-1}*B^{-1}*A^{-1}$$
