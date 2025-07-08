# Pour un logiciel de gestion rh d'une agence d'interim
# complétez la fonction suivante sui calcule le salaire journalier
# d'un intérimaire
# après 8 heures de travail, les heures sont majorées de 25%, après 11heures de 50%

def calcul_salaire_journalier(nb_heures, taux_horaire):
    salaire = 0.0

    if nb_heures <= 8:
        salaire = nb_heures * taux_horaire
    else:
        salaire += 8 * taux_horaire

        if nb_heures <= 11:
            heure_25_majore = nb_heures - 8
            salaire += heure_25_majore * (taux_horaire * 1.25)
        else:
            salaire += 3 * taux_horaire * 1.25
            heure_50_majore = nb_heures - 11
            salaire += heure_50_majore * (taux_horaire * 1.50)
    return salaire

print(calcul_salaire_journalier(13, 12))







