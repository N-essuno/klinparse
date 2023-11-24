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

]
KLINGON_PHRASES = [
    ["tlhIngan", "Hol", "Dajatlh", "'a’"],
    ["puq", "vIlegh", "jIH"],
    ["pa'Daq", "jIHtaH"],
    ["tlhIngan", "maH"]
]
