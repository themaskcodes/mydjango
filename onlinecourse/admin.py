
from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, QuestionTwo, QuestionThree, Choice, ChoiceTwo, ChoiceThree 

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class QuestionTwoInline(admin.StackedInline):
    model = QuestionTwo
    extra = 3

class QuestionThreeInline(admin.StackedInline):
    model = QuestionThree
    extra = 3

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceTwoInline(admin.StackedInline):
    model = ChoiceTwo
    extra = 3

class ChoiceThreeInline(admin.StackedInline):
    model = ChoiceThree
    extra = 3




# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceInline]

class QuestionTwoAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceTwoInline]

class QuestionThreeAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceThreeInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']

class ChoiceTwoAdmin(admin.ModelAdmin):
    list_display = ['choice_text']

class ChoiceThreeAdmin(admin.ModelAdmin):
    list_display = ['choice_text']



# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionTwo, QuestionTwoAdmin)
admin.site.register(QuestionThree, QuestionThreeAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(ChoiceTwo, ChoiceTwoAdmin)
admin.site.register(ChoiceThree, ChoiceThreeAdmin)