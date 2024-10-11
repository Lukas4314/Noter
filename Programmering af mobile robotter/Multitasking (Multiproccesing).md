multitasking eller multiprocessing er at gøre flere forskellige ting på en gange

#### Forskellige termer
Tasks: de opgaver som skal gøres, og er egentlig bare et generelt term for processorer og threads

Processer: de linjer koder som skal køres på proceseneren. flere kerner vil kunne køre flere 
processor og det smarte er at de ikke har samme hukommelse hvilket betyder at de kan køre uafhængigt af hinanden

threads: disse kører parallelt i en proces hvor de så deler hukommelse, man har ofte også en main tråd som er sin main kode, threads deler hukommelse og kan derfor godt han en indvirkning på hinanden
dette kan også medfører problemer hvis de forskellige threads bruger det samme hukommelse, dette er betegnet som en race condition fordi at de forsøger begge to at rbuge det samme hukommelse og derfor handler om at være der først
en løsning på dette kan være Synchronisering


#### Parallelism vs Concurrency
parallelism er når det kører parallelt på flere kerne og kører derfor på samme tid

Concurrency er når koden kører 1 task af gangen men med et tidspunkt imellem og der derved bliver lavet forskellige tasks næsten ligesom parallelt men der kører egentlig kun 1 kode af gangen


#### Synchronization
en ting man kan bruge til at synkronisere er Mutex som er hvis forskellige threads bruger samme hukommelse så kan man låse en variable og frigive den når ens thread er færdig med at bruge den og andre threads som vil tilgå denne variable først kan gøre det når den er blevet frigivet igen.
denne måde at synkronisere kan støde på et problem hvis man har flere låse, man kan nemlig komme ud efter det man kalder deadlock hvor 2 tråde venter på hinanden frigiver deres variable før de selv frigiver deres egen variable og programmet er derfor låst. en løsning er timeouts hvor efter noget tid så frigiver den bare sin egen variable fordi den godt ved at den nok venter på at man selv har frigivet


### Async
async er en måde at bruge concurrency.
for at bruge async skal man før man definere en function skrive async som fx "async def somethin()" man skal så inde i sine funktioner blandt andet kalde await asyncio.sleep() som er der for den giver plads til andet kode bliver kørt.