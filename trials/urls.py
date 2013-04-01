from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url

import trials.apps.people.views
import trials.apps.exercises.views

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'apps.core.views.index'),
    url(r'^about$', 'apps.core.views.about'),
    url(r'^contact$', 'apps.core.views.contact'),

    # Students
    url(r'^students$', trials.apps.people.views.StudentList.as_view(),
        name='student_list'),
    url(r'^students/(?P<pk>\w+)$',
        trials.apps.people.views.StudentDetail.as_view(),
        name='student_detail'),

    url(r'exercises$', trials.apps.exercises.views.ExerciseList.as_view(),
        name='exercise_list'),
    url(r'exercises/(?P<pk>\w+)$',
        trials.apps.exercises.views.ExerciseDetail.as_view(),
        name='exercise_detail'),
)
