

import numpy as np
# 1A -primitiv funktion till polynom
print(f'\nFRÅGA 1A: PRIMITIV funktion till polynom: \n')

'''
    - p_array: NumPy-array eller lista med koefficienter
    - x: ett tal eller en NumPy-array av x-värden

    Returnerar:
    - p(x), antingen som tal eller som array beroende på vad x är.
    
    exempel: p(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
     så p_array = [a0, a1, a2, ..., an]
     FÖRSTA elementet i p_array KONSTANT. 
    '''



def poly_value(p_array, x):

    value = 0.0

    # enumerate ger både index k och värdet a_k
    # k är exponenten till x
    # a_k är koefficienten framför x^k
    for k, a_k in enumerate(p_array):
        value += a_k * x**k

    return value

"""
Returnerar koefficientarrayen för en primitiv funktion P(x)
till polynomet p(x).
C = 0. 
Exempel:
p_array = [3, 2, 1] betyder:
p(x) = 3 + 2x + x^2

Då blir primitiven: 
P(x) = 0 + 3x + x^2 + (1/3)x^3

alltså returnerar vi:
[0, 3, 1, 1/3]
"""
def primitiv(p_array):

    # np.zeros skapar en array fylld med nollor
    # primitiven får en grad högre, alltså en koefficient mer och med detta antar jag att konstanten C ska vara 0,
    # C påverkar inte resultatet av integralen så kunde väljas vad som helst.
    P_array = np.zeros(len(p_array) + 1)

    # För varje term a_k * x^k blir primitiven
    # (a_k / (k+1)) * x^(k+1)
    for k, a_k in enumerate(p_array):
        P_array[k + 1] = a_k / (k + 1) # när vi tar integralen då ökas expoenenten av x med 1.
        # då vi ska lägga den nya primitiv termen i k+1:e dvs nästa platsen i arrayen

    return P_array


print(f'\n TEST AV PRIMITIV OCH INTEGRAL\n')
'''TEST primitiv + integral '''
# p(x) = x^2
# Då är koefficientarrayen:
# [0, 0, 1]
# eftersom
# p(x) = 0 + 0*x + 1*x^2
p = np.array([0.0, 0.0, 1.0])
# Primitiv ska bli P(x) = x^3/3
P = primitiv(p)

print("Polynomets koefficientarray p =", p)
print("Primitivens koefficientarray P =", P)

#1B- bestämd integral av polynom
print(f'\nFRÅGA 1B: INTEGRAL av polynom: \n')
"""
    Skapar en primitiv funktion P av p_array och räknar:  P(b) - P(a)

    Parametrar:
    - p_array: koefficientarray för polynomet
    - a, b: integrationsgränser

    Returnerar:
    - ett reellt tal
    """
def integrera(p_array, a, b):

    #tar primitiven av p_array mha funktionen "primitiv"
    P_array = primitiv(p_array)

    # Beräkna P(b) - P(a)
    return poly_value(P_array, b) - poly_value(P_array, a)


'''TEST primitiv + integral '''
# p(x) = x^2
# Då är koefficientarrayen:
# [0, 0, 1]
# eftersom
# p(x) = 0 + 0*x + 1*x^2
p = np.array([0.0, 0.0, 1.0])
# Primitiv ska bli P(x) = x^3/3
P = primitiv(p)

print(f'Polynomets koefficientarray p = {p}')
print(f'Primitivens koefficientarray P = {P} ')


# integralen från 0 till 1:
Integral_p = integrera(p, 0,1) # svaret borde bli 1/3.

print(f'Integral av x^2 från 0 till 1 = {Integral_p}')

# ============================================================# ============================================================
# ============================================================# ============================================================
# ============================================================# ============================================================
# ============================================================# ============================================================
# ============================================================# ============================================================
# ============================================================# ============================================================
# ============================================================# ============================================================
#2A: REINMANN
print(f'\n2A: REINMANN: \n')

'''
Funktionen riemann tar en funktion och gränserna [a,b] och antal delningspunkter n. 
det returnerar arean av varje rektangel som ligger under funktionen. 
a och b är intervallets gränser.
n är antalet delintervall så, antalet delningspunkter blir därför n+1.
returnerar tal. 
'''
def riemann(funktion, a, b, n):
    h = (b - a) / n # räknar ut h värdet.
    x_grid = np.linspace(a, b, n + 1)
    f_values = funktion(x_grid) # y värden av funktionen
    # höjd (h) * bredd (np.sum(f_values[:-1])
    return h * np.sum(f_values[:-1]) # här multiplicerar jag hela summan med h värdet:
                                     # istället att multiplicera alla element i en for loop.
                                     # Slutpunkten dvs, f_values[:-1] tas inte med i summan.
#2B: TRAPEZ
print(f'\n2B: TRAPEZ: \n')
'''
Funktionen trapez tar en funktion (f) och gränserna [a,b] och antal delningspunkter n. 
det returnerar arean av varje trapeziod som ligger under funktionen. 
returnerar tal. 
'''
def trapez(funktion, a, b, n):
    h = (b - a) / n
    x_grid = np.linspace(a, b, n + 1)
    f_values = funktion(x_grid) # y värden.
    return h * (0.5 * f_values[0] + np.sum(f_values[1:-1]) + 0.5 * f_values[-1])
'''
AREAN AV EN TRAPEZOID: 
1/2 * f(x0)(vänster sidan av trapezoid dvs. toppen) * f(x1) (högersidan av trapezoid dvs botten) * h(höjd)

När programmet beräknar arean med trapezregeln på intervallet [a,b] räknas den första punkten f[0] 
och den sista punkten f[-1] bara en gång, medan alla inre punkter räknas två gånger. 
Därför multipliceras f_values[0] och f_values[-1] med 0.5.
'''

