import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

User = get_user_model()  # ✅ AUTH_USER_MODEL로 설정한 CustomUser 사용

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            name = data.get('name')
            student_number = data.get('student_number')
            password = data.get('password')
            password2 = data.get('password2')
            phone = data.get('phone')
            location = data.get('location')

            # 비밀번호 확인
            if password != password2:
                return JsonResponse({"error": "비밀번호가 일치하지 않습니다."}, status=400)

            # 이메일 유효성 검사
            if "@" not in email:
                return JsonResponse({"error": "이메일 형식이 올바르지 않습니다."}, status=400)

            # 이메일 중복 확인
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "이미 존재하는 이메일입니다."}, status=400)

            # 학생 번호 중복 확인
            if User.objects.filter(student_number=student_number).exists():
                return JsonResponse({"error": "이미 존재하는 학생 번호입니다."}, status=400)

            # 전화번호 중복 확인
            if UserProfile.objects.filter(phone=phone).exists():
                return JsonResponse({"error": "이미 존재하는 전화번호입니다."}, status=400)

            # 사용자 생성 (CustomUser 모델에 맞게 수정)
            user = User.objects.create_user(
                email=email,               # 이메일을 사용자명으로 사용
                username=email,            # username을 email로 설정
                first_name=name,           # 이름을 first_name에 저장
                student_number=student_number,
                password=password
            )

            # 프로필 생성
            UserProfile.objects.create(user=user, phone=phone, location=location)

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': f"서버 오류: {str(e)}"}, status=500)

    return render(request, 'signup.html')




def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']  # 이메일을 username 필드로 쓰고 있음
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            messages.error(request, '잘못된 이메일이나 비밀번호입니다.')
    return render(request, 'login.html')
