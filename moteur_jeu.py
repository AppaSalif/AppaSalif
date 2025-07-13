import random
from civilisation import Civilisation
from figure_historique import FigureHistorique
from courant_de_pensee import CourantDePensee
from entree_journal import EntreeJournal
from murmure import Murmure
from typing import List

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def ajouter_entree_journal(civilisation: Civilisation, temps: int, message: str, est_lie_au_joueur: bool, type_evenement: str, reference_id: str = None):
    civilisation.JournalDeBord.append(EntreeJournal(temps, message, est_lie_au_joueur, type_evenement, reference_id))

def initialiser_civilisation(type_scenario: str) -> Civilisation:
    nouvelle_civilisation = Civilisation()

    figure_alpha = FigureHistorique(
        ID="FigureAlpha",
        Nom="Le Penseur Solitaire",
        Traits=["Pragmatique"],
        InfluenceSurTechnologie=0.1,
        InfluenceSurStabilite=0.05,
        InfluenceSurFoi=-0.05
    )
    nouvelle_civilisation.FigureCle = figure_alpha

    courant_progres = CourantDePensee(
        ID="CourantProgres",
        Nom="Idée de Progrès Technologique",
        ImpactSurTechnologie=0.05,
        ImpactSurStabilite=-0.01,
        ImpactSurFoi=-0.02,
        AntagonisteID="CourantTradition"
    )
    nouvelle_civilisation.CourantProgres = courant_progres

    courant_tradition = CourantDePensee(
        ID="CourantTradition",
        Nom="Voie de la Tradition Ancestrale",
        ImpactSurTechnologie=-0.01,
        ImpactSurStabilite=0.03,
        ImpactSurFoi=0.05,
        AntagonisteID="CourantProgres"
    )
    nouvelle_civilisation.CourantTradition = courant_tradition

    nouvelle_civilisation.Technologie = random.uniform(20, 40)
    nouvelle_civilisation.StabiliteSociale = random.uniform(60, 80)
    nouvelle_civilisation.Foi = random.uniform(40, 60)
    nouvelle_civilisation.EssenceCausale = 50
    nouvelle_civilisation.PotentielDeRupture = random.uniform(0, 10)
    nouvelle_civilisation.SeuilDeRuptureActuel = random.uniform(70, 90)
    nouvelle_civilisation.CourantProgres.Force = random.uniform(30, 50)
    nouvelle_civilisation.CourantTradition.Force = random.uniform(50, 70)
    message_debut = "Un nouveau cycle de civilisation commence. Le Penseur Solitaire se penche sur son destin."

    if type_scenario == "AgeDore":
        nouvelle_civilisation.Technologie = random.uniform(30, 50)
        nouvelle_civilisation.StabiliteSociale = random.uniform(70, 90)
        nouvelle_civilisation.Foi = random.uniform(50, 70)
        nouvelle_civilisation.EssenceCausale = 70
        nouvelle_civilisation.PotentielDeRupture = random.uniform(0, 5)
        nouvelle_civilisation.SeuilDeRuptureActuel = random.uniform(80, 100)
        nouvelle_civilisation.CourantProgres.Force = random.uniform(40, 60)
        nouvelle_civilisation.CourantTradition.Force = random.uniform(60, 80)
        figure_alpha.Traits.append("Pacificateur")
        message_debut = "Le nouveau cycle débute sous les auspices d'un âge d'or, mais l'équilibre est fragile."
    elif type_scenario == "EreDeTroubles":
        nouvelle_civilisation.Technologie = random.uniform(10, 30)
        nouvelle_civilisation.StabiliteSociale = random.uniform(30, 50)
        nouvelle_civilisation.Foi = random.uniform(20, 40)
        nouvelle_civilisation.EssenceCausale = 40
        nouvelle_civilisation.PotentielDeRupture = random.uniform(20, 40)
        nouvelle_civilisation.SeuilDeRuptureActuel = random.uniform(50, 70)
        nouvelle_civilisation.CourantProgres.Force = random.uniform(20, 40)
        nouvelle_civilisation.CourantTradition.Force = random.uniform(30, 50)
        figure_alpha.Traits.append("Chaotique")
        message_debut = "Ce nouveau cycle s'annonce tourmenté. La civilisation est au bord du chaos."
    elif type_scenario == "L'EveilTechnologique":
        nouvelle_civilisation.Technologie = random.uniform(60, 80)
        nouvelle_civilisation.StabiliteSociale = random.uniform(50, 70)
        nouvelle_civilisation.Foi = random.uniform(10, 30)
        nouvelle_civilisation.EssenceCausale = 60
        nouvelle_civilisation.PotentielDeRupture = random.uniform(10, 20)
        nouvelle_civilisation.SeuilDeRuptureActuel = random.uniform(60, 80)
        nouvelle_civilisation.CourantProgres.Force = random.uniform(60, 80)
        nouvelle_civilisation.CourantTradition.Force = random.uniform(10, 30)
        figure_alpha.Traits.append("Innovateur")
        message_debut = "La civilisation est lancée dans une ère de découvertes sans précédent, mais au prix de ses anciennes croyances."
    elif type_scenario == "LeCredoAscendant":
        nouvelle_civilisation.Technologie = random.uniform(10, 30)
        nouvelle_civilisation.StabiliteSociale = random.uniform(40, 60)
        nouvelle_civilisation.Foi = random.uniform(60, 80)
        nouvelle_civilisation.EssenceCausale = 55
        nouvelle_civilisation.PotentielDeRupture = random.uniform(5, 15)
        nouvelle_civilisation.SeuilDeRuptureActuel = random.uniform(75, 95)
        nouvelle_civilisation.CourantProgres.Force = random.uniform(20, 40)
        nouvelle_civilisation.CourantTradition.Force = random.uniform(60, 80)
        figure_alpha.Traits.append("Mystique")
        message_debut = "Une ferveur spirituelle profonde s'empare de la civilisation, ouvrant la voie à une nouvelle ère de foi."

    nouvelle_civilisation.TempsActuel = 0
    nouvelle_civilisation.AgeActuel = "AgeStable"
    nouvelle_civilisation.TypeDeRuptureImminent = "Aucun"
    nouvelle_civilisation.DerniereRupture = "Aucune"
    nouvelle_civilisation.HistoriqueMurmures = []
    nouvelle_civilisation.JournalDeBord = []
    nouvelle_civilisation.ImpactCumuleMurmuresJoueur = {"Technologie": 0, "StabiliteSociale": 0, "Foi": 0}
    nouvelle_civilisation.NombreDeRupturesDeclenchees = 0
    nouvelle_civilisation.NombreDeMurmuresJoues = 0

    ajouter_entree_journal(nouvelle_civilisation, nouvelle_civilisation.TempsActuel, message_debut, False, "DébutDeCycle")

    return nouvelle_civilisation

