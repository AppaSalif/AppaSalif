from dataclasses import dataclass

@dataclass
class CourantDePensee:
    ID: str
    Nom: str
    Force: float = 0.0
    ImpactSurTechnologie: float = 0.0
    ImpactSurStabilite: float = 0.0
    ImpactSurFoi: float = 0.0
    AntagonisteID: str = ""
