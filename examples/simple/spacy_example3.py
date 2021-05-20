import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")
doc1 = nlp("Fill a mixing glass a few inches high with ice. Add the whiskey, vermouth and bitters. Stir in a circular motion for about 30 seconds, or until the drink is very cold (if you'd like a drink with less bite, stir longer). Strain the liquid into a coupe or martini glass. Garnish with a cocktail cherry.")
doc2 = nlp("Muddle the sugar cube and bitters with one bar spoon of water at the bottom of a chilled rocks glass. (If using simple syrup, combine bitters and one bar spoon of syrup.) Add rye or bourbon. Add one large ice cube, or three or four smaller cubes. Stir until chilled and properly diluted, about 30 seconds.")
doc3 = nlp("William Shakespeare was an English playwright, poet, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist. He is often called England's national poet and the Bard of Avon.")
print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
print(doc2.similarity(doc3))
