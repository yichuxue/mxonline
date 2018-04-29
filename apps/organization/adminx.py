__date__ = '2018/4/15 0:55'

import xadmin


from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city__name']
    list_filter = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)