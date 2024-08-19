from rest_framework import serializers
from .models import Post, Comment 
from  register.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta():
        model = Post
        fields = ['title', 'content','cover_image', 'slug','published','updated_at','author', 'category']
        extra_kwargs = {'published':{'read_only':True},
                        'updated_at':{'read_only':True},
                        'cover_image':{'required':False},
                        'category':{'required':True}
                        }

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    user = CustomUserSerializer(read_only=True) 
    class Meta():
        model = Comment
        fields = ['post', 'user', 'created_on','body', 'updated_on']
        extra_kwargs = {'created_on':{'read_only':True},
                        'updated_on':{'read_only':True}
                        }