import random
import time

import numpy as np

"""Erwartungswert"""


def hubkloth_method():
    start = time.time()
    hub = 901
    kloth = 151112314
    zufalls_zahl_k = random.randint(hub, kloth)
    zufalls_zahl_z = random.randint(hub, kloth)
    if zufalls_zahl_k > zufalls_zahl_z:
        duper_wert = np.random.randint(zufalls_zahl_z, zufalls_zahl_k, size=(1, 10000))
    else:
        duper_wert = np.random.randint(zufalls_zahl_k, zufalls_zahl_z, size=(1, 10000))
    end = time.time()
    gen_zeit = end - start
    zufall_1 = hub + int(gen_zeit)
    zufall_2 = kloth - int(gen_zeit)
    vec_wert = np.random.randint(zufall_1, zufall_2, size=(1, 10000))
    werte = duper_wert + vec_wert
    erstes_moment_p_oi = np.random.poisson(werte)

    return erstes_moment_p_oi


"""Auswahl von Antworten"""


def call_response_pattern():
    randomizierte = hubkloth_method()
    choice = np.max(randomizierte)
    print(choice)
    print(randomizierte)


def main():
    call_response_pattern()


if __name__ == "__main__":
    main()
