from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

#{"id": 2111783846, "connected_at": "2022-02-08T09:17:28Z", 
# "properties": {"nickname": "Tom", 
# "profile_image": "http://k.kakaocdn.net/dn/wN4qJ/btsBiRUEgPl/zyHgk69z4W53BPhOgyNV41/img_640x640.jpg", 
# "thumbnail_image": "http://k.kakaocdn.net/dn/wN4qJ/btsBiRUEgPl/zyHgk69z4W53BPhOgyNV41/img_110x110.jpg"}, 
# "kakao_account": {"profile_nickname_needs_agreement": false, "profile_image_needs_agreement": false, 
# "profile": {"nickname": "Tom", "thumbnail_image_url": 
# "http://k.kakaocdn.net/dn/wN4qJ/btsBiRUEgPl/zyHgk69z4W53BPhOgyNV41/img_110x110.jpg", 
# "profile_image_url": "http://k.kakaocdn.net/dn/wN4qJ/btsBiRUEgPl/zyHgk69z4W53BPhOgyNV41/img_640x640.jpg", "is_default_image": false, "is_default_nickname": false}, "has_email": true, "email_needs_agreement": false, "is_email_valid": true, "is_email_verified": true, "email": "nqwrt@ymail.com", "has_gender": true, "gender_needs_agreement": false, "gender": "male"}}

#소셜 로그인 시점에 Allauth 내부에서 자동으로 호출
#사용자 생성, 로그인 전 처리 등을 커스터마이징할 수 있는 핵심 지점
# 전체 흐름 순서 요약
#=========================================
# 1. Provider callback → views.py
# 2. complete_social_login(request, sociallogin)
#=========================================
#=========================================
# 3. get_adapter(request) → DefaultSocialAccountAdapter
# 4. adapter.pre_social_login()
# 5. adapter.populate_user()
# 6. adapter.save_user()
#=========================================

# 7. login(request, user)



class KakaoSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    카카오 소셜 로그인 어댑터
    카카오 로그인 시 사용자 정보를 매핑하고 초기화하는 역할을 수행
    
    소셜 로그인 처리 흐름:
    1. Provider callback → views.py
    2. complete_social_login(request, sociallogin)
    3. get_adapter(request) → DefaultSocialAccountAdapter
    4. adapter.pre_social_login()
    5. adapter.populate_user()
    6. adapter.save_user()
    7. login(request, user)
    """

    def populate_user(self, request, sociallogin, data):
        """
        소셜 로그인 사용자 정보 초기화
        카카오에서 받은 정보를 User 모델 필드에 매핑
        
        Args:
            request: HTTP 요청 객체
            sociallogin: 소셜 로그인 정보
            data: 추가 데이터
            
        Returns:
            User: 초기화된 사용자 객체
        """
        user = super().populate_user(request, sociallogin, data)

        # 카카오 계정 정보 추출
        kakao_data = sociallogin.account.extra_data
        kakao_account = kakao_data.get("kakao_account", {})
        profile = kakao_account.get("profile", {})
        
        # 필수 필드 설정
        user.email = kakao_account.get("email", "")
        user.profile_image = profile.get("profile_image_url")

        # 성별 매핑 (카카오 → M/F)
        kakao_gender = kakao_account.get("gender")
        if kakao_gender == "male":
            user.gender = "M"
        elif kakao_gender == "female":
            user.gender = "F"
        
        # 직업 기본값 설정
        if not user.job:
            user.job = "E"  # 기타(Etc.)로 기본 설정

        return user