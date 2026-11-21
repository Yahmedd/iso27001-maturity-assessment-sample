# Atelier 5 — Traitement du risque

> **Velmora Payments est une entreprise fictive.** Analyse réalisée à titre d'exemple, selon la méthode EBIOS Risk Manager (ANSSI). Suite de l'[atelier 4](atelier-4-scenarios-operationnels.md).

**Question de l'atelier :** que fait-on de chaque risque, avec quelles mesures, et quel risque reste-t-il ensuite ?

## 1. Cartographie des risques initiaux

Règle d'acceptation retenue par la direction :
- 🟥 **Inacceptable** : G4 avec V3 ou plus, ou G3 avec V4 → traitement obligatoire
- 🟧 **Tolérable sous contrôle** : G4/G3 avec V2 → traitement prévu
- 🟩 **Acceptable** : le reste

| Gravité ↓ / Vraisemblance → | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| **G4** | | 🟧 R2 | 🟥 **R1**, 🟥 **R3** | |
| **G3** | | 🟧 R4 | | |
| **G2** | | | | |
| **G1** | | | | |

## 2. Stratégie de traitement

| Risque | Niveau initial | Stratégie | Justification |
|---|---|---|---|
| **R1** Rançongiciel | G4 / V3 🟥 | **Réduire** + **transférer** une partie (assurance cyber) | Menace n°1 du secteur, impact vital |
| **R2** Fraude via l'API | G4 / V2 🟧 | **Réduire** | Pertes directes, mesures techniques simples |
| **R3** Vol de données | G4 / V3 🟥 | **Réduire** | Obligations RGPD et DORA, perte de confiance |
| **R4** Initié malveillant | G3 / V2 🟧 | **Réduire** | Mesures d'hygiène peu coûteuses |

## 3. Plan d'amélioration continue de la sécurité (PACS)

| ID | Mesure | Risques traités | ISO 27001 (Annexe A) | Écart (évaluation) | Responsable | Échéance | Effort |
|---|---|---|---|---|---|---|---|
| **M1** | MFA obligatoire sur tous les comptes (identité, cloud, CI/CD), y compris les externes | R1, R3 | A.8.5 | I-02 | Responsable sécurité | T+1 mois | Faible |
| **M2** | Sauvegardes immuables ou hors ligne, test de restauration chaque trimestre | R1 | A.8.13 | B-01 | CTO | T+2 mois | Moyen |
| **M3** | Suppression des comptes administrateurs permanents, élévation temporaire et journalisée | R1, R4 | A.8.2 | I-03 | CTO | T+3 mois | Moyen |
| **M4** | Détection de secrets dans le pipeline et coffre-fort de secrets | R3 | A.8.25, A.8.28 | D-01 | Lead développement | T+2 mois | Faible |
| **M5** | Clés d'API à portée limitée, liste d'IP, plafonds et détection d'anomalies sur les remboursements | R2 | A.8.16 | O-02 | Lead développement | T+3 mois | Moyen |
| **M6** | Centralisation des journaux et alertes sur les actions sensibles (console cloud, accès base, exports) | R1, R3, R4 | A.8.15, A.8.16 | O-02 | Responsable sécurité | T+4 mois | Élevé |
| **M7** | Revue trimestrielle des accès et procédure arrivée/départ appliquée aux externes | R3, R4 | A.5.15, A.5.18 | I-01 | Responsable sécurité | T+2 mois | Faible |
| **M8** | Registre des prestataires TIC et clauses de sécurité dans les contrats (DORA) | R1, R3 | A.5.19, A.5.20 | S-01 | Responsable conformité | T+6 mois | Moyen |
| **M9** | Sensibilisation à l'hameçonnage, y compris pour les freelances | R1, R3 | A.6.3 | H-01 | Responsable sécurité | T+3 mois | Faible |
| **M10** | Assurance cyber couvrant l'extorsion et l'interruption d'activité | R1 | — | — | Direction | T+6 mois | Moyen |

**Ordre de priorité :** M1 → M4 → M7 → M2 → M3 (gains rapides sur les deux risques inacceptables), puis M5, M6, M8, M9, M10.

## 4. Risques résiduels

| Risque | Avant | Mesures | Après | Commentaire |
|---|---|---|---|---|
| **R1** Rançongiciel | G4 / V3 🟥 | M1, M2, M3, M6, M9, M10 | **G3 / V1** 🟩 | Restauration possible grâce aux sauvegardes testées ; impact financier en partie transféré |
| **R2** Fraude via l'API | G4 / V2 🟧 | M5 | **G3 / V1** 🟩 | Les plafonds limitent la perte maximale |
| **R3** Vol de données | G4 / V3 🟥 | M1, M4, M6, M7, M8 | **G4 / V1** 🟧 | La gravité reste critique (données de paiement) : risque résiduel **accepté par la direction** et suivi |
| **R4** Initié malveillant | G3 / V2 🟧 | M3, M6, M7 | **G3 / V1** 🟩 | Actions sensibles tracées et détectables |

## 5. Suivi

| Indicateur | Cible |
|---|---|
| Comptes avec MFA active | 100 % |
| Tests de restauration réussis | 1 par trimestre |
| Comptes administrateurs permanents | 0 |
| Secrets détectés dans le code | 0 non traité sous 24 h |
| Revues d'accès réalisées | 4 par an |
| Prestataires TIC sous contrat avec clauses de sécurité | 100 % des critiques |

**Révision de l'étude :** cycle opérationnel chaque année (ateliers 4 et 5), cycle stratégique tous les 3 ans (ateliers 1 à 3), et après tout incident majeur.

**Conclusion :** les deux risques inacceptables (R1, R3) descendent en zone tolérable ou acceptable en 6 mois, principalement grâce à 5 mesures peu coûteuses (M1, M2, M3, M4, M7). Le seul risque résiduel critique (R3, gravité G4) est explicitement accepté et suivi par la direction.
