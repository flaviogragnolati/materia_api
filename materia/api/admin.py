from django.contrib import admin
from .models import Address, Cart, CartItem, Category, Order, OrderItem, Product, ProductReview, Review, Transaction, User


# Register your models here.
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(Review)
admin.site.register(Transaction)
admin.site.register(User)
