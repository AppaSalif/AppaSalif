from dataclasses import dataclass, field
from typing import List, Dict
from figure_historique import FigureHistorique
from courant_de_pensee import CourantDePensee
from murmure import Murmure
from entree_journal import EntreeJournal

@dataclass
class Civilisation:
    Technologie: float = 0.0
    StabiliteSociale: float = 0.0
    Foi: float = 0.0
    TempsActuel: int = 0
    AgeActuel: str = "AgeStable"
    PotentielDeRupture: float = 0.0
    SeuilDeRuptureActuel: float = 0.0
    TypeDeRuptureImminent: str = "Aucun"
    FigureCle: FigureHistorique = None
    CourantProgres: CourantDePensee = None
    CourantTradition: CourantDePensee = None
    DerniereRupture: str = "Aucune"
    HistoriqueMurmures: List[Murmure] = field(default_factory=list)
    JournalDeBord: List[EntreeJournal] = field(default_factory=list)
    EssenceCausale: int = 0
    ImpactCumuleMurmuresJoueur: Dict[str, float] = field(default_factory=dict)
    NombreDeRupturesDeclenchees: int = 0
    NombreDeMurmuresJoues: int = 0
