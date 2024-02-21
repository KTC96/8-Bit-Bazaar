from django.contrib import admin
from .models import Order, OrderLineItem, Discount


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',
                       'original_bag', 'stripe_pid', 'discount_amount')  # Include 'discount_amount'

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'total', 'original_bag', 'stripe_pid', 'discount_amount')  # Include 'discount_amount'

    list_display = ('order_number', 'date', 'full_name',
                    'total', 'discount_amount')  # Include 'discount_amount'

    ordering = ('-date',)

    def save_model(self, request, obj, form, change):
        """
        Override save_model to add the discount_amount to the Order model.
        """
        # Assuming you have stored 'discount_amount' in the session during checkout_success
        obj.discount_amount = request.session.get('discount_amount', 0)
        super().save_model(request, obj, form, change)


    inlines = (OrderLineItemAdminInline,)

    # Add 'discount_amount' to the readonly_fields
    readonly_fields = ('order_number', 'date', 'total',
                       'original_bag', 'stripe_pid', 'discount_amount')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'total', 'original_bag', 'stripe_pid', 'discount_amount')

    list_display = ('order_number', 'date', 'full_name',
                    'total', 'discount_amount')  # Add 'discount_amount' to list_display

    ordering = ('-date',)

    def get_readonly_fields(self, request, obj=None):
        # Dynamically add 'discount_amount' to readonly_fields if it exists
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if obj and hasattr(obj, 'discount_amount'):
            readonly_fields.append('discount_amount')
        return readonly_fields

class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'percentage',
        'start_date',
        'end_date',
        'for_new_users',
    )

    ordering = ('start_date',)

admin.site.register(Discount, DiscountAdmin)

admin.site.register(Order, OrderAdmin)
