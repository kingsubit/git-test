

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from django.core.exceptions import ValidationError

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
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
        if "@" not in username:
            return JsonResponse({"error": "이메일 형식이 올바르지 않습니다."}, status=400)

        # 이미 존재하는 이메일 확인
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "이미 존재하는 이메일입니다."}, status=400)

        # 사용자 저장
        try:
            user = User(
                username=username,
                name=name,
                student_number=student_number,
                password=password,  # 실제로는 해싱을 적용해야 함
                phone=phone,
                location=location
            )
            user.save()
            return JsonResponse({"message": "회원가입이 완료되었습니다."}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, 'signup/signup.html')
