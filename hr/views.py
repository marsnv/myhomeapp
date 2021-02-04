from django.shortcuts import render, redirect
from hr.models import hr_staff
from hr.forms import hr_createForm
from django.views.generic import DetailView, UpdateView, DeleteView


class Hr_Staff_DetailView(DetailView):
    model = hr_staff
    template_name = 'hr/hr_staff_details_view.html'
    context_object_name = 'hr_staff'


class Hr_Staff_UpdateView(UpdateView):
    model = hr_staff
    template_name = 'hr/hr_create.html'

    #fields = ['LastName', 'Name', 'MiddleName', 'BirthDate', 'Salary']
    form_class = hr_createForm


class Hr_Staff_DeleteView(DeleteView):
    model = hr_staff
    success_url = '/hr'
    template_name = 'hr/hr_delete.html'


def hr_create(request):
    error = ''
    if request.method == 'POST':
        form = hr_createForm(request.POST)
        if form.is_valid():
            form.save()
            end_hr_staff = hr_staff.objects.last()
            end_hr_staff.ViewStaff="ТН: "+str(end_hr_staff.id)+" "+end_hr_staff.LastName+" "+end_hr_staff.Name+" "+end_hr_staff.MiddleName+" "+str(end_hr_staff.BirthDate)
            end_hr_staff.save()
            return redirect('hr_index')
        else:
            error = 'Данные формы неверны.'

    form = hr_createForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'hr/hr_create.html', context)


def hr_index(request):
    hr_staffs = hr_staff.objects.all()
    return render(request, 'hr/hr.html', {'title': 'Сотрудники', 'hr_staffs': hr_staffs})

