from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer 
from .models import Product, Brand
from products.serializers import BrandSerializer,BrandDetailSerializer



""" @api_view(['GET'])
def product_list_api(request):            #list
    queryset = Product.objects.all()[:10]            
    data = ProductSerializer(queryset,many=True,context={'request':request}).data   #the list to jason data of products
    return Response ({'data':data}) """



""" @api_view(['GET'])
def product_detail_api(request,product_id):
    queryset = Product.objects.get(id=product_id)
    data = ProductSerializer(queryset,context={'request':request}).data   
    return Response ({'data':data})
 """

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()[:10]
    serializer_class = ProductSerializer 





class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 





class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer 
    
    
    
class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
   