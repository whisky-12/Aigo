from django.urls import path
from rest_framework import routers

from fuc.algorithm.views.xxx import XxxView
from fuc.algorithm.views.Categorization_of_dishes import Categorization_of_dishes_View
from fuc.algorithm.views.Classification_of_animals import Classification_of_animals_View
from fuc.algorithm.views.Driver_abnormal_behavior import Driver_abnormal_behavior_View
from fuc.algorithm.views.Animation_style_conversion import Animation_style_conversion_View
from fuc.algorithm.views.Cartoon_profile import Cartoon_profile_View
from fuc.algorithm.views.Hayao_Miyazaki_Animation_Style import Hayao_Miyazaki_Animation_Style_View
from fuc.algorithm.views.Quick_Sketch import Quick_Sketch_View
algorithm_url = routers.SimpleRouter()
# algorithm_url.register(r'xxx', XxxViewSet)

urlpatterns = [
    path("xxx/", XxxView.as_view()),
    path("Image_classification/Categorization_of_dishes/", Categorization_of_dishes_View.as_view()),
    path("Image_classification/Classification_of_animals/", Classification_of_animals_View.as_view()),
    path("Image_classification/DriverStatus/", Driver_abnormal_behavior_View.as_view()),
    path("Image2Image/Animation_style_conversion", Animation_style_conversion_View.as_view()),
    path("Image2Image/Cartoon_profile", Cartoon_profile_View.as_view()),
    path("Image2Image/Hayao_Miyazaki_Animation_Style", Hayao_Miyazaki_Animation_Style_View.as_view()),
    path("Image2Image/Quick_Sketch", Quick_Sketch_View.as_view()),
]
urlpatterns += algorithm_url.urls
