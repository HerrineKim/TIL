import useInput from '@hooks/useInput';
import { Button, Error, Form, Header, Input, Label, LinkContainer, Success } from '@pages/SignUp/styles';
import fetcher from '@utils/fetcher';
import axios from 'axios';
import React, { useCallback, useState } from 'react';
import { Redirect } from 'react-router-dom';
import useSWR from 'swr';

const SignUp = () => {
  const { data: userData } = useSWR('/api/users', fetcher);
  const [signUpError, setSignUpError] = useState(false);
  const [signUpSuccess, setSignUpSuccess] = useState(false);
  const [mismatchError, setMismatchError] = useState(false);
  const [email, onChangeEmail] = useInput('');
  const [nickname, onChangeNickname] = useInput('');
  const [password, , setPassword] = useInput('');
  const [passwordCheck, , setPasswordCheck] = useInput('');

  // useCallback: 리렌더링을 줄여주기 위한 함수
  // .target.value: 해당 함수 기준으로 외부의 변수일 때만 사용하면 된다.

  const onChangePassword = useCallback(
    (e) => {
      // .target.value: 해당 함수 기준으로 외부의 변수일 때만 사용하면 된다.
      setPassword(e.target.value);
      setMismatchError(passwordCheck !== e.target.value);
    },
    [passwordCheck, setPassword],
  );

  const onChangePasswordCheck = useCallback(
    (e) => {
      // 이 함수들을 캐싱해두어라
      setPasswordCheck(e.target.value);
      setMismatchError(password !== e.target.value);
    },
    // 이 값들 중 하나라도 바뀔 때까지
    [password, setPasswordCheck],
  );

  const onSubmit = useCallback(
    (e) => {
      e.preventDefault();
      if (!nickname || !nickname.trim()) {
        return;
      }
      if (!mismatchError) {
        setSignUpError(false);
        setSignUpSuccess(false);
        axios
          .post('/api/users', { email, nickname, password })
          // 이 주소로 괄호 안 데이터들을 post 요청 보냄
          .then(() => {
            setSignUpSuccess(true);
          })
          .catch((error) => {
            // console.log(error.response?.data);
            setSignUpError(error.response?.data?.code === 403);
          });
      }
    },
    [email, nickname, password, mismatchError],
  );

  if (userData) {
    return <Redirect to="/workspace/sleact" />;
  }

  return (
    <div id="container">
      <Header>Sleact</Header>
      <Form onSubmit={onSubmit}>
        <Label id="email-label">
          <span>이메일 주소</span>
          <div>
            {/* 값들 중 하나가 바뀌었다고 전체를 다시 그리는 것은 아니다. Virtual DOM을 통해 일부만 그려주는 것이 React의 역할 */}
            <Input type="email" id="email" name="email" value={email} onChange={onChangeEmail} />
          </div>
        </Label>
        <Label id="nickname-label">
          <span>닉네임</span>
          <div>
            <Input type="text" id="nickname" name="nickname" value={nickname} onChange={onChangeNickname} />
          </div>
        </Label>
        <Label id="password-label">
          <span>비밀번호</span>
          <div>
            <Input type="password" id="password" name="password" value={password} onChange={onChangePassword} />
          </div>
        </Label>
        <Label id="password-check-label">
          <span>비밀번호 확인</span>
          <div>
            <Input
              type="password"
              id="password-check"
              name="password-check"
              value={passwordCheck}
              onChange={onChangePasswordCheck}
            />
          </div>
          {mismatchError && <Error>비밀번호가 일치하지 않습니다.</Error>}
          {!nickname && <Error>닉네임을 입력해주세요.</Error>}
          {signUpError && <Error>이미 가입된 이메일입니다.</Error>}
          {signUpSuccess && <Success>회원가입되었습니다! 로그인해주세요.</Success>}
        </Label>
        <Button type="submit">회원가입</Button>
      </Form>
      <LinkContainer>
        이미 회원이신가요?&nbsp;
        <a href="/login">로그인 하러가기</a>
      </LinkContainer>
    </div>
  );
};

export default SignUp;
