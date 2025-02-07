import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';  // Home 전용 CSS 파일 연결

function Home() {
  const navigate = useNavigate();

  return (
    <div className="container">
      {/* 오른쪽 상단 로그인 버튼 */}
      <div className="top-bar">
        <button className="login-button" onClick={() => navigate('/login')}>
          로그인
        </button>
      </div>

      {/* 왼쪽 섹션 */}
      <div className="left-section">
        <h1>withpaw🐾</h1>
        <p>반려동물을위한 훈련 보조 어플리케이션!</p>
        <button className="primary-button">다운로드</button>
      </div>

      {/* 오른쪽 섹션 */}
      <div className="right-section">
        <img
          src="https://example.com/dog-image.jpg"  // 실제 이미지 경로로 변경
          alt="강아지 훈련 이미지"
        />
      </div>
    </div>
  );
}

export default Home;