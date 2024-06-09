from django.db import IntegrityError
from django.utils import timezone
from faker import Faker
import random
from accounts.models import SchoolMember
from core import settings
from school.models import Occupation, Organisation, Movement, StudentGuardian, StudentTeacher
from random import sample
 
 
fake = Faker()
 
from collections import Counter

def generate_sample_data(num_school_members=500, num_movements=200, num_student_guardian=500, num_student_teacher=500):
    
    # Initialize counters for each role
    admin_count = 0
    teacher_count = 0
    guardian_count = 0
    student_count = 0
    email_counters = {}    

    #creating Members
    for i in range(num_school_members):
        # Check if limits for each role have been reached
        if admin_count < 15:
            role = 'Adminstrator'
            admin_count += 1
        elif teacher_count < 80:
            role = 'Teacher'
            teacher_count += 1
        elif guardian_count < 150:
            role = 'Guardian'
            guardian_count += 1
        else:
            role = 'Student'
            student_count += 1

        occupation = Occupation.objects.order_by("?").first()
        organisation = Organisation.objects.order_by("?").first()
        
        # Generate initial email
        email = f"{fake.first_name().lower()}{fake.last_name().lower()}@petalmafrica.com"
        
        # Increment counter if email exists
        while SchoolMember.objects.filter(email=email).exists():
            if email not in email_counters:
                email_counters[email] = 1
            else:
                email_counters[email] += 1
            email = f"{email.split('@')[0]}{email_counters[email]}@petalmafrica.com"
            
        member = SchoolMember.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            role=role,
            member_id=fake.uuid4(),
            mobile_phone=fake.phone_number(), 
            occupation=occupation,  
            school=organisation,  
            level=fake.word(),  
            gender=random.choice(['Male', 'Female']),
            joining_date=fake.date_time_between(start_date='-2y', end_date='now'),
            date_of_birth=fake.date_time_between(start_date='-30y', end_date='-18y'), 
            status=random.choice(['Permanent', 'Students on Attachment', 'Graduate Trainees', 'Contract']),
            email=email,
        )

        # Assign occupation based on role
        if member.role == 'Teacher':
            occupation_choices = ['Senior Teacher', 'Teacher', 'Sports Director']
            occupation_name = random.choice(occupation_choices)
        elif member.role == 'Adminstrator':
            occupation_choices = ['HeadMaster', 'Director', 'Burser', 'Principal', 'Clerk', 'Deputy HeadMaster']
            occupation_name = random.choice(occupation_choices)
        elif member.role == 'Student':
            occupation_choices = ['Student', 'Class Monitor', 'Prefect', 'Head Boy', 'Head Girl']
            occupation_name = random.choice(occupation_choices)
        elif member.role == 'Guardian':
            occupation_name = 'Guardian'
        else:
            occupation_name = None

        if occupation_name:
            occupation = Occupation.objects.get_or_create(name=occupation_name)[0]
            member.occupation = occupation
            member.save()




    #creating Members
    for i in range(num_movements):
        school_member = SchoolMember.objects.order_by("?").first() 
    
        Movement.objects.create(
            school_member=school_member,
            movement_type=fake.random_element(
                elements=(
                    "Promotions",
                    "Transfer In",
                    "Transfer Out",
                )
            ),
            movement_date=fake.date_time_between(start_date='-2y', end_date='now'),
            reason=fake.sentence(),
        )        

    students = SchoolMember.objects.filter(role='Student')
    guardians = SchoolMember.objects.filter(role='Guardian')
    num_student_guardian = min(num_student_guardian, len(students))
    sampled_students = sample(list(students), num_student_guardian)

    for student in sampled_students:

        guardian = guardians.order_by("?").first()

        StudentGuardian.objects.create(
            guardian=guardian,
            student=student,
            relationship=fake.word(),
        )
  

    students = SchoolMember.objects.filter(role='Student')
    num_student_teacher = min(num_student_teacher, len(students))
    sampled_students = sample(list(students), num_student_teacher)

    for student in sampled_students:
        teacher = SchoolMember.objects.order_by("?").first()

        StudentTeacher.objects.create(
            teacher=teacher,
            student=student,
            effective_until=fake.date_time_between(start_date='-2y', end_date='now'),
        )


    settings.LOGGER.success("data generation complete")
