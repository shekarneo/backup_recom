from django.db import models


# Create your models here.

class MasterEvent(models.Model):
    id = models.AutoField(primary_key=True)
    vc_main_title = models.CharField(max_length=200, blank=True, null=True)
    vc_event_location = models.CharField(max_length=200, null=True, blank=True)
    vc_city = models.CharField(max_length=200, null=True, blank=True)
    vc_state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    vc_status = models.CharField(max_length=200, null=True, blank=True)
    db_registrationCharge = models.FloatField(null=True, blank=True)
    db_registrationTax = models.FloatField(null=True, blank=True)
    db_registrationTotal = models.FloatField(null=True, blank=True)
    vc_eventBanner = models.CharField(max_length=300, null=True, blank=True)
    vc_description = models.CharField(max_length=5000, null=True, blank=True)
    vc_backgroundImage = models.CharField(max_length=300, null=True, blank=True)
    vc_agenda_link = models.CharField(max_length=200, null=True, blank=True)
    vc_brochure_link = models.CharField(max_length=200, null=True, blank=True)
    vc_floorPlan_link = models.CharField(max_length=200, null=True, blank=True)
    vc_eventType = models.CharField(max_length=200, null=True, blank=True)
    vc_eventCreatedEmpId = models.CharField(max_length=200, null=True, blank=True)
    dt_eventCreatedEmpDatetime = models.DateTimeField(null=True, blank=True)
    dt_lastModifiedEmpId = models.CharField(max_length=200, null=True, blank=True)
    dt_lastModifiedDatetime = models.DateTimeField(null=True, blank=True)
    vc_virtualPartner = models.CharField(max_length=200, null=True, blank=True)
    req_conference = models.BooleanField(default=True, null=True, blank=True)
    req_exhibitor = models.BooleanField(default=True)
    req_partners = models.BooleanField(default=True)
    req_visitor = models.BooleanField(default=True)
    req_virtual = models.BooleanField(default=True)
    about_bg = models.CharField(max_length=100, null=True, blank=True)
    event_date = models.CharField(max_length=100, null=True, blank=True)
    news =  models.CharField(max_length=500, null=True, blank=True)
    presentation =  models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}"




class EventDetails(models.Model):
    id = models.AutoField(primary_key=True)
    master_event_id = models.ForeignKey(MasterEvent, default=1, on_delete=models.SET_NULL, null=True)
    vc_event_title = models.CharField(max_length=200, blank=True)
    vc_event_location = models.CharField(max_length=200)
    vc_status = models.CharField(max_length=200)
    db_registrationCharge = models.FloatField()
    db_registrationTax = models.FloatField()
    db_registrationTotal = models.FloatField()
    vc_eventBanner = models.CharField(max_length=300)
    vc_description = models.CharField(max_length=5000)
    vc_backgroundImage = models.CharField(max_length=300)
    vc_agenda_link = models.CharField(max_length=200)
    vc_brochure_link = models.CharField(max_length=200)
    vc_floorPlan_link = models.CharField(max_length=200)
    vc_eventType = models.CharField(max_length=200)
    vc_eventCreatedEmpId = models.CharField(max_length=200)
    dt_eventCreatedEmpDatetime = models.DateTimeField()
    dt_lastModifiedEmpId = models.CharField(max_length=200)
    dt_lastModifiedDatetime = models.DateTimeField()
    event_date = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.vc_event_title


class EventImages(models.Model):
    id = models.AutoField(primary_key=True)
    vc_event_images = models.CharField(max_length=200, blank=True, null=True)
    image_description = models.CharField(max_length=200, blank=True, null=True)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_event_images



class EventAssociation(models.Model):
    id = models.AutoField(primary_key=True)
    ch_name = models.CharField(max_length=200)
    vc_img_url = models.CharField(max_length=200)
    vc_link = models.CharField(max_length=200)
    vc_status = models.CharField(max_length=200)
    dt_uploaded_datetime = models.DateTimeField()
    vc_uploadedEmpId = models.CharField(max_length=200)
    dt_last_updated_datetime = models.DateTimeField()
    dt_last_updated_empid = models.CharField(max_length=200)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_name



class EventDelegates(models.Model):
    id = models.AutoField(primary_key=True)
    ch_name = models.CharField(max_length=200)
    vc_designation = models.CharField(max_length=200)
    vc_company = models.CharField(max_length=200)
    vc_phonenum = models.CharField(max_length=200)
    vc_mail = models.CharField(max_length=200)
    vc_city = models.CharField(max_length=200)
    vc_GST = models.CharField(max_length=200)
    ft_amount_charged = models.FloatField()
    vc_purpose_of_registration = models.CharField(max_length=200)
    vc_address = models.CharField(max_length=200)
    vc_state = models.CharField(max_length=200)
    vc_country = models.CharField(max_length=200)
    dt_registered_datetime = models.DateTimeField()
    vc_status = models.CharField(max_length=200)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_name



