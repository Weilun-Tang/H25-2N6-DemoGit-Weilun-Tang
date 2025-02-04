# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os
os.chdir("C:\\Users\\6235451\\OneDrive - Cégep Édouard-Montpetit\\A2025\Programmation 2\\R03 Exercices Depart\\Ex3 Videos")
os.getcwd()
Videos = os.listdir()
for Video in Videos :
    nom_est = os.path.splitext(Video)
    list_split = nom_est.split("_")
    list_split.strip(" ")
    x = list_split[2].zfill() 