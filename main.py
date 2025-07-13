import moteur_jeu
from murmure import Murmure
import uuid

def afficher_etat_civilisation(civilisation):
    print("\n" + "="*50)
    print(f"Temps: {civilisation.TempsActuel} | Age: {civilisation.AgeActuel}")
    print(f"Technologie: {civilisation.Technologie:.1f} | Stabilité Sociale: {civilisation.StabiliteSociale:.1f} | Foi: {civilisation.Foi:.1f}")
    print(f"Essence Causale: {civilisation.EssenceCausale}")
    print(f"Potentiel de Rupture: {civilisation.PotentielDeRupture:.1f} / {civilisation.SeuilDeRuptureActuel:.1f}")
    print(f"Courant Progrès: {civilisation.CourantProgres.Force:.1f} | Courant Tradition: {civilisation.CourantTradition.Force:.1f}")
    print("="*50)

def choisir_murmure(civilisation):
    print("\n--- Quel murmure voulez-vous envoyer ? ---")
    print("1. Murmurer à la Figure Clé")
    print("2. Murmurer au Courant du Progrès")
    print("3. Murmurer au Courant de la Tradition")
    print("4. Ne rien faire et laisser le temps passer")

    choix_cible = input("Votre choix : ")
    if choix_cible not in ["1", "2", "3"]:
        return None

    cible_id = ""
    if choix_cible == "1":
        cible_id = civilisation.FigureCle.ID
    elif choix_cible == "2":
        cible_id = civilisation.CourantProgres.ID
    elif choix_cible == "3":
        cible_id = civilisation.CourantTradition.ID

    print("\n--- Quel concept voulez-vous influencer ? ---")
    print("1. Technologie")
    print("2. Stabilité")
    print("3. Foi")

    choix_concept = input("Votre choix : ")
    if choix_concept not in ["1", "2", "3"]:
        return None

    concept = ""
    impact_technologie = 0
    impact_stabilite = 0
    impact_foi = 0

    if choix_concept == "1":
        concept = "Technologie"
        impact_technologie = 10
    elif choix_concept == "2":
        concept = "Stabilite"
        impact_stabilite = 10
    elif choix_concept == "3":
        concept = "Foi"
        impact_foi = 10

    return Murmure(
        ID=str(uuid.uuid4()),
        Concept=concept,
        CibleID=cible_id,
        TempsDuMurmure=civilisation.TempsActuel,
        ImpactSouhaiteSurTechnologie=impact_technologie,
        ImpactSouhaiteSurStabilite=impact_stabilite,
        ImpactSouhaiteSurFoi=impact_foi,
    )

def main():
    print("Bienvenue dans Architecte du Temps !")
    print("Choisissez votre scénario de départ :")
    print("1. Age d'Or")
    print("2. Ere de Troubles")
    print("3. L'Eveil Technologique")
    print("4. Le Credo Ascendant")

    choix_scenario = input("Votre choix : ")
    scenarios = {"1": "AgeDore", "2": "EreDeTroubles", "3": "L'EveilTechnologique", "4": "LeCredoAscendant"}
    scenario = scenarios.get(choix_scenario, "AgeDore")

    civilisation = moteur_jeu.initialiser_civilisation(scenario)

    while civilisation.AgeActuel not in ["Effondrement", "ApogeeTechnologique", "EreSpirituelleHarmonieuse", "HarmonieParfaite"]:
        afficher_etat_civilisation(civilisation)

        for entree in civilisation.JournalDeBord:
            if entree.Temps == civilisation.TempsActuel:
                print(f"[JOURNAL] {entree.Message}")

        murmure = choisir_murmure(civilisation)
        if murmure:
            moteur_jeu.appliquer_murmure(civilisation, murmure)

        moteur_jeu.mettre_a_jour_civilisation(civilisation)

    moteur_jeu.terminer_cycle_de_jeu(civilisation)

if __name__ == "__main__":
    main()
