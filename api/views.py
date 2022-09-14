from django.db.models import Count, Prefetch
from rest_framework import generics
from .models import *
from .serializers import FoodListSerializer


class FoodListApiView(generics.ListAPIView):
    # with LEFT OUTER JOIN
    #queryset = FoodCategory.objects.prefetch_related(Prefetch('food', queryset=Food.objects.filter(is_publish=True))).annotate(total=Count('food')).filter(total__gt=0)

    # with INNER JOIN
    queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(Prefetch("food", queryset=Food.objects.filter(is_publish=True))).distinct()
    serializer_class = FoodListSerializer
