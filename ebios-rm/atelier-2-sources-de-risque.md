# Atelier 2 — Sources de risque et objectifs visés

> **Velmora Payments est une entreprise fictive.** Analyse réalisée à titre d'exemple, selon la méthode EBIOS Risk Manager (ANSSI). Suite de l'[atelier 1](atelier-1-cadrage-socle.md).

**Question de l'atelier :** *qui* pourrait s'en prendre à Velmora, et *pour obtenir quoi* ?

## 1. Sources de risque (SR) et objectifs visés (OV) identifiés

| ID | Source de risque | Objectif visé | Lien avec les événements redoutés (atelier 1) |
|---|---|---|---|
| **SR/OV 1** | Cybercriminel organisé (groupe de rançongiciel) | Obtenir une rançon en bloquant la plateforme | ER1 (indisponibilité) |
| **SR/OV 2** | Cybercriminel organisé (fraude financière) | Détourner des paiements ou des fonds | ER3 (fraude) |
| **SR/OV 3** | Cybercriminel (revente de données) | Voler et revendre les données de paiement | ER2 (fuite de données) |
| **SR/OV 4** | Employé ou prestataire malveillant | Se venger ou s'enrichir (vol de données, sabotage) | ER2, ER5 |
| **SR/OV 5** | Hacktiviste | Nuire à l'image (défiguration, fuite médiatisée) | ER1, ER2 |
| **SR/OV 6** | Concurrent | Voler le code source ou des informations commerciales | ER5 |
| **SR/OV 7** | Acteur étatique | Espionnage du secteur financier | ER2 |

## 2. Évaluation de la pertinence

Échelle : ● faible · ●● moyenne · ●●● forte

| ID | Motivation | Ressources | Activité constatée dans le secteur | Pertinence | Retenu ? |
|---|---|---|---|---|---|
| SR/OV 1 — Rançongiciel | ●●● (gain élevé, paiement probable sous pression) | ●●● (outils industrialisés, accès revendus) | ●●● (secteur financier très ciblé) | **Forte** | ✅ |
| SR/OV 2 — Fraude financière | ●●● (gain direct) | ●● | ●●● | **Forte** | ✅ |
| SR/OV 3 — Revente de données | ●● | ●● | ●●● | **Moyenne à forte** | ✅ |
| SR/OV 4 — Initié malveillant | ●● | ●●● (accès légitimes déjà obtenus) | ●● | **Moyenne** | ✅ |
| SR/OV 5 — Hacktiviste | ● (cible peu symbolique) | ● | ● | Faible | ❌ |
| SR/OV 6 — Concurrent | ● | ●● | ● | Faible | ❌ |
| SR/OV 7 — Acteur étatique | ● (taille et données peu stratégiques) | ●●● | ● | Faible | ❌ |

## 3. Couples retenus pour la suite

| Couple | Pourquoi |
|---|---|
| **SR/OV 1 — Rançongiciel → rançon** | Menace n°1 du secteur ; vise directement l'événement critique ER1 (G4) |
| **SR/OV 2 — Fraude → détournement de fonds** | Gain direct pour l'attaquant ; vise ER3 (G4) |
| **SR/OV 3 — Revente de données** | Données de paiement monnayables ; vise ER2 (G4) |
| **SR/OV 4 — Initié malveillant** | Accès légitimes et comptes administrateurs permanents (écart I-03) : chemin court vers ER2 et ER5 |

**Conclusion de l'atelier 2 :** quatre couples sont retenus. Les menaces écartées (hacktivistes, concurrent, acteur étatique) seront réexaminées au prochain cycle stratégique. L'atelier 3 étudiera *par où* ces attaquants passeraient, directement ou via l'écosystème (hébergeur cloud, prestataire de paiement, fournisseur d'identité, développeurs).
