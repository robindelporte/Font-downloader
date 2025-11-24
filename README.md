# Google Fonts WOFF2 Downloader

Un outil simple pour télécharger des polices Google Fonts au format WOFF2.

## 🚀 Installation

Ce script utilise uniquement la bibliothèque standard Python (Python 3.6+). Aucune dépendance externe requise !

```bash
# Cloner le repository
git clone <votre-repo-url>
cd Font-downloader

# Rendre le script exécutable (Linux/Mac)
chmod +x font_downloader.py
```

## 📖 Utilisation

### Syntaxe de base

```bash
python font_downloader.py "NOM_DE_LA_POLICE" [-o DOSSIER_DE_SORTIE]
```

### Exemples

**1. Télécharger une police par son nom :**
```bash
python font_downloader.py "Roboto"
```

**2. Télécharger depuis une URL Google Fonts (specimen) :**
```bash
python font_downloader.py "https://fonts.google.com/specimen/Roboto"
```

**3. Télécharger depuis une URL CSS Google Fonts :**
```bash
python font_downloader.py "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700"
```

**4. Spécifier un dossier de sortie personnalisé :**
```bash
python font_downloader.py "Open Sans" -o mes-polices
```

**5. Télécharger une police avec des espaces dans le nom :**
```bash
python font_downloader.py "Playfair Display"
```

## 📁 Structure des fichiers

Par défaut, les polices sont téléchargées dans le dossier `fonts/` :

```
Font-downloader/
├── font_downloader.py
├── fonts/              # Dossier créé automatiquement
│   ├── font-file-1.woff2
│   ├── font-file-2.woff2
│   └── ...
└── README.md
```

## 🎯 Fonctionnalités

- ✅ Télécharge automatiquement toutes les variantes disponibles (poids et styles)
- ✅ Format WOFF2 optimisé pour le web
- ✅ Support des noms de police avec espaces
- ✅ Support des URL Google Fonts (specimen et CSS)
- ✅ Évite les téléchargements en double
- ✅ Interface en ligne de commande simple
- ✅ Aucune dépendance externe

## 🔧 Options

```
positional arguments:
  font                  URL Google Fonts ou nom de la famille de police

optional arguments:
  -h, --help            Afficher l'aide
  -o OUTPUT, --output OUTPUT
                        Dossier de sortie pour les polices (défaut: fonts)
```

## 💡 Notes

- Le script télécharge automatiquement tous les poids disponibles (100-900) et styles (normal, italic)
- Les fichiers sont nommés automatiquement selon leur source Google Fonts
- Les fichiers existants ne sont pas re-téléchargés
- Nécessite une connexion Internet pour accéder à Google Fonts

## ⚠️ Dépannage

**Erreur 403 Forbidden :**
- Vérifiez votre connexion Internet
- Certains réseaux d'entreprise ou proxies peuvent bloquer l'accès à Google Fonts
- Si vous êtes derrière un proxy, configurez les variables d'environnement HTTP_PROXY et HTTPS_PROXY

## 📝 Licence

Ce projet est libre d'utilisation.