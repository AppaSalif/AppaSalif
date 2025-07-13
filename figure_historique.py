from dataclasses import dataclass, field
from typing import List

@dataclass
class FigureHistorique:
    ID: str
    Nom: str
    Traits: List[str] = field(default_factory=list)
    InfluenceSurTechnologie: float = 0.0
    InfluenceSurStabilite: float = 0.0
    InfluenceSurFoi: float = 0.0
