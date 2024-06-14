from django.views.generic import TemplateView

from mailing.models import Mailing, Client
from main.services import get_cached_blogs


class HomeView(TemplateView):
    template_name = 'main/prohome.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings = Mailing.objects.all()
        clients = Client.objects.all()
        context_data['all_mailings'] = mailings.count()
        context_data['active_mailings'] = mailings.filter(status=Mailing.STARTED).count()
        context_data['active_clients'] = clients.values('email').distinct().count()

        context_data['random_blogs'] = get_cached_blogs().order_by('?')[:3]
        return context_data