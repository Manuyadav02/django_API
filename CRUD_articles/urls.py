"""
URL configuration for CRUD_articles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from.views import (
    article_list,
    article_create,
    article_detail,
    article_update,
    article_delete,
)

urlpatterns = [
    path('api/articles/', article_list, name='article-list'),
    path('api/articles/create/', article_create, name='article-create'),
    path('api/articles/<int:pk>/', article_detail, name='article-detail'),
    path('api/articles/<int:pk>/update/', article_update, name='article-update'),
    path('api/articles/<int:pk>/delete/', article_delete, name='article-delete'),
]
