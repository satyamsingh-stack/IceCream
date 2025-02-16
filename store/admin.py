from django.contrib import admin
from .models import Contact,IceCream,Cart,Order,OrderItem,Category

# Register your models here.
 
admin.site.register(IceCream)    
admin.site.register(Category)    
admin.site.register(Cart)                                                                                                                                     
admin.site.register(Order)  
@admin.register(Contact)
class SignupDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','desc','date')  # Customize fields to display
    # search_fields = ('username', 'email', 'password')  # Optional: add search fields      

admin.site.register(OrderItem)                                                                                                                                     
