from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import User

# dev_5_fruit
# djoser 회원가입, User 정보 customizing
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "gender",
            "job",
        )

class UserSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "gender",
            "job",
            "created_at",
            "updated_at",
        )