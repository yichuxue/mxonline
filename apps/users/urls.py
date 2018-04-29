__date__ = '2018/4/15 2:57'

from django.urls import re_path
from .views import *

app_name = 'users'

urlpatterns = [
    re_path('login/', LoginView.as_view(), name='login'),

    # 退出
    re_path('logout/', LogoutView.as_view(), name='logout'),
    re_path('register/', RegisterView.as_view(), name='register'),
    re_path('active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    re_path('forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    re_path('modify/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 用户信息
    re_path('users/info/$', UserinfoView.as_view(), name='user_info'),

    # 用户头像上传
    re_path('users/image/upload/$', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码
    re_path('users/update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),

    # 发送邮箱验证码
    re_path('users/send_email_code/$', SendEmailCodeView.as_view(), name='send_email_code'),

    # 修改邮箱
    re_path('users/update_email/$', UpdateEmailView.as_view(), name='update_email'),

    # 我的课程
    re_path('users/my_course/$', MyCourseView.as_view(), name='my_course'),

    # 我收藏的课程
    re_path('users/my_fav/org/$', MyFavOrgView.as_view(), name='my_fav_org'),

    # 我收藏的授课讲师
    re_path('users/my_fav/teacher/$', MyFavTeacherView.as_view(), name='my_fav_teacher'),

    # 我收藏的课程
    re_path('users/my_fav/course/$', MyFavCourseView.as_view(), name='my_fav_course'),

    # 我的消息
    re_path('users/my_message/$', MyMessageView.as_view(), name='my_message'),
]