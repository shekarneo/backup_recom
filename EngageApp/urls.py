from django.conf.urls import include, url
from . import views

from EngageProject import settings

# from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'EngageApp'

urlpatterns = [

    url(r'^date_filter/upcoming3/$', views.filter_date_event1),
    url(r'^date_filter/upcomingall/$', views.filter_date_event2),
    url(r'^date_filter/past3/$', views.filter_date_event3),
    url(r'^date_filter/pastall/$', views.filter_date_event4),
    url(r'^association_list/$', views.association_data),
    url(r'^association_list_order/$', views.association_data_order),
    url(r'^event_detail/$', views.Eventslist.as_view()),
    url(r'^alleventslist/$', views.AllEventslist.as_view()),
    url(r'^delegateslist/$', views.EventDelegateslist.as_view()),
    url(r'^eventdates/$', views.EventDateslist.as_view()),
    url(r'^loglist/$', views.EventLoglist.as_view()),
    url(r'^partners/$', views.EventPartnerslist.as_view()),
    url(r'^partnerships/$', views.EventPartnershipslist.as_view()),
    url(r'^salesperson/$', views.EventSalespersonlist.as_view()),
    url(r'^speakers/$', views.EventSpeakerslist.as_view()),
    url(r'^supported_by/$', views.EventSupportedlist.as_view()),
    url(r'^testimonials/$', views.EventTestimonialslist.as_view()),
    url(r'^visitors/$', views.EventVisitorslist.as_view()),
    url(r'^event_data/$', views.EventData.as_view()),
    url(r'^about_us/$', views.AboutUsView.as_view()),
    url(r'^gallary/$',views.EventGallary.as_view()),

    # API'S FOR POSTING THE DATA INTO THE TABLES ###

    url(r'^event_register/$', views.EventRegisterView.as_view()),
    url(r'^event_date_register/$', views.EventDateRegisterView.as_view()),
    url(r'^contact_register/$', views.ContactDetailsRegister.as_view()),
    url(r'^partnership_register/$', views.PartnershipRegister.as_view()),
    url(r'^exhibitor_register/$', views.ExhibitorRegister.as_view()),
    url(r'^conference_register/$', views.ConferenceRegister.as_view()),
    url(r'^visitor_register/$', views.VisitorRegister.as_view()),
    url(r'^virtual_register/$', views.VirtualRegisterView.as_view()),
    url(r'^required/$', views.EventRequired.as_view()),
    url(r'^digital_partners/$', views.DigitalPartner.as_view()),
    url(r'^associate_partners/$', views.AssociatePartner.as_view()),
    url(r'^media_partners/$', views.MediaPartner.as_view()),
    url(r'^media/$', views.MediaPartnerView.as_view()),
    url(r'^associations/$', views.AssociateView.as_view()),
    url(r'^coupon/$', views.CouponValidate.as_view()),
    url(r'^get_in_touch/$', views.GetInRegister.as_view()),
]

# if settings.DEBUG:
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
