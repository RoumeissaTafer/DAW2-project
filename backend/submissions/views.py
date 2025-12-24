from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.utils import timezone

from .models import Submission
from .serializers import SubmissionSerializer
 
class SubmissionViewSet(viewsets.ModelViewSet):
    """
   Gestion des soumissions scientifiques(CRUD)
    """
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
         
        user = self.request.user
        # user li 3ando role communicant/author ychouf ghir proposition ta3ou
        if user.role == 'AUTHOR':
            return Submission.objects.filter(author=user)

        # Organizer / Reviewer / Admin يشوفو كل المقترحات
        return Submission.objects.all()
    
       
    def perform_create(self, serializer):
        """
        ربط المقترح بالمستخدم الحالي تلقائياً
        """
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        submission = self.get_object()#YJIB PROPOSITION LI RAY7 Y3ADLO
       # منع التعديل بعد الموعد النهائي
        if submission.event.submission_deadline < timezone.now().date():
            return Response(
                {"error": "The modification period has ended."},  
                status=status.HTTP_403_FORBIDDEN
            )
         #else ydir update normale
        return super().update(request, *args, **kwargs)
          #retirer
    def destroy(self, request, *args, **kwargs):
        submission = self.get_object()

        if submission.event.submission_deadline < timezone.now().date():
            return Response(
                {"error": "You cannot withdraw your proposal after the submission deadlineلا يمكن سحب المقترح بعد انتهاء الأجل"},
                status=status.HTTP_403_FORBIDDEN
            )
            #else 
        return super().destroy(request, *args, **kwargs)

"""
module 5:
def validate_status(self, value):
    @action(detail=True, methods=['post'])
def change_status(self, request, pk=None):


"""