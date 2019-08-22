from django.conf.urls import url
from customers import views 
 
urlpatterns = [ 
    url(r'^customers/$', views.customer_list),
    url(r'^(?P<id>[0-9]+)$', views.customer_detail),
    url(r'^age/(?P<age>[0-9]+)/$', views.customer_list_age),
    url(r'^login/',views.login_data),
    # url(r'^add_data/(?P<id>[0-9]+)$',views.customer_detail),
    url(r'^add_data/(?P<pk>\w+)/',views.add_user),


    # url(r'^customers/(?P&lt;pk&gt;[0-9]+)$', views.customer_detail),
    # url(r'^customers/age/(?P&lt;age&gt;[0-9]+)/$', views.customer_list_age),

]	
