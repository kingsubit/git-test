const enableBtn = () => {
    const inputId = document.getElementById("input__id");
    const inputPassword = document.getElementById("input__password");
    const loginBtn = document.getElementById("loginBtn");

    if (inputId.value.length > 0 && inputPassword.value.length > 0) {
        loginBtn.disabled = false;
    } else {
        loginBtn.disabled = true;
    }
};

document.getElementById("input__id").addEventListener("input", enableBtn);
document.getElementById("input__password").addEventListener("input", enableBtn);