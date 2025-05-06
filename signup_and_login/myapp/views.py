# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password  # 비밀번호 비교를 위한 임포트
from .models import UserProfile
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['username']  # 이메일 필드
        name = request.POST['name']
        student_number = request.POST['student_number']
        password = request.POST['password']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        location = request.POST['location']

        # 비밀번호 확인
        if password != password2:
            return JsonResponse({"error": "비밀번호가 일치하지 않습니다."}, status=400)

        # 이메일 유효성 검사
        if "@" not in email:
            return JsonResponse({"error": "이메일 형식이 올바르지 않습니다."}, status=400)

        # 이미 존재하는 이메일 확인
        if User.objects.filter(username=email).exists():
            # 같은 이메일이 존재하는지 체크
            existing_user = User.objects.get(username=email)
            if check_password(password, existing_user.password):
                return JsonResponse({"error": "같은 아이디와 비밀번호로 이미 가입된 계정이 존재합니다."}, status=400)

            return JsonResponse({"error": "이미 존재하는 이메일입니다."}, status=400)

        # 이미 존재하는 학생 번호 확인
        if User.objects.filter(last_name=student_number).exists():
            return JsonResponse({"error": "이미 존재하는 학생 번호입니다."}, status=400)

        # 이미 존재하는 전화번호 확인
        if UserProfile.objects.filter(phone=phone).exists():
            return JsonResponse({"error": "이미 존재하는 전화번호입니다."}, status=400)

        # 사용자 저장
        try:
            user = User.objects.create_user(username=email, password=password, first_name=name, last_name=student_number)
            
            # UserProfile 객체 생성
            user_profile = UserProfile(user=user, phone=phone, location=location)
            user_profile.save()
            
            # 회원가입 후 바로 로그인 페이지로 리디렉션
            return redirect('login')  # 로그인 페이지 URL을 지정해주세요 (예: 'login' 또는 'login_url')

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, 'signup/signup.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # 이메일 필드
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 후 리디렉션할 페이지 (예: home 페이지)
        else:
            messages.error(request, '잘못된 사용자 이름이나 비밀번호입니다.')
    return render(request, 'login.html')

