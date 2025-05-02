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
