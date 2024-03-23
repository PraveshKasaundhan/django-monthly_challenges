from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    'january': 'Jumping JAN',
    'february': 'Funny FEB',
    'march': 'Marching MAR',
    'april': 'Attitue APR',
    'may': 'Maybe MAY',
    'june': 'Jiggly JUN',
    'july': 'Jammer JUL',
    'august': 'Awkward AUG',
    'september': 'Sleepy SEP',
    'october': 'Outdoor OCT',
    'november': 'Nemesis NOV',
    'december': None #'Dumping DEC'
}


def index(request):
    mytext = 'qwerty'
    myhtml = "<ul>"
    months=list(monthly_challenges.keys())
    month_urls=list(monthly_challenges.values())
    for month in months:
        month_cap = month.capitalize()
        reverse_path = reverse('month-challenge', args=[month])
        line = f"<li><a href='{reverse_path}'>{month_cap}</a></li>"
        myhtml += line
    myhtml += "</ul>"
    # return HttpResponse(myhtml)
    res_dic={
        "months":months,
        "month_urls":month_urls
    }
    return render(request,"challenges/index.html",res_dic)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month-1]
    except:
        # return HttpResponseNotFound("OOPS! Invalid Month Number")
        raise Http404()

    ridirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(ridirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        # return HttpResponseNotFound("OOPS! There is no such Month")
        # res_data=render_to_string("404.html")
        # return HttpResponse(res_data)
        raise Http404()
    # response_data = f"<h1>{challenge_text}</h1>"
    # response_data = render_to_string(template_name="challenges/challenge.html")
    # return HttpResponse(response_data)
    res_dic = {
        "month_name":month,
        "text":challenge_text
    }
    return render(request,"challenges/challenge.html",res_dic)
