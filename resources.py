# Toy Resources
TOY_GRAMMAR = [
    ("S", ["NP", "VP"]),
    ("NP", ["Det", "N"]),
    ("VP", ["V", "NP"]),
    ("PP", ["P", "NP"]),
    ("NP", ["NP", "PP"]),
    ("Det", ["a"]),
    ("Det", ["the"]),
    ("N", ["dog"]),
    ("N", ["cat"]),
    ("N", ["rug"]),
    ("V", ["chased"]),
    ("P", ["in"]),
    ("P", ["on"]),
    ("P", ["by"])
]
TOY_PHRASES = [
    ["a", "dog", "chased", "a", "cat"],
]
# L1 Rsources
L1_GRAMMAR = [
    # Rules for S
    ("S", ["NP", "VP"]),
    ("S", ["X1", "VP"]),
    ("S", ["V", "NP"]),
    ("S", ["X2", "PP"]),
    ("S", ["V", "PP"]),
    ("S", ["VP", "PP"]),
    ("S", ["book"]),
    ("S", ["prefer"]),

    # Rules for X1
    ("X1", ["Aux", "NP"]),

    # Rules for NP
    ("NP", ["Det", "Nominal"]),
    ("NP", ["she"]),
    ("NP", ["Houston"]),

    # Rules for VP
    ("VP", ["V", "NP"]),
    ("VP", ["X2", "PP"]),
    ("VP", ["V", "PP"]),
    ("VP", ["VP", "PP"]),
    ("VP", ["book"]),
    ("VP", ["prefer"]),

    # Rules for V
    ("V", ["book"]),
    ("V", ["prefer"]),

    # Rules for PP
    ("PP", ["P", "NP"]),

    # Rules for X2
    ("X2", ["V", "NP"]),

    # Rules for Det
    ("Det", ["the"]),
    ("Det", ["a"]),

    # Rules for Nominal
    ("Nominal", ["Nominal", "Noun"]),
    ("Nominal", ["Nominal", "PP"]),
    ("Nominal", ["book"]),
    ("Nominal", ["flight"]),
    ("Nominal", ["morning"]),

    # Rules for Noun
    ("Noun", ["flight"]),
    ("Noun", ["book"]),
    ("Noun", ["morning"]),

    # Rules for P
    ("P", ["through"]),

    # Rules for PN
    ("PN", ["Houston"]),

    # Rules for Aux
    ("Aux", ["does"])
]
L1_PHRASES = [
    ["book", "the", "flight", "through", "Houston"],
    ["does", "she", "prefer", "a", "morning", "flight"]
]
# Klingon Resources
KLINGON_GRAMMAR = [
    # TERMINALS
    # Nouns
    ("Noun", ["tlhIngan Hol"]),  # Klingon Language
    ("Noun", ["puq"]),  # child
    ("Noun", ["pa'"]),  # room
    ("Noun", ["tlhIngan"]),  # Klingon
    # Noun Suffixes
    ("NounSuffix", ["Daq"]),  # In the proximity of (noun)
    # Pronouns
    ("Pronoun", ["jIH"]),  # I
    # Verbs
    ("Verb", ["jatlh"]),  # speak
    ("Verb", ["legh"]),  # see
    ("Verb", ["jIH"]),  # I (am)
    ("Verb", ["maH"]),  # we (are)
    # Verb Prefixes
    ("VerbPrefix", ["Da"]),  # 2nd person singular subject - 3rd person singular object
    ("VerbPrefix", ["vI"]),  # 1st person singular subject - 3rd person singular object
    # Verb Suffixes
    ("VerbSuffix", ["'a'"]),  # Interrogative suffix
    ("VerbSuffix", ["taH"]),  # (verb) occurs continuously E.g. I am staying

    # NON-TERMINALS
    # Verb Compounds - prefix
    ("VerbCompound", ["VerbPrefix", "Verb"]),
    ("VerbWithPrefix", ["VerbPrefix", "Verb"]),
    ("VerbCompound", ["VerbWithPrefix", "VerbSuffix"]),
    # Verb Compounds - suffix
    ("VerbCompound", ["Verb", "VerbSuffix"]),
    ("VerbWithSuffix", ["Verb", "VerbSuffix"]),
    ("VerbCompound", ["VerbPrefix", "VerbWithSuffix"]),

    # Noun Compounds
    ("NounCompound", ["Noun", "NounSuffix"]),

    # Verb Phrases
    # TODO: check if this is correct
    # ("NounVerb", ["NounCompound", "Verb"]),
    # ("NounVerb", ["NounCompound", "VerbCompound"]),
    # ("NounVerb", ["Noun", "Verb"]),
    # ("NounVerb", ["Noun", "VerbCompound"]),

    ("VerbNoun", ["VerbCompound", "Noun"]),
    ("VerbNoun", ["VerbCompound", "NounCompound"]),
    ("VerbNoun", ["Verb", "Noun"]),
    ("VerbNoun", ["Verb", "NounCompound"]),

    ("VerbNoun", ["Verb", "Pronoun"]),
    ("VerbNoun", ["VerbCompound", "Pronoun"]),

    # Sentences
    # Simple sentences (NounVerb or VerbNoun)
    ("Sentence", ["NounCompound", "Verb"]),
    ("Sentence", ["NounCompound", "VerbCompound"]),
    ("Sentence", ["Noun", "Verb"]),
    ("Sentence", ["Noun", "VerbCompound"]),

    ("Sentence", ["VerbCompound", "Noun"]),
    ("Sentence", ["VerbCompound", "NounCompound"]),
    ("Sentence", ["Verb", "Noun"]),
    ("Sentence", ["Verb", "NounCompound"]),

    ("Sentence", ["Verb", "Pronoun"]),
    ("Sentence", ["VerbCompound", "Pronoun"]),

    # Complex sentences (NounVerb + Noun or Noun + VerbNoun)
    ("Sentence", ["Noun", "VerbNoun"])
]
KLINGON_PHRASES = [
    ["tlhIngan Hol", "Da", "jatlh", "'a'"],
    ["puq", "vI", "legh", "jIH"],
    ["pa'", "Daq", "jIH", "taH"],
    ["tlhIngan", "maH"]
]
