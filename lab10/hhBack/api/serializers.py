from rest_framework import serializers
from .models import Vacancy,Company


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
    
    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    
    def update(self, instance:Company, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    
    class Meta:
        model = Company
        fields = "__all__"


class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.CharField()
    company = CompanySerializer()


    def create(self, validated_data):
        company_data=validated_data.pop('company')
        company_id=company_data.get('id')
        company_inst=Company.objects.get(id=company_id)
        return Vacancy.objects.create(company=company_inst,**validated_data)
    
    def update(self, instance:Vacancy, validated_data): 
        instance.name = validated_data.get('name', instance.name) 
        instance.salary = validated_data.get('salary', instance.salary) 
        instance.description = validated_data.get('description', instance.description) 
 
        company_data = validated_data.get('company') 
        company_id = company_data.get('id') 
        if company_id: 
            try: 
                company_instance = Company.objects.get(id=company_id) 
                instance.company = company_instance 
            except Company.DoesNotExist: 
                raise serializers.ValidationError("Company with provided ID does not exist") 
 
        instance.save() 
        return instance
    
    class Meta:
        model = Vacancy
        fields = "__all__"

class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"