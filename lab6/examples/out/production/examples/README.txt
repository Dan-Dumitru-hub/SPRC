Am facut taskul1 . In WebCacheEntry am adaugat campul accesari si in WebCache am modificat functia ca atunci cand trebuie sa eliminam un url il eliminam in functie de nr de accesari.

Un exemplu de output:

am ales http://www.yahoo.com cu accesari1
am ales http://www.ms.ro/ cu accesari1
am ales http://httpforever.com cu accesari1
am ales http://www.yahoo.com cu accesari2
am ales http://www.ms.ro/ cu accesari2
am ales http://www.ms.ro/ cu accesari3
Am ales http://google.com cu accesari 0

am eliminat intrarea http://www.ms.ro/ cu accesari4