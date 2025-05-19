from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class RegisterUserForm(UserCreationForm):
    """
    사용자 회원가입 폼
    UserCreationForm을 상속받아 커스텀 사용자 모델에 맞게 확장
    """
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
            "job",
            "gender",
        ]
        labels = {
            "username": "아이디",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
            "email": "이메일",
            "job": "직업",
            "gender": "성별",
        }
        help_texts = {
            "username": "150자 이하의 문자, 숫자, @/./+/-/_ 만 사용 가능합니다.",
            "password1": "8자 이상의 비밀번호를 입력해주세요.",
            "password2": "비밀번호를 한 번 더 입력해주세요.",
            "email": "이메일 주소를 입력해주세요.",
            "job": "직업을 선택해주세요.",
            "gender": "성별을 선택해주세요.",
        }

    #   <!-- 직업 선택 -->
    #   <div class="mb-3">
    #         <label for="id_job" class="form-label" name="job" id="job">직업</label>
    #         {{ form.job }}
    #   </div>
    #   <!-- 성별 선택 -->
    #   <div class="mb-3">
    #         <label for="id_gender" class="form-label" name="gender" id="gender">성별</label>
    #         {{ form.gender }}
    #   </div>

    def __init__(self, *args, **kwargs):
        """
        폼 초기화
        모든 필드에 Bootstrap 클래스와 placeholder 추가
        """
        super().__init__(*args, **kwargs)

        # 모든 필드에 Bootstrap form-control 클래스와 placeholder 추가
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": field.label
            })

        # 성별과 직업 선택 필드에 form-select 클래스 추가
        self.fields["gender"].widget.attrs.update({"class": "form-select"})
        self.fields["job"].widget.attrs.update({"class": "form-select"})