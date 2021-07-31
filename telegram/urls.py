
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
#from graphene_django.views import GraphQLView
#from django.views.decorators.csrf import csrf_exempt
from telegram import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.bot),
    #url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
