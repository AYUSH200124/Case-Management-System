from sterilization_module.models import CaseDetails
from .utils import Calendar
from django.utils.safestring import mark_safe
from django.views import generic
from django.core.paginator import Paginator
import csv
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from .models import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'sterilization_module/login.html', {'error': "Username or Password is incorrect."})
    else:
        return render(request, 'sterilization_module/login.html')


# @login_required(login_url="/sterilization/login")
def logout(request):
    # TODO Need to route to login page
    # Don't forget to logout
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'sterilization_module/login.html')


# @login_required(login_url="/sterilization/login")
def dashboard(request):
    error_message = None
    all_cases = None
    if "search" in request.GET:  # this will be GET now
        search_by = request.GET['search_by']
        search_field = request.GET.get('search')
        try:
            if search_by == "Status":
                all_cases = CaseDetails.objects.filter(status__icontains=search_field)
            elif search_by == "Case ID":
                all_cases = CaseDetails.objects.filter(pk__icontains=search_field)
            elif search_by == "Location":
                all_cases = CaseDetails.objects.filter(location__icontains=search_field)
            elif search_by == "Landmark":
                all_cases = CaseDetails.objects.filter(landmark__icontains=search_field)
            elif search_by == "Pincode":
                all_cases = CaseDetails.objects.filter(pincode__icontains=search_field)
            elif search_by == "Reporter Name":
                all_cases = CaseDetails.objects.filter(reporter_name__icontains=search_field)

            if not all_cases:
                all_cases = CaseDetails.objects.order_by('-pk')
                error_message = search_by+" does not exist"
        except ValueError as e:
            all_cases = CaseDetails.objects.order_by('-pk')
            error_message = "Please enter an appropriate "+search_by
    else:
        all_cases = CaseDetails.objects.order_by('-pk')

    p = Paginator(CaseDetails.objects.all(),  2)

    page = request.GET.get('page')
    c = p.get_page(page)
    num_reported_cases = len(CaseDetails.objects.filter(status="Reported"))
    num_admitted_cases = len(CaseDetails.objects.filter(status="Admitted"))
    num_released_cases = len(CaseDetails.objects.filter(status="Released"))
    blood_test_done_cases = len(CaseDetails.objects.filter(status="Blood Test Done"))
    operation_started_cases = len(CaseDetails.objects.filter(status="Operation Started"))
    post_operation = len(CaseDetails.objects.filter(status="Post Operation"))
    pending_cases = len(CaseDetails.objects.all()) - num_released_cases

    return render(request, 'sterilization_module/dashboard.html', {"error": error_message, "all_cases": all_cases, "total_num_cases": len(CaseDetails.objects.all()), "num_reported_cases": num_reported_cases, "num_admitted_cases": num_admitted_cases, "num_reported_cases": num_reported_cases, "num_released_cases": num_released_cases, "c": c})


def case_delete(request, pk):
    data = get_object_or_404(CaseDetails, pk=pk)

    if request.method == "POST":
        data.delete()
        return redirect('dashboard')
    elif request.method != "POST":
        context = {"object": data}
        return render(request, 'sterilization_module/case_delete.html', context)


