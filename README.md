# Flask / React.js Stack Template

This template implements a Flask backend that serves a PWA TypeScript React.js application client-side, equipped with routing behavior, state management via Redux, and Material UI. 

### Setup Dependencies
```bash
brew update

brew install pyenv
pyenv install $(pyenv install --list | grep -v - | grep -v b | tail -1)
pyenv global $(pyenv install --list | grep -v - | grep -v b | tail -1)

brew install pipenv
pip install --user pipenv

pip install black

npm install -g npm-check-updates
```

### Environment Setup
```bash
pipenv install
```

### Local Development
Refer to package.json for the list of scripts.

