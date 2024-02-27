from django.urls import path


from lionapp import views

urlpatterns = [
    path('v1/create/',views.create_post),
    path('v1/<int:pk>/',views.get_post),
    path('v1/delete/<int:pk>/',views.delete_post),
    path('v2/post/<int:pk>',views.PostApiView.as_view()),
    path('v2/post',views.create_post_v2)
]