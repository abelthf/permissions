from django.views.generic.list import ListView
from app.models import Todo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.forms import TodoForm
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


@method_decorator(permission_required('app.list_app'))
def listar(request):
    porhacer = Todo.objects.all()
    return render(request, 'app/listar.html', {'porhacer':porhacer})

class TodoList(ListView):
    model = Todo

class TodoDetail(DetailView):
    model = Todo
    @method_decorator(permission_required('app.view_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDetail, self).dispatch(*args, **kwargs)

class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    @method_decorator(permission_required('app.add_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return redirect(self.object)

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    @method_decorator(permission_required('app.change_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoUpdate, self).dispatch(*args, **kwargs)

class TodoDelete(DeleteView):
    model = Todo
    @method_decorator(permission_required('app.delete_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDelete, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        # To do this because the success_url class variable isn't reversed...
        return reverse('app_list')
