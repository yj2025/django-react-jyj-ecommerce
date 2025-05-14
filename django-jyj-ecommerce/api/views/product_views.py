from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product, Category

# dev_34
from api.serializers.product_serializers import ProductSerializer

# http://127.0.0.1:8000/api/products/
# 방식   url         기능
# GET   products/    list
# POST  products/   create


# dev_29
@api_view(["GET", "POST"])
def products_api(request):

    if request.method == "GET":
        products = Product.objects.all()
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스
        serializer = ProductSerializer(products, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    # dev_30
    # 디시리얼라이져
    # if request.method == "POST":
    #     print("데이터", request.data)  # json , dic
    #     print("타입", type(request.data))  # json , dic

    #     serializer = ProductSerializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)

    # dev_33 view 에서 직접 처리
    if request.method == "POST":

        # request.data 는 기본적으로 불변임
        data = request.data.copy()

        # category 정보 추출 후 제거
        category_data = data.pop("category")
        category_data = request.data["category"]

        # get_or_create 는 dict 형식으로 받기 때문에 category_data는 리스트일 수 있어서 주의
        if isinstance(category_data, list):
            category_data = category_data[0]

        # 카테고리 저장 조회
        category, _ = Category.objects.get_or_create(**category_data)

        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(category=category)

        return Response(serializer.data)


from django.shortcuts import get_object_or_404
from rest_framework import status


# dev_30
@api_view(["GET", "DELETE", "PUT"])
def product_api(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "GET":
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        product.delete()
        return Response("SUCCESS", status=status.HTTP_204_NO_CONTENT)
    
# dev_10_Fruit
# 페이지네이션 클래스 (옵션)
# 요청 예시
# /api/product-list/?page=2    페이지 2
# /api/product-list/?search=포도    '포도' 포함 검색
# /api/product-list/?category=4    카테고리 ID가 4번인 상품 필터링
# /api/product-list/?ordering=price    가격 오름차순 정렬
# /api/product-list/?ordering=-id    최신순 정렬
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

#http://127.0.0.1:8000/api/product-list/?page_size=5
#http://127.0.0.1:8000/api/product-list/?/api/products/?page=3&page_size=25
class ProductPagination(PageNumberPagination):
    page_size = 10 # 기본 페이지 크기
    page_size_query_param = "page_size"  # 클라이언트가 지정할 수 있는 파라미터
    max_page_size = 100  # 최대 페이지 크기 제한


# ModelViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    # 정렬/검색
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