def mettre_a_jour_civilisation(civilisation: Civilisation):
    civilisation.TempsActuel += 1

    net_change_tech = 0
    net_change_stab = 0
    net_change_foi = 0

    net_change_tech += 0.1
    net_change_stab -= 0.05
    net_change_foi += 0.02

    net_change_tech += civilisation.CourantProgres.Force * civilisation.CourantProgres.ImpactSurTechnologie
    net_change_foi += civilisation.CourantTradition.Force * civilisation.CourantTradition.ImpactSurFoi
    net_change_stab += civilisation.CourantProgres.Force * civilisation.CourantProgres.ImpactSurStabilite
    net_change_tech += civilisation.CourantTradition.Force * civilisation.CourantTradition.ImpactSurTechnologie
    net_change_stab += civilisation.CourantTradition.Force * civilisation.CourantTradition.ImpactSurStabilite

    civilisation.CourantProgres.Force *= 0.98
    civilisation.CourantTradition.Force *= 0.99

    civilisation.CourantProgres.Force = clamp(civilisation.CourantProgres.Force, 0, 100)
    civilisation.CourantTradition.Force = clamp(civilisation.CourantTradition.Force, 0, 100)

    net_change_tech += random.uniform(-0.5, 0.5)
    net_change_stab += random.uniform(-1.0, 1.0)
    net_change_foi += random.uniform(-0.5, 0.5)

    civilisation.Technologie += net_change_tech
    civilisation.StabiliteSociale += net_change_stab
    civilisation.Foi += net_change_foi

    civilisation.Technologie = clamp(civilisation.Technologie, 0, 100)
    civilisation.Foi = clamp(civilisation.Foi, 0, 100)
    civilisation.StabiliteSociale = clamp(civilisation.StabiliteSociale, 0, 100)

    if civilisation.StabiliteSociale == 0:
        civilisation.AgeActuel = "Effondrement"
        terminer_cycle_de_jeu(civilisation)
        return

    civilisation.EssenceCausale = clamp(civilisation.EssenceCausale + 1, 0, 200)

    ajouts = []
    if net_change_tech != 0: ajouts.append(f"Technologie {net_change_tech:+.1f}")
    if net_change_stab != 0: ajouts.append(f"Stabilité {net_change_stab:+.1f}")
    if net_change_foi != 0: ajouts.append(f"Foi {net_change_foi:+.1f}")

    if ajouts:
        message_evolution = "La civilisation évolue naturellement : " + ", ".join(ajouts) + "."
        ajouter_entree_journal(civilisation, civilisation.TempsActuel, message_evolution, False, "Normal")

    civilisation.PotentielDeRupture += civilisation.Technologie * 0.02
    civilisation.PotentielDeRupture += (100 - civilisation.StabiliteSociale) * 0.05
    civilisation.PotentielDeRupture = clamp(civilisation.PotentielDeRupture, 0, 100)

    if civilisation.PotentielDeRupture >= civilisation.SeuilDeRuptureActuel:
        civilisation.AgeActuel = "PointDeRupture"

        concept_dominant_murmures = analyser_historique_murmures(civilisation.HistoriqueMurmures)

        civilisation.EssenceCausale = clamp(civilisation.EssenceCausale + 20, 0, 200)
        civilisation.NombreDeRupturesDeclenchees += 1

        if concept_dominant_murmures:
            ajouter_entree_journal(civilisation, civilisation.TempsActuel, f"L'écho de vos Murmures passés se fait sentir : les efforts sur le thème de la '{concept_dominant_murmures}' se font dominants dans la civilisation.", False, None)

        type_rupture_base = ""
        if civilisation.Technologie > random.uniform(65, 75):
            type_rupture_base = "DecouverteMajeure"
        elif civilisation.StabiliteSociale < random.uniform(25, 35):
            type_rupture_base = "Revolution"
        elif civilisation.Foi > random.uniform(65, 75):
            type_rupture_base = "RenouveauSpirituel"
        else:
            type_rupture_base = "EvenementImprevuMajeur"

        civilisation.TypeDeRuptureImminent = type_rupture_base
        description_supplementaire = ""

        if concept_dominant_murmures == "Technologie" and type_rupture_base != "Revolution":
            civilisation.TypeDeRuptureImminent = "DecouverteMajeure"
            description_supplementaire = " (une conséquence directe des innovations incessantes)."
        elif concept_dominant_murmures == "Stabilite" and type_rupture_base != "Revolution":
            civilisation.TypeDeRuptureImminent = "ReformeSociale"
            description_supplementaire = " (le fruit des efforts pour maintenir l'ordre et la cohésion)."
        elif concept_dominant_murmures == "Foi" and type_rupture_base != "DecouverteMajeure":
            civilisation.TypeDeRuptureImminent = "RenouveauSpirituel"
            description_supplementaire = " (alimenté par une quête spirituelle grandissante)."

        civilisation.DerniereRupture = civilisation.TypeDeRuptureImminent

        if civilisation.TypeDeRuptureImminent == "Revolution":
            civilisation.CourantProgres.Force += 15
            civilisation.CourantTradition.Force -= 5
        elif civilisation.TypeDeRuptureImminent == "DecouverteMajeure":
            civilisation.CourantProgres.Force += 10
            civilisation.CourantTradition.Force -= 2
        elif civilisation.TypeDeRuptureImminent == "RenouveauSpirituel":
            civilisation.CourantTradition.Force += 15
            civilisation.CourantProgres.Force -= 5
        elif civilisation.TypeDeRuptureImminent == "ReformeSociale":
            civilisation.CourantProgres.Force += 3
            civilisation.CourantTradition.Force += 7

        civilisation.PotentielDeRupture = random.uniform(10, 30)

        prochain_seuil_base = random.uniform(70, 90)
        if "Pacificateur" in civilisation.FigureCle.Traits:
            civilisation.SeuilDeRuptureActuel = prochain_seuil_base + 10
        elif "Chaotique" in civilisation.FigureCle.Traits:
            civilisation.SeuilDeRuptureActuel = prochain_seuil_base - 10
        else:
            civilisation.SeuilDeRuptureActuel = prochain_seuil_base

        messages_rupture = {
            "Revolution": "Le peuple se soulève ! La situation politique est tendue et les traditions sont bousculées.",
            "DecouverteMajeure": f"Une invention ou une idée révolutionnaire voit le jour ! La {civilisation.FigureCle.Nom} a joué un rôle clé.",
            "RenouveauSpirituel": "Un souffle de spiritualité parcourt la civilisation, redéfinissant les croyances ancestrales.",
            "ReformeSociale": "Des changements structurels majeurs sont en cours, cherchant à remodeler la société.",
            "EvenementImprevuMajeur": "Un événement imprévu secoue la civilisation jusqu'à ses fondations. Son impact est encore incertain."
        }
        ajouter_entree_journal(civilisation, civilisation.TempsActuel, messages_rupture[civilisation.TypeDeRuptureImminent] + description_supplementaire, True, "Rupture")
    else:
        civilisation.AgeActuel = "AgeStable"

    if verifier_conditions_fin_de_cycle(civilisation):
        terminer_cycle_de_jeu(civilisation)
        return