# @login_required(login_url="/sterilization/login")
def case_details(request, pk=None):
    case_detail = get_object_or_404(CaseDetails, pk=pk)
    if request.method == "POST":
        case_detail = CaseDetails.objects.filter(pk=pk)[0]
        if request.POST.get("status", None) is not None:
            case_detail.status = request.POST.get("status", None)
        if request.POST["reporter_name"] != "":
            case_detail.reporter_name = request.POST["reporter_name"]
        if request.POST["phone_number"] != "":
            case_detail.phone_number = request.POST["phone_number"]
        if request.POST["alt_phone_number"] != "":
            case_detail.phone_number = request.POST["alt_phone_number"]
        if request.POST["reported_time"] != "":
            case_detail.reported_time = request.POST["reported_time"]
        if request.POST["location"] != "":
            case_detail.location = request.POST["location"]
        if request.POST["landmark"] != "":
            case_detail.landmark = request.POST["landmark"]
        if request.POST["pincode"] != "":
            case_detail.pincode = request.POST["pincode"]
        if request.POST.get("can_drop_animal", None) is not None:
            case_detail.can_drop_animal = request.POST.get("can_drop_animal", None)
        if request.POST["animal_marking"] != "":
            case_detail.animal_marking = request.POST["animal_marking"]
        if request.POST["animal_color"] != "":
            case_detail.animal_color = request.POST["animal_color"]
        if request.FILES.get('reporter_photo_id_1') is not None:
            case_detail.reporter_photo_id_1 = request.FILES.get("reporter_photo_id_1")
        if request.FILES.get('reporter_photo_id_2') is not None:
            case_detail.reporter_photo_id_2 = request.FILES.get("reporter_photo_id_2")
        if request.FILES.get("animal_picture_1") is not None:
            case_detail.animal_picture_1 = request.FILES.get("animal_picture_1")
        if request.FILES.get("animal_picture_2") is not None:
            case_detail.animal_picture_2 = request.FILES.get("animal_picture_2")
        if request.FILES.get("animal_picture_3") is not None:
            case_detail.animal_picture_3 = request.FILES.get("animal_picture_3")
        if request.FILES.get("animal_picture_4") is not None:
            case_detail.animal_picture_4 = request.FILES.get("animal_picture_4")
        if request.FILES.get("animal_picture_5") is not None:
            case_detail.animal_picture_5 = request.FILES.get("animal_picture_5")
        if request.FILES.get("consent_form") is not None:
            case_detail.consent_form = request.FILES.get("consent_form")
        if request.POST.get("animal_type", None) is not None:
            case_detail.animal_type = request.POST.get("animal_type", None)
        if request.POST.get("age_of_animal", None) is not None:
            case_detail.age_of_animal = request.POST.get("age_of_animal", None)
        if request.POST.get("animal_temperament", None) is not None:
            case_detail.animal_temperament = request.POST.get("animal_temperament", None)
        if request.POST.get("gender", None) is not None:
            case_detail.gender = request.POST.get("gender", None)
        if request.POST.get("pregnant", None) is not None:
            case_detail.pregnant = request.POST.get("pregnant", None)
        if request.POST.get("breed", None) is not None:
            case_detail.breed = request.POST.get("breed", None)
        if request.POST.get("catchable", None) is not None:
            case_detail.catchable = request.POST.get("catchable", None)
        if request.POST["pickup_date"] != "":
            case_detail.pickup_date = datetime.datetime.strptime(
                request.POST["pickup_date"], '%d-%m-%Y')
        if request.POST["pickup_time"] != "":
            case_detail.pickup_time = datetime.datetime.strptime(
                request.POST["pickup_time"], '%H:%M').time()
        if request.POST["medical_history_other_issues"] != "":
            case_detail.medical_history_other_issues = request.POST["medical_history_other_issues"]
        if request.POST.get("fit_for_surgery", None) is not None:
            case_detail.fit_for_surgery = request.POST.get("fit_for_surgery", None)
        if request.POST.get("vaccinated", None) is not None:
            case_detail.vaccinated = request.POST.get("vaccinated", None)
        if request.POST.get("dewormed", None) is not None:
            case_detail.dewormed = request.POST.get("dewormed", None)
        if request.POST["other_details"] != "":
            case_detail.other_details = request.POST["other_details"]
        if request.FILES.get("blood_test_report_1") is not None:
            case_detail.blood_test_report_1 = request.FILES.get("blood_test_report_1")
        if request.FILES.get("blood_test_report_2") is not None:
            case_detail.blood_test_report_2 = request.FILES.get("blood_test_report_2")
        if request.FILES.get("blood_test_report_3") is not None:
            case_detail.blood_test_report_3 = request.FILES.get("blood_test_report_3")
        if request.FILES.get("blood_test_report_4") is not None:
            case_detail.blood_test_report_4 = request.FILES.get("blood_test_report_4")
        if request.FILES.get("blood_test_report_5") is not None:
            case_detail.blood_test_report_5 = request.FILES.get("blood_test_report_5")

        if request.POST["admission_date"] != "":
            case_detail.admission_date = datetime.datetime.strptime(
                request.POST["admission_date"], '%d-%m-%Y')
        if request.POST["vet_assigned"] != "":
            case_detail.vet_assigned = request.POST["vet_assigned"]
        if request.POST["operation_date"] != "":
            case_detail.operation_date = datetime.datetime.strptime(
                request.POST["operation_date"], '%d-%m-%Y')
        if request.POST["operation_cost"] != "":
            case_detail.operation_cost = request.POST["operation_cost"]
        if request.POST["operation_start_time"] != "":
            case_detail.operation_start_time = datetime.datetime.strptime(
                request.POST["operation_start_time"], '%H:%M').time()
        if request.POST["operation_end_time"] != "":
            case_detail.operation_end_time = datetime.datetime.strptime(
                request.POST["operation_end_time"], '%H:%M').time()
        if request.POST.get("operation_outcome", None) is not None:
            case_detail.operation_outcome = request.POST.get("operation_outcome", None)
        if request.POST["cause_of_failure"] != "":
            case_detail.cause_of_failure = request.POST["cause_of_failure"]
        if request.FILES.get("after_operation_pic_1") is not None:
            case_detail.after_operation_pic_1 = request.FILES.get("after_operation_pic_1")
        if request.FILES.get("after_operation_pic_2") is not None:
            case_detail.after_operation_pic_2 = request.FILES.get("after_operation_pic_2")
        if request.FILES.get("after_operation_pic_3") is not None:
            case_detail.after_operation_pic_3 = request.FILES.get("after_operation_pic_3")
        if request.FILES.get("after_operation_pic_4") is not None:
            case_detail.after_operation_pic_4 = request.FILES.get("after_operation_pic_4")
        if request.FILES.get("after_operation_pic_5") is not None:
            case_detail.after_operation_pic_5 = request.FILES.get("after_operation_pic_5")

        # POST OP DETAILS
        if request.POST["post_op_comments"] != "":
            case_detail.post_op_comments = request.POST["post_op_comments"]
        if request.POST["cage_num"] != "":
            case_detail.cage_num = request.POST["cage_num"]
        if request.POST["post_op_start_date"] != "":
            case_detail.post_op_start_date = datetime.datetime.strptime(
                request.POST["post_op_start_date"], '%d-%m-%Y')
        if request.POST["post_op_start_time"] != "":
            case_detail.post_op_start_time = datetime.datetime.strptime(
                request.POST["post_op_start_time"], '%H:%M').time()
        if request.POST["release_date"] != "":
            case_detail.release_date = datetime.datetime.strptime(
                request.POST["release_date"], '%d-%m-%Y')
        if request.POST["post_op_start_time"] != "":
            case_detail.release_time = datetime.datetime.strptime(
                request.POST["release_time"], '%H:%M').time()
        if request.POST["other_comments"] != "":
            case_detail.other_comments = request.POST["other_comments"]
        if request.FILES.get("medicine_photos_1") is not None:
            case_detail.medicine_photos_1 = request.FILES.get("medicine_photos_1")
        if request.FILES.get("medicine_photos_2") is not None:
            case_detail.medicine_photos_2 = request.FILES.get("medicine_photos_2")
        if request.FILES.get("medicine_photos_3") is not None:
            case_detail.medicine_photos_3 = request.FILES.get("medicine_photos_3")
        if request.FILES.get("medicine_photos_4") is not None:
            case_detail.medicine_photos_4 = request.FILES.get("medicine_photos_4")
        if request.FILES.get("medicine_photos_5") is not None:
            case_detail.medicine_photos_5 = request.FILES.get("medicine_photos_5")

        # SAVE CASE
        # print("SAVE CASE")
        case_detail.save()

    # case_detail = CaseDetails.objects.filter(pk=pk)[0]
    return render(request, 'sterilization_module/case_details.html', {"case_detail": case_detail})


