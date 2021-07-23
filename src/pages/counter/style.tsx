import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  app: {
    textAlign: 'center',
  },
  appLogo: {
    height: '40vmin',
    animation: `$appLogoFloat infinite 3s ease-in-out`,
    pointerEvents: 'none',
  },
  appHeader: {
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'calc(10px + 2vmin)',
  },
  appLink: {
    color: 'rgb(112, 76, 182)',
  },
  "@keyframes appLogoFloat": {
    "0%": { transform: 'translateY(0)'},
    "50%": { transform: 'translateY(10px)'},
    "100%": { transform: 'translateY(0px)'},
  }
}));

export default useStyles;