def ajouter_murmure_a_historique(civilisation: Civilisation, murmure: Murmure):
    civilisation.HistoriqueMurmures.append(murmure)
    if len(civilisation.HistoriqueMurmures) > 5:
        civilisation.HistoriqueMurmures.pop(0)

def analyser_historique_murmures(historique_murmures: List[Murmure]) -> str:
    comptage_concepts = {}
    for murmure in historique_murmures:
        comptage_concepts[murmure.Concept] = comptage_concepts.get(murmure.Concept, 0) + 1

    concept_le_plus_frequent = None
    max_occurrences = 0
    for concept, occurrences in comptage_concepts.items():
        if occurrences > max_occurrences:
            max_occurrences = occurrences
            concept_le_plus_frequent = concept

    if max_occurrences < 2:
        return None

    return concept_le_plus_frequent

def appliquer_murmure(civilisation: Civilisation, murmure: Murmure):
    cout_murmure = 10
    if civilisation.EssenceCausale < cout_murmure:
        ajouter_entree_journal(civilisation, civilisation.TempsActuel, "Vous n'avez pas assez d'Essence Causale pour ce Murmure.", True, "ErreurMurmure")
        return

    civilisation.EssenceCausale -= cout_murmure

    cible = None
    if murmure.CibleID == civilisation.FigureCle.ID:
        cible = civilisation.FigureCle
    elif murmure.CibleID == civilisation.CourantProgres.ID:
        cible = civilisation.CourantProgres
    elif murmure.CibleID == civilisation.CourantTradition.ID:
        cible = civilisation.CourantTradition

    if cible is None:
        ajouter_entree_journal(civilisation, civilisation.TempsActuel, "Erreur: Cible du Murmure non valide.", True, murmure.ID)
        return

    ajouter_entree_journal(civilisation, civilisation.TempsActuel, f"Votre Murmure a coûté {cout_murmure} Essence Causale. Il vous en reste {civilisation.EssenceCausale}.", True, "DepenseMurmure", murmure.ID)

    civilisation.NombreDeMurmuresJoues += 1

    impact_reel_technologie = 0
    impact_reel_stabilite = 0
    impact_reel_foi = 0

    if isinstance(cible, FigureHistorique):
        modificateur = 1.0

        if murmure.Concept == "Technologie" and "Innovateur" in cible.Traits:
            modificateur *= 1.5
        if murmure.Concept == "Stabilite" and "Pacificateur" in cible.Traits:
            modificateur *= 1.3
        if murmure.Concept == "Foi" and "Mystique" in cible.Traits:
            modificateur *= 1.5
        if "Chaotique" in cible.Traits:
            modificateur *= 0.7

        repetitions = 0
        for mur_ancien in civilisation.HistoriqueMurmures:
            if mur_ancien.CibleID == cible.ID and mur_ancien.Concept == murmure.Concept and (civilisation.TempsActuel - mur_ancien.TempsDuMurmure) < 5:
                repetitions += 1

        if repetitions > 0:
            malus = 0.1 * repetitions
            modificateur *= (1.0 - malus)
            ajouter_entree_journal(civilisation, civilisation.TempsActuel, f"La {cible.Nom} est de plus en plus sollicitée par les murmures sur la '{murmure.Concept}' (x{repetitions}). L'efficacité diminue.", True, murmure.ID)

        impact_reel_technologie = murmure.ImpactSouhaiteSurTechnologie * modificateur * 0.5
        impact_reel_stabilite = murmure.ImpactSouhaiteSurStabilite * modificateur * 0.5
        impact_reel_foi = murmure.ImpactSouhaiteSurFoi * modificateur * 0.5

    elif isinstance(cible, CourantDePensee):
        augmentation_force = 5
        augmentation_force *= (1 - (cible.Force / 100.0))

        if cible.ID == civilisation.CourantTradition.ID and civilisation.Foi > 60:
            augmentation_force *= 1.2

        cible.Force = clamp(cible.Force + augmentation_force, 0, 100)

        impact_reel_technologie = cible.ImpactSurTechnologie * (augmentation_force / 10.0)
        impact_reel_stabilite = cible.ImpactSurStabilite * (augmentation_force / 10.0)
        impact_reel_foi = cible.ImpactSurFoi * (augmentation_force / 10.0)

        if cible.AntagonisteID:
            antagoniste = None
            if cible.AntagonisteID == civilisation.CourantProgres.ID:
                antagoniste = civilisation.CourantProgres
            elif cible.AntagonisteID == civilisation.CourantTradition.ID:
                antagoniste = civilisation.CourantTradition

            if antagoniste:
                antagoniste.Force = clamp(antagoniste.Force - (augmentation_force * 0.2), 0, 100)

    civilisation.Technologie = clamp(civilisation.Technologie + impact_reel_technologie, 0, 100)
    civilisation.StabiliteSociale = clamp(civilisation.StabiliteSociale + impact_reel_stabilite, 0, 100)
    civilisation.Foi = clamp(civilisation.Foi + impact_reel_foi, 0, 100)

    civilisation.ImpactCumuleMurmuresJoueur["Technologie"] += murmure.ImpactSouhaiteSurTechnologie
    civilisation.ImpactCumuleMurmuresJoueur["StabiliteSociale"] += murmure.ImpactSouhaiteSurStabilite
    civilisation.ImpactCumuleMurmuresJoueur["Foi"] += murmure.ImpactSouhaiteSurFoi

    ajouter_entree_journal(civilisation, civilisation.TempsActuel, f"Votre Murmure sur le concept de '{murmure.Concept}' ciblant {cible.Nom} a été appliqué.", True, murmure.ID)

    if impact_reel_technologie != 0 or impact_reel_stabilite != 0 or impact_reel_foi != 0:
        ajouter_entree_journal(civilisation, civilisation.TempsActuel, f"Conséquence: Technologie {impact_reel_technologie:+.1f}, Stabilité {impact_reel_stabilite:+.1f}, Foi {impact_reel_foi:+.1f}.", True, murmure.ID)

    ajouter_murmure_a_historique(civilisation, murmure)

