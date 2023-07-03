#-------------------------------------------------------------------
# 1.Gegeben sind zwei Strings. Verkette sie zu einem:
#-------------------------------------------------------------------

a_1 = "A"
b_1 = "C"
a_1_1 = "Banana"
b_1_1 = "rama"
 
print( a_1 + b_1 )
print( a_1_1 + b_1_1 )

#-------------------------------------------------------------------
# 2.Gegeben sind zwei Strings. Prüfe, ob b in a vorkommt
#-------------------------------------------------------------------

a_2 = "Bellavista"
b_2 = "vis"

a_2_1 = "Rom"
b_2_1 = "Rome"

if b_2 in a_2:
    print("vis kommt in Bellavista vor")

if b_2_1 in a_2_1:
    print("Rome kommt in rom vor")
else:
    print("Rome ist länger als Rom und daher nicht 'ENTHALTEN'")

#-------------------------------------------------------------------
# 3. Ersetze alle Vorkommen von b in a durch c
#-------------------------------------------------------------------

a_3 = "Bellavista"
b_3 = "Bella"
c_3 = "Buena"

a_3_1 = "Nordpol"
b_3_1 = "pol"
c_3_1 = "kap"

A31neu = a_3_1.replace(b_3_1, c_3_1)
A32neu = a_3.replace(b_3, c_3)

print(A31neu, A32neu)
