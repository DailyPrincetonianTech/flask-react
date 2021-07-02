import { Route, Switch } from "react-router-dom";
import routes from "./config/routes";

import './App.css';
import theme from "./config/themes";
import { ThemeProvider } from "@material-ui/core/styles";
import CssBaseline from '@material-ui/core/CssBaseline';

function App() {
  console.log(routes);
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Switch>
        {routes.map((route, index) =>
          <Route
            key={index}
            path={route.path}
            exact={route.exact}
            component={route.component}
          />
        )}
      </Switch>
    </ThemeProvider>
  );
}

export default App;
