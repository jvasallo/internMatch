from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
    url(r'^$', 'quiz.views.index'),
#    url(r'^$',
#        ListView.as_view(
#            queryset=Quiz.objects.get(pk=1),
#            context_object_name='quiz',
#            template_name='quiz/quiz.html'))
    url(r'submit/', 'quiz.views.submit'),
    #url(r'^send$', TemplateView.as_view(template_name="signin.html")),
    #url(r'^send$', 'quiz.views.QuizResultsParsing'),
)
