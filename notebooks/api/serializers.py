from rest_framework import serializers
from notebooks.models import Notebook, Storage, Ram, CPU, VENDOR, CAPACITY, MODEL_VENDOR


class RamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ram
        fields = [
            'pk',
            'capacity',
            'vendor'
        ]
    # id = serializers.IntegerField(read_only=True)
    # capacity = serializers.IntegerField()
    # vendor = serializers.CharField(max_length=20)
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `RAM` instance, given the validated data.
    #     """
    #     return Ram.objects.create(**validated_data)


class CPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPU
        fields = [
            'pk',
            'core',
            'model_vendor'
        ]

    # id = serializers.IntegerField(read_only=True)
    # core = serializers.CharField(max_length=2, default='3')
    # model_vendor = serializers.ChoiceField(choices=MODEL_VENDOR, default='I3')
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `CPU` instance, given the validated data.
    #     """
    #     return CPU.objects.create(**validated_data)


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = [

            'pk',
            'capacity'
        ]

    # id = serializers.IntegerField(read_only=True)
    # capacity = serializers.ChoiceField(choices=CAPACITY, default='HD')
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `STORAGE` instance, given the validated data.
    #     """
    #     return Storage.objects.create(**validated_data)


class NotebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = [

            'pk',
            'model',
            'vendor',
            'description',
            'ram',
            'cpu',
            'storage'
        ]

    # model = serializers.CharField(max_length=20)
    # vendor = serializers.ChoiceField(choices=VENDOR)
    # description = serializers.CharField(max_length=100)
    # ram = serializers.BaseSerializer(RamSerializer)
    # cpu = serializers.BaseSerializer(CPUSerializer)
    # storage = serializers.BaseSerializer(StorageSerializer)
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `NOTEBOOK` instance, given the validated data.
    #     """
    #     return Notebook.objects.create(**validated_data)
    #
    # def to_representation(self, instance):
    #     return ''
