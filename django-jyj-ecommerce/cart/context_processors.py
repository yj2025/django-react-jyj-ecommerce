from .cart import Cart  # 현재폴더 cart.py 에서 Cart객체를 가져옴


# dev_17
def cart(request):

    # 세션확인 테스트
    #cart.decrypt_all_sessions()
    print("카트 함수 호출")

    return {"cart": Cart(request)}