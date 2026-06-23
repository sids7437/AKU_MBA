from django.shortcuts import render
import json
from django.http import JsonResponse
from django.http import HttpResponse


from .models import (
    Syllabus,
    ChatHistory,
    CMSContent,
    Programme
)

from website.models import (
    Faculty,
    Event,
    Notice
)



def chatbot(request):

    answer = ""


    if request.method == "POST":

        question = request.POST.get("question")

        q = question.lower()



        # -------------------------
        # Semester Detection
        # -------------------------

        semester = None


        if any(x in q for x in [
            "semester 1",
            "semester i",
            "sem 1",
            "sem i"
        ]):
            semester = "I"


        elif any(x in q for x in [
            "semester 2",
            "semester ii",
            "sem 2",
            "sem ii"
        ]):
            semester = "II"


        elif any(x in q for x in [
            "semester 3",
            "semester iii",
            "sem 3",
            "sem iii"
        ]):
            semester = "III"


        elif any(x in q for x in [
            "semester 4",
            "semester iv",
            "sem 4",
            "sem iv"
        ]):
            semester = "IV"



        subjects = []



        # -------------------------
        # Finance
        # -------------------------

        if any(x in q for x in [
            "finance",
            "financial",
            "fin"
        ]):


            subjects = Syllabus.objects.filter(
                specialization__in=[
                    "COMMON",
                    "FINANCE"
                ]
            )


            if semester:

                subjects = subjects.filter(
                    semester=semester
                )

                answer = (
                    f"Finance Semester {semester} Subjects:\n\n"
                )


            else:

                answer = (
                    "Finance Syllabus:\n\n"
                )





        # -------------------------
        # HRM
        # -------------------------

        elif any(x in q for x in [
            "hrm",
            "human resource",
            "hr "
        ]):


            subjects = Syllabus.objects.filter(
                specialization__in=[
                    "COMMON",
                    "HRM"
                ]
            )


            if semester:

                subjects = subjects.filter(
                    semester=semester
                )


                answer = (
                    f"HRM Semester {semester} Subjects:\n\n"
                )


            else:

                answer = (
                    "HRM Syllabus:\n\n"
                )





        # -------------------------
        # Marketing
        # -------------------------

        elif any(x in q for x in [
            "marketing",
            "market"
        ]):


            subjects = Syllabus.objects.filter(
                specialization__in=[
                    "COMMON",
                    "MARKETING"
                ]
            )


            if semester:

                subjects = subjects.filter(
                    semester=semester
                )


                answer = (
                    f"Marketing Semester {semester} Subjects:\n\n"
                )


            else:

                answer = (
                    "Marketing Syllabus:\n\n"
                )





        # -------------------------
        # MBA Programme
        # -------------------------

        elif any(x in q for x in [
            "mba",
            "programme",
            "program",
            "duration",
            "eligibility",
            "career"
        ]):


            programme = Programme.objects.first()


            if programme:


                answer = (

                    f"{programme.name}\n\n"

                    f"Duration:\n"
                    f"{programme.duration}\n\n"

                    f"Eligibility:\n"
                    f"{programme.eligibility}\n\n"

                    f"Career Opportunities:\n"
                    f"{programme.career_opportunities}"

                )


            else:

                answer = "MBA Programme details not available."





        # -------------------------
        # Faculty
        # -------------------------


        elif any(x in q for x in [
            "faculty",
            "teacher",
            "professor",
            "staff"
        ]):


            faculty_list = Faculty.objects.all()


            if faculty_list.exists():

                answer = "Faculty Members:\n\n"


                for f in faculty_list:

                    answer += (
                        f"Name: {f.name}\n"
                        f"Designation: {f.designation}\n"
                        f"Qualification: {f.qualification}\n"
                        f"Email: {f.email}\n\n"
                    )


            else:

                answer = "No faculty records available."





        # -------------------------
        # Events
        # -------------------------

        elif "event" in q:


            events = Event.objects.all().order_by(
                "-date"
            )


            answer = "Latest Events:\n\n"


            for e in events:


                answer += (

                    f"Title: {e.title}\n"

                    f"Date: {e.date}\n"

                    f"Description: {e.description}\n\n"

                )





        # -------------------------
        # Notices
        # -------------------------

        elif any(x in q for x in [
            "notice",
            "notices"
        ]):


            notices = Notice.objects.all().order_by('-date')[:5]

            for n in notices:

                pdf = ""

                if n.pdf:
                    pdf = f'<a href="{n.pdf.url}" target="_blank">📄 Open PDF</a>'

                answer += (
                    f"<b>Notice:</b> {n.title}<br>"
                    f"<b>Date:</b> {n.date}<br>"
                    f"{pdf}<br><br>"
                )





        # -------------------------
        # CMS Content
        # -------------------------

        elif "vision" in q:


            content = CMSContent.objects.filter(
                section_type="vision"
            ).first()


            answer = (
                content.content
                if content
                else "Vision not available."
            )



        elif "mission" in q:


            content = CMSContent.objects.filter(
                section_type="mission"
            ).first()


            answer = (
                content.content
                if content
                else "Mission not available."
            )



        elif "objective" in q:


            content = CMSContent.objects.filter(
                section_type="objective"
            ).first()


            answer = (
                content.content
                if content
                else "Objectives not available."
            )



        elif "director" in q:


            content = CMSContent.objects.filter(
                section_type="director"
            ).first()


            answer = (
                content.content
                if content
                else "Director message not available."
            )



        elif "about" in q:


            content = CMSContent.objects.filter(
                section_type="about"
            ).first()


            answer = (
                content.content
                if content
                else "About information not available."
            )





        else:


            answer = (

                "I can help you with:\n\n"

                "• MBA Programme Details\n"

                "• Finance Syllabus\n"

                "• HRM Syllabus\n"

                "• Marketing Syllabus\n"

                "• Semester Wise Subjects\n"

                "• Faculty Details\n"

                "• Latest Notices\n"

                "• Latest Events\n"

                "• Vision, Mission and Objectives"

            )





        # -------------------------
        # Add Syllabus Subjects
        # -------------------------

        if subjects:


            for subject in subjects:


                answer += (

                    f"{subject.course_code} - "

                    f"{subject.subject_name} "

                    f"({subject.credits} Credits)\n"

                )


        elif "subject" in q:


            answer += "\nNo syllabus data available."


        

    if request.method == "POST":

        return HttpResponse(
            answer.replace("\n", "<br>")
        )


    return render(
        request,
        "chatbot/chatbot.html"
    )   

def syllabus_view(request, specialization):


    subjects = Syllabus.objects.filter(
        specialization__in=[
            "COMMON",
            specialization
        ]
    ).order_by(
        "semester"
    )


    return render(
        request,
        "syllabus.html",
        {
            "subjects": subjects,
            "specialization": specialization
        }
    )