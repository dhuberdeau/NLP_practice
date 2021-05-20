import spacy

texts = ["Net income was $9.4 million compared to the prior year.",
"Revenue exceeded our expectations."]

nlp = spacy.load("en_core_web_sm")

for doc in nlp.pipe(texts, disable = ["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    print([(ent.text, ent.label_) for ent in doc.ents])
