from django.urls import path,include
from web import views

#views : Model = browser
#models : DAO


urlpatterns = [
    path('food_list/', views.foodListData),
    path('food_detail/',views.foodDetailData),
    path('emp/',views.empGraphData)
]