class EventDates(models.Model):
    id = models.AutoField(primary_key=True)
    dt_eventDates = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.dt_eventDates



class EventExhibitor(models.Model):
    id = models.AutoField(primary_key=True)
    vc_company_name = models.CharField(max_length=200)
    vc_company_logo_link = models.CharField(max_length=400)
    vc_company_website_url = models.CharField(max_length=400)
    vc_phone_number = models.CharField(max_length=200)
    vc_mail_id = models.CharField(max_length=200)
    vc_contact_person = models.CharField(max_length=200)
    vc_contact_person_phno = models.CharField(max_length=200)
    vc_contact_person_email = models.CharField(max_length=200)
    ft_amount_charged = models.FloatField()
    ft_tax_charged = models.FloatField()
    fl_total_amount = models.FloatField()
    vc_status = models.CharField(max_length=200)
    vc_created_empid = models.CharField(max_length=200)
    dt_created_datetime = models.DateTimeField()
    dt_last_modified_datetime = models.DateTimeField()
    vc_last_modified_empid = models.CharField(max_length=200)
    vc_stall_code = models.CharField(max_length=200)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_company_name



class EventLog(models.Model):
    id = models.AutoField(primary_key=True)
    vc_log_type = models.CharField(max_length=200)
    vc_logDescription = models.CharField(max_length=1000)
    dt_logDatetime = models.DateTimeField()
    
    def __str__(self):
        return self.vc_log_type



class EventPartners(models.Model):
    id = models.AutoField(primary_key=True)
    vc_partner_name = models.CharField(max_length=200)
    vc_partner_logo_link = models.CharField(max_length=400)
    vc_partner_website_url = models.CharField(max_length=400)
    vc_status = models.CharField(max_length=200)
    vc_partner_type = models.CharField(max_length=200)
    dt_created_datetime = models.DateTimeField()
    vc_created_by_empid = models.CharField(max_length=200)
    ft_amount_charged = models.FloatField()
    last_modified_datetime = models.DateTimeField()
    last_modified_empid = models.CharField(max_length=200)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_partner_name



class EventPartnerships(models.Model):
    id = models.AutoField(primary_key=True)
    ch_firstname = models.CharField(max_length=200, default='')
    ch_lastname = models.CharField(max_length=200, default='')
    vc_designation = models.CharField(max_length=400, default='')
    vc_company = models.CharField(max_length=400, default='')
    vc_phonenumber = models.CharField(max_length=200, default='')
    vc_email = models.CharField(max_length=200, default='')
    vc_city = models.CharField(max_length=200, default='')
    vc_state = models.CharField(max_length=200, default='')
    purpose = models.CharField(max_length=2000, default='')
    register_for = models.CharField(max_length=500, null=True, blank=True)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_firstname



class EventSalesPersons(models.Model):
    id = models.AutoField(primary_key=True)
    vc_empid = models.CharField(max_length=200)
    vc_status = models.CharField(max_length=400)
    vc_added_by_empid = models.CharField(max_length=400)
    dt_added_datetime = models.DateTimeField()
    vc_removed_empid = models.CharField(max_length=200)
    dt_removed_datetime = models.DateTimeField()
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_empid



class EventSpeakers(models.Model):
    id = models.AutoField(primary_key=True)
    vc_speaker_name = models.CharField(max_length=200)
    vc_designation = models.CharField(max_length=400)
    vc_img_link = models.CharField(max_length=300)
    vc_linkedin_link = models.CharField(max_length=300)
    vc_twitter_link = models.CharField(max_length=300)
    vc_about_speaker = models.CharField(max_length=2000)
    vc_status = models.CharField(max_length=200)
    vc_created_EmpId = models.CharField(max_length=500)
    dt_created_datetime = models.DateTimeField()
    vc_last_modified_empid = models.CharField(max_length=500)
    dt_last_modified_datetime = models.DateTimeField()
    vidio_url=models.CharField(max_length=4000,null=True)
    presentation=models.CharField(max_length=500,null=True)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_speaker_name



class EventSupportedBy(models.Model):
    id = models.AutoField(primary_key=True)
    vc_comapany_name = models.CharField(max_length=200)
    vc_logo_link = models.CharField(max_length=400)
    vc_status = models.CharField(max_length=200)
    vc_priority = models.IntegerField()
    vc_company_url = models.CharField(max_length=300)
    vc_created_datetime = models.DateTimeField()
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_comapany_name



