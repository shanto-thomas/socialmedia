
from rest_framework import serializers
from socialapp.models import Story, StoryStatus, Image
from django.contrib.auth.models import User

class StorySerialzer(serializers.Serializer):

    user = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    weight = serializers.CharField(required=False, allow_blank=True, max_length=100)
    upload = serializers.ImageField(required=False)


    def create(self, validated_data):

        user = validated_data['user']
        name = validated_data['name']
        description = validated_data['description']
        weight = validated_data['weight']
        upload = validated_data['upload']
        stories = Story.objects.create(
        user_id = User.objects.get(id=user),
        name = name,weight=weight

        )
        Image.objects.create(upload=upload,story_id=Story.objects.get(id=stories.id),description = description)
        return validated_data

#
class StoryListSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = "__all__"
class ListPostSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = "__all__"

class StoryStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryStatus
        fields = "__all__"
class ViewStorySerialzer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = "__all__"

statuses =(
    ('like', 'Like'),
    ('dislike', 'Dislike'),
)
  
class StoryDataSerialzer(serializers.Serializer):
    status = serializers.ChoiceField(choices = statuses)
    user = serializers.CharField(required=False, allow_blank=True, max_length=100)
    story_id = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        user = validated_data['user']
        status = validated_data['status']
        story_id = validated_data['story_id']
        story = StoryStatus.objects.filter(story_id= Story.objects.get(id=story_id))
        if story:
            for i in story:
                if i.status == status:
                    print("hello1")
                    raise serializers.ValidationError({"promptmsg": "Already story liked"})
                elif i.status ==status:
                    print("hello2")
                    raise serializers.ValidationError({"promptmsg": "Already story disliked"})
        else:
            print("hello3")
            story = StoryStatus.objects.create(story_id=Story.objects.get(id=story_id),
                                               user=User.objects.get(id=user),
                                               status=status)

        return validated_data
