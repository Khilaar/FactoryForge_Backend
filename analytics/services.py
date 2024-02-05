from client_order.models import ClientOrder
from raw_material.models import RawMaterial
from raw_material_order.models import RawMaterialOrder

#######################################################################################################

def calculate_total_income(start_date, end_date):
    client_orders = ClientOrder.objects.filter(created__range=[start_date, end_date])

    total_income = 0
    for order in client_orders:
        if order.order_and_quantities is not None:
            for product, quantity in order.order_and_quantities.items():
                price = product.objects.get(title=product).price
                total_income += price * quantity

    return total_income

#######################################################################################################

def calculate_total_cost(start_date, end_date):
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
    total_profit = calculate_total_income(start_date, end_date) - calculate_total_cost(start_date, end_date)

    return total_profit