class EventTestimonials(models.Model):
    id = models.AutoField(primary_key=True)
    vc_name = models.CharField(max_length=200)
    vc_img_url = models.CharField(max_length=400)
    vc_vidio_url = models.CharField(max_length=300)
    vc_comments = models.CharField(max_length=300)
    vc_status = models.CharField(max_length=300)
    vc_type = models.CharField(max_length=300)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_name



class EventVisitors(models.Model):
    id = models.AutoField(primary_key=True)
    vc_name = models.CharField(max_length=200)
    vc_designation = models.CharField(max_length=200)
    vc_company = models.CharField(max_length=200)
    vc_phone = models.CharField(max_length=200)
    vc_mail = models.CharField(max_length=200)
    vc_city = models.CharField(max_length=200)
    dt_created_datetime = models.DateTimeField()
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_name



class GetInTouch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    company = models.CharField(max_length=200,null=True)
    message = models.CharField(max_length=2000,null=True)


class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=5000)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)


class ContactDetails(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    register_for = models.CharField(max_length=400)


class EventExhibitor_1(models.Model):
    id = models.AutoField(primary_key=True)
    ch_firstname = models.CharField(max_length=200, default='')
    ch_lastname = models.CharField(max_length=200, default='')
    vc_designation = models.CharField(max_length=400, default='')
    vc_company = models.CharField(max_length=400, default='')
    vc_phonenumber = models.CharField(max_length=200, default='')
    vc_email = models.CharField(max_length=200, default='')
    vc_city = models.CharField(max_length=200, default='')
    vc_state = models.CharField(max_length=200, default='')
    purpose = models.CharField(max_length=2000, default='')
    register_for = models.CharField(max_length=2000, default='')
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_firstname



class EventConference_1(models.Model):
    id = models.AutoField(primary_key=True)
    ch_firstname = models.CharField(max_length=200, default='')
    ch_lastname = models.CharField(max_length=200, default='')
    vc_designation = models.CharField(max_length=400, default='')
    vc_company = models.CharField(max_length=400, default='')
    vc_phonenumber = models.CharField(max_length=200, default='')
    vc_email = models.CharField(max_length=200, default='')
    vc_city = models.CharField(max_length=200, default='')
    vc_state = models.CharField(max_length=200, default='')
    purpose = models.CharField(max_length=2000, default='')
    event_charges = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    total_amount = models.FloatField()
    gst_no = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=2000, default='')
    register_for = models.CharField(max_length=2000, default='')
    coupen = models.CharField(max_length=200, default='')
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_firstname



class EventVisitor_1(models.Model):
    id = models.AutoField(primary_key=True)
    ch_firstname = models.CharField(max_length=200, default='')
    ch_lastname = models.CharField(max_length=200, default='')
    vc_designation = models.CharField(max_length=400, default='')
    vc_company = models.CharField(max_length=400, default='')
    vc_phonenumber = models.CharField(max_length=200, default='')
    vc_email = models.CharField(max_length=200, default='')
    vc_city = models.CharField(max_length=200, default='')
    vc_state = models.CharField(max_length=200, default='')
    purpose = models.CharField(max_length=2000, default='')
    register_for = models.CharField(max_length=2000, default='')
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_firstname



class VirtualRegister(models.Model):
    id = models.AutoField(primary_key=True)
    ch_firstname = models.CharField(max_length=200, default='')
    ch_lastname = models.CharField(max_length=200, default='')
    vc_designation = models.CharField(max_length=400, default='')
    vc_company = models.CharField(max_length=400, default='')
    vc_phonenumber = models.CharField(max_length=200, default='')
    vc_email = models.CharField(max_length=200, default='')
    vc_city = models.CharField(max_length=200, default='')
    vc_state = models.CharField(max_length=200, default='')
    purpose = models.CharField(max_length=2000, default='')
    event_charges = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    total_amount = models.FloatField()
    gst_no = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=2000, default='')
    register_for = models.CharField(max_length=2000, default='')
    coupen = models.CharField(max_length=200, default='')
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.ch_firstname



class EventMediaPartner(models.Model):
    id = models.AutoField(primary_key=True)
    vc_comapany_name = models.CharField(max_length=200)
    vc_logo_link = models.CharField(max_length=400)
    vc_status = models.CharField(max_length=200)
    vc_priority = models.IntegerField()
    vc_company_url = models.CharField(max_length=300)
    vc_created_datetime = models.DateTimeField()
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.vc_comapany_name



class Coupons(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=200)
    discount_amount = models.FloatField()
    status = models.BooleanField(default=True)
    created_by_empid = models.IntegerField()
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField()
    event_type = models.CharField(max_length=100, null=True)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)

class Gallary(models.Model):
    id = models.AutoField(primary_key=True)
    images = models.CharField(max_length=200)
    event_id = models.ForeignKey(EventDetails, default=1, on_delete=models.SET_NULL, null=True)
