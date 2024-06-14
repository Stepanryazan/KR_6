from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, MessageListView, \
    MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, AttemptsListView, AttemptsDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('mailing_list/', MailingListView.as_view(), name='home'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
    path('mailing_create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),

    path('client_list/', ClientListView.as_view(), name='clients'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('client_create/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('message_list/', MessageListView.as_view(), name='messages'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('message_create/', MessageCreateView.as_view(), name='create_message'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('attempts_list/<int:pk>/', AttemptsListView.as_view(), name='attempts'),
    path('attempts_detail/<int:pk>/', AttemptsDetailView.as_view(), name='view_attempt'),
]