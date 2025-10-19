import loadable from '@loadable/component';
import React from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';

// 코드 분할: https://ko.reactjs.org/docs/code-splitting.html
const Workspace = loadable(() => import('@layouts/Workspace'));
const LogIn = loadable(() => import('@pages/LogIn'));
const SignUp = loadable(() => import('@pages/SignUp'));

const App = () => (
  <Switch>
    <Route exact path="/">
      <Redirect to="/login" />
    </Route>
    <Route path="/login" component={LogIn} />
    <Route path="/signup" component={SignUp} />
    {/* 워크스페이스 이름을 주소에 넣어주기 */}
    <Route path="/workspace/:workspace" component={Workspace} />
  </Switch>
);

export default App;
