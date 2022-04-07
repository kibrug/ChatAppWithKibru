"""verticalfarmingone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include


from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

#after add Public_chat_room app

from django.contrib.auth import views as auth_views
from django.urls import path

'''from personal.views import (
	home_screen_view
)

from public_chat.views import (
	public_chat
)






from account.views import (
    register_view,
    login_view,
    logout_view,
    account_search_view,

)'''

'''from verfarmapp.views import (
   bloge,
   whatvf,
   advantagevf,
   leadervf,

)'''
# chang admin panale 
admin.site.site_header = "Debo Partnership Admin"
admin.site.site_title = "Debo Admin Portal"
admin.site.index_title = "Welcome to Debo Partnership "

urlpatterns = [

      path('admin/', admin.site.urls),
      path('', include('verfarmapp.urls')),
   
   # path('', home_screen_view, name='home'),
    #path('account/', include('account.urls', namespace='account')),
	#path('admin/', admin.site.urls),
   # path('chat/', include('chat.urls', namespace='chat')),
    #path('friend/', include('friend.urls', namespace='friend')),
    #path('login/', login_view, name="login"),
    #path('logout/', logout_view, name="logout"),
    #path('register/', register_view, name="register"),
    #path('search/', account_search_view, name="search"),



    #before
    #path('', include('personal.urls',namespace='personal')),
    #path('', include('verfarmapp.urls', namespace='verfarmapp')),
   
    #path('pubic_chat/', include('public_chat.urls',namespace='pubic_chat')),
    #path('account/', include('account.urls', namespace='account')),
  
   
  #after add public chat app
   # path('', bloge, name='bloge'),
   # path('', home_screen_view, name='home'),
   # path('whatvf/', whatvf, name="whatvf"),
   # path('advf/', advantagevf, name="advf"),
    #path('gvfl/', leadervf, name="gvfl"),
    #path('public_chat/', public_chat, name="public_chat"),
    #path('login/', login_view, name="login"),
    #path('logout/', logout_view, name="logout"),
    #path('register/', register_view, name="register"),
    #path('search/', account_search_view, name="search"),
    

]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

