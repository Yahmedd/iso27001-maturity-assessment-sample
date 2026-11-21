# Analyse d'impact sur l'activité (BIA)

> **Velmora Payments est une entreprise fictive.** Exemple réalisé pour un portfolio, selon les principes d'ISO 22301 (continuité d'activité) et les exigences de résilience de DORA. Il s'appuie sur l'[analyse EBIOS RM](../ebios-rm/README.md) (événement redouté ER1 : indisponibilité de la plateforme).

**Question du BIA :** quelles activités sont vitales, combien de temps peuvent-elles s'arrêter, et combien de données peut-on perdre ?

## 1. Définitions

| Terme | Signification |
|---|---|
| **DMIA** (MTPD) | Durée maximale d'interruption admissible avant des conséquences inacceptables |
| **RTO** | Délai visé pour redémarrer l'activité (toujours inférieur à la DMIA) |
| **RPO** | Perte de données maximale admissible (âge de la dernière sauvegarde utilisable) |
| **NMSA** (MBCO) | Niveau minimal de service acceptable pendant la crise |

## 2. Échelle d'impact

| Niveau | Financier | Réglementaire | Image / clients |
|---|---|---|---|
| **1 Faible** | < 10 k€ | Aucun | Quelques réclamations |
| **2 Modéré** | 10–100 k€ | Question de l'autorité | Réclamations nombreuses |
| **3 Grave** | 100 k€–1 M€ | Incident majeur à notifier (DORA, RGPD) | Départ de commerçants, presse spécialisée |
| **4 Critique** | > 1 M€ | Sanction, remise en cause de l'agrément | Perte de confiance durable, presse nationale |

## 3. Impact dans le temps par activité

| ID | Activité | 1 h | 4 h | 24 h | 72 h | 1 semaine |
|---|---|---|---|---|---|---|
| **A1** | Autorisation des paiements (temps réel) | 2 | **3** | 4 | 4 | 4 |
| **A2** | API marchands (création de paiements, remboursements) | 2 | **3** | 4 | 4 | 4 |
| **A3** | Règlement des fonds aux commerçants (versements quotidiens) | 1 | 1 | 2 | **3** | 4 |
| **A4** | Reporting réglementaire et notification des incidents | 1 | 2 | **3** | 4 | 4 |
| **A5** | Support client des commerçants | 1 | 1 | 2 | 2 | **3** |
| **A6** | Développement et déploiement (CI/CD) | 1 | 1 | 1 | 2 | 2 |

## 4. Objectifs de continuité

| ID | Activité | Criticité | DMIA | RTO | RPO | Niveau minimal pendant la crise |
|---|---|---|---|---|---|---|
| **A1** | Autorisation des paiements | Vitale | 4 h | **2 h** | **0** (aucune transaction perdue) | Autorisations acceptées, fonctionnalités annexes coupées |
| **A2** | API marchands | Vitale | 4 h | **2 h** | 5 min | Paiements et remboursements uniquement |
| **A4** | Reporting et notification | Vitale (obligation légale) | 24 h | 4 h | 1 h | Notification possible même sans l'outil (modèles hors ligne) |
| **A3** | Règlement des fonds | Importante | 72 h | 24 h | 0 | Versements traités en lot dès le retour |
| **A5** | Support client | Importante | 1 semaine | 24 h | 24 h | Messagerie et page d'état uniquement |
| **A6** | Développement / déploiement | Non critique | > 1 semaine | 72 h | 24 h | Correctifs urgents seulement |

## 5. Dépendances (biens supports de l'atelier 1 EBIOS)

| Activité | Dépend de | Prestataire critique |
|---|---|---|
| A1, A2 | Plateforme cloud (BS1), API (BS2), fournisseur d'identité (BS3) | Hébergeur cloud, prestataire de paiement |
| A3 | Plateforme (BS1), acquéreur bancaire (BS6) | Acquéreur bancaire |
| A4 | Outil de reporting (BS7), messagerie (BS3) | Fournisseur SaaS |
| A5 | Messagerie (BS3) | Fournisseur SaaS |
| A6 | Dépôt de code et CI/CD (BS4) | Plateforme CI/CD |

## 6. Écarts constatés (voir `assessment.csv`)

| Constat | Écart | Conséquence pour la continuité |
|---|---|---|
| Sauvegardes quotidiennes jamais testées | B-01 | RTO de 2 h **non démontré** : impossible de garantir la reprise |
| Aucun plan de continuité documenté | B-02 | Pas de rôles, pas de procédure de crise |
| Pas de registre des prestataires TIC | S-01 | Dépendances critiques non suivies (exigence DORA) |
| Notification d'incident non formalisée | N-01 | Risque de dépasser les délais réglementaires |

**Conclusion du BIA :** deux activités sont **vitales à 4 h** (autorisation des paiements, API marchands) et exigent un RTO de 2 h. Avec des sauvegardes quotidiennes jamais testées, Velmora ne peut aujourd'hui garantir ni ce RTO ni un RPO nul : c'est l'écart prioritaire du [plan de continuité](pca-plan-continuite.md).
