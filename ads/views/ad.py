import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from ads.models import Ad, Category
from dz_dj_1.settings import TOTAL_ON_PAGE
from users.models import User


"""
Стартовая страница.
"""
def start(request):
    return JsonResponse({"status": "ok"}, status=200)


"""
Список объявлений с пагинацией по 10 на странице.
"""
class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        # ads = self.object_list.all()
        self.object_list = self.object_list.order_by('-price')
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page = request.GET.get('page')
        obj = paginator.get_page(page)
        response = {}
        items_list = [{'id': ad.pk,
                     'name': ad.name,
                     'author': ad.author_id.first_name,
                     'price': ad.price,
                     'description': ad.description,
                     'is_published': ad.is_published,
                     'category': ad.category_id.name,
                     'image': ad.image.url if ad.image else None} for ad in obj]
        response['items'] = items_list
        response['total'] = self.object_list.count()
        response['num_pages'] = paginator.num_pages

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


"""
Вывод указанного объявление.
"""
class AdDetailView(DetailView):
    # queryset = Ad.objects.all()
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author': ad.author_id.username,
            'price': ad.price,
            'description': ad.description,
            'category': ad.category_id.name,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None
        }, safe=False, json_dumps_params={"ensure_ascii": False})


"""
Создание объявления.
"""
@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        author = get_object_or_404(User, username=data['author'])
        category = get_object_or_404(Category, name=data['category'])

        ad = Ad.objects.create(
            name=data['name'],
            price=data['price'],
            description=data['description'],
            is_published=data['is_published'],
            author_id=author,
            category_id=category,
        )
        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author': ad.author_id.username,
            'price': ad.price,
            'description': ad.description,
            'category': ad.category_id.name,
            'is_published': ad.is_published,
        }, safe=False, json_dumps_params={"ensure_ascii": False})


"""
Добавление ссылки на медиафайл к указанному объявлению.
"""
@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImage(UpdateView):
    model = Ad
    fields = ['name']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name,
            'author': self.object.author_id.username,
            'price': self.object.price,
            'description': self.object.description,
            'category': self.object.category_id.name,
            'is_published': self.object.is_published,
            'image': self.object.image.url if self.object.image else None
        }, safe=False, json_dumps_params={"ensure_ascii": False})


"""
Обновление указанного объявления.
"""
@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        # author = get_object_or_404(User, data['author'])
        # category = get_object_or_404(Category, data['category'])
        if 'name' in data:
            self.object.name = data['name']
        if 'price' in data:
            self.object.price = data['price']
        if 'description' in data:
            self.object.description = data['description']
        if 'is_published' in data:
            self.object.is_published = data['is_published']
        self.object.save()
        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name,
            'author': self.object.author_id.username,
            'price': self.object.price,
            'description': self.object.description,
            'category': self.object.category_id.name,
            'is_published': self.object.is_published,
        }, safe=False, json_dumps_params={"ensure_ascii": False})


"""
Удаление указанного объявления.
"""
@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)

