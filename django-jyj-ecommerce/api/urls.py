from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# dev_28
# from api.views import hello_world, hello_world_json, hello_world_drf
from .views import base_views, product_views, category_views,cart_views

app_name = "api"

# dev_38
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"categories", category_views.CategoryViewSet)

category_list = category_views.CategoryViewSet.as_view(
    {"get": "list", "post": "create"}
)

category_detail = category_views.CategoryViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)


urlpatterns = [
    # path("hello-world/", base_views.hello_world),
    # path("hello-world-json/", base_views.hello_world_json),
    # path("hello-world-drf/", base_views.hello_world_drf),
    # dev_29 proudct_view.py
    # http://127.0.0.1:8000/api/products/
    # 방식   url                 기능
    # GET  products/            list
    # POST products/            create
    # Get  product/{id}         product
    # PUT  product/{id}       modify product
    # DELETE  product/{id}    delete product
    path("products/", product_views.products_api),
    path("product/<int:pk>/", product_views.product_api),
    # dev_32
    # path("categories/", category_views.categories_api),
    # dev_35
    # 방식   url                  기능
    # GET  categories/           list
    # POST categories/           create
    # Get  category/{id}       category
    # PUT  category/{id}       modify category
    # DELETE  category/{id}    delete category
    # path("categories/", category_views.CategoriesAPI.as_view()),
    # path("category/<int:pk>/", category_views.CategoryAPI.as_view()),
    # dev_36
    # path("categories/", category_views.CategoriesMixins.as_view()),
    # path("category/<str:name>/", category_views.CategoryMixins.as_view()),
    # dev_37
    # path("categories/", category_views.CategoriesGenericView.as_view()),
    # path("category/<int:pk>/", category_views.CategoryGenericView.as_view()),
    # dev_38
    # 이렇게 하면 다음 경로들이 자동으로 만들어집니다:
    # GET /categories/
    # POST /categories/
    # GET /categories/<pk>/
    # PUT /categories/<pk>/
    # PATCH /categories/<pk>/
    # DELETE /categories/<pk>/
    # path("categories/", category_list),
    # path("category/<int:pk>/", category_detail),
    path("", include(router.urls)),
    # dev_5_Fruit
    path("auth/", include("djoser.urls")), # 회원가입, 비밀번호 변경 등
    path("auth/", include("djoser.urls.jwt")),  # JWT 로그인/로그아웃, 토큰 갱신 등   
    #dev_6_Fruit
    path("cart/", cart_views.CartAPIView.as_view()),
    path("cart/merge/", cart_views.CartMergeAPIView.as_view()),
]

# 2. 생성되는 URL
# ✅ djoser.urls (/auth/ 아래에 생성되는 URL)

# 메서드	경로	설명
# POST	/auth/users/	회원가입
# GET	/auth/users/me/	현재 로그인된 유저 정보
# POST	/auth/users/resend_activation/	활성화 이메일 재전송 (선택)
# POST	/auth/users/activation/	계정 활성화 (선택)
# POST	/auth/users/set_password/	비밀번호 변경 (로그인 상태)
# POST	/auth/users/reset_password/	비밀번호 재설정 이메일 전송
# POST	/auth/users/reset_password_confirm/	비밀번호 재설정 확인
# POST	/auth/token/login/	세션 로그인 (Token 기반 인증 사용 시)
# POST	/auth/token/logout/	세션 로그아웃 (Token 기반 인증 사용 시)

# ✅ djoser.urls.jwt (/auth/jwt/ 아래에 생성되는 URL)

# 메서드	경로	설명
# POST	/auth/jwt/create/	JWT 로그인 (access + refresh 발급)
# POST	/auth/jwt/refresh/	access 토큰 재발급
# POST	/auth/jwt/verify/	토큰 유효성 검사
# POST	/auth/jwt/logout/	로그아웃 (refresh 토큰 블랙리스트 처리)