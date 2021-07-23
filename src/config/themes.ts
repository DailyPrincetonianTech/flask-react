import { createTheme } from '@material-ui/core/styles';

declare module '@material-ui/core/styles/createTheme' {
  interface Theme {
    customPalette: {
    }
  }
  interface ThemeOptions {
    customPalette?: {
    }
  }
}

const theme = createTheme({
  palette: {
    type: 'dark',
  },
  customPalette: {
  },
});

export default theme;
