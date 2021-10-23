from queue import Queue
import math
from typing import Union
from enum import Enum
from dataclasses import dataclass


class Boja(Enum):
    Bijela = 0
    Siva = 1
    Crna = 2


@dataclass
class Cvor:
    # ovo je neophodno da bi objekt tipa Cvor mogao biti kljuc
    # rjecnika
    def __hash__(self):
        return hash(self.__naziv)

    # ako je definiran __hash__ treba biti i __eq__
    def __eq__(self, drugi):
        return self.__naziv == drugi.__naziv

    def __repr__(self):
        return self.naziv

    @property
    def naziv(self):
        return self.__naziv

    __naziv: str
    boja: Boja = Boja.Bijela
    udaljenost: float = math.inf
    prethodnik: Union['Cvor ', None] = None
    zavrsen: int = 0
    otkriven: int = 0


@dataclass
class BFSCvor (Cvor):
    ''' Pretraživanje u širinu '''
    __hash__ = Cvor.__hash__
    __eq__ = Cvor.__eq__

    def __repr__(self):
        return f'({ self.naziv }) udaljenost : {self. udaljenost }'


@dataclass
class DFSCvor (Cvor):
    ''' Pretraživanje u dubinu '''
    __hash__ = Cvor.__hash__
    __eq__ = Cvor.__eq__

    def __repr__(self):
        return (f'({ self.naziv }) otkriven / zavrsen : '
                f'{self.otkriven }/{ self.zavrsen }')

    otkriven: int = 0
    zavrsen: int = 0

