from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from TodoApp.form import TodoForms
from . models import Task
from django.shortcuts import redirect, render
from django.views.generic import ListView

# Create your views here.

def first(request):
    return render(request,'home.html')

# Generic Views in Django
class TaskListView(ListView):
    model = Task
    template_name = 'ViewTask.html'
    context_object_name = 'taskres'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'ViewDetails.html'
    context_object_name = 'obj'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "Edit.html"
    context_object_name = 'upObj'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'DeleteTask.html'
    success_url = reverse_lazy('cbvtask')


def resultView(request):
    taskresult = Task.objects.all()     #select tasks for viewing
    if request.method == 'POST':
        name = request.POST.get('taskname')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'ViewTask.html',{'taskres':taskresult})

def update(request,task_id):
    task = Task.objects.get(id=task_id)
    form = TodoForms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'Update.html',{'tasks':task,'form':form})
    
def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'DeleteTask.html',{'del_task':task})
