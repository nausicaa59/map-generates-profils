import datetime


def rangeYears(start, end, default=0):
	plage = {}
	for x in range(end, start, -1):
		plage[str(x)] = 0

	return plage



def rangeLastMonth(year, month, max=12, default=0):
	plage = {}
	compteur = 0

	for a in range(year, 0, -1):
		for m in range(month, 0, -1):
			plage[str(a) + "-" + monthIntToString(m)] = 0
			compteur += 1
			if compteur == max:
				return plage
		month = 12

	return plage



def monthFrench():
	return ["Jan","Fev","Mar","Avr","Mai","Juin","Jui","Aou","Sep","Oct","Nov","Dec"]



def monthIntToString(m):
	mois = monthFrench()
	return mois[m-1]



def byYear(sujets):
	now = datetime.datetime.now()
	statsAnnees = rangeYears(2003, now.year)
	
	for sujet in sujets:
		date = datetime.datetime.strptime(sujet["initialised_at"], '%Y-%m-%d %H:%M:%S')
		statsAnnees[str(date.year)] += 1

	return statsAnnees



def byLastMouth(sujets):
	now = datetime.datetime.now()
	year = now.year
	month = now.month
	statsMonth = rangeLastMonth(year, month)
	
	for sujet in sujets:
		date = datetime.datetime.strptime(sujet["initialised_at"], '%Y-%m-%d %H:%M:%S')
		sujetYear = str(date.year)
		sujetMonth = monthIntToString(date.month)
		sujetKey = sujetYear + "-" + sujetMonth

		if sujetKey in statsMonth:
			statsMonth[sujetKey] += 1

	return statsMonth


