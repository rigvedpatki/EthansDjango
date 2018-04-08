from django.shortcuts import render
from app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    topic_list = Topic.objects.order_by('top_name')
    date_dict = {
        'access_records': webpage_list,
        'topic_records': topic_list
    }
    return render(request, 'app/index.html', context= date_dict)

