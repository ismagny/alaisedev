# créez une fonction qui prend en paramètres un **kwargs
# et qui renvoi la concaténation de toutes les clés valeur
# exemple function(je="suis", un="kwarg") doit renvoyer "jesuisunkwarg"
# exemple function(la="jolie", maison="dans", la="prairie") doit renvoyer "lajoliemaisondanslaprairie"

def cle_valeur(**param):
    result = ""

    for cle, valeur in param.items():
        result += f"{cle}{valeur}"
    return result

print(cle_valeur(je="suis", un="kwarg"))

# peut pas avoir deux arguments du même nom dans le meme appel
# print(cle_valeur(la="jolie", maison="dans", la="prairie"))

print(cle_valeur(la="jolie", maison="dans", le="prairie"))