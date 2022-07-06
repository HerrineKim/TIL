// 커스텀 훅: 리액트에서 제공하는 훅들을 합쳐 만든다.
// any 보다는 generic을 사용하는 것을 권장한다.
import { Dispatch, SetStateAction, useCallback, useState } from 'react';

type Handler = (e: any) => void;
type ReturnTypes<T = any> = [T, Handler, Dispatch<SetStateAction<T>>];
const useInput = <T = any>(initialValue: T): ReturnTypes<T> => {
  const [value, setValue] = useState(initialValue);
  const handler = useCallback((e) => {
    setValue(e.target.value);
  }, []);
  return [value, handler, setValue];
};

export default useInput;
