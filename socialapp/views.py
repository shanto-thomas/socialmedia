from rest_framework import generics, viewsets, status
from socialapp.serializers import StorySerialzer, StoryListSerialzer, StoryStatusSerializer, StoryDataSerialzer, \
    ListPostSerialzer, ViewStorySerialzer
from rest_framework.response import Response
from socialapp.models import Story, StoryStatus, Image
from django.contrib.auth.models import User
from .pagination import LargeResultsSetPagination

class StoryCreateViewSet(viewsets.ModelViewSet):
    """ Admin must be able to add posts containing multiple images and description """

    queryset = Story.objects.all()
    serializer_class = StorySerialzer
    pagination_class = LargeResultsSetPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added ', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)
class StoryViewSet(viewsets.ModelViewSet):
    """ Posts will sort by this weight in descending order from most similar post to least similar post """

    queryset = Story.objects.all()
    serializer_class = ViewStorySerialzer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Story.objects.all().order_by('-weight')


class LikeDislikeViewSet(viewsets.ModelViewSet):
    """ API for liking and disliking a post """

    queryset = StoryStatus.objects.all()
    serializer_class = StoryDataSerialzer
    pagination_class = LargeResultsSetPagination
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added ', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)

class ListPostViewSet(viewsets.ModelViewSet):
    """ API for list of posts """

    queryset = Story.objects.all()
    serializer_class = ListPostSerialzer
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        user = self.request.query_params.get('customer')
        post = Story.objects.filter(user_id = User.objects.get(id=user))
        datalist =[]
        imagelist =[]
        for item in post:
            likecount=StoryStatus.objects.filter(story_id = item.id,status="like").count()
            dislikecount=StoryStatus.objects.filter(story_id = item.id,status="dislike").count()
            images = Image.objects.filter(story_id = item.id)
            for img in images:
                data={
                    "img":str(img.upload),
                    "description":img.description,
                    "likecount":likecount,
                    "dislikecount":dislikecount
                }
                imagelist.append(data)
            data={
                "user_id" :item.user_id.id,
                "name" :item.name,
                "weight" :item.weight,
                "created_date" :item.created_date,
                # "images":imagelist

            }
            datalist.append(data)

        return Response({"detailsSnippet":datalist,"imges":imagelist})

class UserLikedPostViewSet(viewsets.ModelViewSet):
    """ API for  list of all the users who liked a post """

    queryset = Story.objects.all()
    serializer_class = ListPostSerialzer
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):

        post = Story.objects.all()

        datalist =[]
        imagelist =[]
        for item in post:
            likes=StoryStatus.objects.filter(story_id = item.id,status="like")
            if likes:
                images = Image.objects.filter(story_id = item.id)
                for img in images:
                    data={
                        "img":str(img.upload),
                        "description":img.description,

                    }
                    imagelist.append(data)
                data={
                    "user_id" :item.user_id.id,
                    "name" :item.name,
                    "weight" :item.weight,
                    "created_date" :item.created_date,
                    # "images":imagelist

                }
                datalist.append(data)
            else:
               pass

        return Response({"detailsSnippet":datalist,"imges":imagelist})
class ViewLikedPostViewSet(viewsets.ModelViewSet):
    """ API for  list of all the users who liked a post """

    queryset = Story.objects.all()
    serializer_class = ListPostSerialzer
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):

        post = Story.objects.all()

        datalist =[]
        imagelist =[]
        for item in post:
            likes=StoryStatus.objects.filter(story_id = item.id,status="like").count()
            dislikes=StoryStatus.objects.filter(story_id = item.id,status="dislike").count()
            if likes and dislikes:
                images = Image.objects.filter(story_id = item.id)
                for img in images:
                    data={
                        "img":str(img.upload),
                        "description":img.description,
                        "like":likes,
                        "dislike":dislikes,

                    }
                    imagelist.append(data)
                data={
                    "user_id" :item.user_id.id,
                    "name" :item.name,
                    "weight" :item.weight,
                    "created_date" :item.created_date,
                    # "images":imagelist

                }
                datalist.append(data)
            else:
               pass

        return Response({"detailsSnippet":datalist,"imges":imagelist})


