"""
Schwer

Gegeben ist eine Zahl n und ein Name.
Drucke den Namen n-mal aus wie im Beispiel gezeigt:

name = Paul
n = 4

Output:
P|a|u|l P|a|u|l P|a|u|l P|a|u|l

Hinweis: die String-Methode join kann eine ihr übergebene Sequenz
anhand eines Strings zu einem neuen String zusammenfügen

ein String ist eine Sequenz.
"""

name = "Paul"
n = 4
space = " "
divider = "|"

name1 = name + space
print(divider.join(name1) * n)
