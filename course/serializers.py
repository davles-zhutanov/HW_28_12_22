from rest_framework import serializers

from .models import Course, Student, Mentor

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    date = serializers.DateField()
    student = serializers.CharField(max_length=20)
    mentor = serializers.CharField(max_length=20)

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        courses = Course.objects.create(
            name=validated_data['name'],
            date=validated_data['date'],
            student=validated_data['student'],
            mentor=validated_data['mentor']
        )
        return courses

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.date = validated_data['date']
        instance.student = validated_data['student']
        instance.mentor = validated_data['mentor']
        instance.save()
        return instance



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        students = Student.objects.create(
            name=validated_data['name'],
            birth_date=validated_data['birth_date'],
        )
        return students

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.birth_date = validated_data['birth_date']
        instance.save()
        return instance

class MentorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    experience = serializers.IntegerField()

    def __str__(self):
        return f'{self.name}-{self.experience}'

    def create(self, validated_data):
        mentors = Mentor.objects.create(
            name=validated_data['name'],
            experience=validated_data['experience'],
        )
        return mentors

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.experience = validated_data['experience']
        instance.save()
        return instance
