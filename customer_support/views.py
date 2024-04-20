from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.contrib.auth import login, authenticate
from .forms import ServiceRequestForm, SignUpForm
from .models import ServiceRequest
from django.http import HttpResponse

# home
def home(request):
    isSupportStaff = is_support_staff(request.user)
    return render(request, 'home.html', {'isSupportStaff': isSupportStaff})

# signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# customer methods
@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('view_request', id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def view_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)  
    return render(request, 'view_requests.html', {'requests': requests})

@login_required
def view_request(request, id):
    service_request = ServiceRequest.objects.get(id=id, user=request.user)
    return render(request, 'view_request.html', {'service_request': service_request})

@login_required
@require_POST  
def delete_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id, user=request.user)
    service_request.delete()
    return redirect('view_requests')

# support staff methods
def is_support_staff(user):
    return user.groups.filter(name='SupportStaff').exists()

@login_required
@user_passes_test(is_support_staff)
def support_dashboard(request):
    open_requests = ServiceRequest.objects.filter(status='OPEN').order_by('-created_at').reverse()
    return render(request, 'support_dashboard.html', {'open_requests': open_requests})

@login_required
@user_passes_test(is_support_staff)
def handle_request(request, request_id):
    request_detail = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        request_detail.status = request.POST.get('status')
        request_detail.save()
        return redirect('support_dashboard')
    return render(request, 'handle_request.html', {'request_detail': request_detail})