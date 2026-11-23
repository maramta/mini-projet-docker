# Application Flask conteneurisée

Petite application web Flask qui affiche un message d'accueil configurable.
Mini-projet 1 – Docker (ISET Tozeur).

## Image Docker Hub

Image : `taweli/app`

| Tag | Description |
|---|---|
| `1.0.1` | Dernière version |
| `1.0.0` | Première version |
| `1.0` | Alias mobile : pointe toujours sur la dernière version 1.0.x |

## Lancer l'application (à partir de l'image publiée)

```bash
docker run -d --name mon-app \
  -p 8081:5000 \
  -e MESSAGE_ACCUEIL="Salut les DevOps" \
  --memory 256m --cpus 0.5 \
  taweli/app:1.0.1
```

Vérifier :

```bash
curl http://localhost:8081
docker logs mon-app
```

Arrêter et supprimer :

```bash
docker rm -f mon-app
```

## Variables d'environnement

| Variable | Valeur par défaut | Rôle |
|---|---|---|
| `MESSAGE_ACCUEIL` | `Bonjour depuis mon conteneur !` | Message renvoyé par la page d'accueil |

Sans `-e`, la valeur par défaut est utilisée.

## Port

L'application écoute sur le port `5000` dans le conteneur. L'exemple
ci-dessus le publie sur le port `8081` de l'hôte.

## Construire l'image soi-même

```bash
git clone <URL_DU_DEPOT>
cd mini-projet-docker
docker build -t taweli/app:1.0.1 .
```

## Auteurs

Tawel Maram
