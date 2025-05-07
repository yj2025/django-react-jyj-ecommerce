from rest_framework.views import APIView
# ✅ 카트 API endpoint 예시:
# HTTP       Method	       Endpoint	 기능
# GET	   /api/cart/	   장바구니       조회
# POST	   /api/cart/	   장바구니에    상품 추가
# PUT	   /api/cart/	   장바구니    상품 수량 변경
# DELETE   /api/cart/	   상품 제거 or 전체 비우기
# 🔁 DELETE에서 product_id를 넘기면 해당 상품만 제거, 안 넘기면 전체 비움 처리됩니다.

class CartAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self,request):
        pass

    def post(self,request):
        pass
    
    def put(self,request):
        pass

    def delete(self,request):
        pass


import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#dev_6_Fruit
# POST	   /api/cart/merge	  장바구니에    상품 추가
class CartMergeAPIView(APIView):
    permission_classes = [IsAuthenticated] #로그인된 사람만 아래 함수가 실행 되도록

    def post(self,request):
        """
        localStorage의 장바구니를 서버 old_cart에 병합
        """
        user = request.user

        local_storage_cart = request.data.get("cart","{}")

        local_storage_cart = json.loads(local_storage_cart or "{}")
        old_cart = json.loads(user.old_cart or "{}")

        # 병합: 같은 상품이 있다면 수량 증가
        for product_id, item in local_storage_cart.items():
            quantity = int(item.get("quantity", 0))
            if product_id in old_cart:
                old_cart[product_id]["quantity"] += quantity
            else:
                old_cart[product_id] = {"quantity": quantity}

        user.old_cart = json.dumps(old_cart) #json을 string 만들어서 집어 넣어야함
        user.save()

        return Response({"message": "장바구니가 병합되었습니다."})



