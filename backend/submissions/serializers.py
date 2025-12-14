# submissions/serializers.py

from rest_framework import serializers
from .models import Submission
class SubmissionSerializer(serializers.ModelSerializer):
  author_name = serializers.CharField(source='author.get_full_name', read_only=True)
  author_email = serializers.EmailField(source='author.email', read_only=True)
  event_title = serializers.CharField(source='event.title', read_only=True)
  #هذه الحقول مهمة جداً لكي يفهم الـ Frontend لمن يعود هذا المقترح ولأي حدث ينتمي، دون الحاجة لطلب بيانات إضافية.
  class Meta:
    model = Submission
    fields = '__all__'

    '''['id',
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
            'sub_date',]
     '''
    read_only_fields = ('status', 'author', 'sub_date') 
       