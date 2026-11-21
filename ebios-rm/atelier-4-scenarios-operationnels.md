# Atelier 4 — Scénarios opérationnels

> **Velmora Payments est une entreprise fictive.** Analyse réalisée à titre d'exemple, selon la méthode EBIOS Risk Manager (ANSSI). Suite de l'[atelier 3](atelier-3-scenarios-strategiques.md).

**Question de l'atelier :** *comment*, techniquement, chaque scénario stratégique se déroulerait-il, et est-il vraisemblable ?

Chaque scénario est découpé en 4 phases : **Connaître** (repérer la cible) → **Rentrer** (obtenir un premier accès) → **Trouver** (se déplacer, repérer les biens) → **Exploiter** (atteindre l'objectif). Les techniques sont référencées dans MITRE ATT&CK.

## Échelle de vraisemblance

| Niveau | Libellé | Signification |
|---|---|---|
| **V1** | Peu vraisemblable | L'attaquant a peu de chances de réussir |
| **V2** | Vraisemblable | Réussite possible avec des moyens significatifs |
| **V3** | Très vraisemblable | Réussite probable, les défenses actuelles l'arrêtent mal |
| **V4** | Quasi certain | Réussite quasi certaine, aucune défense efficace |

## SO1 — Rançongiciel (issu de SS1)

| Phase | Action de l'attaquant | Technique ATT&CK | Ce qui la facilite aujourd'hui |
|---|---|---|---|
| Connaître | Repère les développeurs et freelances sur LinkedIn et GitHub | T1589 (informations sur les identités) | Équipe visible en ligne |
| Rentrer | Hameçonnage d'un freelance, vol de ses identifiants | T1566 (hameçonnage) | Pas de formation pour les externes (H-01) |
| Rentrer | Connexion avec le compte volé | T1078 (comptes valides) | **MFA non généralisée** (I-02) |
| Trouver | Exploration de la console cloud, repérage des sauvegardes | T1580 (découverte de l'infrastructure cloud) | Droits trop larges, journaux non surveillés (O-02) |
| Exploiter | Suppression des sauvegardes puis chiffrement de la production, vol de données pour double extorsion | T1490, T1486, T1567 | **Sauvegardes jamais restaurées en test** (B-01) |

**Vraisemblance : V3 (très vraisemblable)** — chaque étape est facile tant que la MFA n'est pas généralisée et que les sauvegardes ne sont pas isolées.

## SO2 — Fraude via l'API marchands (issu de SS2)

| Phase | Action de l'attaquant | Technique ATT&CK | Ce qui la facilite aujourd'hui |
|---|---|---|---|
| Connaître | Lit la documentation publique de l'API, repère les commerçants intégrés | T1593 (recherche sur sites publics) | Documentation publique (normal) |
| Rentrer | Récupère une clé d'API exposée dans le code ou le serveur d'un commerçant | T1552 (identifiants non protégés) | Clés à portée trop large, sans liste d'IP |
| Trouver | Teste les appels de remboursement et de virement | — | Pas de plafond par clé |
| Exploiter | Émet des remboursements frauduleux vers ses propres comptes | — | **Pas de détection d'anomalies** (O-02) |

**Vraisemblance : V2 (vraisemblable)** — il faut tomber sur un commerçant peu sécurisé, mais une fois la clé obtenue, rien ne bloque la fraude.

## SO3 — Vol de données via un développeur (issu de SS3)

| Phase | Action de l'attaquant | Technique ATT&CK | Ce qui la facilite aujourd'hui |
|---|---|---|---|
| Connaître | Repère les développeurs externes et le dépôt de code | T1589 | Contributeurs visibles |
| Rentrer | Logiciel malveillant ou vol de jeton sur le poste d'un développeur | T1528 (vol de jeton d'accès) | Postes externes non maîtrisés |
| Trouver | Récupère des secrets dans le dépôt ou les variables du pipeline | T1552 | **Pas de détection de secrets** (D-01) |
| Exploiter | Accès direct à la base de production et exfiltration | T1567 | Pas d'alerte sur les accès inhabituels (O-02) |

**Vraisemblance : V3 (très vraisemblable)** — l'absence de détection de secrets rend le chemin court.

## SO4 — Initié malveillant (issu de SS4)

| Phase | Action de l'attaquant | Technique ATT&CK | Ce qui la facilite aujourd'hui |
|---|---|---|---|
| Connaître / Rentrer | Déjà à l'intérieur, avec des droits administrateur | T1078 | **Comptes administrateurs permanents** (I-03) |
| Trouver | Connaît les systèmes et les données | — | — |
| Exploiter | Exporte les données ou insère du code malveillant avant son départ | T1567, T1195 (compromission de la chaîne logicielle) | Pas de revue des accès (I-01), changements d'infrastructure non suivis (O-03) |

**Vraisemblance : V2 (vraisemblable)** — l'intention est rare, mais rien ne l'empêcherait ni ne la détecterait.

## Synthèse des risques (entrée de l'atelier 5)

| Risque | Scénario | Événement redouté | Gravité | Vraisemblance |
|---|---|---|---|---|
| **R1** | Rançongiciel | ER1 (+ ER2) | G4 | **V3** |
| **R2** | Fraude via l'API | ER3 | G4 | V2 |
| **R3** | Vol de données via développeur | ER2 | G4 | **V3** |
| **R4** | Initié malveillant | ER2, ER5 | G3 | V2 |

**Conclusion de l'atelier 4 :** deux risques sont à la fois **critiques et très vraisemblables** (R1 rançongiciel, R3 vol de données). Ils partagent les mêmes causes : MFA incomplète, secrets non protégés, sauvegardes non testées et absence de surveillance. L'atelier 5 transformera ces constats en plan de traitement.
