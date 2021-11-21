def sintaksna_analiza_vu(gramatika, pocetni_simbol, recenica):
    pozicija = 0
    izvodi = []
    stog_izvoda = [pocetni_simbol]
    neterminali = gramatika.keys()

    def analiza(neterminal, nastavak='', tab=''):
        '''
        neterminal : trenutni neterminal za koji dalje
        razvijamo stablo
        nastavak : neobradjeni dio izvoda
        '''
        nonlocal pozicija, izvodi, stog_izvoda
        alternative = gramatika[neterminal]

        # pocetna pozicija na ovoj razini stabla
        pocetna_poz = pozicija

        for alt in alternative:
            pozicija = pocetna_poz
            trenutni_izvod = (recenica[: pozicija] + alt
                              + nastavak)
            print('\n', tab, '<' + trenutni_izvod + '>', ' [' + str(pocetna_poz) + ': ' + alt
                  + nastavak + ']',
                  end='')
            stog_izvoda . append(trenutni_izvod)
            for i, sim in enumerate(alt + nastavak):
                if sim in neterminali:
                    analiza(sim, (alt + nastavak)[i + 1:],
                            tab + (' ' * 4))
                    break  # idi na iducu alternativu
                else:
                    if pozicija >= len(recenica):
                        break  # idi na iducu alternativu

                           if recenica[pozicija] == sim:
                                pozicija += 1
                            else:
                                break  # idi na iducu alternativu

                        else:
                            # Ako ovdje imamo sve terminale i prosli
                            # smo sve ulazne simbole onda smo dobili
                            # jedan izvod .
                            if (trenutni_izvod == recenica and pozicija == len(recenica)):
                                izvodi += [stog_izvoda.copy ()]
                        # prethodna alternativa vise nam ne treba
                        stog_izvoda.pop()

                try:
                    print (' <' + pocetni_simbol + '>[' + str( pozicija ) + ': ' + pocetni_simbol + ']', end='')
                    analiza (pocetni_simbol )
                    print ('\n\n', recenica + ':', izvodi)
                except Exception as e:
                    print('\n!!! GRESKA ', e. with_traceback ())


gram = {
'S': ['T', 'T+S'],
'T': ['F', 'F*T'],
'F': ['(S)', 'v'],
}


recenica = 'v+v'
sintaksna_analiza_vu (gram , 'S', recenica )
