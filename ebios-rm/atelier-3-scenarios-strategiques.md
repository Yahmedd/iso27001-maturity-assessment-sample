# Atelier 3 — Scénarios stratégiques

> **Velmora Payments est une entreprise fictive.** Analyse réalisée à titre d'exemple, selon la méthode EBIOS Risk Manager (ANSSI). Suite de l'[atelier 2](atelier-2-sources-de-risque.md).

**Question de l'atelier :** *par où* les attaquants retenus passeraient-ils : directement, ou en rebondissant sur l'écosystème (prestataires, clients, partenaires) ?

## 1. Cartographie de la menace de l'écosystème

Chaque partie prenante est notée de 1 (faible) à 4 (fort) :
- **Dépendance** : à quel point Velmora a besoin d'elle
- **Pénétration** : à quel point elle a accès au SI de Velmora
- **Maturité cyber** : son niveau de sécurité
- **Confiance** : la confiance qu'on peut lui accorder (contrat, transparence, historique)

**Niveau de menace = (Dépendance × Pénétration) / (Maturité × Confiance)**

Seuils retenus pour cette étude : **≥ 2,5 zone de danger** · 1 à 2,4 zone de contrôle · < 1 zone de veille.

| ID | Partie prenante | Dép. | Pén. | Mat. | Conf. | Menace | Zone |
|---|---|---|---|---|---|---|---|
| **P1** | Hébergeur cloud (IaaS) | 4 | 4 | 4 | 3 | 1,3 | Contrôle |
| **P2** | Fournisseur d'identité et messagerie (SaaS) | 4 | 4 | 4 | 3 | 1,3 | Contrôle |
| **P3** | Prestataire de paiement / acquéreur bancaire | 4 | 2 | 4 | 4 | 0,5 | Veille |
| **P4** | Plateforme de dépôt de code et CI/CD (SaaS) | 3 | 4 | 3 | 3 | 1,3 | Contrôle |
| **P5** | Développeurs freelances externes | 2 | 3 | 2 | 1 | **3,0** | **Danger** |
| **P6** | Commerçants clients connectés par API | 3 | 2 | 1 | 2 | **3,0** | **Danger** |

**Lecture :** les grands fournisseurs (cloud, identité, CI) sont matures mais très intégrés, donc à **contrôler**. Les deux maillons faibles sont les **développeurs externes** (accès au code, peu encadrés) et les **commerçants** (faible maturité, détiennent des clés d'API).

## 2. Scénarios stratégiques

Un scénario stratégique relie un **couple SR/OV** (atelier 2) à un **événement redouté** (atelier 1), en passant éventuellement par une partie prenante.

| ID | Source de risque → objectif | Chemin d'attaque | Événement redouté | Gravité |
|---|---|---|---|---|
| **SS1** | Rançongiciel → rançon | Hameçonnage d'un employé ou d'un freelance (P5), prise de contrôle de son compte via le fournisseur d'identité (P2, MFA non généralisée), accès à la console cloud (P1), chiffrement de la production **et des sauvegardes**, menace de publication des données | ER1 (+ ER2 en double extorsion) | **G4** |
| **SS2** | Fraude → détournement de fonds | Vol de la clé d'API d'un commerçant peu sécurisé (P6), émission de remboursements ou de virements frauduleux via l'API marchands | ER3 | **G4** |
| **SS3** | Revente de données → vol de données | Compromission du poste ou du compte d'un développeur externe (P5), récupération de secrets dans le pipeline CI/CD (P4), accès direct à la base de production | ER2 | **G4** |
| **SS4** | Initié malveillant → vengeance / gain | Un administrateur disposant d'un **accès permanent** (écart I-03) exporte les données ou sabote le code avant son départ ; départ mal géré (procédure arrivée/départ non appliquée) | ER2, ER5 | **G3–G4** |

## 3. Mesures de sécurité sur l'écosystème

| Partie prenante | Mesure | Écart traité (évaluation de maturité) | Menace avant → après |
|---|---|---|---|
| **P5** Développeurs externes | Comptes nominatifs, MFA obligatoire, droits limités au projet, retrait des accès à la fin de mission, clause de sécurité dans le contrat | I-01, I-02, S-01 | 3,0 → **1,0** (maturité 2→3, confiance 1→2) |
| **P6** Commerçants | Clés d'API à portée limitée, rotation, liste d'IP autorisées, plafonds et détection d'anomalies sur les remboursements | O-02 | 3,0 → **1,5** (pénétration 2→1, confiance 2→2) |
| **P2** Fournisseur d'identité | MFA généralisée, accès conditionnel pour les comptes administrateurs | I-02 | 1,3 → 1,0 (confiance 3→4) |
| **P1** Hébergeur cloud | Sauvegardes immuables ou hors ligne, testées chaque trimestre | B-01 | 1,3 (inchangé, impact réduit) |
| **P4** CI/CD | Détection de secrets, coffre-fort de secrets, revue des accès au dépôt | D-01, I-01 | 1,3 → 1,0 (maturité 3→4) |
| Tous | Registre des prestataires TIC et clauses de sécurité (exigence DORA) | S-01 | — |

**Conclusion de l'atelier 3 :** après mesures, plus aucune partie prenante n'est en zone de danger. Les quatre scénarios stratégiques restent pertinents (les mesures réduisent la menace, elles ne l'annulent pas). L'atelier 4 détaillera *techniquement* comment chaque scénario se déroulerait, et sa vraisemblance.
