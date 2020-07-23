from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, Category


def make_request_granted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_request_granted.short_description = 'Update orders to request granted'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'category', 'label')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'price', 'category', 'label']
    list_editable = ['price', 'discount_price']
    search_fields = ['name']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'ordered')
    list_filter = ['item', 'ordered']
    search_fields = ['item']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'being_delivered', 'received', 'refund_requested', 'refund_granted',
                    'shipping_address', 'billing_address', 'payment', 'coupon']
    list_display_links = ['user', 'shipping_address', 'billing_address', 'payment', 'coupon']
    list_filter = ['ordered', 'being_delivered', 'received', 'refund_requested', 'refund_granted']
    search_fields = ['user__username', 'ref_code']
    actions = [make_request_granted]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address', 'zip', 'address_type', 'default']
    list_filter = ['default', 'street_address', 'address_type']
    search_fields = ['user__username']


class RefundAdmin(admin.ModelAdmin):
    list_display = ['order', 'email']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund, RefundAdmin)

