from rest_framework import serializers
from . models import (EventDetails, EventAssociation, EventDelegates, EventDates,
                      EventExhibitor, EventLog, EventPartners, EventPartnerships,
                      EventSalesPersons, EventSpeakers, EventSupportedBy, EventTestimonials, EventVisitors,AboutUs,EventMediaPartner)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventDetails
        fields=('id',
                'vc_event_title',
                'vc_event_location',
                'vc_city',
                'vc_state',
                'country',
                'vc_status',
                'db_registrationCharge',
                'db_registrationTax',
                'db_registrationTotal',
                'vc_eventBanner',
                'vc_description',
                'vc_backgroundImage',
                'vc_agenda_link',
                'vc_brochure_link',
                'vc_floorPlan_link',
                'vc_eventType',
                'vc_eventCreatedEmpId',
                'dt_eventCreatedEmpDatetime',
                'dt_lastModifiedEmpId',
                'dt_lastModifiedDatetime',
                'vc_virtualPartner',
                'about_bg'
                )

class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventAssociation
        fields=('id',
                'ch_name',
                'vc_img_url',
                'vc_link',
                'vc_status',
                'dt_uploaded_datetime',
                'vc_uploadedEmpId',
                'dt_last_updated_datetime',
                'dt_last_updated_empid'
                )

class DelegateSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventDelegates
        fields=('id',
                'ch_name',
                'vc_designation',
                'vc_company',
                'vc_phonenum',
                'vc_mail',
                'vc_city',
                'vc_GST',
                'ft_amount_charged',
                'vc_purpose_of_registration',
                'vc_address',
                'vc_state',
                'vc_country',
                'dt_registered_datetime',
                'vc_status',
                )

class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventDates
        fields=('id',
                'dt_eventDates',
                'status',
                )
class ExhibitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventExhibitor
        fields = '__all__'

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = '__all__'

class EventPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPartners
        fields = '__all__'

class EventPartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPartnerships
        fields = '__all__'

class EventSalesPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSalesPersons
        fields = '__all__'

class EventSpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSpeakers
        fields = '__all__'

class EventSupportedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSupportedBy
        fields = '__all__'

class EventTestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTestimonials
        fields = '__all__'

class EventVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVisitors
        fields = '__all__'


class aboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class EventSerializerReq(serializers.ModelSerializer):
    class Meta:
        model=EventDetails
        fields=('req_conference',
                'req_exhibitors',
                'req_partners',
                'req_visitors',
                'req_virtual'
                )




class EventMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventMediaPartner
        fields=('vc_comapany_name',
                'vc_logo_link',
                'vc_company_url',
                )

class EventAssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventAssociation
        fields=('ch_name',
                'vc_img_url',
                'vc_link',
                )
