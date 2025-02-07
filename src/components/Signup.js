import React, { useState } from 'react';
import { getAuth, createUserWithEmailAndPassword } from 'firebase/auth';
import { useNavigate } from 'react-router-dom';

function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const auth = getAuth();
  const navigate = useNavigate();

  const handleSignup = () => {
    createUserWithEmailAndPassword(auth, email, password)
      .then(() => {
        alert('회원가입이 완료되었습니다!');
        navigate('/'); // 로그인 성공 시 메인 홈으로 이동
      })
      .catch((error) => {
        alert('회원가입 실패: ' + error.message);
      });
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>회원가입</h1>
      <input
        type="email"
        placeholder="이메일"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{ padding: '10px', marginBottom: '10px', display: 'block' }}
      />
      <input
        type="password"
        placeholder="비밀번호"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ padding: '10px', marginBottom: '10px', display: 'block' }}
      />
      <button onClick={handleSignup} style={{ padding: '10px 20px' }}>회원가입</button>
    </div>
  );
}

export default Signup;