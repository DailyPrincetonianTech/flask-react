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
```

### Environment Setup
```bash
pipenv install flask flask_restful
pipenv shell

cd app/http/client
npx create-react-app app --template cra-template-pwa-typescript 

cd app
yarn add react-redux @types/react-redux @reduxjs/toolkit 
yarn add react-router-dom @types/react-router-dom 
yarn add @material-ui/core

ncu -u && yarn install
```

### Local Deployment
```bash
cd app/http/client/app && yarn build && cd ../../../.. && pipenv run flask run
```
 
