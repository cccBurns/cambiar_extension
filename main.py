from pathlib import Path
carpeta = Path('Cambiar Extension')

# Pasar archivos .txt a .csv

for c in list(carpeta.iterdir()):
    #print(c)
    if c.suffix == ".txt":
        nueva_extension = c.with_suffix(".csv")
        c.rename(nueva_extension)
        
# Operacion inversa

for c in carpeta.glob("**/*.csv"):
    print(c)
    nueva_extension = c.with_suffix(".csv")
    c.rename(nueva_extension)
