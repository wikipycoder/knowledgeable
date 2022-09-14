from xml.dom import ValidationErr
from rest_framework.serializers import ModelSerializer
from .models import Relationship, Group
from users.serializers import RegisterSerializer, UserDataSerializer
from rest_framework import serializers
from users.models import User




class RelationshipSerializer(ModelSerializer):
    
    following = RegisterSerializer(many=False, read_only=True)
    follower = RegisterSerializer(many=False, read_only=True)
    username = serializers.CharField(max_length=200, write_only=True)
    unfollow = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Relationship
        fields = ["id", "fan", "friend", "following", "follower", "username", "unfollow"]
    

    def is_already_following(self, user, user2):

        if user.relationship.filter(following=user2):
            raise serializers.ValidationError("{} is already following this {}".format(user, user2))

        return False

    def create(self, validated_data):

        user = self.context["request"].user
        user2 = validated_data.pop("username", None)
        unfollow = validated_data.pop("unfollow", None)


        try:
            user2 = User.objects.get(username=user2)

            if unfollow:
                return self.unfollowing(user, user2)

            self.is_already_following(user, user2)
            
            if user == user2:
                raise serializers.ValidationError("you can't follow yourself")
            
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")


        r2 = user2.relationship.filter(following=user).first()

        if r2:
            r2.friend = True
            r2.fan = False
            r2.follower = user
            r2.save()
            r1 = Relationship(following=user2, follower=user2)
            r1.friend = True
            r1.save()
            user.relationship.add(r1)
            user.save()
            return r1
    
        else:
            r1 = Relationship(following=user2)
            r1.fan = True
            r1.save()
            user.relationship.add(r1)
            user.save()
            return r1



    def unfollowing(self, user, user2):

        r1 = user.relationship.filter(following=user2).first()
        r2 = user2.relationship.filter(following=user).first()
        
        if r1:
            print("r1 got executed")
            r1.delete()
            print("deleted")


            if r2:
                r2.follower = None
                r2.friend = False
                r2.fan = True
                r2.save()

        else:
            error_message = "{} is not following {}".format(user, user2)
            raise serializers.ValidationError(error_message)
        return user.relationship.all()
      





class GroupSerializer(ModelSerializer):
    
    owner = RegisterSerializer(many=False, required=False)
    class Meta:
        model = Group
        fields = ["id", "title", "description", "group_type", "members", "post", "owner"]  


        
