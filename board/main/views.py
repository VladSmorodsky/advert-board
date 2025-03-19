from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from main.models import Advert, Category, Comment


# Create your views here.
@staff_member_required
def admin_statistics(request: HttpRequest) -> HttpResponse:
    """
    Show statistics page.
    :param request:
    :return:
    """
    total_advert_count = Advert.objects.all().count()
    comments_count = Comment.objects.all().count()
    total_inactive_advert_count = Advert.objects.filter(is_active=False).count()
    total_active_advert_count = Advert.objects.filter(is_active=True).count()
    categories = Category.objects.annotate(advert_count=Count('adverts'))
    return render(request, 'admin/statistics.html', {
        'total_advert_count': total_advert_count,
        'total_inactive_advert_count': total_inactive_advert_count,
        'total_active_advert_count': total_active_advert_count,
        'comments_count': comments_count,
        'categories': categories,
    })


def home(request: HttpRequest) -> HttpResponse:
    """
    Redirect to adverts page
    """
    return redirect('adverts')


class AdvertListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Get adverts list with filtering results.
        :param request:
        :return:
        """
        advert_list = Advert.objects.filter(is_active=True).order_by('-created_at')
        if request.GET.get('category_id') is not None:
            advert_list = advert_list.filter(category__id=request.GET.get('category_id'))
        if request.GET.get('user_id') is not None:
            advert_list = advert_list.filter(user_id=request.GET.get('user_id'))
        return render(request, 'main/adverts.html', {'adverts': advert_list})


class AdvertDetailView(View):
    def get(self, request: HttpRequest, advert_id: int) -> HttpResponse:
        """
        Get advert detail page.
        :param request:
        :param advert_id:
        :return:
        """
        advert = get_object_or_404(Advert, id=advert_id)
        return render(request, 'main/advert_item.html', {'advert': advert})
