from django.views.generic import View
from django.shortcuts import render
from apps.course.models import CourseCategory,Teacher,Course
from .forms import AddCourseForm
from utils import restful
from apps.xfzauth.decorators import xfz_permission_required
from django.utils.decorators import method_decorator

@method_decorator(xfz_permission_required(Course),name='dispatch')
class PubCourse(View):
    def get(self,request):
        context = {
            'categories':CourseCategory.objects.all(),
            'teachers':Teacher.objects.all()
        }
        return render(request,'cms/pub_course.html',context=context)

    def post(self,request):
        form = AddCourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category_id = form.cleaned_data.get('category_id')
            video_url = form.cleaned_data.get('video_url')
            cover_url = form.cleaned_data.get('cover_url')
            price = form.cleaned_data.get('price')
            duration = form.cleaned_data.get('duration')
            profile = form.cleaned_data.get('profile')
            teacher_id = form.cleaned_data.get('teacher_id')

            category = CourseCategory.objects.get(pk=category_id)
            teacher = Teacher.objects.get(pk=teacher_id)

            Course.objects.create(title=title,video_url=video_url,cover_url=cover_url,price=price,profile=profile,
                                  duration=duration,category=category,teacher=teacher)


            return restful.ok()
        else:
            return restful.params_error(message=form.get_error())