# denna funktion returnerar felet i relation till exakta värdet av integralen.
def relativt_fel(approx, exact):
    return abs(exact - approx) / abs(exact)

print(f'\nTest av rienmann och trapez algoritmerna ')
''' TEST 2: testar reinmann och trapez algoritmerna för att se vilken 
av de ger bättre resultat'''
#samma funktion som jag använde i första del: x**2 då integralen mellan 0-1 = 0.33
def x_kvadrat_funktion(x):
    return x**2

for n in [10,20,40,80,10**7]:
    R = riemann(x_kvadrat_funktion, 0.0, 1.0, n)
    T = trapez(x_kvadrat_funktion, 0.0, 1.0, n)
    print(f"n = {n:2d}: Riemann = {R:.10f}, Trapez = {T:.10f}") #d står för integer f (float) 10 = 10 siffror efter ,.

print(f'ju större n är, desto mer precis svar får man\n')

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#=======================================================================================================================
#========================================================================================================================
#========================================================================================================================

#3: FELANALYS
print(f'3: Vilken är mer accurate? TRAPEZ eller RIEMANN?')
# hittar svaret för integralen mellan [0,1] för polynomet x**2.
exakt_värde_I = integrera(np.array([0.0, 0.0, 1.0]),0,1)

# olika n-värden: dessa kommer stå i x axeln
n_values = np.array([10, 20, 40, 80, 160, 320])

# tomma listor som ska hålla olika resultat från RIEMANN och TRAPEZ för olika delningspunkter.
riemann_fel = []
trapez_fel = []

def f(x):
    return x**2

for n in n_values:
    R_approx = riemann(f, 0, 1, n)
    T_approx = trapez(f, 0, 1, n)

    riemann_fel.append(relativt_fel(R_approx, exakt_värde_I))
    trapez_fel.append(relativt_fel(T_approx, exakt_värde_I))

# jag gör om till numpy-arrayer för att kunna rita graf.
riemann_fel = np.array(riemann_fel)
trapez_fel = np.array(trapez_fel)

print(f'\nTrapez är bättre, eftersom dess fel går mot 0 snabbare än Riemanns fel. Det syns tydligt i grafen.\n')
#ritning av graf för approx sin
import matplotlib.pyplot  as plt

plt.figure()
plt.plot(n_values, riemann_fel, 'o-', label = "RIEMANN")
plt.plot(n_values, trapez_fel, 'x-', label = "TRAPEZ")
plt.xlabel("n")
plt.ylabel("Relativt fel")
plt.title("Relativt fel för Riemann och trapez")
plt.grid(True)
plt.legend() # visar vilken linje står för ivlken graf
plt.show()

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#=======================================================================================================================
#========================================================================================================================
#========================================================================================================================

print(f'4: GAUSS, felet ska vara <= 10**-6')

''' 4: Hur många delningspunkter, n+1 krävs för att ha felmarginalen mindre än 10**-6'''
def f4(x):
    # Funktionen i uppgift 4 e^-x^2
    return np.exp(-x**2)



'''
 För sats 2 behövs gränser för andra derivatan. f´´(x) = (4x^2 - 2) * e^-x^2.
 För att hitta dessa gränser hittade jag extrempunkterna mellan [0,2]
 genom att kolla på f´´´(x) = 0 och hittade jag, x1 = 0 och x2= 1.5^0.5
 jag behövde även undersöka start och slutpunkterna i intervallet [0,2] dvs x1 = 0, x3= 2
 f´´(x) är kontinuerlig i intervallet [0,2] eftersom det är en produkt av 
 ett polynom (4x^2 - 2) och en exponentialfunktion (e^-x^2). 
 Polynomer exponentialfunktioner är deriverbara överallt, då produkten
 av dem bör också vara deriverbar. P.g.a det behöver jag inte undersöka fallen där
 f´´´ är odefinierade. (det finns inga skarpa punkter i intervallet[0,2] som gör att derivatan blir odefinierad. 
 
 Efter insättning av de x värden i f''(x) för att hitta M och m:
# f''(0) = -2
# f''(2) = 0,256
# f''(1.5^0.5) = 0,8925
  Då enligt formeln
 -2 <= f''(x) <= 0,8925 på intervallet [0,2]
'''
# Integrationsgränser
a = 0
b = 2

# Vi vill att absolutfelet ska vara mindre än 10^(-6)
tol = 1e-6

m = -2
M = 0.8925

# För absolutfelet bör jag använda den största absoluta gränsen
K = max(abs(m), abs(M))

# Felgränsen för trapezregeln är i boken 7.11 s.359: obs(h = (b-a)/n)
# |T_n - I| <= K * (b-a)^3 / (12*n^2)
# OBS: jag fick denna formel genom att sätta in h = (b-a)/n där vid h^2
# Vi vill ha:
# K * (b-a)^3 / (12*n^2) < tol
# Löserrut n:
# n > sqrt( K*(b-a)^3 / (12*tol) )

import math
n = math.ceil(math.sqrt(K * (b - a)**3 / (12 * tol)))

# Antalet delningspunkter är alltid n+1 eftesom 2 punkter ger 1 intervall (n)
antal_delningspunkter = n + 1

# Beräkna approximationen med trapezregeln
approx = trapez(f4, a, b, n)


print("Minsta antal delintervall n =", n)
print("Antal delningspunkter =", antal_delningspunkter)
print("Approximation av integralen =", approx)