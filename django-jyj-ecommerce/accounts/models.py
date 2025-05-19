from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# dev_9
# User 계정을 커스텀 마이징 시키는 방법은 4가지 정도가 있음
# 1) proxy 활용
# 2) AbstractUser 상속 하는 방법
# 3) AbstractBaseUser 을 상속 하는 방법


class User(AbstractUser):
    """
    커스텀 사용자 모델
    AbstractUser를 상속받아 기본 사용자 모델을 확장
    """
    
    class GenderChoices(models.TextChoices):
        """성별 선택 옵션"""
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    class JobChoices(models.TextChoices):
        """직업 선택 옵션"""
        PROFESSOR = "P", "교수/강사(Professor/Lecturer)"
        STUDENT = "S", "학생(Student)"
        RESEARCHER = "R", "연구원(Researcher)"
        ETC = "E", "기타(Etc.)"

    # 사용자 정보 필드
    gender = models.CharField(
        verbose_name="성별",
        max_length=1,
        choices=GenderChoices.choices,
        help_text="사용자의 성별을 선택해주세요"
    )

    job = models.CharField(
        verbose_name="직업",
        max_length=1,
        choices=JobChoices.choices,
        help_text="사용자의 직업을 선택해주세요"
    )

    # 시간 정보 필드
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성일"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="수정일"
    )

    # 장바구니 관련 필드
    old_cart = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="이전 장바구니"
    )

    # 프로필 이미지 필드
    profile_image = models.URLField(
        blank=True,
        null=True,
        verbose_name="프로필 이미지"
    )

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자들"