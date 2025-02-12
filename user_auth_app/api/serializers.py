from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User


def check_existing_mail_adress(validated_data):
    mail_adress = validated_data.get('email')
    mail_adress_exists = User.objects.filter(email=mail_adress).get()
    if mail_adress_exists:
        raise serializers.ValidationError({'error': 'email adress already exists'})


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']


class RegistrationSerializer(serializers.ModelSerializer):

    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        


    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        
        if pw != repeated_pw:
            raise serializers.ValidationError({'error':'password dont match'})

        # check_existing_mail_adress(self.validated_data) # funktioniert ?
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)




