from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# from .forms import RegisterUserForm # 상대 경로형식
from accounts.forms import RegisterUserForm  # 절대 경로 형식

# dev_23
from accounts.models import User
import json
from cart.cart import Cart
from store.models import Product

# Create your views here.


# class HTTPRequest:
#    POST = {"username":"admim","password":"1234"}
#    GET = {}
# dev_9


def logout_user(request):
    """
    사용자 로그아웃 처리
    세션에서 사용자 정보를 삭제하고 메인 페이지로 리다이렉트
    """
    logout(request)
    messages.success(request, "로그아웃되었습니다.")
    return redirect("/")


def login_user(request):
    """
    사용자 로그인 처리
    POST 요청 시 사용자 인증 및 로그인 처리
    GET 요청 시 로그인 페이지 렌더링
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # 저장된 장바구니 정보 복원
            current_user = User.objects.get(id=request.user.id)
            saved_cart = current_user.old_cart
            cart = Cart(request)

            # 현재 장바구니가 있으면 DB에 저장
            if len(cart) > 0:
                cart.cart_to_db()

            # 저장된 장바구니가 있으면 복원
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                for product_id, data in converted_cart.items():
                    quantity = data["quantity"]
                    product = Product.objects.get(id=product_id)
                    cart.add(product, quantity)

            messages.success(request, "로그인되었습니다.")
            return redirect("/")
        else:
            messages.error(request, "로그인에 실패했습니다. 다시 시도해주세요.")
            return redirect("accounts:login_user")
    
    return render(request, "accounts/login.html", {})


# dev_10
# dev_11 회원가입 로직
def register_user(request):
    """
    사용자 회원가입 처리
    POST 요청 시 회원가입 처리 및 자동 로그인
    GET 요청 시 회원가입 페이지 렌더링
    """
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            form = RegisterUserForm(request.POST)

            if form.is_valid():
                form.save()
                
                # 회원가입 후 자동 로그인
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)
                login(request, user)

                messages.success(request, "회원가입이 완료되었습니다.")
                return redirect("/")
            else:
                messages.error(request, "입력하신 정보를 확인해주세요.")
        else:
            messages.error(request, "비밀번호가 일치하지 않습니다.")

    form = RegisterUserForm()
    return render(request, "accounts/register.html", {"form": form})


# dev_27
def kakao_login_user(request):
    """
    카카오 로그인 페이지 렌더링
    """
    return render(request, "accounts/kakao_login.html")