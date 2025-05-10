document.addEventListener("DOMContentLoaded", () => {
    const inputs = Array.from(document.querySelectorAll(".inputbox, .phoneNum"));
    const tokenButton = document.getElementById("token__button");
    const tokenDiv = document.getElementById("token");
    const confirmButton = document.getElementById("token__timer__confirm__button");
    const signupButton = document.getElementById("signup__button");

    // 엔터 누르면 다음 입력란으로 포커스
    inputs.forEach((input, index) => {
        input.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault();
                if (index < inputs.length - 1) {
                    inputs[index + 1].focus();
                } else {
                    signupButton.focus();
                }
            }
        });
    });

    // 전화번호 입력 시 인증번호 전송 버튼 활성화
    inputs.slice(-3).forEach(input => {
        input.addEventListener("input", () => {
            const phone1 = document.getElementById("phone1").value;
            const phone2 = document.getElementById("phone2").value;
            const phone3 = document.getElementById("phone3").value;
            if (phone1 && phone2 && phone3) {
                tokenButton.disabled = false;
            } else {
                tokenButton.disabled = true;
            }
        });
    });

    // 인증번호 전송
    window.getToken = () => {
        const token = Math.floor(100000 + Math.random() * 900000).toString();
        tokenDiv.innerText = token;
        confirmButton.disabled = false;
        alert(`인증번호가 발송되었습니다: ${token}`);
    };

    // 인증번호 확인 (즉시 성공)
    window.getTokenTimerConfirm = () => {
        alert("인증이 완료되었습니다.");
        signupButton.disabled = false;
    };

    // 회원가입
    window.signup = () => {
        const my_id = document.getElementById("my_id").value;
        const writer = document.getElementById("writer").value;
        const student_number = document.getElementById("student_number").value;
        const password1 = document.getElementById("password1").value;
        const password2 = document.getElementById("password2").value;
        const phone1 = document.getElementById("phone1").value;
        const phone2 = document.getElementById("phone2").value;
        const phone3 = document.getElementById("phone3").value;
        const location = document.getElementById("location").value;

        let isValid = true;

        // 이메일 검증
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        document.getElementById("error__my_id").innerText = emailPattern.test(my_id) ? "" : "올바른 이메일 형식이 아닙니다.";
        isValid = isValid && emailPattern.test(my_id);

        // 이름
        document.getElementById("error__writer").innerText = writer ? "" : "이름을 입력해 주세요.";
        isValid = isValid && !!writer;

        // 학번
        document.getElementById("error__student_number").innerText = student_number ? "" : "학번을 입력해 주세요.";
        isValid = isValid && !!student_number;

        // 비밀번호
        document.getElementById("error__password1").innerText = password1 ? "" : "비밀번호를 입력해 주세요.";
        document.getElementById("error__password2").innerText = password2 ? "" : "비밀번호 확인을 입력해 주세요.";
        isValid = isValid && !!password1 && !!password2;

        // 비밀번호 일치
        if (password1 && password2 && password1 !== password2) {
            document.getElementById("error__password1").innerText = "비밀번호가 일치하지 않습니다.";
            document.getElementById("error__password2").innerText = "비밀번호가 일치하지 않습니다.";
            isValid = false;
        }

        // 전화번호
        if (!(phone1 && phone2 && phone3)) {
            alert("전화번호를 모두 입력해 주세요.");
            isValid = false;
        }

        // 지역
        document.getElementById("error__location").innerText = location === "지역을 선택하세요." ? "지역을 선택해 주세요." : "";
        isValid = isValid && location !== "지역을 선택하세요.";

        if (isValid) {
            fetch("/signup/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")  // CSRF 토큰 포함
                },
                body: JSON.stringify({
                    email: my_id,
                    name: writer,
                    student_number: student_number,
                    password: password1,
                    password2: password2,
                    phone: `${phone1}-${phone2}-${phone3}`,
                    location: location
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("가입을 축하합니다!");
                } else {
                    alert("가입에 실패했습니다: " + (data.error || "알 수 없는 오류"));
                }
            })
            .catch(error => {
                alert("서버와 통신 중 오류가 발생했습니다.");
                console.error("Error:", error);
            });
        }
    };

    // CSRF 토큰 가져오기
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
