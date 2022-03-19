Am facut taskul1 . In WebCacheEntry am adaugat campul accesari si in WebCache am modificat functia ca atunci cand trebuie sa eliminam un url il eliminam in functie de nr de accesari.

Un exemplu de output:


Client started with maxStorageSpace=10000 and maxTimeToKeep=10000
Am ales http://google.com cu accesari 0

am eliminat intrarea http://google.com cu accesari1

Am ales http://www.yahoo.com cu accesari 0
Am ales http://www.ms.ro/ cu accesari 0

am eliminat intrarea http://www.yahoo.com cu accesari1

Am ales http://www.yahoo.com cu accesari 0
Am ales http://httpforever.com cu accesari 0
Am ales http://www.romania-actualitati.ro/ cu accesari 0

am eliminat intrarea http://www.yahoo.com cu accesari1

Am ales http://www.yahoo.com cu accesari 0
am ales http://www.ms.ro/ cu accesari1
am ales http://httpforever.com cu accesari1