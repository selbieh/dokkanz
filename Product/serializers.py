from rest_framework import serializers
from .models import categories,product


class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'


#return  the product and nasted catagory id only
class productSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = product



#return  product with it`s full neasted catagory object of name and ID
class productReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = product
        depth = 1









