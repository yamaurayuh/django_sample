from django.urls import path
from .views import init, detail, result

app_name = 'salesapp'
urlpatterns = [
    path('init/', init.as_view(), name='init'),
    path('detail/', detail.as_view(), name='detail'),
    path('result/', result.as_view(), name='result'),
]