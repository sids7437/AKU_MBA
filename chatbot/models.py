from django.db import models


# About, Vision, Mission etc.
class CMSContent(models.Model):

    SECTION_CHOICES = [

        ('about', 'About'),
        ('vision', 'Vision'),
        ('mission', 'Mission'),
        ('objective', 'Objective'),
        ('director', 'Director Message'),

    ]

    title = models.CharField(max_length=200)

    section_type = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES
    )

    content = models.TextField()


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.title




# MBA Programme Details
class Programme(models.Model):

    name = models.CharField(
        max_length=200,
        default="MBA Programme"
    )

    overview = models.TextField()

    duration = models.CharField(
        max_length=100
    )

    eligibility = models.TextField()

    career_opportunities = models.TextField()


    def __str__(self):
        return self.name
    
# MBA Syllabus

class Syllabus(models.Model):

    SPECIALIZATION_CHOICES = [

        ('COMMON', 'Common'),
        ('FINANCE', 'Finance'),
        ('HRM', 'Human Resource Management'),
        ('MARKETING', 'Marketing'),

    ]


    SEMESTER_CHOICES = [

        ('I', 'Semester I'),
        ('II', 'Semester II'),
        ('III', 'Semester III'),
        ('IV', 'Semester IV'),

    ]


    specialization = models.CharField(
        max_length=20,
        choices=SPECIALIZATION_CHOICES,
        default='COMMON'
    )


    semester = models.CharField(
        max_length=10,
        choices=SEMESTER_CHOICES
    )


    course_code = models.CharField(
        max_length=50
    )


    subject_name = models.CharField(
        max_length=200
    )


    credits = models.IntegerField()


    def __str__(self):

        return f"{self.specialization} - {self.subject_name}"
    
class ChatHistory(models.Model):

    question = models.TextField()

    answer = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.question
    
class Faculty(models.Model):

    name = models.CharField(
        max_length=200
    )

    designation = models.CharField(
        max_length=200
    )

    qualification = models.CharField(
        max_length=300
    )

    specialization = models.CharField(
        max_length=200, null=True, blank=True
    )

    experience = models.CharField(
        max_length=100
    )


    def __str__(self):

        return self.name



class Event(models.Model):

    title = models.CharField(
        max_length=200
    )

    event_date = models.DateField()

    description = models.TextField()


    def __str__(self):

        return self.title



class Notice(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    notice_date = models.DateField()

    pdf = models.FileField(
        upload_to="notices/"
    )


    def __str__(self):

        return self.title