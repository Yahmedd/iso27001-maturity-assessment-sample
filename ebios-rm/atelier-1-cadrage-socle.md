# Atelier 1 — Cadrage et socle de sécurité

> **Velmora Payments est une entreprise fictive.** Analyse réalisée à titre d'exemple, selon la méthode EBIOS Risk Manager (ANSSI). Elle prolonge l'évaluation de maturité du même dépôt.

## 1. Cadrage de l'étude

| Élément | Contenu |
|---|---|
| **Organisation** | Velmora Payments, fintech de paiement, 120 personnes |
| **Objectif de l'étude** | Identifier les risques majeurs pesant sur la plateforme de paiement et construire le plan de traitement, en préparation de la certification ISO 27001 et de la conformité DORA |
| **Périmètre** | Plateforme de paiement en ligne pour les commerçants : traitement des transactions, API marchands, données clients, reporting réglementaire |
| **Hors périmètre** | Activités marketing et RH (traitées dans une étude ultérieure) |
| **Participants (fictifs)** | Direction générale, CTO, responsable sécurité, responsable conformité, lead développement, responsable support |
| **Cycle** | Stratégique : 3 ans · Opérationnel : 1 an |

## 2. Valeurs métier (ce qu'on veut protéger)

| ID | Valeur métier | Description | Responsable |
|---|---|---|---|
| **VM1** | Traitement des paiements | Autorisation et exécution des transactions des commerçants | CTO |
| **VM2** | Données clients et de paiement | Données des commerçants, des porteurs et historique des transactions | Responsable conformité |
| **VM3** | Reporting réglementaire | Déclarations à l'autorité, notification des incidents majeurs (DORA) | Responsable conformité |
| **VM4** | Plateforme logicielle | Code source, pipeline CI/CD, configurations | Lead développement |

## 3. Biens supports (sur quoi reposent les valeurs métier)

| ID | Bien support | VM concernées | Gestion |
|---|---|---|---|
| BS1 | Plateforme de paiement hébergée dans le cloud (conteneurs, base de données) | VM1, VM2 | Interne + hébergeur cloud |
| BS2 | API marchands | VM1, VM2 | Interne |
| BS3 | Fournisseur d'identité et messagerie (SaaS) | VM1–VM4 | Prestataire SaaS |
| BS4 | Dépôt de code et pipeline CI/CD | VM4 | Interne + prestataire SaaS |
| BS5 | Postes de travail des développeurs et administrateurs | VM2, VM4 | Interne |
| BS6 | Prestataire de paiement / acquéreur bancaire | VM1 | Prestataire |
| BS7 | Outil de reporting et de gestion des incidents | VM3 | Interne |

## 4. Événements redoutés et gravité

### Échelle de gravité

| Niveau | Libellé | Signification |
|---|---|---|
| **G1** | Mineure | Impact limité, sans conséquence durable |
| **G2** | Significative | Perturbation visible, gérable en interne |
| **G3** | Grave | Perte financière ou atteinte à l'image importante, sanction possible |
| **G4** | Critique | Menace la survie de l'activité ou l'agrément |

### Événements redoutés

| ID | Valeur métier | Événement redouté | Impacts | Gravité |
|---|---|---|---|---|
| **ER1** | VM1 | Indisponibilité de la plateforme de paiement pendant plus de 4 heures | Perte de chiffre d'affaires des commerçants, pénalités contractuelles, incident majeur DORA | **G4** |
| **ER2** | VM2 | Fuite des données clients et de paiement | Violation de données (RGPD, 72 h), sanctions, perte de confiance | **G4** |
| **ER3** | VM1 | Altération ou détournement de transactions (fraude) | Pertes financières directes, responsabilité vis-à-vis des commerçants | **G4** |
| **ER4** | VM3 | Notification d'incident majeur hors délai ou erronée | Sanction de l'autorité, perte de confiance du régulateur | **G3** |
| **ER5** | VM4 | Vol ou altération du code source / injection de code dans le pipeline | Porte dérobée en production, perte de propriété intellectuelle | **G3** |

## 5. Socle de sécurité

| Référentiel | Type | État d'application | Principaux écarts (voir `assessment.csv`) |
|---|---|---|---|
| **ISO/IEC 27001:2022** | Cible de certification | Partiel | Pas de déclaration d'applicabilité ni de plan de traitement (R-02), politique non approuvée (G-01), revues d'accès absentes (I-01) |
| **DORA** | Obligation réglementaire | Partiel | Pas de registre des prestataires TIC (S-01), pas de procédure de classification et de notification des incidents (N-01), plan de continuité absent (B-02) |
| **RGPD** | Obligation légale | Partiel | Classification des données absente (A-02) |
| **Règles d'hygiène internes** | Bonnes pratiques | Partiel | MFA non généralisée (I-02), comptes administrateurs permanents (I-03), restaurations jamais testées (B-01) |

**Conclusion de l'atelier 1 :** trois événements redoutés sont **critiques (G4)** et concernent le cœur de métier (disponibilité, données, intégrité des paiements). Les écarts du socle les plus liés à ces événements (MFA, accès à privilèges, sauvegardes, prestataires, incidents) seront repris dans l'atelier 5.
