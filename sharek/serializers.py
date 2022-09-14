from rest_framework.serializers import ModelSerializer
from sharek.models import Options, Post, PublicOpenion, AnswerHistory
from users.serializers import RegisterSerializer
from rest_framework import serializers
from users.models import User

class OptionSerializer(ModelSerializer):

    class Meta:
        model = Options
        fields = ["title"]

class PublicOpenionSerializer(ModelSerializer):

    class Meta:
        model = PublicOpenion
        fields = ["appreciate", "depreciate"]


class PostSerializer(ModelSerializer):

    option = OptionSerializer(many=True)
    answer = OptionSerializer(many=False)
    
    class Meta:
        model = Post
        fields = ["id", "question", "answer", "option", "posted"]


    def create(self, validated_data):

        user = self.context["request"].user
        options = validated_data.pop("option", None)
        options = [Options.objects.create(title=option.get("title")) for option in options]
        answer = Options.objects.create(title=validated_data.pop("answer", None).get("title"))
        options.append(answer)
        post = Post(**validated_data, answer=answer)
        post.save()
        post.option.add(*options)
        post.save()
        user.post.add(post)
        user.save()

        return post


class AnswerHistorySerializer(ModelSerializer):

    user = RegisterSerializer(many=False, read_only=True)

    class Meta:
        model = AnswerHistory
        fields = ["question", "answer", "user"]

    
    def create(self, validated_data):
    
        user = self.context["request"].user
        validated_data["user"] = user
        answer_history = AnswerHistory.objects.create(**validated_data)
        return answer_history
    










