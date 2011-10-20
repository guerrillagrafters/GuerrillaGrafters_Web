import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.contrib.gis.geos import Point, GEOSGeometry

from main.forms import *
from main.models import *

log = logging.getLogger(__name__)

gcoord = SpatialReference('EPSG:4326')
mycoord = SpatialReference('EPSG:900913')
trans = CoordTransform(gcoord, mycoord)


def add_tree(request):

  if request.method == 'POST':  
    form = AddTreeForm(request.POST)
    
    lat = request.POST['lat']
    lon = request.POST['lon']
    latlon = (float(lon), float(lat))
    point = Point(latlon, srid=4326).transform(trans, clone=True)
    tree = Tree(common_name="test tree", location=point)
    tree.save()
    return HttpResponseRedirect('/add_tree')
  else:
    form = AddTreeForm()  
    tree_points = []
    trees = Tree.objects.all()
    for tree in trees:
      tree.geom.transform(4326)
      pnt = GEOSGeometry(tree.geom.wkt) # WKT
      tree_points.append(pnt)
    c.update(dict(points=tree_points))
    log.info(c)
  return render_to_response("add_tree.html", {'form' : form}, RequestContext(request))


def index(request):
    return render_to_response("index.html", {}, RequestContext(request))

def register(request):
    print request.POST
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=new_user.username,
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, csrfContext)
