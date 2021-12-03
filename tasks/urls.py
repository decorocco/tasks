from django.urls import path

from views import index, listTask,postTask,deleteTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
