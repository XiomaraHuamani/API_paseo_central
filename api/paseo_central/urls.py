from django import views
from django.urls import path
from . import views

app_name = "paseo_central"
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    #Users login
    path('users',views.UserList.as_view(), name='users'),
    path('userDetail',views.UserDetail.as_view(), name='userDetail'),
    
    #usuarios
    path('usuarios',views.UsuariosList.as_view(), name='usuarios'),
    path('usuarios/<int:id_usuarios>',views.UsuariosDetail.as_view()),
    
    #roles
    path('roles',views.RolesList.as_view(), name='roles'),
    path('usuarios/<int:id_rol>',views.RolesDetail.as_view()),
    
    #producto
    path('productos',views.ProductosList.as_view(), name='productos'),
    path('productos/<int:id_producto>',views.ProductosDetail.as_view()),
    
    #RegistroClienteTienda
    path('registrocliente',views.RegistroClienteTiendaList.as_view(), name='registrocliente'),
    path('registrocliente/<int:id_cli>',views.RegistroClienteTiendaDetail.as_view()),
    
    #Tiendas
    path('tiendas',views.TiendasList.as_view(), name='tiendas'),
    path('tiendas/<int:id_tienda>',views.TiendasDetail.as_view()),
    
    #Ventas
    path('ventas',views.VentasList.as_view(), name='ventas'),
    path('ventas/<int:id_ventas>',views.VentasDetail.as_view()),
    
]

