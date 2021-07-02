// .App {
//     text-align: center;
// }

// .App-logo {
//     height: 40vmin;
//     pointer-events: none;
// }

// @media (prefers-reduced-motion: no-preference) {
//     .App-logo {
//         animation: App-logo-float infinite 3s ease-in-out;
//     }
// }

// .App-header {
//     min-height: 100vh;
//     display: flex;
//     flex-direction: column;
//     align-items: center;
//     justify-content: center;
//     font-size: calc(10px + 2vmin);
// }

// .App-link {
//     color: rgb(112, 76, 182);
// }

// @keyframes App-logo-float {
//     0% {
//         transform: translateY(0);
//     }

//     50% {
//         transform: translateY(10px);
//     }

//     100% {
//         transform: translateY(0px);
//     }
// }

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