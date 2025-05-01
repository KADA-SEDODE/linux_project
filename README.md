# 🏙️ Visualisation des Anomalies Urbaines avec *Dans Ma Rue*

## 📌 Introduction

Ce projet vise à **collecter, intégrer et visualiser les anomalies signalées dans l'espace public via cette application _Dans Ma Rue_ de la Ville de Paris que j'ai crée**.  
L'application permet aux citoyens de signaler divers problèmes tels que :
- la propreté
- les graffitis
- les encombrants
- les anomalies liées au mobilier urbain

➡️ Les données couvrent une période de **13 mois glissants**, allant de **J-16 mois à J-3 mois**. Elles sont récupérées via l’API Open Data de la Ville de Paris et utilisées pour produire :
- des **visualisations interactives**
- des **rapports synthétiques** accessibles via une **application web.**

---

## 🛠️ Guide d'installation

1. **Clonez le projet depuis le dépôt GitHub** :

```bash
git clone https://github.com/KADA-SEDODE/linux_project.git
cd linux_project

2.Lancez le script d'installation pour configurer l'environnement (installation des dépendances et préparation de Docker) :
```bash
bash install.sh
Accédez à l'application web via votre navigateur à l'adresse suivante :
👉 http://23.100.8.30:5003

