formato = """
FORMATO: AAA-BB-CC-DD-EEEE-FF-GGGG

- El primer bloque AAA corresponde al código de la empresa:
APSA --------------------------------------> APSA
BLC ---------------------------------------> BLC
Boortmalt ---------------------------------> BLMT
BASF Gral Lagos ---------------------------> BSFGL
BASF Santo Tomé ---------------------------> BSFSTO
Basf Tortuguitas --------------------------> BSFTOR
Bunge Ramallo -----------------------------> BURA
Bunge San Jeronimo ------------------------> BUSJ
Bunge Puerto General San Martín -----------> BUSM 
CENTRAL SORRENTO --------------------------> CSO
Cerro Vanguardia --------------------------> CVSA
LC Tech -----------------------------------> LCT
Louis Dreyfous Company --------------------> LDC 
Promaiz -----------------------------------> PRM
Renova ------------------------------------> RNV
Styropek ----------------------------------> STY

- El segundo bloque BB corresponde a el tipo de trabajo:
Proyecto ----------------------------------> PR
Relevamiento ------------------------------> RE
Mantenimiento -----------------------------> MAN

- El tercer bloque CC corresponde al año del proyecto/relevamiento/mantenimiento;

- El cuarto bloque DD corresponde al número de la carpeta del proyecto/relevamiento/mantenimiento(*VER NOTA);

- El quinto bloque EEEE corresponde al número de la última anidación de subcarpeta en el que se encuentra este archivo (EN CASO DE NO HABER SUBCARPETA COMPLETAR CON 00)

- El sexto bloque FF corresponde al código del tipo de archivo. Este código por ahora sólo depende
del acrónimo del nombre del documento. Por ejemplo si es "Esquema Topográfico", el código será "ET";
Partes diarios ----------------------------> PD
Pruebas	-----------------------------------> PRB
Esquemas topograficos ---------------------> ET
Esquemas unifilar -------------------------> EU
Esquemas de red ---------------------------> ER
Funcionales -------------------------------> FUN
Manuales ----------------------------------> MAN
Logica ------------------------------------> LOG
Layout ------------------------------------> LAY
P&ID --------------------------------------> PID
Puesta en marcha --------------------------> PEM
Informes ----------------------------------> INF
Listado de documentos ---------------------> LD
Listado de materiales ---------------------> LM
Pliego de especificaciones técnicas -------> PET
"""