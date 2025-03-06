from rest_framework import serializers

from ..models import Team, Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('full_name', 'email', 'phone_number', 'role', 'age', 'is_captain')


class TeamCreateSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True)

    class Meta:
        model = Team
        fields = ('name', 'university', 'participants')

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        team = Team.objects.create(**validated_data)

        for participant_data in participants_data:
            Participant.objects.create(team=team, **participant_data)

        return team

    def validate(self, data):
        participants_data = data.get('participants', [])
        captain_count = sum(1 for participant in participants_data if participant.get('is_captain'))

        if captain_count == 0:
            raise serializers.ValidationError("Должен быть хотя бы один капитан в команде.")
        if captain_count > 1:
            raise serializers.ValidationError("В команде может быть только один капитан.")
        return data
