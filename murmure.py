from dataclasses import dataclass

@dataclass
class Murmure:
    ID: str
    Concept: str
    CibleID: str
    TempsDuMurmure: int
    ImpactSouhaiteSurTechnologie: float = 0.0
    ImpactSouhaiteSurStabilite: float = 0.0
    ImpactSouhaiteSurFoi: float = 0.0
