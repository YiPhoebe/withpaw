// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBxXas8jDPa2glEHicWEEtqAoVt4nrv2ec",
  authDomain: "withpaw-fa199.firebaseapp.com",
  projectId: "withpaw-fa199",
  storageBucket: "withpaw-fa199.firebasestorage.app",
  messagingSenderId: "1070314398231",
  appId: "1:1070314398231:web:5748e6013c53a4a14c7252"
};

// Firebase 앱 초기화
const app = initializeApp(firebaseConfig);

// 인증 객체 가져오기
const auth = getAuth(app);

// 인증 객체 내보내기
export { auth };