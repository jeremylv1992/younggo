# coding=utf-8
from common.log import logger
from common.model2json import render_mjson, to_dict

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from home.models import School

def locate_school(request):
    '''
    @summary: 定位到学校
    '''
    school_id = request.GET.get('school_id', '')
    if school_id != '':
        try:
            school = School.objects.get(id=school_id)
            request.session['school_id'] = school.id
        except Exception, e:
            logger.error(e) 
    return HttpResponseRedirect(reverse('home'))   
    

def locate_required(fun):
    def _wrap(request, *args, **kwargs):
        if not request.session.__contains__('school_id'):
            schools = School.objects.all()
            if schools.count() > 0:
                request.session['school_id'] = schools[0].id
            else:
                return HttpResponse(u"网站建设中。。。")
        return fun(request, *args, **kwargs)
    return _wrap

def get_school_list(request):
    '''
    @summary: 返回学校信息列表
    '''
    s_list = [to_dict(_s) for _s in School.objects.all()]
    return render_mjson(s_list)