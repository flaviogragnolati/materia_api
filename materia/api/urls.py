from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'address', views.AddressViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'cart_item', views.CartItemViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'order_item', views.OrderItemViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'product_category', views.ProductCategoryViewSet)
router.register(r'product_review', views.ProductReviewViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'transaction', views.TransactionViewSet)
router.register(r'user', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
