"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    # url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'post/', include('post.urls', namespace='post')),
    url(r'^$', lambda r: redirect('post:post_list'), name='root'), # NOTE: lambda 함수를 통한 리다이렉트
]

# NOTE: serving media files uploaded by a user during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# NOTE: debug_toolbar용 url 설정
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
