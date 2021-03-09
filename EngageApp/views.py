"""
views.py
"""
import re

from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.db import IntegrityError
from .models import (EventDetails, EventAssociation, EventDelegates, EventDates,
                     EventExhibitor, EventLog, EventPartners, EventPartnerships,
                     EventSalesPersons, EventSpeakers, EventSupportedBy, EventTestimonials, EventVisitors, AboutUs,
                     EventExhibitor_1,GetInTouch,Gallary,
                     EventConference_1, EventVisitor_1, VirtualRegister, EventMediaPartner, ContactDeatils, Coupons)
from .serializers import (EventSerializer, AssociationSerializer, DelegateSerializer, EventDateSerializer,
                          ExhibitorSerializer, EventLogSerializer, EventPartnersSerializer, EventPartnershipSerializer,
                          EventSalesPersonSerializer, EventSpeakersSerializer, EventSupportedSerializer,
                          EventTestimonialsSerializer,EventSerializerUpcoming,
                          EventVisitorSerializer, aboutUsSerializer, EventSerializerReq, EventMediaSerializer,
                          EventAssociateSerializer,GallarySerializer)
from django.views.decorators.csrf import csrf_exempt
import datetime
from rest_framework import serializers


# Create your views here.
@csrf_exempt
@csrf_exempt
def filter_date_event1(request):
    if request.method == "POST":
        events = EventDetails.objects.filter(dt_eventCreatedEmpDatetime__gte=datetime.datetime.now()).values('id','vc_event_title','vc_backgroundImage','vc_description')[0:3]
        upcoming_serializer=EventSerializerUpcoming(events,many=True)
        return JsonResponse({'upcoming_events': upcoming_serializer.data}, safe=False)


@csrf_exempt
def filter_date_event2(request):
    if request.method == "POST":
        events = EventDetails.objects.filter(dt_eventCreatedEmpDatetime__gte=datetime.datetime.now()).values('id','vc_event_title','vc_backgroundImage','vc_description')
        upcoming_serializer=EventSerializerUpcoming(events,many=True)
        return JsonResponse({'upcoming_events_all': upcoming_serializer.data}, safe=False)


@csrf_exempt
def filter_date_event3(request):
    if request.method == "POST":
        events = EventDetails.objects.filter(dt_eventCreatedEmpDatetime__lte=datetime.datetime.now()).values('id','vc_event_title','vc_backgroundImage','vc_description')[0:3]
        event_serializer = EventSerializerUpcoming(events, many=True)
        return JsonResponse({'past_events': event_serializer.data}, safe=False)


@csrf_exempt
def filter_date_event4(request):
    if request.method == "POST":
        events = EventDetails.objects.filter(dt_eventCreatedEmpDatetime__lte=datetime.datetime.now()).values('id','vc_event_title','vc_backgroundImage','vc_description')
        event_serializer = EventSerializerUpcoming(events, many=True)
        return JsonResponse({'past_events_all': event_serializer.data}, safe=False)


