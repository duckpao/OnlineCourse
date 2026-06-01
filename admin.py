from django.contrib import admin
# Đảm bảo import đủ 7 classes (Course, Lesson, Instructor, Enrollment, Question, Choice, Submission)
from .models import Course, Lesson, Instructor, Enrollment, Question, Choice, Submission

# Tạo Inline cho Choice (để thêm đáp án trực tiếp khi tạo câu hỏi)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

# Tạo Inline cho Question (để thêm câu hỏi trực tiếp khi tạo khóa học)
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Cấu hình QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

# Cấu hình LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Đăng ký các model vào trang admin
admin.site.register(Course) # (Thường có sẵn inlines cho CourseAdmin, bạn giữ nguyên code cũ của họ nếu có)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)