from django.db import models
from django import forms

# class CaseDetails(forms.Form):
#
#     class Meta:
#         verbose_name_plural = "Case Details"
#
#     # STATUS
#     status = forms.CharField(required=False)
#
#     # REPORTED
#     reporter_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)
#     alt_phone_number = forms.CharField(required=True)
#     reported_date = forms.DateField(required=True)
#     reported_time = forms.TimeField(required=True)
#     location = forms.CharField(required=True)
#     landmark = forms.CharField(required=True)
#     pincode = forms.CharField(required=True)
#     can_pick_animal = forms.CharField(required=True)
#     animal_marking = forms.CharField(required=True)
#     animal_color = forms.CharField(required=True)
#     animal_picture_1 = forms.ImageField(upload_to='images/', required=True)
#     animal_picture_2 = forms.ImageField(upload_to='images/', required=False)
#     animal_picture_3 = forms.ImageField(upload_to='images/', required=False)
#     animal_picture_4 = forms.ImageField(upload_to='images/', required=False)
#     animal_picture_5 = forms.ImageField(upload_to='images/', required=False)
#     reporter_photo_id_1 = forms.ImageField(upload_to='images/', required=True)
#     reporter_photo_id_2 = forms.ImageField(upload_to='images/', required=False)
#
#
#     # ADDITIONAL DETAILS
#     animal_type = forms.CharField(required=False)
#     age_of_animal = forms.CharField(required=False)
#     pickup_date = forms.DateField(required=False)
#     pickup_time = forms.TimeField(required=False)
#     animal_temperament = forms.CharField(required=False)
#     gender = forms.CharField(required=False)
#     pregnant = forms.CharField(required=False)
#     breed = forms.CharField(required=False)
#     catchable = forms.CharField(required=False)
#     medical_history_other_issues = forms.TextField(required=False)
#     fit_for_surgery = forms.CharField(required=False)
#     vaccinated = forms.CharField(required=False)
#     dewormed = forms.CharField(required=False)
#     other_details = forms.CharField(required=False)
#     blood_test_report_1 = forms.FileField(required=False,upload_to='images/')
#     blood_test_report_2 = forms.FileField(required=False,upload_to='images/')
#     blood_test_report_3 = forms.FileField(required=False,upload_to='images/')
#     blood_test_report_4 = forms.FileField(required=False,upload_to='images/')
#     blood_test_report_5 = forms.FileField(required=False,upload_to='images/')
#
#     # OPERATIONAL DETAILS
#     admission_date = forms.DateField(required=False)
#     vet_assigned = forms.CharField(required=False)
#     operation_date = forms.DateField(required=False)
#     operation_cost = forms.FloatField(required=False)
#     operation_start_time = forms.TimeField(required=False)
#     operation_end_time = forms.TimeField(required=False)
#     operation_outcome = forms.CharField(required=False)
#     cause_of_failure = forms.CharField(required=False)
#     after_operation_pic_1 = forms.ImageField(required=False,upload_to='images/')
#     after_operation_pic_2 = forms.ImageField(required=False,upload_to='images/')
#     after_operation_pic_3 = forms.ImageField(required=False,upload_to='images/')
#     after_operation_pic_4 = forms.ImageField(required=False,upload_to='images/')
#     after_operation_pic_5 = forms.ImageField(required=False,upload_to='images/')
#
#     # POST OP DETAILS
#     post_op_comments = forms.CharField(required=False)
#     cage_num = forms.CharField(required=False)
#     post_op_start_date = forms.DateField(required=False)
#     post_op_start_time = forms.TimeField(required=False)
#     release_date = forms.DateField(required=False)
#     release_time = forms.TimeField(required=False)
#     other_comments = forms.CharField(required=False)
#     medicine_photos_1 = forms.ImageField(required=False,upload_to='images/')
#     medicine_photos_2 = forms.ImageField(required=False,upload_to='images/')
#     medicine_photos_3 = forms.ImageField(required=False,upload_to='images/')
#     medicine_photos_4 = forms.ImageField(required=False,upload_to='images/')
#     medicine_photos_5 = forms.ImageField(required=False,upload_to='images/')
#
#
#     def __str__(self):
#         return self.reporter_name+' '+self.location+' '+self.landmark

# Create your models here.


class CaseDetails(models.Model):

    class Meta:
        verbose_name_plural = "Case Details"

    # hide = models.

    # STATUS
    status = models.CharField(max_length=100, blank=True, null=True)

    # REPORTED
    reporter_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    case_per_page = models.CharField(max_length=100, blank=True, null=True)
    alt_phone_number = models.CharField(max_length=100, blank=True, null=True)
    reported_date = models.DateField(blank=True, null=True)
    reported_time = models.TimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    landmark = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    can_drop_animal = models.CharField(max_length=3, blank=True, null=True)
    animal_marking = models.CharField(max_length=100, blank=True, null=True)
    animal_color = models.CharField(max_length=100, blank=True, null=True)
    animal_picture_1 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    animal_picture_2 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    animal_picture_3 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    animal_picture_4 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    animal_picture_5 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    reporter_photo_id_1 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    reporter_photo_id_2 = models.FileField(upload_to='images/', default='images/upload_pic.jpg')
    consent_form = models.FileField(upload_to='images/', default='images/upload_pic.jpg')

    # ADDITIONAL DETAILS
    animal_type = models.CharField(max_length=100, blank=True, null=True)
    age_of_animal = models.CharField(max_length=100, blank=True, null=True)
    pickup_date = models.DateField(blank=True, null=True)
    pickup_time = models.TimeField(blank=True, null=True)
    animal_temperament = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    pregnant = models.CharField(max_length=100, blank=True, null=True)
    breed = models.CharField(max_length=100, blank=True, null=True)
    catchable = models.CharField(max_length=100, blank=True, null=True)
    medical_history_other_issues = models.TextField(blank=True, null=True)
    fit_for_surgery = models.CharField(max_length=100, blank=True, null=True)
    vaccinated = models.CharField(max_length=100, blank=True, null=True)
    dewormed = models.CharField(max_length=100, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    blood_test_report_1 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    blood_test_report_2 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    blood_test_report_3 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    blood_test_report_4 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    blood_test_report_5 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')

    # OPERATIONAL DETAILS
    admission_date = models.DateField(blank=True, null=True)
    vet_assigned = models.CharField(max_length=100, blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)
    operation_cost = models.FloatField(blank=True, null=True)
    operation_start_time = models.TimeField(blank=True, null=True)
    operation_end_time = models.TimeField(blank=True, null=True)
    operation_outcome = models.CharField(max_length=100, blank=True, null=True)
    cause_of_failure = models.TextField(blank=True, null=True)
    after_operation_pic_1 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    after_operation_pic_2 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    after_operation_pic_3 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    after_operation_pic_4 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    after_operation_pic_5 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')

    # POST OP DETAILS
    post_op_comments = models.TextField(blank=True, null=True)
    cage_num = models.CharField(max_length=100, blank=True, null=True)
    post_op_start_date = models.DateField(blank=True, null=True)
    post_op_start_time = models.TimeField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    release_time = models.TimeField(blank=True, null=True)
    other_comments = models.TextField(blank=True, null=True)
    medicine_photos_1 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    medicine_photos_2 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    medicine_photos_3 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    medicine_photos_4 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')
    medicine_photos_5 = models.FileField(
        blank=True, null=True, upload_to='images/', default='images/upload_pic.jpg')

    def __str__(self):
        return self.reporter_name+' '+self.location+' '+self.landmark
