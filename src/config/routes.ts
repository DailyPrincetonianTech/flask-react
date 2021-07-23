import CounterView from '../pages/counter/CounterView';
import NotFound from '../pages/error/404/NotFound';

const routes: Array<{
  path: string;
  exact: boolean;
  component: () => JSX.Element;
}> = [
  { path: '/', exact: true, component: CounterView },
  { path: '', exact: true, component: NotFound },
];

export default routes;
