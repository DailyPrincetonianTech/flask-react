import CounterView from "../pages/counter/CounterView";

const routes: Array<{path: string; exact: boolean; component: () => JSX.Element;}> = [
    { path: "/", exact: true, component: CounterView }
];

export default routes;