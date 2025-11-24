# 🌐 Google Fonts WOFF2 Downloader - Version Web

Version web du téléchargeur Google Fonts WOFF2, accessible directement dans votre navigateur.

## ✨ Fonctionnalités

- 🔍 **Recherche de polices** - Recherchez n'importe quelle police Google Fonts par son nom
- 👁️ **Aperçu en temps réel** - Prévisualisez la police avant de télécharger
- 🎯 **Sélection de variantes** - Choisissez exactement les poids et styles dont vous avez besoin
- 📥 **Téléchargement direct** - Téléchargez les fichiers WOFF2 directement dans votre navigateur
- 📱 **Design responsive** - Interface moderne qui fonctionne sur tous les appareils
- ⚡ **Aucune installation** - Tout fonctionne dans le navigateur, pas de dépendances

## 🚀 Déploiement sur GitHub Pages

### Méthode 1 : Depuis l'interface GitHub (Recommandé)

1. **Allez dans les paramètres de votre repository**
   ```
   GitHub → Votre Repository → Settings
   ```

2. **Accédez à la section Pages**
   ```
   Settings → Pages (dans le menu de gauche)
   ```

3. **Configurez la source**
   - **Source** : Deploy from a branch
   - **Branch** : Sélectionnez votre branche (ex: `main` ou `claude/...`)
   - **Folder** : Sélectionnez `/docs`
   - Cliquez sur **Save**

4. **Attendez le déploiement**
   - GitHub va automatiquement construire et déployer votre site
   - Cela prend généralement 1-2 minutes
   - Une fois terminé, l'URL de votre site apparaîtra en haut de la page

5. **Accédez à votre site**
   ```
   https://[votre-username].github.io/Font-downloader/
   ```

### Méthode 2 : En ligne de commande

```bash
# 1. Assurez-vous que vos changements sont committés
git add docs/
git commit -m "Add web version for GitHub Pages"

# 2. Poussez vers GitHub
git push origin main

# 3. Activez GitHub Pages via l'interface GitHub
# (suivez les étapes de la Méthode 1, étapes 2-5)
```

### Méthode 3 : Avec GitHub Actions (Avancé)

Créez `.github/workflows/deploy.yml` :

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Pages
        uses: actions/configure-pages@v3

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: 'docs'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

## 🛠️ Développement local

Pour tester localement avant de déployer :

### Option 1 : Python SimpleHTTPServer

```bash
cd docs
python -m http.server 8000
```

Puis ouvrez : `http://localhost:8000`

### Option 2 : Node.js http-server

```bash
# Installer http-server (une seule fois)
npm install -g http-server

# Lancer le serveur
cd docs
http-server -p 8000
```

### Option 3 : VS Code Live Server

1. Installez l'extension "Live Server" dans VS Code
2. Ouvrez `docs/index.html`
3. Clic droit → "Open with Live Server"

## 📝 Utilisation

1. Ouvrez l'application web
2. Entrez le nom d'une police Google Fonts (ex: "Roboto", "Inter", "Poppins")
3. Cliquez sur "🔍 Rechercher"
4. Prévisualisez la police
5. Sélectionnez les variantes souhaitées
6. Cliquez sur "📥 Télécharger les fichiers WOFF2"

## 🎨 Personnalisation

### Modifier les couleurs

Éditez les variables CSS dans `index.html` (section `<style>`) :

```css
:root {
    --primary-color: #4285f4;      /* Couleur principale */
    --secondary-color: #34a853;    /* Couleur secondaire */
    --background: #f8f9fa;         /* Fond de la page */
    /* ... */
}
```

### Modifier le texte de prévisualisation

Dans `index.html`, ligne ~453 :

```html
<div class="preview-text" id="previewText">
    Votre texte personnalisé ici
</div>
```

## 🔧 Structure des fichiers

```
docs/
├── index.html          # Application complète (HTML + CSS + JS)
└── README.md          # Ce fichier
```

## 🌍 Technologies utilisées

- **HTML5** - Structure
- **CSS3** - Design moderne avec CSS Grid et Flexbox
- **JavaScript ES6+** - Logique et interaction
- **Google Fonts API** - Récupération des polices
- **Fetch API** - Téléchargement des fichiers

## 📱 Compatibilité

- ✅ Chrome / Edge (90+)
- ✅ Firefox (88+)
- ✅ Safari (14+)
- ✅ Opera (76+)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🐛 Dépannage

### Le site ne se charge pas après le déploiement

- Attendez 2-5 minutes après le premier déploiement
- Vérifiez que GitHub Pages est bien activé dans Settings → Pages
- Assurez-vous que le dossier `/docs` contient bien `index.html`
- Videz le cache de votre navigateur (Ctrl+F5 ou Cmd+Shift+R)

### Les polices ne se téléchargent pas

- Vérifiez votre connexion Internet
- Certaines polices peuvent avoir des variantes limitées
- Vérifiez la console du navigateur (F12) pour les erreurs

### La prévisualisation ne fonctionne pas

- Assurez-vous que le nom de la police est correct (sensible à la casse)
- Essayez avec une police populaire (Roboto, Open Sans) pour tester

## 📄 Licence

Ce projet est libre d'utilisation.

## 🔗 Liens utiles

- [Repository GitHub](https://github.com/robindelporte/Font-downloader)
- [Google Fonts](https://fonts.google.com)
- [Documentation GitHub Pages](https://docs.github.com/pages)
