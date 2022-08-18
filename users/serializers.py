from wsgiref.validate import validator

from django.contrib.auth import \
    authenticate  # django기본 authenticate 함수, DefaultAuthBackend인 TokenAuth방식
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import \
    validate_password  # django기본 패스워드 검증도구
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # Token 모델
from rest_framework.validators import UniqueValidator  # 이메일 중복방지 검증 도구
from typing_extensions import Required


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password], #비밀번호에 대한 검증
    )
    password2 = serializers.CharField(write_only=True, required=True) #비밀번호 확인 필드

    class Meta:
        model = User
        fields = ('username',  'password', 'password2', 'email')

    def validate(self, data): #추가적으로 비밀번호 일치여부 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': "비밀번호가 일치하지 않습니다."}
            )
        return data
    
    def create(self, validated_data): #CREATE요청에 대해 create메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하게 함
        user = User.objects.create_user(
            username=validated_data['username']
            # email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user) #토큰에서 유저 찾아 응답
            
            return token

        raise serializers.ValidationError(
                {"error": "Unable to log in with provided credentials."}
            )
