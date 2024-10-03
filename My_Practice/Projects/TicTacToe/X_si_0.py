"""
Implementati jocul X si 0.

Avem doi jucatori (X si 0) care isi vor scrie numele pe rand pe tabla de joc.

Tabla are de 3 X 3 casute, si este initial goala.

Jocul se incheie in momentul in care:

 - pe o linie avem doar X sau doar 0

 - pe o coloana avem doar X sau doar 0

 - pe o diagoanala avem doar X sau doar 0

- tabla s-a umplut si nu este indeplinita niciuna din conditiile de mai sus -> remiza


"""

import random
print("\nWelcome to X & 0!\n")
casute = "123456789"
casute_cu_spatii = " ".join(casute)  # 1 2 3 4 5 6 7 8 9
tabla_joc = casute_cu_spatii[0:5] + "\n" + casute_cu_spatii[6:11] + "\n" + casute_cu_spatii[12:]
print(tabla_joc)
# 1 2 3
# 4 5 6
# 7 8 9
# odata ce avem tabla de joc, putem incepe


for casuta in tabla_joc:
    casuta_user = input("- Este randul tau sa alegi o casuta: ")
    casute = casute.replace(casuta_user, "")  # limitam optiunile user ului
    # print(casute)
    if casuta_user in tabla_joc:
        tabla_joc = tabla_joc.replace(casuta_user, "X")  # inlocuim casuta aleasa cu "X"
        print(tabla_joc)
        # toate pozitiile castigatoare in functie de randuri pentru X
        if tabla_joc[0] == "X" and tabla_joc[2] == "X" and tabla_joc[4] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[6] == "X" and tabla_joc[8] == "X" and tabla_joc[10] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[12] == "X" and tabla_joc[14] == "X" and tabla_joc[16] == "X":
            print("HUMAN WINNNNS")
            break
        # toate pozitiile castigatoare in functie de coloane pentru X
        elif tabla_joc[0] == "X" and tabla_joc[6] == "X" and tabla_joc[12] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[2] == "X" and tabla_joc[8] == "X" and tabla_joc[14] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[4] == "X" and tabla_joc[10] == "X" and tabla_joc[16] == "X":
            print("HUMAN WINNNNS")
            break
        # diagonalele pentru X
        elif tabla_joc[0] == "X" and tabla_joc[8] == "X" and tabla_joc[16] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[4] == "X" and tabla_joc[8] == "X" and tabla_joc[12] == "X":
            print("HUMAN WINNNNS")
            break
        elif casute == "":
            print("Remiza. Nu mai sunt mutari disponibile.")
            break
    if casute != "":  # prevenim programul sa afiseze:
        # Index Error, acest bloc ruleaza doar daca mai sunt mutari disponibile
        casuta_PC = random.choice(casute)
        print(f"- Computerul a ales sa joace casuta: {casuta_PC}")
        casute = casute.replace(casuta_PC, "")  # limitam optiunile PC ului
    else:
        print("Remiza. Nu mai sunt mutari disponibile.")
        break
    if casuta_PC in tabla_joc:
        tabla_joc = tabla_joc.replace(casuta_PC, "0")
        # print(casute)
        print(tabla_joc)
        # toate pozitiile castigatoare in functie de randuri pentru 0
        if tabla_joc[0] == "0" and tabla_joc[2] == "0" and tabla_joc[4] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[6] == "0" and tabla_joc[8] == "0" and tabla_joc[10] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[12] == "0" and tabla_joc[14] == "0" and tabla_joc[16] == "0":
            print("PC WINNNNS")
            break
        # toate pozitiile castigatoare in functie de coloane pentru 0
        elif tabla_joc[0] == "0" and tabla_joc[6] == "0" and tabla_joc[12] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[2] == "0" and tabla_joc[8] == "0" and tabla_joc[14] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[4] == "0" and tabla_joc[10] == "0" and tabla_joc[16] == "0":
            print("PC WINNNNS")
            break
            # diagonalele pentru 0
        elif tabla_joc[0] == "0" and tabla_joc[8] == "0" and tabla_joc[16] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[4] == "0" and tabla_joc[8] == "0" and tabla_joc[12] == "0":
            print("PC WINNNNS")
            break
        elif casute == "":
            print("Remiza. Nu mai sunt mutari disponibile.")
            break
# pozitiile pe tabla de joc in functie de casute

#
# for idx, i in enumerate(casute_cu_spatii):
#     print(idx,i)
