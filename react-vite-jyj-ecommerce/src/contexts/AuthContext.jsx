import { loginUser } from '@/api/AuthApi';
import { createContext, useContext, useState } from 'react';

//dev_5_Fruit
const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState(localStorage.getItem('access'));

  const login = async (username, password) => {
    try {
      const response = await loginUser(username, password);
      const { access, refresh } = response.data;

      //저장 영역은 크게 4 가지 정도 있음
      //1.local storage 2.session storage 3.cookie
      localStorage.setItem('access', access);
      localStorage.setItem('refresh', refresh);
      setAccessToken(access);

      //로그인이 된후 로그인 정보를 받아서 어디서든 로그인 정보를 공유 할수 있게 함
      //await getUser()
    } catch (error) {
      console.error('로그인 실패', error);
      throw error;
    }
  };

  const value = {
    login,
    accessToken,
    user,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
