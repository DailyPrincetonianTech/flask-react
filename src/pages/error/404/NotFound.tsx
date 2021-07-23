import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';

import Grid from '@material-ui/core/Grid';
import { Typography } from '@material-ui/core';
import Logo from '../../../assets/img/logo-white.svg';

import useStyles from './style';

function NotFound(): JSX.Element {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar color="transparent" elevation={0}>
        <Toolbar>
          <img src={Logo} alt="Logo" className={classes.logo} />
        </Toolbar>
      </AppBar>
      <Grid container>
        <Grid className={classes.grid} item xs={12}>
          <Typography variant="h1" className={classes.title}>
            404
          </Typography>
          <Typography variant="h5" className={classes.subtitle}>
            We can&apos;t find what you&apos;re looking for.
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
}

export default NotFound;
