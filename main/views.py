from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@login_required
def client_list(request):
    if request.user.is_superuser:
        clients = Client.objects.all()
    else:
        clients = Client.objects.filter(created_by=request.user)
    return render(request, 'clients/list.html', {'clients': clients})

@login_required
def client_create(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        phone = request.POST.get('phone')
        Client.objects.create(f_name=f_name, phone=phone, created_by=request.user)
        return redirect('client_list')
    return render(request, 'clients/create.html')

@login_required
def client_update(request, id):
    client = get_object_or_404(Client, id=id)
    if not request.user.is_superuser and client.created_by != request.user:
        return redirect('client_list')

    if request.method == 'POST':
        client.f_name = request.POST.get('f_name')
        client.phone = request.POST.get('phone')
        client.save()
        return redirect('client_list')

    return render(request, 'clients/update.html', {'client': client})


@login_required
def client_delete(request, id):
    client = get_object_or_404(Client, id=id)
    if not request.user.is_superuser and client.created_by != request.user:
        return redirect('client_list')
    client.delete()
    return redirect('client_list')

@login_required
def client_filter(request):
    f_name = request.GET.get('f_name')
    created_by = request.GET.get('created_by')
    clients = Client.objects.all()

    if f_name:
        clients = clients.filter(f_name__icontains=f_name)
    if created_by:
        clients = clients.filter(created_by__username__icontains=created_by)

    return render(request, 'clients/list.html', {'clients': clients})