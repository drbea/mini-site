age = 15

# si age > 10 affiche "acces autorise" 
# sinon affiche vous etes recale

if age > 18:
    print("acces autorise vous pouvez avoir un permis")
    age = 11
    print("la valeur de age a changé: age vaut", age)
else:
    print("acces non autorise vous ne pouvez pas avoir un permis")
    