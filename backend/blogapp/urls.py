from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blogs/',views.BlogView.as_view(),name="Blogs"),
    path('blogs/<id>',views.SingleBlogView.as_view(),name="singleBlog"),
    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

