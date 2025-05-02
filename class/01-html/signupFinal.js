function changePhone1(){
    const phone1 = document.getElementById("phone1").value
    if(phone1.length === 3) {
        document.getElementById("phone2").focus()
    }
}

function changePhone2(){
    const phone2 = document.getElementById("phone2").value
    if(phone2.length === 4) {
        document.getElementById("phone3").focus()
    }
}

function changePhone3(){
    const phone1 = document.getElementById("phone1").value
    const phone2 = document.getElementById("phone2").value
    const phone3 = document.getElementById("phone3").value
    if(phone1.length === 3 && phone2.length === 4 && phone3.length === 4){
        document.getElementById("token__button").style = "background-color: #FFFFFF; color: #0068FF; cursor: pointer;"
        document.getElementById("token__button").removeAttribute("disabled")
    }

}

function getToken(){
    const token = String(Math.floor(Math.random() * 1000000)).padStart(6, "0")
    document.getElementById("token").innerText = token

    document.getElementById("token__button").style = "background-color: #FFFFFF; cursor: default;"
    document.getElementById("token__button").setAttribute("disabled", "true")
    document.getElementById("token__timer__confirm__button").style="background-color: #0068FF; color: #FFFFFF; cursor: pointer;"
    document.getElementById("token__timer__confirm__button").removeAttribute("disabled")
    getTokenTimer()
}

let interval;
function getTokenTimer(){
    let timer = 10
    interval = setInterval(() => {
        if(timer >= 0){
            const minutes = Math.floor(timer / 60)
            const seconds = timer % 60

            document.getElementById("token__timer").innerText = minutes + ":" + String(seconds).padStart(2, "0")
            timer -= 1
        } else {
            document.getElementById("token").innerText = "000000"
            document.getElementById("token__button").style = ""
            document.getElementById("token__button").setAttribute("disabled", "true")

            document.getElementById("token__timer").innerText = "3:00"
            document.getElementById("token__timer__confirm__button").style = ""
            document.getElementById("token__timer__confirm__button").setAttribute("disabled", "true")

            clearInterval(interval)
        }
    }, 1000)
}

function getTokenTimerConfirm(){
    clearInterval(interval)
    document.getElementById("token__timer__confirm__button").style = "background-color: #FFFFFF; cursor: default;"
    document.getElementById("token__timer__confirm__button").setAttribute("disabled", "true")
    document.getElementById("token__timer__confirm__button").innerText = "인증완료"
    alert("인증이 완료되었습니다.")

    // document.getElementById("signup__button").style = "background-color: rgb(255,215,0); color: rgb(0, 0, 0);cursor: pointer;"
    document.getElementById("signup__button").removeAttribute("disabled")
    document.getElementById("signup__button").classList.add('authorized_state')
}

function signup(){
    const my_id = document.getElementById("my_id").value
    const writer = document.getElementById("writer").value
    const student_number = document.getElementById("student_number").value
    const password1 = document.getElementById("password1").value
    const password2 = document.getElementById("password2").value
    const location = document.getElementById("location").value
    
    let isValid = true
    if(my_id.includes("@") === false) {
        document.getElementById("error__my_id").innerText = "이메일이 올바르지 않습니다."
        isValid = false
    } else {
        document.getElementById("error__my_id").innerText = ""
    }

    if(writer === "") {
        document.getElementById("error__writer").innerText = "이름이 올바르지 않습니다."
        isValid = false
    } else {
        document.getElementById("error__writer").innerText = ""
    }
    if(student_number === ""){
        document.getElementById("error__student_number").innerText = "학번이 올바르지 않습니다."
    } else{
        document.getElementById("error__student_number").innerText = ""
    }

    if(password1 === ""){
        document.getElementById("error__password1").innerText = "비밀번호를 입력해 주세요."
        isValid = false
    } else {
        document.getElementById("error__password1").innerText = ""
    }

    if(password2 === ""){
        document.getElementById("error__password2").innerText = "비밀번호를 입력해 주세요."
        isValid = false
    } else {
        document.getElementById("error__password2").innerText = ""
    }

    if(password1 !== password2) {
        document.getElementById("error__password1").innerText = "비밀번호가 일치하지 않습니다."
        document.getElementById("error__password2").innerText = "비밀번호가 일치하지 않습니다."
        isValid = false
    }

    if(location !== "서울" && location !== "경기" && location !== "인천"){
        document.getElementById("error__location").innerText = "지역을 선택해 주세요."
        isValid = false
    } else {
        document.getElementById("error__location").innerText = ""
    }

    if(isValid === true){
        alert("가입을 축하합니다.")
    }
}
