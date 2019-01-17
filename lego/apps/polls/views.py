from rest_framework import decorators, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lego.apps.permissions.api.views import AllowedPermissionsMixin
from lego.apps.polls.models import Poll
from lego.apps.polls.serializers import (
    DetailedPollSerializer,
    PollCreateSerializer,
    PollSerializer,
    PollUpdateSerializer,
)


class PollViewSet(AllowedPermissionsMixin, viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    ordering = "-created_at"

    def get_serializer_class(self):
        if self.action == "create":
            return PollCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return PollUpdateSerializer
        elif self.action == "retrieve":
            return DetailedPollSerializer
        return PollSerializer

    @decorators.detail_route(methods=["POST"], permission_classes=[IsAuthenticated])
    def vote(self, request, *args, **kwargs):
        poll = self.get_object()
        vote_result = poll.vote(request.user, request.data["option_id"])
        serializer = self.get_serializer_class()(poll, context={"request": request})
        if vote_result == "forbidden":
            return Response(serializer.data, status=403)
        return Response(serializer.data)
