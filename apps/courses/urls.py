__date__ = '2018/4/20 23:37'


from django.urls import re_path
from .views import *

app_name = 'course'

urlpatterns = [
    re_path('^list/', CourseListView.as_view(), name='course_list'),
    re_path('^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    re_path('^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    re_path('^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comments'),
    # 添加课程评论
    re_path('^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    re_path('^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),
]