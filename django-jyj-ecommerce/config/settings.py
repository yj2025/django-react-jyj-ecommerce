from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0gzzd&b5#)f2**v7dn@^-w&1=6%l1y=iynu3iks+rj)yp!85wu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # dev_5 쉼표(,)를 추가하여 통화 형식(₩1,000,000)으로 변환하는 방법 (통화 형식 변환)
    "django.contrib.humanize",  
    "store",  # 상점 앱
    "accounts",  # 사용자 계정 앱
    "cart",  # 장바구니 앱
    "orders",  # 주문 앱
    "payment",  # 결제 앱
    # dev_27 소셜로그인 관련
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # provider 추가 (추가로 다른 사이트도 하고 싶을 경우 뒤에 이름만 변경하면 됨)
    #'allauth.socialaccount.providers.google', #구글로그인 구현시 추가
    "allauth.socialaccount.providers.kakao",  # 카카오로그인 구현시 추가
    #'allauth.socialaccount.providers.naver', # 네이버 로그인 구현시 추가

    # API 관련
    "rest_framework", #DRF
    "api",
    "corsheaders",  # CORS 설정
    "djoser" # JWT 인증
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   # CORS 미들웨어 추가
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # 소셜 로그인 미들웨어
]

# CORS 설정
# 정확히 허용할 도메인만
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",  # 프론트 도메인
# ]

CORS_ORIGIN_ALLOW_ALL = True  # 모든 출처에서의 요청 허용

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # dev_1
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # dev_17 cart(request)가 모든 템플릿에서 사용 가능해짐.
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"  # dev_1

TIME_ZONE = "Asia/Seoul"  # dev_1

USE_I18N = True

# Timezone의 사용여부를 정한다.
# False면 모든 datetime들을 표시하고 True면 template과 form에만 적용된다.
# 즉 DB에 저장되는 정보도 한국 시간대로 사용하려면 이 부분을 False로 지정해주어야 한다.
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# 스태틱(static) 디렉터리
# URL 상의 스택틱 폴더를 ,로컬(내컴퓨터)의 파일 폴더와 매칭 시키는 부분
# http://127.0.0.1:8000/static/a.jpg
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 미디어 파일 경로 설정
import os

# http://127.0.0.1:8000/media/파일경로
MEDIA_URL = "media/"  # ex) /media/photo1.png
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# dev_9 커스텀 사용자 모델 사용
# 다시 migrate 
AUTH_USER_MODEL = "accounts.User"

# dev_15 장바구니 세션 아이디 설정
CART_SESSION_ID = "cart"

# AUTH_USER_MODEL = "accounts.User"
# 추가!! 없으면 오류 발생 "앱이름.모델명" user모델생성 후 allauth말고 내가 생성한 모델을 우선으로 적용

# dev_27 소셜 로그인 설정
SITE_ID = 1  
AUTHENTICATION_BACKENDS = [
    # 장고에서 사용자의 이름을 기준으로 로그인하도록 설정
    "django.contrib.auth.backends.ModelBackend",
    # 'allauth'의 인증방식 추가
    "allauth.account.auth_backends.AuthenticationBackend",
]


# dev_27 소셜로그인 설정
# 소셜 로그인 시 GET 요청만으로 로그인 처리를 허용
# 사용자가 로그인 버튼을 클릭했을 때 redirect URI로 오는 GET 요청만으로도 자동 로그인
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = (
    "/"  # 로그아웃 한 뒤에 어느 페이지로 리다이렉트할지 경로를 설정
)
ACCOUNT_LOGOUT_ON_GET = True

# dev_27 로그인후 리다이렉트
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# pip install python-decouple
from decouple import config

# dev_27 소셜로그인 설정
SOCIALACCOUNT_PROVIDERS = {
    # 카카오 로그인
    "kakao": {
        "APP": {
            "client_id": config("KAKAO_CLIENT_ID"),
            "secret": config("KAKAO_SECRET"),
            "key": "",
        },
        # scope의 경우 내가 어떤 데이터를 가져올건지를 선택하는 것인데 사이트마다
        # 제공하는 값이 다르기 때문에 가져올 데이터를 설정한 이후 추가/삭제 해보면 됩니다.
        # SCOPE값에 제공하지 않는 값을 넣거나 하는 이유로 오류가 나올 수 있음
        "SCOPE": [],
        # 추가
        "AUTH_PARAMS": {
            "access_type": "online",
            "prompt": "select_account",  # 간편로그인 지원
        },
    }
}


# dev_5_Fruit

# 대략적인 구현
# class JWTAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         header = self.get_header(request)  # Authorization 헤더 추출
#         raw_token = self.get_raw_token(header)  # "Bearer abc.def.ghi" → 토큰만 추출
#         validated_token = self.get_validated_token(raw_token)  # 유효성 검사
#         user = self.get_user(validated_token)  # payload에서 user_id를 추출 → User 객체
#         return (user, validated_token)

#JWTAuthentication은 다음을 자동으로 처리
#HTTP 요청의 Authorization 헤더에서 JWT 토큰을 추출
#그 토큰을 디코딩해서 유효한지 검사
#토큰에서 사용자 ID를 추출하고, 해당 사용자를 DB에서 가져옴
#해당 사용자를 request.user에 할당
#DRF에서 모든 API 뷰가 사용할 기본 인증 클래스들을 지정 
    
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=3), #timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# 도져(djoser) 커스텀마이징 세팅
DJOSER = {
    "USER_ID_FIELD": "id",
    "LOGIN_FIELD": "username",  # 또는 email
    "SERIALIZERS": {
        "user_create": "accounts.serializers.UserCreateSerializer",
        "user": "accounts.serializers.UserSerializer",
        "current_user": "accounts.serializers.UserSerializer",
    },
    "CREATE_SESSION_ON_LOGIN": True,  # 로그인하면 세션도 생성됨
}

