from django.contrib import admin
from accounts.models import User

# Register your models here.
# dev_9


# dev_12
# 어드민 페이지 등록방법 3가지
# 1. 기본적인 관리자 페이지에서 기본적인 등록
# admin.site.register(User)


# 하지만 커스텀 기능 (검색, 필터, 필드 설정 등)을 추가할 수 없음.
# 2. ModelAdmin 클래스를 활용하는 방법 (커스텀 가능)
@admin.register(User)
class UserAccountsAdmin(admin.ModelAdmin):
    """
    사용자 관리자 페이지 설정
    사용자 목록 표시, 검색, 필터링 기능 제공
    """
    # 목록에 표시할 필드
    list_display = [
        "username",
        "email",
        "job",
        "gender",
        "is_active",
        "date_joined",
    ]

    # 검색 가능한 필드
    search_fields = [
        "username",
        "email",
        "job",
        "gender",
    ]

    # 필터링 가능한 필드
    list_filter = [
        "is_active",
        "job",
        "gender",
        "date_joined",
    ]

    # 정렬 가능한 필드
    ordering = ["-date_joined"]

    # 페이지당 표시할 항목 수
    list_per_page = 20

    # 필드 그룹화
    fieldsets = (
        ("기본 정보", {
            "fields": ("username", "email", "password")
        }),
        ("개인 정보", {
            "fields": ("job", "gender", "profile_image")
        }),
        ("권한", {
            "fields": ("is_active", "is_staff", "is_superuser")
        }),
    )


# admin.site.register(User, UserAccountsAdmin)
# 3. @admin.register 데코레이터 사용

# @admin.register(User)
# class UserAccountsAdmin(admin.ModelAdmin):
#     list_display = [
#         "username",
#         "email",
#         "job",
#         "gender",
#     ]