class Eventslist(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        events = EventDetails.objects.filter(id=id).values()
        event_serializer = EventSerializer(events, many=True)

        return JsonResponse(event_serializer.data, safe=False)


class AllEventslist(APIView):
    def post(self, request):
        events = EventDetails.objects.all()
        event_serializer = EventSerializer(events, many=True)
        return JsonResponse({'allevents': event_serializer.data}, safe=False)


class EventDelegateslist(APIView):
    def post(self, request):
        delegates = EventDelegates.objects.all()
        event_serializer = DelegateSerializer(delegates, many=True)
        return JsonResponse({'delegates': event_serializer.data}, safe=False)


class EventDateslist(APIView):
    def post(self, request):
        dates = EventDates.objects.all()
        event_serializer = EventDateSerializer(dates, many=True)
        return JsonResponse({'events dates': event_serializer.data}, safe=False)


class EventExhibitorlist(APIView):
    def post(self, request):
        exhibitors = EventExhibitor.objects.all()
        event_serializer = ExhibitorSerializer(exhibitors, many=True)
        return JsonResponse({'exhibitor': event_serializer.data}, safe=False)


class EventLoglist(APIView):
    def post(self, request):
        logs = EventLog.objects.all()
        event_serializer = EventLogSerializer(logs, many=True)
        return JsonResponse({'event logs': event_serializer.data}, safe=False)


class EventPartnerslist(APIView):
    def post(self, request):
        partners = EventPartners.objects.all()
        event_serializer = EventPartnersSerializer(partners, many=True)
        return JsonResponse({'partners': event_serializer.data}, safe=False)


class EventPartnershipslist(APIView):
    def post(self, request):
        partnership = EventPartnerships.objects.all()
        event_serializer = EventPartnersSerializer(partnership, many=True)
        return JsonResponse({'partnership': event_serializer.data}, safe=False)


class EventSalespersonlist(APIView):
    def post(self, request):
        salesperson = EventSalesPersons.objects.all()
        event_serializer = EventSalesPersonSerializer(salesperson, many=True)
        return JsonResponse({'sales persons': event_serializer.data}, safe=False)


class EventSpeakerslist(APIView):
    def post(self, request):
        speakers = EventSpeakers.objects.all()
        event_serializer = EventSpeakersSerializer(speakers, many=True)
        return JsonResponse({'speakers': event_serializer.data}, safe=False)


class EventSupportedlist(APIView):
    def post(self, request):
        supporters = EventSupportedBy.objects.all()
        event_serializer = EventSupportedSerializer(supporters, many=True)
        return JsonResponse({'supported by': event_serializer.data}, safe=False)


class EventTestimonialslist(APIView):
    def post(self, request):
        testimonials = EventTestimonials.objects.all()
        event_serializer = EventTestimonialsSerializer(testimonials, many=True)
        return JsonResponse({'testimonials': event_serializer.data}, safe=False)


class EventVisitorslist(APIView):
    def post(self, request):
        visitors = EventVisitors.objects.all()
        event_serializer = EventVisitorSerializer(visitors, many=True)
        return JsonResponse({'visitors': event_serializer.data}, safe=False)


# @csrf_exempt
# def filter_date_event(request, id=0):
#     if request.method == "POST":
#         list1 = []
#         dict1 = {}
#         event1 = EventDetails.objects.filter(id=1).values()
#         event2 = EventDetails.objects.filter(id=2).values()
#         # events = EventDetails.objects.filter().all()
#         # list1.append(event)
#         event_serializer = EventSerializer(event1, many=True)
#         # list1.append(event_serializer.data)
#         dict1['event1'] = event1
#         dict1['event2'] = event2
#         return JsonResponse({'events': dict1}, safe=False)

@csrf_exempt
def association_data(request, id=0):
    if request.method == "POST":
        list1 = []
        association_data = EventAssociation.objects.filter().all()
        association_serializer = AssociationSerializer(association_data, many=True)
        for dict1 in association_serializer.data:
            dict2 = {}
            dict2['id'] = dict1['id']
            dict2['ch_name'] = dict1['ch_name']
            dict2['vc_img_url'] = dict1['vc_img_url']
            list1.append(dict2)
    return JsonResponse({'associations': list1}, safe=False)


@csrf_exempt
def association_data_order(request, id=0):
    if request.method == "POST":
        list1 = []
        association_data = EventAssociation.objects.order_by('ch_name').values()
        association_serializer = AssociationSerializer(association_data, many=True)
        for dict1 in association_serializer.data:
            dict2 = {}
            dict2['id'] = dict1['id']
            dict2['ch_name'] = dict1['ch_name']
            dict2['vc_img_url'] = dict1['vc_img_url']
            list1.append(dict2)
    return JsonResponse({'associations': list1}, safe=False)


@csrf_exempt
def association_data1(request, id=0):
    if request.method == "POST":
        list1 = []
        association_data = EventAssociation.objects.filter().all()
        association_serializer = AssociationSerializer(association_data, many=True)

    return JsonResponse({'associations': list1}, safe=False)


class EventData(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        events = EventDetails.objects.filter(id=id).values()
        supporters = EventSupportedBy.objects.filter(event_id=id).values()
        our_partners = EventPartners.objects.filter(event_id=id).values()
        media_partners = EventMediaPartner.objects.filter(event_id=id).values()
        speakers = EventSpeakers.objects.raw(
            "SELECT * FROM engageapp_eventspeakers WHERE event_id = {0} ORDER BY SUBSTRING_INDEX(SUBSTRING_INDEX("
            "vc_speaker_name, ' ', 2), ' ', -1)".format(
                id))
        association_partners = EventAssociation.objects.filter(event_id=id).values()

        event_serializer = EventSerializer(events, many=True)
        supported_serializer = EventSupportedSerializer(supporters, many=True)
        partners_serializer = EventPartnersSerializer(our_partners, many=True)
        speakers_serializer = EventSpeakersSerializer(speakers, many=True)
        association_serializer = AssociationSerializer(association_partners, many=True)
        media_serializer = EventMediaSerializer(media_partners, many=True)

        return JsonResponse({'events': event_serializer.data,
                             'supported_by': supported_serializer.data,
                             'our_partners': partners_serializer.data,
                             'speakers': speakers_serializer.data,
                             'associations': association_serializer.data,
                             'media': media_serializer.data
                             }, safe=False)


class AboutUsView(APIView):
    def post(self, request):
        about_us_data = AboutUs.objects.all()
        about_serializer = aboutUsSerializer(about_us_data, many=True)
        return JsonResponse({'about_us': about_serializer.data}, safe=False)

# POST METHODS FOR TABLES ####

class ContactDetailsRegister(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            contact_data = ContactDeatils.objects.create(
                first_name=register_data['first_name'],
                last_name=register_data['last_name'],
                email=register_data['email'],
                phone=register_data['phone'],
                designation=register_data['designation'],
                city=register_data['city'],
                register_for=register_data['register_for'],
            )

            contact_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class EventRegisterView(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            events_data = EventDetails.objects.create(
                vc_event_title=register_data['vc_event_title'],
                vc_event_location=register_data['vc_event_location'],
                vc_city=register_data['vc_city'],
                vc_state=register_data['vc_state'],
                country=register_data['country'],
                vc_status=register_data['vc_status'],
                db_registrationCharge=register_data['db_registrationCharge'],
                db_registrationTax=register_data['db_registrationTax'],
                db_registrationTotal=register_data['db_registrationTotal'],
                vc_eventBanner=register_data['vc_eventBanner'],
                vc_description=register_data['vc_description'],
                vc_backgroundImage=register_data['vc_backgroundImage'],
                vc_agenda_link=register_data['vc_agenda_link'],
                description=register_data['description'],
                vc_brochure_link=register_data['vc_brochure_link'],
                vc_floorPlan_link=register_data['vc_floorPlan_link'],
                vc_eventType=register_data['vc_eventType'],
                vc_eventCreatedEmpId=register_data['vc_eventCreatedEmpId'],
                dt_eventCreatedEmpDatetime=register_data['dt_eventCreatedEmpDatetime'],
                dt_lastModifiedEmpId=register_data['dt_lastModifiedEmpId'],
                dt_lastModifiedDatetime=register_data['dt_lastModifiedDatetime'],
                vc_virtualPartner=register_data['vc_virtualPartner'],
            )
            events_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class EventDateRegisterView(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            register_data = EventDates.objects.create(
                dt_eventDates=register_data['dt_eventDates'],
                status=register_data['status'],
            )

            register_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class PartnershipRegister(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            contact_data = EventPartnerships.objects.create(
                ch_firstname=register_data['ch_firstname'],
                ch_lastname=register_data['ch_lastname'],
                vc_designation=register_data['vc_designation'],
                vc_company=register_data['vc_company'],
                vc_phonenumber=register_data['vc_phonenumber'],
                vc_email=register_data['vc_email'],
                vc_city=register_data['vc_city'],
                vc_state=register_data['vc_state'],
                purpose=register_data['purpose'],
                register_for=register_data['register_for'],
            )

            rule1_chr = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
            pattern_comp = re.compile(r'^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$')
            rule3_ph = re.compile(r'^[0-9]{10}$')
            rule2_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            ch_firstname = register_data['ch_firstname']
            ch_lastname = register_data['ch_lastname']
            vc_designation = register_data['vc_designation']
            vc_company = register_data['vc_company']
            vc_phonenumber = register_data['vc_phonenumber']
            vc_email = register_data['vc_email']
            vc_city = register_data['vc_city']
            vc_state = register_data['vc_state']
            purpose = register_data['purpose']
            register_for = register_data['register_for']
            if not rule1_chr.search(ch_firstname):
                return JsonResponse("invalid first name", safe=False)
            elif not rule1_chr.search(ch_lastname):
                return JsonResponse("invalid last name", safe=False)
            elif not rule1_chr.search(vc_designation):
                return JsonResponse("invalid last name", safe=False)
            elif not pattern_comp.search(vc_company):
                return JsonResponse("invalid  company", safe=False)
            elif not rule3_ph.search(vc_phonenumber):
                return JsonResponse("invalid  phone", safe=False)
            elif not rule2_email.search(vc_email):
                return JsonResponse("invalid  email", safe=False)
            elif not rule1_chr.search(vc_city):
                return JsonResponse("invalid city", safe=False)
            elif not rule1_chr.search(vc_state):
                return JsonResponse("invalid state", safe=False)
            elif not rule1_chr.search(purpose):
                return JsonResponse("invalid purpose", safe=False)
            elif not rule1_chr.search(str(register_for)):
                return JsonResponse("invalid register for", safe=False)
            contact_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class ExhibitorRegister(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            contact_data = EventExhibitor_1.objects.create(
                ch_firstname=register_data['ch_firstname'],
                ch_lastname=register_data['ch_lastname'],
                vc_designation=register_data['vc_designation'],
                vc_company=register_data['vc_company'],
                vc_phonenumber=register_data['vc_phonenumber'],
                vc_email=register_data['vc_email'],
                vc_city=register_data['vc_city'],
                vc_state=register_data['vc_state'],
                purpose=register_data['purpose'],
                register_for=register_data['register_for'],
            )
            
            
            rule1_chr = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
            pattern_comp = re.compile(r'^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$')
            rule3_ph = re.compile(r'^[0-9]{10}$')
            rule2_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            ch_firstname = register_data['ch_firstname']
            ch_lastname = register_data['ch_lastname']
            vc_designation = register_data['vc_designation']
            vc_company = register_data['vc_company']
            vc_phonenumber = register_data['vc_phonenumber']
            vc_email = register_data['vc_email']
            vc_city = register_data['vc_city']
            vc_state = register_data['vc_state']
            purpose = register_data['purpose']
            register_for = register_data['register_for']
            if not rule1_chr.search(ch_firstname):
                return JsonResponse("invalid first name", safe=False)
            elif not rule1_chr.search(ch_lastname):
                return JsonResponse("invalid last name", safe=False)
            elif not rule1_chr.search(vc_designation):
                return JsonResponse("invalid last name", safe=False)
            elif not pattern_comp.search(vc_company):
                return JsonResponse("invalid  company", safe=False)
            elif not rule3_ph.search(vc_phonenumber):
                return JsonResponse("invalid  phone", safe=False)
            elif not rule2_email.search(vc_email):
                return JsonResponse("invalid  email", safe=False)
            elif not rule1_chr.search(vc_city):
                return JsonResponse("invalid city", safe=False)
            elif not rule1_chr.search(vc_state):
                return JsonResponse("invalid state", safe=False)
            elif not rule1_chr.search(purpose):
                return JsonResponse("invalid purpose", safe=False)
            elif not rule1_chr.search(str(register_for)):
                return JsonResponse("invalid register for", safe=False)

            contact_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class ConferenceRegister(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            print(register_data)
            rule1_chr = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
            pattern_comp = re.compile(r'^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$')
            rule3_ph = re.compile(r'^[0-9]{10}$')
            rule2_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            rule3_amount = re.compile("[0-9]*[.,]?[0-9]*")
            pattern_gstpan = re.compile(r'^[A-Za-z0-9_-]*$')
            ch_firstname = register_data['ch_firstname']
            ch_lastname = register_data['ch_lastname']
            vc_designation = register_data['vc_designation']
            vc_company = register_data['vc_company']
            vc_phonenumber = register_data['vc_phonenumber']
            vc_email = register_data['vc_email']
            vc_city = register_data['vc_city']
            vc_state = register_data['vc_state']
            purpose = register_data['purpose']
            register_for = register_data['register_for']
            total_amount = register_data['total_amount']
            gst_no = register_data['gst_no']
            address = register_data['address']
            if not rule1_chr.search(ch_firstname):
                return JsonResponse("invalid first name", safe=False)
            elif not rule1_chr.search(ch_lastname):
                return JsonResponse("invalid last name", safe=False)
            elif not rule1_chr.search(vc_designation):
                return JsonResponse("invalid last name", safe=False)
            elif not pattern_comp.search(vc_company):
                return JsonResponse("invalid  company", safe=False)
            elif not rule3_ph.search(vc_phonenumber):
                return JsonResponse("invalid  phone", safe=False)
            elif not rule2_email.search(vc_email):
                return JsonResponse("invalid  email", safe=False)
            elif not rule1_chr.search(vc_city):
                return JsonResponse("invalid city", safe=False)
            elif not rule1_chr.search(vc_state):
                return JsonResponse("invalid state", safe=False)
            elif not rule1_chr.search(purpose):
                return JsonResponse("invalid purpose", safe=False)
            elif not rule1_chr.search(str(register_for)):
                return JsonResponse("invalid register for", safe=False)
            elif not rule3_amount.search(str(total_amount)):
                return JsonResponse("invalid amount", safe=False)
            elif not pattern_gstpan.search(gst_no):
                return JsonResponse("invalid gst or pan", safe=False)
            elif not pattern_comp.search(address):
                return JsonResponse("invalid address", safe=False)

                print("hello")

            else:
                contact_data = EventConference_1.objects.create(
                    ch_firstname=register_data['ch_firstname'],
                    ch_lastname=register_data['ch_lastname'],
                    vc_designation=register_data['vc_designation'],
                    vc_company=register_data['vc_company'],
                    vc_phonenumber=register_data['vc_phonenumber'],
                    vc_email=register_data['vc_email'],
                    vc_city=register_data['vc_city'],
                    vc_state=register_data['vc_state'],
                    purpose=register_data['purpose'],
                    total_amount=register_data['total_amount'],
                    gst_no=register_data['gst_no'],
                    address=register_data['address'],
                    register_for=register_data['register_for']
                )
                contact_data.save()
                return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class VisitorRegister(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            contact_data = EventVisitor_1.objects.create(
                ch_firstname=register_data['ch_firstname'],
                ch_lastname=register_data['ch_lastname'],
                vc_designation=register_data['vc_designation'],
                vc_company=register_data['vc_company'],
                vc_phonenumber=register_data['vc_phonenumber'],
                vc_email=register_data['vc_email'],
                vc_city=register_data['vc_city'],
                vc_state=register_data['vc_state'],
                purpose=register_data['purpose'],
                register_for=register_data['register_for'],
            )
            
            

            contact_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class VirtualRegisterView(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            contact_data = VirtualRegister.objects.create(
                ch_firstname=register_data['ch_firstname'],
                ch_lastname=register_data['ch_lastname'],
                vc_designation=register_data['vc_designation'],
                vc_company=register_data['vc_company'],
                vc_phonenumber=register_data['vc_phonenumber'],
                vc_email=register_data['vc_email'],
                vc_city=register_data['vc_city'],
                vc_state=register_data['vc_state'],
                purpose=register_data['purpose'],
                total_amount=register_data['total_amount'],
                gst_no=register_data['gst_no'],
                address=register_data['address'],
                register_for=register_data['register_for'],
            )
            
            
            rule1_chr = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
            pattern_comp = re.compile(r'^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$')
            rule3_ph = re.compile(r'^[0-9]{10}$')
            rule2_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            rule3_amount = re.compile("[0-9]*[.,]?[0-9]*")
            pattern_gstpan = re.compile(r'^[A-Za-z0-9_-]*$')
            ch_firstname = register_data['ch_firstname']
            ch_lastname = register_data['ch_lastname']
            vc_designation = register_data['vc_designation']
            vc_company = register_data['vc_company']
            vc_phonenumber = register_data['vc_phonenumber']
            vc_email = register_data['vc_email']
            vc_city = register_data['vc_city']
            vc_state = register_data['vc_state']
            purpose = register_data['purpose']
            register_for = register_data['register_for']
            total_amount = register_data['total_amount']
            gst_no = register_data['gst_no']
            address = register_data['address']
            if not rule1_chr.search(ch_firstname):
                return JsonResponse("invalid first name", safe=False)
            elif not rule1_chr.search(ch_lastname):
                return JsonResponse("invalid last name", safe=False)
            elif not rule1_chr.search(vc_designation):
                return JsonResponse("invalid last name", safe=False)
            elif not pattern_comp.search(vc_company):
                return JsonResponse("invalid  company", safe=False)
            elif not rule3_ph.search(vc_phonenumber):
                return JsonResponse("invalid  phone", safe=False)
            elif not rule2_email.search(vc_email):
                return JsonResponse("invalid  email", safe=False)
            elif not rule1_chr.search(vc_city):
                return JsonResponse("invalid city", safe=False)
            elif not rule1_chr.search(vc_state):
                return JsonResponse("invalid state", safe=False)
            elif not rule1_chr.search(purpose):
                return JsonResponse("invalid purpose", safe=False)
            elif not rule1_chr.search(str(register_for)):
                return JsonResponse("invalid register for", safe=False)
            elif not rule3_amount.search(str(total_amount)):
                return JsonResponse("invalid amount", safe=False)
            elif not pattern_gstpan.search(gst_no):
                return JsonResponse("invalid gst or pan", safe=False)
            elif not pattern_comp.search(address):
                return JsonResponse("invalid address", safe=False)


            contact_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class EventRequired(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        events_req = EventDetails.objects.filter(id=id).values()
        event_serializer = EventSerializerReq(events_req, many=True)
        return JsonResponse({'events_req': event_serializer.data}, safe=False)
        # return JsonResponse("events_req", safe=False)


class DigitalPartner(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        partners = EventPartners.objects.raw(
            ("SELECT * FROM engageapp_eventpartners WHERE  event_id= {0} AND vc_partner_type='digital'").format(id))
        event_serializer = EventPartnersSerializer(partners, many=True)
        return JsonResponse({'digital_partners': event_serializer.data}, safe=False)


class AssociatePartner(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        partners = EventPartners.objects.raw(
            "SELECT * FROM engageapp_eventpartners WHERE event_id={0} AND vc_partner_type = 'associate'".format(id))
        event_serializer = EventPartnersSerializer(partners, many=True)
        return JsonResponse({'associate_partners': event_serializer.data}, safe=False)


class MediaPartner(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        partners = EventPartners.objects.raw(
            "SELECT * FROM engageapp_eventpartners WHERE event_id={0} AND vc_partner_type = 'media partner'".format(id))
        event_serializer = EventPartnersSerializer(partners, many=True)
        return JsonResponse({'associate_partners': event_serializer.data}, safe=False)


class MediaPartnerView(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        media_partners = EventMediaPartner.objects.filter(event_id=id).values()
        event_serializer = EventMediaSerializer(media_partners, many=True)
        return JsonResponse({'media': event_serializer.data}, safe=False)


class AssociateView(APIView):
    def post(self, request):
        register_data = JSONParser().parse(request)
        id = register_data['id']
        associate_partners = EventAssociation.objects.filter(event_id=id).values()
        event_serializer = EventAssociateSerializer(associate_partners, many=True)
        return JsonResponse({'associations': event_serializer.data}, safe=False)


class CouponValidate(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            id = register_data['id']
            coupon_code=register_data['coupon_code']
            event_type=register_data['event_type']
            event_data=EventDetails.objects.filter(id=id).values('db_registrationTotal', 'vc_eventType').first()
            if not event_data:
                return JsonResponse({"Error": "Event Does Not Exist"}, safe=False)
            # coupen_data=Coupons.objects.raw("SELECT * from engageapp_coupons WHERE event_id={0} and coupon_code={1}".format(id,coupon_code))
            coupon_data = Coupons.objects.filter(coupon_code=coupon_code, status=True
                                                 ).values('discount_amount', 'event_type').first()
            # print(coupon_data['event_type'])
            if coupon_data:
                if event_type != coupon_data['event_type']:
                    return JsonResponse({"Error":"event type and coupon type does not match"}, safe=False)
                if event_type != event_data['vc_eventType']:
                    return JsonResponse({"Error":"event type does not match"}, safe=False)
                net_amount = event_data['db_registrationTotal']-coupon_data['discount_amount']
                return JsonResponse({"new_amount": net_amount}, safe=False)
            else:
                return JsonResponse({'Error':'coupon does not exist!!'}, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse(str(e), safe=False)


class GetInRegister(APIView):
    def post(self, request):
        try:
            register_data = JSONParser().parse(request)
            contact_data = GetInTouch.objects.create(
                                                        name=register_data['name'],
                                                        mail=register_data['mail'],
                                                        phone=register_data['phone'],
                                                        company=register_data['company'],
                                                        message=register_data['message'],
                                                    )
            mail=register_data['mail']
            phone=register_data['phone']
            rule3_ph = re.compile(r'^[0-9]{10}$')
            rule2_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            if not rule2_email.search(mail):
                return JsonResponse("invalid Email", safe=False)
            elif not rule3_ph.search(phone):
                return JsonResponse("invalid phone", safe=False)

            contact_data.save()
            return JsonResponse("successfully registered!!", safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!', safe=False)


class EventGallary(APIView):
    def post(self, request):
        images = Gallary.objects.all()
        gallary_serializer = GallarySerializer(images, many=True)
        return JsonResponse({'gallary': gallary_serializer.data}, safe=False)
