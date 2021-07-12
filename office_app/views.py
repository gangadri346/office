from django.shortcuts import render
from .models import *




# Create your views here.
from django.shortcuts import render,redirect


from .models import Employee
from django.contrib.auth import authenticate, logout,login
from .forms import*
from django.contrib.auth.decorators import login_required,permission_required



from .forms import *



@login_required
def index(request):
    DRDO_data = Employee.objects.all()
    return render(request,"index.html",{'DRDO_data':DRDO_data})

def userlogout(request):
    return render(request,'logout.html')





@permission_required('office_app.add_employee')
@login_required
def create(request):
    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            n=form.cleaned_data['name']
            e = form.cleaned_data['eid']
            ex = form.cleaned_data['exp']
            a = form.cleaned_data['address']
            c = form.cleaned_data['contact']
            responce = redirect('/office/index/')

            request.session['name']=n
            request.session['eid'] = e
            request.session['exp'] = ex
            request.session['address'] = a
            request.session['contact'] = c
        return responce
    else:
           form = EmployeeForm()
    return render(request, 'create.html', {'form': form})


@permission_required('office_app.change_employee')
@login_required
def edit(request,eid):
    DRDO_data = Employee.objects.get(eid=eid)
    form=EmployeeForm(instance=DRDO_data)
    return render(request,"update.html",{'form':form,'eid':eid})



@permission_required('office_app.change_employee')
@login_required
def update(request,eid):
    DRDO_data = Employee.objects.get(eid=eid)
    form= EmployeeForm(request.POST,instance=DRDO_data)
    if form.is_valid():
        form.save()
        return redirect("/office/index/")
    return render(request,"update.html", {'form':form,'eid':eid})


@permission_required('office_app.delete_employee')
@login_required
def delete(request,eid):
    DRDO_data = Employee.objects.get(eid=eid)
    print("DRDO_data",DRDO_data)
    DRDO_data.delete()
    return redirect("/office/index/")