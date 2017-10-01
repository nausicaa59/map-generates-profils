import config
import model
import auteur
import sujet
import json
import stats.sujets as statsSujet
import lexique.sujets as lexiqueSujet
import tools.tools as tools

db = model.prepareDb()
nbOperation = 1000
compteur = 0;

for i in range(1, nbOperation):
	if i == 8:
		continue

	compteur += 1
	a = auteur.getFull(db,i)
	a["nb_sujet"] = len(a["sujets"])
	a["analyseTextuel"] = lexiqueSujet.occurenres(a["sujets"])
	a["sujetByYear"] = statsSujet.byYear(a["sujets"])
	a["sujetByLastMouth"] = statsSujet.byLastMouth(a["sujets"])
	a["similaires"] = []
	tools.saveProfil(a)
	print("traité :", compteur, "/", nbOperation)




