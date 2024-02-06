

# Comptage du nombre d'étudiants dont l'âge est compris entre 18 et 25 ans présents en base de données

SELECT COUNT(*) AS nombre_etudiants_age_entre_18_et_25 FROM etudiant WHERE age >= 18 AND age <= 25;
