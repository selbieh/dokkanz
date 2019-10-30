from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import categories,product
from .serializers import categoriesSerializer,productSerializer,productReadSerializer
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin
from .pagination import cutumPagination



class categoriesViewSet(ModelViewSet):
    queryset = categories.objects.all()
    serializer_class=categoriesSerializer




# using 2 serializer for  more simple code
#to enable pagintaion with modelViewSet should use mixins for duble class inhertance
class prodductViewSet(ModelViewSet,ListModelMixin):
    queryset = product.objects.all()
    serializer_class = productSerializer
    pagination_class = cutumPagination

    def list(self, request):
        serializer = productReadSerializer # use ReadSerializer alternative to class declared productSerializer
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = serializer(self.queryset, many=True)
        return Response(serializer.data) # to remove yield worning add the paginations call globaly in setting.py instaed of class

    def retrieve(self, request, pk=None):
        the_product = get_object_or_404(self.queryset, pk=pk)
        serializer = productReadSerializer(the_product)
        return Response(serializer.data)
# NOTE: to use only only serializer you should override post,put,patch or in serializer create and update method
# here is exampel for my own cod https://github.com/selbieh/Glass-Office/blob/master/backend/shopcart/views.py






