from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo

class CamdevSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'JOB_LOG_PK',
            'IS_COMPLETE',
            'SUBMIT_DT',
            'XPR_JOB_ID',
            'OVRD_FILE_PATH',
            'JOB_STATUS',
            'API_JOB_NAME',
            'X_RUN_ID',
            'X_PROCESS_ID',
            'X_LOG_PATH',
            'X_SERVER',
        )
        model = models.Camdev
