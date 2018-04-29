__date__ = '2018/4/16 22:22'

from django.urls import re_path
from .views import *

app_name = 'org'

urlpatterns = [
    re_path('^list/', OrgView.as_view(), name='org_list'),
    re_path('^add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path('^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    re_path('^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    re_path('^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    re_path('^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    re_path('^add_fav/', AddFavView.as_view(), name='add_fav'),

    # 讲师列表页
    re_path('^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),

    # 讲师详情页
    re_path('^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
]