from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User


# dev_5_Fruit
# 도져 회원가입 및 User 정보 커스텀 마이징
class UserCreateSerializer(BaseUserCreateSerializer):
    """
    사용자 생성 시리얼라이저
    회원가입 시 필요한 필드 정의
    """
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "gender",
            "job",
            #   "old_cart",
        )

class UserSerializer(BaseUserSerializer):
    """
    사용자 정보 시리얼라이저
    사용자 정보 조회 시 필요한 필드 정의
    """
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "gender",
            "job",
            "old_cart",
            "created_at",
            "updated_at",
        )

#dev_9_2_Fruit
#https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#register-serializer
class UserResAuthSerializer(serializers.ModelSerializer):
    """
    REST API 사용자 인증 시리얼라이저
    dj-rest-auth를 사용한 인증에 필요한 필드 정의
    """
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "gender",
            "job",
            "old_cart",
            "created_at",
            "updated_at",
        )

#http://127.0.0.1:8000/api/dj-rest-auth/registration/
#https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#register-serializer
class UserRegisterRestAuthSerializer(RegisterSerializer):
    """
    REST API 회원가입 시리얼라이저
    dj-rest-auth를 사용한 회원가입에 필요한 필드 정의
    """
    # 추가 필드 정의
    gender = serializers.ChoiceField(
        choices=User.GenderChoices.choices,
        required=True,
        help_text="사용자의 성별을 선택해주세요"
    )
    job = serializers.ChoiceField(
        choices=User.JobChoices.choices,
        required=True,
        help_text="사용자의 직업을 선택해주세요"
    )

    def get_cleaned_data(self):
        """
        유효성 검사가 완료된 데이터 반환
        """
        data = super().get_cleaned_data()
        data['gender'] = self.validated_data.get('gender', '')
        data['job'] = self.validated_data.get('job', '')
        return data

    def custom_signup(self, request, user):
        """
        회원가입 시 추가 필드 저장
        """
        user.gender = self.validated_data.get('gender')
        user.job = self.validated_data.get('job')
        user.save()