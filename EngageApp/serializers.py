from rest_framework import serializers
from .models import (EventDetails, EventAssociation, EventDelegates, EventDates,
                     EventExhibitor, EventLog, EventPartners, EventPartnerships,
                     EventSalesPersons, EventSpeakers, EventSupportedBy, EventTestimonials, EventVisitors, AboutUs,
                     EventMediaPartner,Gallary,MasterEvent)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ('__all__')
                  

class MasterEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterEvent
        fields = ('__all__')
        
                 
class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAssociation
        fields = ('id',
                  'ch_name',
                  'vc_img_url',
                  'vc_link',
                  'vc_status',
                  'dt_uploaded_datetime',
                  'vc_uploadedEmpId',
                  'dt_last_updated_datetime',
                  'dt_last_updated_empid',
                  'event_id',
                  )


class DelegateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDelegates
        fields = ('id',
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
                  'event_id',
                  )


class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDates
        fields = ('id',
                  'dt_eventDates',
                  'status',                
                  'event_id',
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
        fields = ('address',
                  'email',
                  'phone',
                  )

class EventSerializerReq(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ('req_conference',
                  'req_exhibitors',
                  'req_partners',
                  'req_visitors',
                  'req_virtual',
                  'event_id'
                  )


class EventMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMediaPartner
        fields = ('vc_comapany_name',
                  'vc_logo_link',
                  'vc_company_url',
                  'event_id'
                  )


class EventAssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAssociation
        fields = ('ch_name',
                  'vc_img_url',
                  'vc_link',
                  'event_id'
                  )

class EventSerializerUpcoming(serializers.ModelSerializer):
    class Meta:
        model=MasterEvent
        fields=(
                'id',
                'vc_main_title',
                'vc_backgroundImage',
                'vc_description'
            )

class GallarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallary
        fields = ('images',)
