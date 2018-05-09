from rest_framework import serializers
from .models import Protein


class ProteinSerializer(serializers.ModelSerializer):
    # class ProteinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Protein
        fields = '__all__'
        # fields = ('id', 'p_id')
