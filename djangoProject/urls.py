from django.urls import path, include  # 수정된 부분

urlpatterns = [
    path("", include('meteo.urls')),  # 수정된 부분
]
