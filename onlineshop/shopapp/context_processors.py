from . models import Category
app_name = 'shopapp'

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)