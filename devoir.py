# Importation des bibliothèques nécessaires
import numpy as np  # Importation de la bibliothèque pour les opérations numériques
import skfuzzy as fuzz  # Importation de la bibliothèque pour la logique floue
import matplotlib.pyplot as plt  # Importation de la bibliothèque pour créer des graphiques
from skfuzzy import control as ctrl  # Importation d'un module spécifique de skfuzzy

# Définition des antécédents et des conséquents
grippe = ctrl.Antecedent(np.arange(1, 100, 2), 'grippe')  # Variable antécédente "grippe" avec des valeurs de 1 à 100 (pas de 2)
palu = ctrl.Antecedent(np.arange(1, 30, 1), 'palu')  # Variable antécédente "palu" avec des valeurs de 1 à 30 (pas de 1)
omicron = ctrl.Antecedent(np.arange(0, 6, 0.1), 'omicron')  # Variable antécédente "omicron" avec des valeurs de 0 à 6 (pas de 0.1)

# Définition des conséquences
prescription = ctrl.Consequent(np.arange(1, 100, 1), 'prescription')  # Variable conséquente "prescription" avec des valeurs de 1 à 100 (pas de 1)
laborantin = ctrl.Consequent(np.arange(1, 100, 1), 'laborantin')  # Variable conséquente "laborantin" avec des valeurs de 1 à 100 (pas de 1)

# Configuration des graphiques
fig = plt.figure(figsize=(12, 8))  # Création d'une figure avec une taille spécifiée
subfigs = fig.subfigures(1, 2, wspace=0.07, width_ratios=[1.5, 1.])  # Création de sous-figures avec espacement et proportions spécifiés
axes_a = subfigs[0].subplots(2, 2)  # Création de sous-graphiques pour les antécédents
subfigs[0].set_facecolor('lightblue')  # Définition de la couleur de fond
subfigs[0].suptitle('Antécédents')  # Ajout d'un titre aux antécédents

axes_c = subfigs[1].subplots(2, 1)  # Création de sous-graphiques pour les conséquences
subfigs[1].suptitle('Conséquences')  # Ajout d'un titre aux conséquences

# Définition des ensembles flous avec trapmf pour "grippe"
toux_faible = fuzz.trapmf(grippe.universe, [1, 1, 30, 45])  # Définition de l'ensemble "toux_faible" avec trapmf
grippe['toux_faible'] = toux_faible  # Attribution de l'ensemble défini à la variable "grippe"
rhume = fuzz.trapmf(grippe.universe, [20, 20, 70, 70])  # Définition de l'ensemble "rhume" avec trapmf
grippe['rhume'] = rhume  # Attribution de l'ensemble défini à la variable "grippe"
toux_fort = fuzz.trapmf(grippe.universe, [45, 45, 100, 100])  # Définition de l'ensemble "toux_fort" avec trapmf
grippe['toux_fort'] = toux_fort  # Attribution de l'ensemble défini à la variable "grippe"

# Définition des ensembles flous avec trapmf pour "palu"
dm_fort = fuzz.trapmf(palu.universe, [12, 12, 30, 30])  # Définition de l'ensemble "dm_fort" avec trapmf
palu['dm_fort'] = dm_fort  # Attribution de l'ensemble défini à la variable "palu"
dm_moyenne = fuzz.trapmf(palu.universe, [8, 8, 15, 15])  # Définition de l'ensemble "dm_moyenne" avec trapmf
palu['dm_moyenne'] = dm_moyenne  # Attribution de l'ensemble défini à la variable "palu"
dm_leger = fuzz.trapmf(palu.universe, [1, 1, 10, 10])  # Définition de l'ensemble "dm_leger" avec trapmf
palu['dm_leger'] = dm_leger  # Attribution de l'ensemble défini à la variable "palu"

# Définition des ensembles flous avec trapmf pour "omicron"
pt_appetit = fuzz.trapmf(omicron.universe, [0, 0, 2, 2])  # Définition de l'ensemble "pt_appetit" avec trapmf
omicron['pt_appetit'] = pt_appetit  # Attribution de l'ensemble défini à la variable "omicron"
pm_appetit = fuzz.trapmf(omicron.universe, [1, 1, 4, 4])  # Définition de l'ensemble "pm_appetit" avec trapmf
omicron['pm_appetit'] = pm_appetit  # Attribution de l'ensemble défini à la variable "omicron"
sp_appetit = fuzz.trapmf(omicron.universe, [2, 2, 6, 6])  # Définition de l'ensemble "sp_appetit" avec trapmf
omicron['sp_appetit'] = sp_appetit  # Attribution de l'ensemble défini à la variable "omicron"

