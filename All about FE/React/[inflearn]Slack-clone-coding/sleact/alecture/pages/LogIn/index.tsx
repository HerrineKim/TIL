// https://swr.vercel.app/ko
// https://velog.io/@soryeongk/SWRBasic
            // BE가 Cookie를 만들어 FE가 보내주는 부분
            // 위치가 정해져 있다.

          // 사용자 데이터를 얻어오기 위함. 그러나 비효율적이다.
          // mutate를 사용하면 되는데, mutate는 서버에 요청을 다시 보내지 않고서 내용을 수정해준다.
          // revalidate();

          // OPTIMISTIC UI: 내가 보내는 요청이 성공할 것이라고 낙관적 예측한 뒤 예측(true)
          // SWR이 mutate로 제공하는 기능
          // 기본적으로는 PESIMISTIC UI: 서버 요청 후에 결과 확인 후에야 표시
          // false: 서버에 확인하지 않고 프론트에서만 확인/변경

import useInput from '@hooks/useInput';
import { Button, Error, Form, Header, Input, Label, LinkContainer } from '@pages/SignUp/styles';
import fetcher from '@utils/fetcher';
import axios from 'axios';
import React, { useCallback, useState } from 'react';
import { Redirect } from 'react-router-dom';
import useSWR from 'swr';

const LogIn = () => {
  const { data: userData, error, mutate } = useSWR('/api/users', fetcher);
  const [logInError, setLogInError] = useState(false);
  const [email, onChangeEmail] = useInput('');
  const [password, onChangePassword] = useInput('');
  const onSubmit = useCallback(
    (e) => {
      e.preventDefault();
      setLogInError(false);
      axios
        .post(
          '/api/users/login',
          { email, password },
          {
            withCredentials: true,
          },
        )
        .then(() => {
          mutate();
        })
        .catch((error) => {
          setLogInError(error.response?.data?.code === 401);
        });
    },
    [email, password, mutate],
  );

  console.log(error, userData);
  if (!error && userData) {
    // console.log('로그인됨', userData);
    return <Redirect to="/workspace/sleact/channel/일반" />;
  }

  return (
    <div id="container">
      <Header>Sleact</Header>
      <Form onSubmit={onSubmit}>
        <Label id="email-label">
          <span>이메일 주소</span>
          <div>
            <Input type="email" id="email" name="email" value={email} onChange={onChangeEmail} />
          </div>
        </Label>
        <Label id="password-label">
          <span>비밀번호</span>
          <div>
            <Input type="password" id="password" name="password" value={password} onChange={onChangePassword} />
          </div>
          {logInError && <Error>이메일과 비밀번호 조합이 일치하지 않습니다.</Error>}
        </Label>
        <Button type="submit">로그인</Button>
      </Form>
      <LinkContainer>
        아직 회원이 아니신가요?&nbsp;
        <a href="/signup">회원가입 하러가기</a>
      </LinkContainer>
    </div>
  );
};

export default LogIn;
