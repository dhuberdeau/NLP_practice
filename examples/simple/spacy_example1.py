import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Fill a mixing glass a few inches high with ice. Add the whiskey, vermouth and bitters. Stir in a circular motion for about 30 seconds, or until the drink is very cold (if you'd like a drink with less bite, stir longer). Strain the liquid into a coupe or martini glass. Garnish with a cocktail cherry.")

for token in doc:
    print(token.text, token.lemma_)

# for token in doc:
#     print(token.lemma_)

# displacy.serve(doc, style = "dep")
