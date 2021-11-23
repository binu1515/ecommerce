from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
# importing views from views..py
from . import views
 
urlpatterns = [
    path('', views.index, name="index" ),
    path('register',views.register, name="register"),
    path('adminpanel',views.adminpanel, name="adminpanel"),
    path('logout',views.Logout,name='logout'),
    path('detail',views.detail,name='detail'),
    path('addnew',views.addnew,name='addnew'),
    path('detailupdate/<int:id>',views.detailupdate,name='detailupdate'),
    path('detaildelete/<int:id>',views.detaildelete,name='detaildelete'),
    path('productdetail',views.productdetail,name='productdetail'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('productcategory',views.productcategory,name='productcategory'),
    path('categoryupdate/<int:id>',views.categoryupdate,name='categoryupdate')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)