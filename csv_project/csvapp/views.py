import pandas as pd
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):
        chunk_size = 1000
        batch_no = 1
        file_uploaded = request.FILES.get('file_uploaded')
        for chunk in pd.read_csv(file_uploaded, chunksize=chunk_size):
            chunk.to_csv('uploaded_csv/people_' + str(batch_no) + '.csv', index=False)
            batch_no += 1
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
