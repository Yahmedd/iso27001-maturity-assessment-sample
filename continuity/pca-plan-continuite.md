# Plan de continuité et de reprise d'activité (PCA / PRA)

> **Velmora Payments est une entreprise fictive.** Exemple réalisé pour un portfolio. Il répond aux objectifs fixés par le [BIA](bia-analyse-impact.md) et au risque R1 (rançongiciel) de l'[analyse EBIOS RM](../ebios-rm/atelier-5-traitement-du-risque.md).

## 1. Stratégies de continuité

| Activité | RTO / RPO cibles | Stratégie technique | Mesure EBIOS liée |
|---|---|---|---|
| **A1** Autorisation des paiements | 2 h / 0 | Plateforme répartie sur deux zones de disponibilité ; base de données répliquée en continu ; bascule automatique | — |
| **A2** API marchands | 2 h / 5 min | Même architecture que A1 ; mode dégradé (paiements et remboursements uniquement) | M5 |
| **A1–A3** en cas de rançongiciel | 24 h / 1 h | Sauvegardes **immuables**, copie hors ligne dans un compte cloud séparé ; reconstruction de la production depuis le code d'infrastructure | M2, M3 |
| **A4** Reporting et notification | 4 h / 1 h | Modèles de notification hors ligne, contacts de l'autorité imprimés dans le kit de crise | — |
| **A5** Support client | 24 h / 24 h | Page d'état hébergée chez un autre fournisseur ; messages types préparés | — |
| **A6** Développement | 72 h / 24 h | Miroir du dépôt de code ; reconstruction des pipelines depuis leur configuration versionnée | M4 |

## 2. Organisation de crise

| Rôle | Titulaire (fictif) | Suppléant | Responsabilités |
|---|---|---|---|
| **Directeur de crise** | Directeur général | Directeur financier | Décisions, communication avec la direction et l'assurance |
| **Responsable technique** | CTO | Lead développement | Bascule, restauration, reconstruction |
| **Responsable sécurité** | Responsable sécurité | Ingénieur sécurité | Investigation, confinement, preuves |
| **Responsable conformité** | Responsable conformité | Juriste | Classification de l'incident, notifications (autorité, CNIL/APD, commerçants) |
| **Communication** | Responsable support | Responsable marketing | Page d'état, messages aux commerçants, presse |

**Déclenchement :** toute indisponibilité de A1 ou A2 de plus de **30 minutes**, ou tout soupçon de rançongiciel, déclenche la cellule de crise.

## 3. Procédure de reprise après rançongiciel (résumé)

| Étape | Action | Délai cible |
|---|---|---|
| 1 | **Isoler** : couper les accès compromis, révoquer les jetons, bloquer la console cloud aux seuls comptes de crise | 30 min |
| 2 | **Évaluer** : périmètre touché, données exfiltrées ou non, état des sauvegardes immuables | 2 h |
| 3 | **Notifier** : classifier l'incident ; lancer les notifications réglementaires (DORA, RGPD 72 h) | dès la classification |
| 4 | **Reconstruire** : nouvel environnement depuis le code d'infrastructure, restauration des données depuis la copie immuable | 24 h |
| 5 | **Vérifier** : contrôles d'intégrité des données, rapprochement des transactions avec l'acquéreur | 24–36 h |
| 6 | **Reprendre** : réouverture progressive (A1, A2, puis A3, A5, A6) | selon les RTO |
| 7 | **Retour d'expérience** : analyse des causes, mise à jour d'EBIOS et du plan | 2 semaines |

## 4. Plan de tests

| Test | Fréquence | Objectif | Écart traité |
|---|---|---|---|
| Restauration d'une sauvegarde de la base | Trimestrielle | Prouver le RPO et mesurer le temps réel de restauration | B-01 |
| Bascule entre zones de disponibilité | Semestrielle | Prouver le RTO de 2 h pour A1 et A2 | B-02 |
| Exercice sur table « rançongiciel » | Annuelle | Tester la cellule de crise, les rôles et les notifications | B-02, N-01 |
| Reconstruction complète depuis le code d'infrastructure | Annuelle | Prouver la reprise sans l'environnement compromis | B-02 |
| Revue des contacts et du kit de crise | Semestrielle | Contacts à jour (autorité, assureur, prestataires) | S-01 |

## 5. Maintien en condition

- Mise à jour du BIA et du plan **chaque année**, et après tout changement majeur (nouveau prestataire, nouvelle activité) ou incident.
- Résultats des tests présentés en **revue de direction** (ISO 27001 cl. 9.3, ISO 22301 cl. 9.3).
- Indicateurs : taux de réussite des restaurations, temps réel de restauration vs RTO, nombre d'exercices réalisés.

## Correspondance avec les référentiels

| Exigence | Couverte par |
|---|---|
| ISO 27001 A.5.29 — Sécurité pendant une perturbation | Organisation de crise, procédure rançongiciel |
| ISO 27001 A.5.30 — Préparation des TIC à la continuité | Stratégies techniques, tests de bascule |
| ISO 27001 A.8.13 — Sauvegarde des informations | Sauvegardes immuables, tests trimestriels |
| DORA art. 11 — Politique de continuité des TIC | Ce plan, tests annuels |
| DORA art. 12 — Sauvegarde et restauration | Copie séparée, restaurations testées |
| ISO 22301 cl. 8.2–8.5 — BIA, stratégies, plans, exercices | BIA, sections 1 à 4 |

*Exemple indicatif réalisé pour un portfolio.*