# Définition des ensembles flous avec trapmf pour "prescription"
sur_rv = fuzz.trapmf(prescription.universe, [1, 1, 50, 50])  # Définition de l'ensemble "sur_rv" avec trapmf
prescription['sur_rv'] = sur_rv  # Attribution de l'ensemble défini à la variable "prescription"
via_l_appli = fuzz.trapmf(prescription.universe, [40, 40, 100, 100])  # Définition de l'ensemble "via_l_appli" avec trapmf
prescription['via_l_appli'] = via_l_appli  # Attribution de l'ensemble défini à la variable "prescription"

# Définition des ensembles flous avec trapmf pour "laborantin"
bilan = fuzz.trapmf(laborantin.universe, [1, 1, 30, 30])  # Définition de l'ensemble "bilan" avec trapmf
laborantin['bilan'] = bilan  # Attribution de l'ensemble défini à la variable "laborantin"
test = fuzz.trapmf(laborantin.universe, [30, 30, 70, 70])  # Définition de l'ensemble "test" avec trapmf
laborantin['test'] = test  # Attribution de l'ensemble défini à la variable "laborantin"
scan = fuzz.trapmf(laborantin.universe, [80, 80, 100, 100])  # Définition de l'ensemble "scan" avec trapmf
laborantin['scan'] = scan  # Attribution de l'ensemble défini à la variable "laborantin"

# Affichage des ensembles flous pour "grippe"
axes_a[0, 0].plot(grippe.universe, toux_faible, 'b', linewidth=1.5, label='Toux faible')  # Affichage de l'ensemble "toux_faible"
axes_a[0, 0].plot(grippe.universe, rhume, 'g', linewidth=1.5, label='Rhume')  # Affichage de l'ensemble "rhume"
axes_a[0, 0].plot(grippe.universe, toux_fort, 'r', linewidth=1.5, label='Toux fort')  # Affichage de l'ensemble "toux_fort"
axes_a[0, 0].set_title('Grippe saisonnière')  # Définition du titre du sous-graphique
axes_a[0, 0].legend()  # Affichage de la légende

# Affichage des ensembles flous pour "palu"
axes_a[0, 1].plot(palu.universe, dm_fort, 'b', linewidth=1.5, label='DM Fort')  # Affichage de l'ensemble "dm_fort"
axes_a[0, 1].plot(palu.universe, dm_moyenne, 'g', linewidth=1.5, label='DM Moyenne')  # Affichage de l'ensemble "dm_moyenne"
axes_a[0, 1].plot(palu.universe, dm_leger, 'r', linewidth=1.5, label='DM Leger')  # Affichage de l'ensemble "dm_leger"
axes_a[0, 1].set_title('Douleur Musculaire')  # Définition du titre du sous-graphique
axes_a[0, 1].legend()  # Affichage de la légende

# Affichage des ensembles flous pour "omicron"
axes_a[1, 1].plot(omicron.universe, pt_appetit, 'b', linewidth=1.5, label='PT Appetit')  # Affichage de l'ensemble "pt_appetit"
axes_a[1, 1].plot(omicron.universe, pm_appetit, 'g', linewidth=1.5, label='PM Appetit')  # Affichage de l'ensemble "pm_appetit"
axes_a[1, 1].plot(omicron.universe, sp_appetit, 'r', linewidth=1.5, label='SP Appetit')  # Affichage de l'ensemble "sp_appetit"
axes_a[1, 1].set_title('Appetit (Degust)')  # Définition du titre du sous-graphique
axes_a[1, 1].legend()  # Affichage de la légende

# Affichage des ensembles flous pour "prescription"
axes_c[0].plot(prescription.universe, sur_rv, 'b', linewidth=1.5, label='Sur RV')  # Affichage de l'ensemble "sur_rv"
axes_c[0].plot(prescription.universe, via_l_appli, 'g', linewidth=1.5, label='Via l\'Appli')  # Affichage de l'ensemble "via_l_appli"
axes_c[0].set_title('Prescription Ordonnance')  # Définition du titre du sous-graphique
axes_c[0].legend()  # Affichage de la légende

