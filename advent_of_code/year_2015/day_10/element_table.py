from dataclasses import dataclass

"""
This represents the elements in Conway's autoactive series for the Look-and-say game
"""


@dataclass
class Element:
    sequence: str
    decay: list[str]


"""
This was taken from Wikipedia:
    https://en.wikipedia.org/wiki/Look-and-say_sequence
"""
element_table: dict[str, Element] = {
    "Be": Element(
        sequence="111312211312113221133211322112211213322112", decay=["Ge", "Ca", "Li"]
    ),
    "Re": Element(
        sequence="111312211312113221133211322112211213322113", decay=["Ge", "Ca", "W"]
    ),
    "B": Element(sequence="1321132122211322212221121123222112", decay=["Be"]),
    "Os": Element(sequence="1321132122211322212221121123222113", decay=["Re"]),
    "He": Element(
        sequence="13112221133211322112211213322112", decay=["Hf", "Pa", "H", "Ca", "Li"]
    ),
    "Ta": Element(
        sequence="13112221133211322112211213322113", decay=["Hf", "Pa", "H", "Ca", "W"]
    ),
    "C": Element(sequence="3113112211322112211213322112", decay=["B"]),
    "Nb": Element(sequence="1113122113322113111221131221", decay=["Er", "Zr"]),
    "Ir": Element(sequence="3113112211322112211213322113", decay=["Os"]),
    "Li": Element(sequence="312211322212221121123222112", decay=["He"]),
    "W": Element(sequence="312211322212221121123222113", decay=["Ta"]),
    "As": Element(sequence="11131221131211322113322112", decay=["Ge", "Na"]),
    "N": Element(sequence="111312212221121123222112", decay=["C"]),
    "Rh": Element(sequence="311311222113111221131221", decay=["Ho", "Ru"]),
    "Pt": Element(sequence="111312212221121123222113", decay=["Ir"]),
    "Ge": Element(sequence="31131122211311122113222", decay=["Ho", "Ga"]),
    "Zr": Element(sequence="12322211331222113112211", decay=["Y", "H", "Ca", "Tc"]),
    "Ru": Element(sequence="132211331222113112211", decay=["Eu", "Ca", "Tc"]),
    "Se": Element(sequence="13211321222113222112", decay=["As"]),
    "Mo": Element(sequence="13211322211312113211", decay=["Nb"]),
    "O": Element(sequence="132112211213322112", decay=["N"]),
    "Pd": Element(sequence="111312211312113211", decay=["Rh"]),
    "I": Element(sequence="311311222113111221", decay=["Ho", "Te"]),
    "Au": Element(sequence="132112211213322113", decay=["Pt"]),
    "Ga": Element(
        sequence="13221133122211332", decay=["Eu", "Ca", "Ac", "H", "Ca", "Zn"]
    ),
    "Sc": Element(sequence="3113112221133112", decay=["Ho", "Pa", "H", "Ca", "Co"]),
    "Br": Element(sequence="3113112211322112", decay=["Se"]),
    "Tb": Element(sequence="3113112221131112", decay=["Ho", "Gd"]),
    "Tc": Element(sequence="311322113212221", decay=["Mo"]),
    "F": Element(sequence="31121123222112", decay=["O"]),
    "Ti": Element(sequence="11131221131112", decay=["Sc"]),
    "Kr": Element(sequence="11131221222112", decay=["Br"]),
    "Xe": Element(sequence="11131221131211", decay=["I"]),
    "Tm": Element(sequence="11131221133112", decay=["Er", "Ca", "Co"]),
    "Hg": Element(sequence="31121123222113", decay=["Au"]),
    "Te": Element(sequence="1322113312211", decay=["Eu", "Ca", "Sb"]),
    "Ne": Element(sequence="111213322112", decay=["F"]),
    "P": Element(sequence="311311222112", decay=["Ho", "Si"]),
    "Mn": Element(sequence="111311222112", decay=["Cr", "Si"]),
    "Ag": Element(sequence="132113212221", decay=["Pd"]),
    "Dy": Element(sequence="111312211312", decay=["Tb"]),
    "Tl": Element(sequence="111213322113", decay=["Hg"]),
    "Rn": Element(sequence="311311222113", decay=["Ho", "At"]),
    "Gd": Element(sequence="13221133112", decay=["Eu", "Ca", "Co"]),
    "Mg": Element(sequence="3113322112", decay=["Pm", "Na"]),
    "Al": Element(sequence="1113222112", decay=["Mg"]),
    "S": Element(sequence="1113122112", decay=["P"]),
    "Rb": Element(sequence="1321122112", decay=["Kr"]),
    "Cd": Element(sequence="3113112211", decay=["Ag"]),
    "Ce": Element(sequence="1321133112", decay=["La", "H", "Ca", "Co"]),
    "Yb": Element(sequence="1321131112", decay=["Tm"]),
    "Bi": Element(sequence="3113322113", decay=["Pm", "Pb"]),
    "Po": Element(sequence="1113222113", decay=["Bi"]),
    "Fr": Element(sequence="1113122113", decay=["Rn"]),
    "Na": Element(sequence="123222112", decay=["Ne"]),
    "Er": Element(sequence="311311222", decay=["Ho", "Pm"]),
    "Pb": Element(sequence="123222113", decay=["Tl"]),
    "V": Element(sequence="13211312", decay=["Ti"]),
    "Fe": Element(sequence="13122112", decay=["Mn"]),
    "Ni": Element(sequence="11133112", decay=["Zn", "Co"]),
    "In": Element(sequence="11131221", decay=["Cd"]),
    "Cs": Element(sequence="13211321", decay=["Xe"]),
    "Pr": Element(sequence="31131112", decay=["Ce"]),
    "Si": Element(sequence="1322112", decay=["Al"]),
    "Sr": Element(sequence="3112112", decay=["Rb"]),
    "Y": Element(sequence="1112133", decay=["Sr", "U"]),
    "Sb": Element(sequence="3112221", decay=["Pm", "Sn"]),
    "Eu": Element(sequence="1113222", decay=["Sm"]),
    "Ho": Element(sequence="1321132", decay=["Dy"]),
    "At": Element(sequence="1322113", decay=["Po"]),
    "Cl": Element(sequence="132112", decay=["S"]),
    "Cu": Element(sequence="131112", decay=["Ni"]),
    "Ba": Element(sequence="311311", decay=["Cs"]),
    "Nd": Element(sequence="111312", decay=["Pr"]),
    "Sm": Element(sequence="311332", decay=["Pm", "Ca", "Zn"]),
    "Lu": Element(sequence="311312", decay=["Yb"]),
    "Ra": Element(sequence="132113", decay=["Fr"]),
    "Cr": Element(sequence="31132", decay=["V"]),
    "Co": Element(sequence="32112", decay=["Fe"]),
    "Sn": Element(sequence="13211", decay=["In"]),
    "La": Element(sequence="11131", decay=["Ba"]),
    "Hf": Element(sequence="11132", decay=["Lu"]),
    "Ar": Element(sequence="3112", decay=["Cl"]),
    "K": Element(sequence="1112", decay=["Ar"]),
    "Ac": Element(sequence="3113", decay=["Ra"]),
    "Th": Element(sequence="1113", decay=["Ac"]),
    "Zn": Element(sequence="312", decay=["Cu"]),
    "Pm": Element(sequence="132", decay=["Nd"]),
    "H": Element(sequence="22", decay=["H"]),
    "Ca": Element(sequence="12", decay=["K"]),
    "Pa": Element(sequence="13", decay=["Th"]),
    "U": Element(sequence="3", decay=["Pa"]),
}