@login_required(login_url="/sterilization/login")
def add_case_details(request):
    if request.method == "POST":
        status = request.POST.get("status", None) is None
        reporter_name = request.POST['reporter_name'] == ""
        phone_number = request.POST['phone_number'] == ""
        reporter_photo_id_1 = request.FILES.get('reporter_photo_id_1') is None
        reporter_photo_id_2 = request.FILES.get('reporter_photo_id_2') is None
        reporter_photo_id = reporter_photo_id_1 and reporter_photo_id_2
        reported_date = request.POST["reported_date"] == ""
        reported_time = request.POST['reported_time'] == ""
        location = request.POST['location'] == ""
        landmark = request.POST['landmark'] == ""
        pincode = request.POST['pincode'] == ""
        # can_drop_animal = request.POST.get("can_drop_animal", None) is None
        # animal_marking = request.POST['animal_marking'] == ""
        # animal_color = request.POST['animal_color'] == ""
        animal_picture_1 = request.FILES.get("animal_picture_1") is None
        animal_picture_2 = request.FILES.get("animal_picture_2") is None
        animal_picture_3 = request.FILES.get("animal_picture_3") is None
        animal_picture_4 = request.FILES.get("animal_picture_4") is None
        animal_picture_5 = request.FILES.get("animal_picture_5") is None
        animal_picture = animal_picture_1 and animal_picture_2 and animal_picture_3 and animal_picture_4 and animal_picture_5
        consent_form = request.FILES.get("consent_form") is None
        # print("reporter_name", reporter_name)
        # print("phone_number", phone_number)
        # print("reporter_photo_id", reporter_photo_id)
        # print("reported_time", reported_time)
        # print("location", location)
        # print("landmark", landmark)
        # print("pincode", pincode)
        # print("can_drop_animal", can_drop_animal)
        # print("animal_marking", animal_marking)
        # print("animal_colour", animal_color)
        # print("animal_picture", animal_picture)
        if not(status or reporter_name or phone_number or reporter_photo_id or reported_time or reported_date or location or landmark or pincode or animal_picture or consent_form):
            try:
                global CaseDetails
                case = CaseDetails()
                print("Case Created")
                # try:
                #     phone_pattern = re.compile("((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}")
                #     phone_pattern.match(phone_number) is not None
                #     if alt_phone_number is not None:
                #         phone_pattern.match(alt_phone_number) is not None
                #     print("Phone Number is valid")
                # except:
                #     print("Phone is not valid")
                #     return render(request,'sterilization_module/add_case_details.html',{'error':'Please verify Phone Number.'})

                # REPORTED DETAILS
                case.status = request.POST.get("status", None)
                case.reporter_name = request.POST['reporter_name']
                case.phone_number = request.POST['phone_number']
                case.alt_phone_number = request.POST['alt_phone_number']
                case.reported_date = datetime.datetime.strptime(
                    request.POST["reported_date"], '%d-%m-%Y')
                print(request.POST["reported_date"])
                case.reported_time = datetime.datetime.strptime(
                    request.POST['reported_time'], '%H:%M').time()
                print(request.POST['reported_time'])
                case.location = request.POST['location']
                case.landmark = request.POST['landmark']
                case.pincode = request.POST['pincode']
                case.can_drop_animal = request.POST.get("can_drop_animal", None)
                case.animal_marking = request.POST['animal_marking']
                case.animal_color = request.POST['animal_color']
                case.animal_picture_1 = request.FILES.get("animal_picture_1")
                case.animal_picture_2 = request.FILES.get("animal_picture_2")
                case.animal_picture_3 = request.FILES.get("animal_picture_3")
                case.animal_picture_4 = request.FILES.get("animal_picture_4")
                case.animal_picture_5 = request.FILES.get("animal_picture_5")
                case.consent_form = request.FILES.get("consent_form")
                case.reporter_photo_id_1 = request.FILES.get("reporter_photo_id_1")
                case.reporter_photo_id_2 = request.FILES.get("reporter_photo_id_2")

                # ADDITIONAL DETAILS
                # print(request.POST.get("animal_type", None))
                # print(request.POST.get("age_of_animal", None))
                # print(request.POST["pickup_date"])
                # print(request.POST["pickup_time"])
                # print(request.POST.get("animal_temperament", None))
                # print(request.POST.get("gender", None))
                # print(request.POST.get("pregnant", None))
                # print(request.POST.get("breed", None))
                # print(request.POST.get("catchable", None))
                # print(request.POST["medical_history_other_issues"])
                # print(request.POST.get("fit_for_surgery", None))
                # print(request.POST.get("vaccinated", None))
                # print(request.POST.get("dewormed", None))
                # print(request.POST["other_details"])
                # print(request.FILES.get("blood_test_report_1"))
                # print(request.FILES.get("blood_test_report_2"))
                # print(request.FILES.get("blood_test_report_3"))
                # print(request.FILES.get("blood_test_report_4"))
                # print(request.FILES.get("blood_test_report_5"))
                # case.animal_type = request.POST.get("animal_type", None)
                # case.age_of_animal = request.POST.get("age_of_animal", None)
                if request.POST["pickup_date"] != "":
                    case.pickup_date = datetime.datetime.strptime(
                        request.POST["pickup_date"], '%d-%m-%Y')
                # else:
                #     case.pickup_date = request.POST["pickup_date"]
                if request.POST["pickup_time"] != "":
                    case.pickup_time = datetime.datetime.strptime(
                        request.POST["pickup_time"], '%H:%M').time()
                # else:
                #     case.pickup_time = request.POST["pickup_time"]
                case.animal_temperament = request.POST.get("animal_temperament", None)
                case.gender = request.POST.get("gender", None)
                case.pregnant = request.POST.get("pregnant", None)
                case.breed = request.POST.get("breed", None)
                case.catchable = request.POST.get("catchable", None)
                case.medical_history_other_issues = request.POST["medical_history_other_issues"]
                case.fit_for_surgery = request.POST.get("fit_for_surgery", None)
                case.vaccinated = request.POST.get("vaccinated", None)
                case.dewormed = request.POST.get("dewormed", None)
                case.other_details = request.POST["other_details"]
                case.blood_test_report_1 = request.FILES.get("blood_test_report_1")
                case.blood_test_report_2 = request.FILES.get("blood_test_report_2")
                case.blood_test_report_3 = request.FILES.get("blood_test_report_3")
                case.blood_test_report_4 = request.FILES.get("blood_test_report_4")
                case.blood_test_report_5 = request.FILES.get("blood_test_report_5")

                # OPERATIONAL DETAILS
                if request.POST["admission_date"] != "":
                    case.admission_date = datetime.datetime.strptime(
                        request.POST["admission_date"], '%d-%m-%Y')
                # else:
                #     case.admission_date = request.POST["admission_date"]
                case.vet_assigned = request.POST["vet_assigned"]
                if request.POST["operation_date"] != "":
                    case.operation_date = datetime.datetime.strptime(
                        request.POST["operation_date"], '%d-%m-%Y')
                # else:
                #     case.operation_date = request.POST["operation_date"]
                if request.POST["operation_cost"] != "":
                    case.operation_cost = request.POST["operation_cost"]
                if request.POST["operation_start_time"] != "":
                    case.operation_start_time = datetime.datetime.strptime(
                        request.POST["operation_start_time"], '%H:%M').time()
                # else:
                #     case.operation_start_time = request.POST["operation_start_time"]
                if request.POST["operation_end_time"] != "":
                    case.operation_end_time = datetime.datetime.strptime(
                        request.POST["operation_end_time"], '%H:%M').time()
                # else:
                #     case.operation_end_time = request.POST["operation_end_time"]
                case.operation_outcome = request.POST.get("operation_outcome", None)
                case.cause_of_failure = request.POST["cause_of_failure"]
                case.after_operation_pic_1 = request.FILES.get("after_operation_pic_1")
                case.after_operation_pic_2 = request.FILES.get("after_operation_pic_2")
                case.after_operation_pic_3 = request.FILES.get("after_operation_pic_3")
                case.after_operation_pic_4 = request.FILES.get("after_operation_pic_4")
                case.after_operation_pic_5 = request.FILES.get("after_operation_pic_5")

                # POST OP DETAILS
                case.post_op_comments = request.POST["post_op_comments"]
                case.cage_num = request.POST["cage_num"]
                if request.POST["post_op_start_date"] != "":
                    case.post_op_start_date = datetime.datetime.strptime(
                        request.POST["post_op_start_date"], '%d-%m-%Y')
                # else:
                #     case.post_op_start_date = request.POST["post_op_start_date"]
                if request.POST["post_op_start_time"] != "":
                    case.post_op_start_time = datetime.datetime.strptime(
                        request.POST["post_op_start_time"], '%H:%M').time()
                # else:
                #     case.post_op_start_time = request.POST["post_op_start_time"]

                if request.POST["release_date"] != "":
                    case.release_date = datetime.datetime.strptime(
                        request.POST["release_date"], '%d-%m-%Y')
                # else:
                #     case.release_date = request.POST["release_date"]
                if request.POST["post_op_start_time"] != "":
                    case.release_time = datetime.datetime.strptime(
                        request.POST["release_time"], '%H:%M').time()
                # else:
                #     case.release_time = request.POST["release_time"]
                case.other_comments = request.POST["other_comments"]
                case.medicine_photos_1 = request.FILES.get("medicine_photos_1")
                case.medicine_photos_2 = request.FILES.get("medicine_photos_2")
                case.medicine_photos_3 = request.FILES.get("medicine_photos_3")
                case.medicine_photos_4 = request.FILES.get("medicine_photos_4")
                case.medicine_photos_5 = request.FILES.get("medicine_photos_5")

                # SAVE CASE
                print("SAVE CASE")
                case.save()
                return redirect('dashboard')
            except ValueError as e:
                print("EXCEPTION", e)
                return render(request, 'sterilization_module/add_case_details.html', {'error': 'Incorrect values. Please try again.'})

        else:
            return render(request, 'sterilization_module/add_case_details.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'sterilization_module/add_case_details.html')


def analysis_of_cases(request):
    print(request.method)
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        print(fromdate)
        print(todate)
        data = CaseDetails.objects.filter(
            reported_date__gte=fromdate, reported_date__lte=todate)
        total_num_cases = len(CaseDetails.objects.filter(
            reported_date__gte=fromdate, reported_date__lte=todate))
        num_reported_cases = len(CaseDetails.objects.filter(
            status="Reported", reported_date__gte=fromdate, reported_date__lte=todate))
        num_admitted_cases = len(CaseDetails.objects.filter(
            status="Admitted", reported_date__gte=fromdate, reported_date__lte=todate))
        num_released_cases = len(CaseDetails.objects.filter(
            status="Released", reported_date__gte=fromdate, reported_date__lte=todate))
        blood_test_done_cases = len(CaseDetails.objects.filter(
            status="Blood Test Done", reported_date__gte=fromdate, reported_date__lte=todate))
        operation_started_cases = len(CaseDetails.objects.filter(
            status="Operation Started", reported_date__gte=fromdate, reported_date__lte=todate))
        post_operation = len(CaseDetails.objects.filter(
            status="Post Operation", reported_date__gte=fromdate, reported_date__lte=todate))
        pending_cases = total_num_cases - num_released_cases

    else:
        data = CaseDetails.objects.all()
        total_num_cases = len(CaseDetails.objects.all())
        num_reported_cases = len(CaseDetails.objects.filter(status="Reported"))
        num_admitted_cases = len(CaseDetails.objects.filter(status="Admitted"))
        num_released_cases = len(CaseDetails.objects.filter(status="Released"))
        blood_test_done_cases = len(CaseDetails.objects.filter(status="Blood Test Done"))
        operation_started_cases = len(
            CaseDetails.objects.filter(status="Operation Started"))
        post_operation = len(CaseDetails.objects.filter(status="Post Operation"))
        pending_cases = total_num_cases - num_released_cases

    chartdata = [num_reported_cases, num_admitted_cases, num_reported_cases, num_released_cases,
                 blood_test_done_cases, operation_started_cases, post_operation, pending_cases]
    context = {"total_num_cases": total_num_cases,
               "num_reported_cases": num_reported_cases,
               "num_admitted_cases": num_admitted_cases,
               "num_reported_cases": num_reported_cases,
               "num_released_cases": num_released_cases,
               "blood_test_done_cases": blood_test_done_cases,
               "operation_started_cases": operation_started_cases,
               "post_operation": post_operation,
               "pending_cases": pending_cases,
               "data": data,
               "chartdata": chartdata}

    return render(request, 'sterilization_module/analysis_of_cases.html', context)


def cases_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=cases.csv'
    # Create a csv writer
    writer = csv.writer(response)
    global CaseDetails
    # Designate the Model
    this_month = datetime.datetime.now().month
    cases = CaseDetails.objects.filter(reported_date__month=this_month)

    # Add column headings to the csv file
    writer.writerow(['Reporter Name', 'Phone Number', 'Reported Date',
                    'Reported Time', 'Location', 'Landmark', 'Pincode', 'Status'])
    # Loop Thu and output
    for CaseDetails in cases:
        writer.writerow([CaseDetails.reporter_name, CaseDetails.phone_number, CaseDetails.reported_date,
                        CaseDetails.reported_time, CaseDetails.location, CaseDetails.landmark, CaseDetails.pincode, CaseDetails.status])

    return response


def cases_csv1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=cases.csv'
    # Create a csv writer
    writer = csv.writer(response)
    global CaseDetails
    # Designate the Model
    this_year = datetime.datetime.now().year
    cases = CaseDetails.objects.filter(reported_date__year=this_year)

    # Add column headings to the csv file
    writer.writerow(['Reporter Name', 'Phone Number', 'Reported Date',
                    'Reported Time', 'Location', 'Landmark', 'Pincode', 'Status'])
    # Loop Thu and output
    for CaseDetails in cases:
        writer.writerow([CaseDetails.reporter_name, CaseDetails.phone_number, CaseDetails.reported_date,
                        CaseDetails.reported_time, CaseDetails.location, CaseDetails.landmark, CaseDetails.pincode, CaseDetails.status])

    return response


class Calendarview(generic.ListView):
    global CaseDetails
    model = CaseDetails
    template_name = 'sterilization_module/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs,)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        print(context)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.date.today()
