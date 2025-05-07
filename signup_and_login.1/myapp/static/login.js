const enableBtn = () => {
    const inputId = document.getElementById("input__id");
    const inputPassword = document.getElementById("input__password");
    const loginBtn = document.getElementById("loginBtn");

    // 입력값이 모두 채워지면 로그인 버튼 활성화
    if (inputId.value.length > 0 && inputPassword.value.length > 0) {
        loginBtn.disabled = false;
    } else {
        loginBtn.disabled = true;
    }
};

// 아이디, 비밀번호 입력 시 이벤트 리스너로 활성화/비활성화 처리
document.getElementById("input__id").addEventListener("input", enableBtn);
document.getElementById("input__password").addEventListener("input", enableBtn);
