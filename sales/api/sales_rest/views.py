from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Salesperson, Sale, Customer, AutomobileVO
from .encoders import SalespersonEncoder, CustomerEncoder, SaleEncoder
import json


@require_http_methods(["GET", "POST"])
def api_list_salesperson(request):
    if request.method == "GET":
        salespeople = Salesperson.objects.all()
        return JsonResponse({"salespeople": salespeople}, encoder=SalespersonEncoder)
    else:
        content = json.loads(request.body)
        try:
            salesperson = Salesperson.objects.create(**content)
        except Salesperson.DoesNotExist:
            return JsonResponse(
                {"message": "Could not create salesperson"},
                status=400,
            )
        return JsonResponse(salesperson, encoder=SalespersonEncoder, safe=False)


@require_http_methods(["DELETE"])
def api_show_salesperson(request, id):
    if request.method == "DELETE":
        count, _ = Salesperson.objects.filter(id=id).delete()
        if count > 0:
            return JsonResponse({"deleted": count > 0})
        else:
            return JsonResponse(
                {"message": "Invalid salesperson id"},
                status=400,
            )


@require_http_methods(["GET", "POST"])
def api_list_customer(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        return JsonResponse({"customers": customers}, encoder=CustomerEncoder)
    else:
        content = json.loads(request.body)
        try:
            customer = Customer.objects.create(**content)
        except Customer.DoesNotExist:
            return JsonResponse(
                {"message": "Could not create customer"},
                status=400,
            )
        return JsonResponse(customer, encoder=CustomerEncoder, safe=False)


@require_http_methods(["DELETE"])
def api_show_customer(request, id):
    if request.method == "DELETE":
        count, _ = Customer.objects.filter(id=id).delete()
        if count > 0:
            return JsonResponse({"deleted": count > 0})
        else:
            return JsonResponse(
                {"message": "Invalid customer id"},
                status=404,
            )


@require_http_methods(["GET", "POST"])
def api_list_sales(request):
    if request.method == "GET":
        sales = Sale.objects.all()
        return JsonResponse(
            {"sales": sales},
            encoder=SaleEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            automobile = AutomobileVO.objects.get(vin=content["automobile"])
            content["automobile"] = automobile
        except AutomobileVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid VIN number"},
                status=400,
            )

        try:
            salesperson = Salesperson.objects.get(employee_id=content["salesperson"])
            content["salesperson"] = salesperson
        except Salesperson.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid employee ID"},
                status=400,
            )

        try:
            customer = Customer.objects.get(id=content["customer"])
            content["customer"] = customer
        except Customer.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid customer id"},
                status=400,
            )

        sales = Sale.objects.create(**content)
        return JsonResponse(sales, encoder=SaleEncoder, safe=False)


@require_http_methods(["DELETE"])
def api_show_sales(request, id):
    if request.method == "DELETE":
        count, _ = Sale.objects.filter(id=id).delete()
        if count > 0:
            return JsonResponse({"deleted": count > 0})
        else:
            return JsonResponse(
                {"message": "Invalid sales id"},
                status=400,
            )
