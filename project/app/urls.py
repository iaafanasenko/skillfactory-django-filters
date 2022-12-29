from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>', PostDetail.as_view(), name='post_details'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
]
