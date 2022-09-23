from random import choice
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect


# without render
# def show_departments(request, *args, **kwargs):
#
#     order_by = request.GET.get('order_by', 'name')
#     body = f'path: {request.path}, ' \
#            f'args={args}, ' \
#            f'kwargs={kwargs}, ' \
#            f'order_by: {order_by}'
#
#     return HttpResponse(body)


# with render
def show_departments(request, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
    }
    return render(request, 'departments/all.html', context)


def show_department_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)

    to = f'/departments/?order_by={order_by}'
    #to = 'https://www.abv.bg/'

    #return redirect(to)

    #return redirect('show departments')

    return redirect('details', department_id=13)


# def show_not_found(request):
#     status_code = 404
#     if status_code == 404:
#         return HttpResponseNotFound("Not...")
#     elif status_code == 400:
#         return HttpResponseBadRequest("Bad...")

# def show_not_found(request):
#     status_code = 404
#     return HttpResponse("Error", status=status_code)

def show_not_found(request):
    raise Http404("Nnnn...")








