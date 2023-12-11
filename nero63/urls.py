from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/<int:user_id>/<str:token>', VerifyEmailView.as_view(), name='verify'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('verificationsuccess/', VerificationSuccess.as_view(), name='verificationsuccess'),
    path('verificationerror/', VerificationError.as_view(), name='verificationerror'),
    path('', PostListView.as_view(), name='post_list'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_update/<int:pk>/', UpdatePostView.as_view(), name='post_update'),
    path('post_about/<int:pk>/', DetailPostView.as_view(), name='post_about'),
    path('post_delete/<int:pk>/', DeletePostView.as_view(), name='post_delete'),
    path('comment_create/', CreateCommentView.as_view(), name='comment_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)