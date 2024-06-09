from django.contrib import admin

from school.models import Movement, Organisation, Occupation, AcademicTerm, AcademicYear, Center, Program, Parent, Sibling, Subject, ProgramStructure

# Register your models here.
@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ("school_member", "movement_type", "reason", "movement_date")
    list_filter = ("movement_type", "created", "updated")
    search_fields = ("school_member__first_name", "school_member__last_name", "movement_type")
    ordering = ("-created",)

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_occupied', 'created', 'updated')
    list_filter = ('is_occupied', 'created', 'updated')
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('-created',)

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'director__first_name', 'director__last_name', 'director__member_id', 'director__email')
    date_hierarchy = 'created'
    ordering = ('-created',)   

@admin.register(AcademicTerm)
class AcademicTermAdmin(admin.ModelAdmin):
    list_display = ("year", "term_name", "start_date", "end_date", "fees_amount")
    list_filter = ("fees_amount", "year", "created", "updated")
    search_fields = ("term_name", "year",)
    ordering = ("-created",)

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ('center_name', 'center_number', 'email')
    list_filter = ('center_name', 'created', 'updated')
    search_fields = ('center_name', 'center_number')
    date_hierarchy = 'created'
    ordering = ('-created',)

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'start_date', 'end_date', 'created')
    list_filter = ('created', 'updated', 'year')
    search_fields = ('year', )
    date_hierarchy = 'created'
    ordering = ('-created',)   
        
admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_code', 'program_abbr', 'updated')
    list_filter = ('program_name', 'created', 'updated')
    search_fields = ('program_name', 'program_code')
    date_hierarchy = 'created'
    ordering = ('-created',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'relationship', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('parent', 'relationship')
    date_hierarchy = 'created'
    ordering = ('-created',)   

@admin.register(Sibling)
class Siblingdmin(admin.ModelAdmin):
    list_display = ('sibling', 'relationship', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('sibling', 'relationship')
    date_hierarchy = 'created'
    ordering = ('-created',)  

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_teacher', 'subject_name', 'subject_code', 'created', 'updated')
    list_filter = ('subject_code', 'created', 'updated')
    search_fields = ('subject_teacher', 'subject_name')
    date_hierarchy = 'created'
    ordering = ('-created',)

@admin.register(ProgramStructure)
class ProgramStructureAdmin(admin.ModelAdmin):
    list_display = ('academic_term', 'program_fee', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('academic_term',)
    date_hierarchy = 'created'
    ordering = ('-created',)           