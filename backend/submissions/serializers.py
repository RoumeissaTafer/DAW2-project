# submissions/serializers.py

from rest_framework import serializers
from .models import Submission
from django.utils import timezone


class SubmissionSerializer(serializers.ModelSerializer):
  author_name = serializers.CharField(source='author.get_full_name', read_only=True)
  author_email = serializers.EmailField(source='author.email', read_only=True)
  author_role = serializers.CharField(source='author.role', read_only=True)
  # 2. معلومات الحدث (Read-Only)
  event_title = serializers.CharField(source='event.title', read_only=True)
  event_start_date = serializers.DateField(source='event.start_date', read_only=True) 
  event_location = serializers.CharField(source='event.location', read_only=True)
  #هذه الحقول مهمة جداً لكي يفهم الـ Frontend لمن يعود هذا المقترح ولأي حدث ينتمي، دون الحاجة لطلب بيانات إضافية.
  pdf_file = serializers.FileField(required=True)

  class Meta:
    model = Submission
    fields = [
    'id',
            'event',
            'event_title',
            'author',
            'author_name',
            'author_email',
            'author_role', 
            'title',
            'abstract',
            'keywords',
            'sub_type',
            'pdf_file',
            'status',
            'sub_date','event_location','event_start_date']
     
    
    read_only_fields = ('id','status', 'author', 'sub_date') 
    #communicant ma ya9derch ybadl status 
   
     # def validate_status mba3d nchoufe est ce que nzidha wala la?
  def validate_event(self, value):
                
     if value.end_date < timezone.now().date():
        raise serializers.ValidationError(
         "La date limite de soumission est dépassée pour cet événement"
            )
     return value
    # أضف شرط deadline في views.pyنزيدو شرط التعديل والحدف في    
