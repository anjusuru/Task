import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext

from .forms import OrderForm
from .models import Course, Department, Order
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request=request, template_name='home.html')


def order(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # response_data = {}
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            messages.success(request, 'Order Confirmed!')
            return render(request,'page.html',  {'form':OrderForm()})
            # response_data['message'] = 'Order Confirmed!'
            # response_data['url'] = '/'
            # messages.success(request, 'Order Confirmed')
            # return HttpResponse(
            #     json.dumps(response_data),
            #     content_type="application/json")
            # return redirect('storeapp:home')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = OrderForm()
        return render(request, "page.html", {'form': form})
    return render(request, "page.html", {'form': form},context)


def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
