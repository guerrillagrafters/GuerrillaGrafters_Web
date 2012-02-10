import logging
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseForbidden, HttpResponse

# This is a decorator that can be used to create a custom admin action that
# doesn't require selecting any objects. Specify a list of actions that can be used
# that don't need any objects passed to it.
class allowEmptyQuerySetForActions():

  def __init__(self, actions):
    self.actions = actions

  def __call__(self, original_class):

    def changelist_view(self, request, **kwargs):

      if( '_selected_action' not in request.POST and
          'action' in request.POST and request.POST['action'] in self.actions ):
        new_query_dict = request.POST.copy()
        new_query_dict.__setitem__('_selected_action', '0')
        request._post = new_query_dict

      return super(type(self), self).changelist_view(request, **kwargs)

    original_class.changelist_view = changelist_view
    return original_class

