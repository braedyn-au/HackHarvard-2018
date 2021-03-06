import sqlPython as sqlpy
coinLimit = 1000


def calcCurrCoins(carbonEmiss, milage):
	# Calculate amount of coins based from stats
	milage = max(milage, 0.0001)

	res = (10**6)/(carbonEmiss*milage)
	
	if res > coinLimit:
		return coinLimit
	return res

def totalCarbonOutput(carbonEmiss,milage):
	return carbonEmiss*milage

def calcPassiveRefCoins(carbonEmiss, milage):
	# Calculate amount of coins from person you referred to
	milage = max(milage, 0.0001)

	res = int(0.25*((10**6)/(carbonEmiss*milage)))

	if res > coinLimit:
		return coinLimit/4
	return res

def calcReferalCoins():
	# Amount of coins you would get from referring someone
	
	# Temporarily, it's an arbitrary value
	return 20.0

def getCostFromGas(stateGasCost, milesPerGallon):
	
	return stateGasCost*milesPerGallon


def getCostfromElectric(stateElecCost, milesPerBatt):

	return stateElecCost*milesPerBatt

