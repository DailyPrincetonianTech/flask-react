# Flask / React.js Stack Template

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
pipenv install flask
pipenv install flask_restful
pipenv shell

cd app/http/client
npx create-react-app app --template cra-template-pwa-typescript 

cd app
yarn add react-redux && npm install @types/react-redux  && npm install @reduxjs/toolkit

ncu
ncu -u
npm install
```

### Local Deployment
```bash
cd app/http/client/app && npm run build && cd ../../../.. && pipenv run flask run
```
 