# Affichage des ensembles flous pour "laborantin"
axes_c[1].plot(laborantin.universe, bilan, 'b', linewidth=1.5, label='Faire un bilan')  # Affichage de l'ensemble "bilan"
axes_c[1].plot(laborantin.universe, test, 'g', linewidth=1.5, label='Faire un test')  # Affichage de l'ensemble "test"
axes_c[1].plot(laborantin.universe, scan, 'r', linewidth=1.5, label='Faire un scan')  # Affichage de l'ensemble "scan"
axes_c[1].set_title('Voir un laborantin')  # Définition du titre du sous-graphique
axes_c[1].legend()  # Affichage de la légende

# Boucle pour obtenir les degrés d'appartenance interactivement
while True:
    plt.show(block=False)  # Affichage interactif
    x_clic = input("Entrez une valeur x spécifique (ou 'q' pour quitter) : ")  # Demande à l'utilisateur d'entrer une valeur
    if x_clic.lower() == 'q':  # Vérification si l'utilisateur souhaite quitter
        break
    x_clic = float(x_clic)  # Conversion de l'entrée en flottant

    # Calcul des degrés d'appartenance pour les coordonnées spécifiées
    y_clic_grippe_faible = fuzz.interp_membership(grippe.universe, toux_faible, x_clic)  # Degré d'appartenance à "toux_faible"
    y_clic_grippe_rhume = fuzz.interp_membership(grippe.universe, rhume, x_clic)  # Degré d'appartenance à "rhume"
    y_clic_grippe_fort = fuzz.interp_membership(grippe.universe, toux_fort, x_clic)  # Degré d'appartenance à "toux_fort"

    y_clic_palu_fort = fuzz.interp_membership(palu.universe, dm_fort, x_clic)  # Degré d'appartenance à "dm_fort"
    y_clic_palu_moyenne = fuzz.interp_membership(palu.universe, dm_moyenne, x_clic)  # Degré d'appartenance à "dm_moyenne"
    y_clic_palu_leger = fuzz.interp_membership(palu.universe, dm_leger, x_clic)  # Degré d'appartenance à "dm_leger"

    y_clic_omicron_pt = fuzz.interp_membership(omicron.universe, pt_appetit, x_clic)  # Degré d'appartenance à "pt_appetit"
    y_clic_omicron_pm = fuzz.interp_membership(omicron.universe, pm_appetit, x_clic)  # Degré d'appartenance à "pm_appetit"
    y_clic_omicron_sp = fuzz.interp_membership(omicron.universe, sp_appetit, x_clic)  # Degré d'appartenance à "sp_appetit"

    y_clic_prescription_sur_rv = fuzz.interp_membership(prescription.universe, sur_rv, x_clic)  # Degré d'appartenance à "sur_rv"
    y_clic_prescription_via_app = fuzz.interp_membership(prescription.universe, via_l_appli, x_clic)  # Degré d'appartenance à "via_l_appli"

    y_clic_laborantin_bilan = fuzz.interp_membership(laborantin.universe, bilan, x_clic)  # Degré d'appartenance à "bilan"
    y_clic_laborantin_test = fuzz.interp_membership(laborantin.universe, test, x_clic)  # Degré d'appartenance à "test"
    y_clic_laborantin_scan = fuzz.interp_membership(laborantin.universe, scan, x_clic)  # Degré d'appartenance à "scan"
    
    # Affichage des degrés d'appartenance
    print("Degré d'appartenance à la Toux faible :", y_clic_grippe_faible)
    print("Degré d'appartenance au rhume :", y_clic_grippe_rhume)
    print("Degré d'appartenance à la toux forte :", y_clic_grippe_fort)
    print("")
    print("Degré d'appartenance à la DM Fort :", y_clic_palu_fort)
    print("Degré d'appartenance à la DM Moyenne :", y_clic_palu_moyenne)
    print("Degré d'appartenance à la DM Leger :", y_clic_palu_leger)
    print("")
    print("Degré d'appartenance au PT Appetit :", y_clic_omicron_pt)
    print("Degré d'appartenance au PM Appetit :", y_clic_omicron_pm)
    print("Degré d'appartenance au SP Appetit :", y_clic_omicron_sp)
    print("")
    print("Degré d'appartenance au prescription sur RV :", y_clic_prescription_sur_rv)
    print("Degré d'appartenance au prescription via l'app :", y_clic_prescription_via_app)
    print("")
    print("Degré d'appartenance à faire un bilan:", y_clic_laborantin_bilan)
    print("Degré d'appartenance à faire un test :", y_clic_laborantin_test)
    print("Degré d'appartenance à faire un scan :", y_clic_laborantin_scan)

plt.tight_layout()  # Ajustement automatique de la disposition des graphiques
plt.show()  # Affichage final
