Scripts ATC OPS - CO Division

Archivo FIX_ALL.fix
- Para obtener este archivo, extraerlo de IAB usando los siguentes límites: 
	Arriba: N016
	Abajo: S006
	Izquierda: W83
	Derecha: W66

Filtrar Fixes.py
- El script se usa para filtrar fixes, incluyendo una lista de estos ["FIX01", "FIX02", "FIX03",...]
- Se debe incluir en la misma carpeta un archivo (Con el AIRAC Actual) llamado FIX_ALL.fix
- Como resultado, va a quedar en la misma carpeta un archivo llamado "filtered_fixes.txt"

Update AIRAC.py
- Este script se usa para actualizar el AIRAC de únicamente las distintas áreas terminales de los FIR de SKED y SKEC.
- Se debe incluir en la misma carpeta un archivo (Con el AIRAC actual) llamado FIX_ALL.fix
- Este archivo FIX_ALL.fix no tiene que tener ningún comentario, tras extraer la información de IAB, hay que eliminar el primer comentario y dejar únicamente la información de los fixes.
- Como salida, el script va a crear un archivo [TMA]_TERM.fix para cada TMA del sector. Los cuales, luego se tendrán que reemplazar en las subcarpetas correspondientes.