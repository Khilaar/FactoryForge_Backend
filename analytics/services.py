from datetime import datetime

from django.utils import timezone

from client_order.models import ClientOrder
from raw_material.models import RawMaterial
from raw_material_order.models import RawMaterialOrder


#######################################################################################################

def calculate_total_income(start_date, end_date):
    start_date = timezone.make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
    end_date = timezone.make_aware(datetime.strptime(end_date, "%Y-%m-%d"))

    client_orders = ClientOrder.objects.filter(created__range=[start_date, end_date])

    total_income = 0
    for order in client_orders:
        ordered_products = order.orderedproduct_set.all()

        if ordered_products is not None:
            for ordered_product in ordered_products:
                price = ordered_product.product.price
                quantity = ordered_product.quantity
                total_income += price * quantity

    return total_income

#######################################################################################################

def calculate_total_cost(start_date, end_date):
    start_date = timezone.make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
    end_date = timezone.make_aware(datetime.strptime(end_date, "%Y-%m-%d"))

    raw_material_orders = RawMaterialOrder.objects.filter(order_date__range=[start_date, end_date])

    total_cost = 0
    for order in raw_material_orders:
        if order.raw_materials_order is not None:
            for material, quantity in order.raw_materials_order.items():
                cost = RawMaterial.objects.get(name=material).cost
                total_cost += cost * quantity

    return total_cost

#######################################################################################################

def calculate_profit(start_date, end_date):
    total_income = calculate_total_income(start_date, end_date)
    total_cost = calculate_total_cost(start_date, end_date)
    total_profit = total_income - total_cost

    return total_profit
