from rest_framework import serializers
from api import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    cname = serializers.CharField(source='course.title')
    level_text = serializers.CharField(source='get_level_display')
    class Meta:

        model = models.Module
        fields = ['id','name','level','level_text','cname']


class ModuleNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = "__all__"


class ModuleSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = "__all__"


class VideoSetSerializer(serializers.ModelSerializer):
    tag_txt = serializers.SerializerMethodField()

    class Meta:
        model = models.Video
        fields = ['id', 'title', 'vid', 'tag', 'tag_txt']

    def get_tag_txt(self, obj):
        tag_list = obj.tag.all()
        return [{'id': row.id, 'caption': row.caption} for row in tag_list]
