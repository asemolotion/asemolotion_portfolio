from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Project

class IndexView(TemplateView):
    """ 
    ポートフォリオサイトのトップページ。
    プロジェクトのリストが表示されている。 
    """
    template_name = 'general/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['project_list'] = Project.objects.all()

        return context

class AboutView(TemplateView):
    """
    サイトの概要ページ
    """
    template_name = 'general/about.html'


class ProjectView(DetailView):
    """
    プロジェクトの概要について説明する詳細ページ。各アプリへのリンクをもつページ。
    """
    model = Project
    template_name = 'general/project.html'    
