from dataclasses import dataclass

@dataclass
class EntreeJournal:
    Temps: int
    Message: str
    EstLieAuJoueur: bool
    TypeEvenement: str
    ReferenceID: str = None
