from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 닉네임
        email = request.POST.get('email')
        name = request.POST.get('name')
        student_number = request.POST.get('student_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        location = request.POST.get('location')

        if password != password2:
            return JsonResponse({"error": "비밀번호가 일치하지 않습니다."}, status=400)

        if "@" not in email:
            return JsonResponse({"error": "이메일 형식이 올바르지 않습니다."}, status=400)

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"error": "이미 존재하는 이메일입니다."}, status=400)

        if CustomUser.objects.filter(phone=phone).exists():
            return JsonResponse({"error": "이미 등록된 전화번호입니다."}, status=400)

        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({"error": "이미 존재하는 닉네임입니다."}, status=400)

        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name,
                last_name=student_number,
                phone=phone,
                location=location
            )
        except Exception as e:
            return JsonResponse({"error": f"회원가입 실패: {str(e)}"}, status=500)

        return redirect('login')

    return render(request, 'signup/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, '로그인 정보가 올바르지 않습니다.')

    return render(request, 'login.html')

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')