def verifier_conditions_fin_de_cycle(civilisation: Civilisation) -> bool:
    delai_minimal_pour_victoire = 50
    if civilisation.TempsActuel < delai_minimal_pour_victoire:
        if civilisation.StabiliteSociale <= 0:
            return True
        return False

    if civilisation.StabiliteSociale <= 0:
        return True

    if civilisation.Technologie >= 95 and civilisation.StabiliteSociale >= 35 and civilisation.Foi >= 15:
        civilisation.AgeActuel = "ApogeeTechnologique"
        return True

    if civilisation.Foi >= 85 and civilisation.StabiliteSociale >= 65 and civilisation.Technologie >= 25:
        civilisation.AgeActuel = "EreSpirituelleHarmonieuse"
        return True

    if civilisation.Technologie >= 70 and civilisation.StabiliteSociale >= 70 and civilisation.Foi >= 70:
        civilisation.AgeActuel = "HarmonieParfaite"
        return True

    return False

def terminer_cycle_de_jeu(civilisation: Civilisation):
    message_fin = ""
    if civilisation.AgeActuel == "Effondrement":
        message_fin = "La civilisation s'est effondrée. C'est la fin de ce cycle."
    elif civilisation.AgeActuel == "ApogeeTechnologique":
        message_fin = "La civilisation a atteint son apogée technologique. Un chapitre s'achève."
    elif civilisation.AgeActuel == "EreSpirituelleHarmonieuse":
        message_fin = "Une ère de foi et d'harmonie a été inaugurée. Le cycle est complet."
    elif civilisation.AgeActuel == "HarmonieParfaite":
        message_fin = "La civilisation a atteint un état d'équilibre parfait. Un héritage durable."
    else:
        message_fin = "Le cycle de la civilisation s'achève. Un destin incertain se profile."

    ajouter_entree_journal(civilisation, civilisation.TempsActuel, message_fin, False, "FinDeCycle")

    print("\n--- RAPPORT DE FIN DE CYCLE ---")
    print(f"Durée du cycle : {civilisation.TempsActuel} unités de temps")
    print(f"Technologie finale : {civilisation.Technologie:.1f}")
    print(f"Stabilité Sociale finale : {civilisation.StabiliteSociale:.1f}")
    print(f"Foi finale : {civilisation.Foi:.1f}")

    essence_depensee = 0
    for entree in civilisation.JournalDeBord:
        if entree.TypeEvenement == "DepenseMurmure":
            # This is a hack, we should store the cost in the journal entry
            essence_depensee += 10

    print(f"Essence Causale dépensée totale : {essence_depensee}")
    print(f"Nombre de Points de Rupture traversés : {civilisation.NombreDeRupturesDeclenchees}")
    print(f"Nombre de Murmures joués : {civilisation.NombreDeMurmuresJoues}")

    concept_influence_dominante = "aucun concept identifiable"
    valeur_influence_dominante = 0
    max_magnitude_influence = 0

    for concept, impact_net in civilisation.ImpactCumuleMurmuresJoueur.items():
        if abs(impact_net) > max_magnitude_influence:
            max_magnitude_influence = abs(impact_net)
            concept_influence_dominante = concept
            valeur_influence_dominante = impact_net

    rapport_narratif = ""
    if civilisation.AgeActuel == "Effondrement":
        ton_influence = ""
        if valeur_influence_dominante > 0:
            ton_influence = "positivement"
        elif valeur_influence_dominante < 0:
            ton_influence = "négativement"
        else:
            ton_influence = "sans effet notable"
        rapport_narratif = f"Malgré vos tentatives, la civilisation a succombé à ses propres faiblesses. La discorde l'a emportée, et vos murmures, bien que se concentrant {ton_influence} sur la **{concept_influence_dominante}** (influence totale de {valeur_influence_dominante}), n'ont pu empêcher la chute. Un lourd silence enveloppe désormais ce qui fut."
    elif civilisation.AgeActuel == "ApogeeTechnologique":
        rapport_narratif = f"Vous avez guidé cette civilisation vers un zénith technologique sans précédent. Vos murmures, particulièrement influents sur la **Technologie** (une influence totale de {civilisation.ImpactCumuleMurmuresJoueur.get('Technologie', 0)}), ont forgé un âge d'innovation et de découverte, laissant une empreinte durable sur le monde."
    elif civilisation.AgeActuel == "EreSpirituelleHarmonieuse":
        influence_foi = civilisation.ImpactCumuleMurmuresJoueur.get("Foi", 0)
        influence_stabilite = civilisation.ImpactCumuleMurmuresJoueur.get("StabiliteSociale", 0)
        rapport_narratif = f"Grâce à votre sagesse, une ère de profonde **Foi** et de grande **Stabilité Sociale** s'est épanouie. Vos murmures ont forgé un héritage d'harmonie durable, particulièrement grâce à votre influence sur la Foi (total: {influence_foi}) et la Stabilité (total: {influence_stabilite})."
    elif civilisation.AgeActuel == "HarmonieParfaite":
        rapport_narratif = f"Un équilibre rare et magnifique a été atteint. La civilisation prospère dans une parfaite **Harmonie** où chaque aspect est florissant. Votre touche subtile, souvent axée sur la **{concept_influence_dominante}** (influence totale de {valeur_influence_dominante}), a habilement tissé ce destin idéal."
    else:
        ton_influence = ""
        if valeur_influence_dominante > 0:
            ton_influence = "positive"
        elif valeur_influence_dominante < 0:
            ton_influence = "négative"
        else:
            ton_influence = "neutre"
        rapport_narratif = f"Le cycle de cette civilisation s'achève, laissant derrière lui un destin complexe. Vos murmures ont eu une influence principalement {ton_influence} sur la **{concept_influence_dominante}** (impact total de {valeur_influence_dominante}), façonnant ainsi son cours de manière unique."

    print("")
    print(rapport_narratif)
    print("--- FIN DU RAPPORT ---")
