from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import RoleAccessUser
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'RoleAccess/index.html')

@login_required
def deleteUser(request, pk):
    user = RoleAccessUser.objects.get(id=pk)
    if not user.is_Admin and (request.user.is_Admin or request.user.is_superuser):
        user.delete()
    else:
        raise PermissionDenied()
    return redirect('users')

@login_required
def getUsers(request):

    # all users expect the current user
    users = RoleAccessUser.objects.all()
    if request.user.is_Admin or request.user.is_superuser:
        return render(request, 'RoleAccess/users.html', {'users': users})
    else:
        raise PermissionDenied()

def register(request):
    if request.method == 'POST':
        createAdmin=False
        if request.GET.get('admin')=='true':
            if request.user.is_Admin or request.user.is_superuser:
                createAdmin=True
            else:
                raise PermissionDenied()

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated:
                if createAdmin:
                    new_user=RoleAccessUser.objects.get(id=form.instance.id)
                    new_user.is_Admin=True
                    new_user.save()
                return redirect('index')
            else:
                return redirect('login')
    else:
        if request.GET.get('admin')=='true':
            if not request.user.is_Admin and not request.user.is_superuser:
                raise PermissionDenied()
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'RoleAccess/register.html', context)

