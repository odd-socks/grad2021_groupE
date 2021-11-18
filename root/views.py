from django.shortcuts import render
from django.views import generic
from .models import Facility

# Create your views here.
class TopView(generic.TemplateView):
    template_name = "root/top.html"

# class MapSelectView(LoginRequiredMixin, generic.MapSelectView):
class MapSelectView(generic.ListView):
    model = Facility
    template_name = "root/map_select.html"
    
    def get_queryset(self):
        roots = Blog.objects.filter(user=self.request.user).order_by('-created_at')
        return roots

# class MapCreateView(LoginRequiredMixin, generic.MapCleateView):
class MapCreateView(generic.ListView):
    model = User
    template_name = "root/map_create.html"
    form_class = RootCreateForm
    success_url = reverse_lazy('blog_furukawa:root_list')

    def form_valid(self,form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'ブログの作成に失敗しました。')
        return super().form_invalid(form)