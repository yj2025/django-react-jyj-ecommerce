from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularYAMLAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# URL 패턴 정의
urlpatterns = [
    # 관리자 페이지
    path("admin/", admin.site.urls),
    
    # 앱별 URL 패턴
    path("", include("store.urls")),  # 상점 메인
    path("accounts/", include("accounts.urls")),  # 계정 관리
    path("cart/", include("cart.urls")),  # 장바구니
    path("orders/", include("orders.urls")),  # 주문 관리
    path("payment/", include("payment.urls")),  # 결제 처리
    path("accounts/", include("allauth.urls")),  # 소셜 로그인
    path("api/", include("api.urls")),  # REST API
    
    # API 문서화
    path("swagger.json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("swagger.yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc"),
]

# 개발 환경에서 미디어 파일 서빙 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)