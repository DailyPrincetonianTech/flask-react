import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  root: {
    flexGrow: 1,
    background: 'linear-gradient(45deg, #29d9ff, #0f8fff)',
    backgroundSize: '400% 400%',
    animation: '$gradient 30s ease infinite',
  },
  logo: {
    height: 50,
    marginTop: '25px',
  },
  grid: {
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    margin: '0 30px',
  },
  '@keyframes gradient': {
    '0%': { backgroundPosition: '0% 50%' },
    '50%': { backgroundPosition: '100% 50%' },
    '100%': { backgroundPosition: '0% 50%' },
  },
  title: {
    fontFamily: 'Poppins',
    fontWeight: 500,
    fontSize: '200px',
  },
  subtitle: {
    textAlign: 'left',
    color: 'rgba(255, 255, 255, 0.8)',
    fontSize: '30px',
    fontWeight: 300,
  },
}));

export default useStyles;
