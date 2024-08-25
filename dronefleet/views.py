from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from dronefleet.models import DroneCategory
from dronefleet.models import Drone, Pilot, Competition
from dronefleet.serializers import DroneCategorySerializer, DroneSerializer, \
    PilotCompetitionSerializer, PilotSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
import django_filters as filters
from rest_framework import permissions
from dronefleet import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = (
        'name',

    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )
   
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DroneCategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategoryList
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = ('name', 'drone_category', 'manufacturing_date',
                     'has_it_competed',)
    search_fields = ('^name', )
    ordering_fields = ('name', 'manufacturing_date',)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )


class PilotList(generics.ListCreateAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_fields = (
        'name',
        'gender',
        'races_count',
    )
    search_fields = (
        '^name',
    )

    ordering_fields = (
          'name',
          'races_count'

     )
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
        )


class CompetitionFilter(filters.FilterSet):
    """
    # lookup expression 'gte', means greater than or equal to.
    # 'lte' means less than or equal to.
"""
    from_achievement_date = DateTimeFilter(name='distance_achievement_date',
                                           lookup_expr='gte')
    to_achievement_date = DateTimeFilter(name='distance_achievement_date',
                                         lookup_expr='lte')
    min_distance_in_metres = NumberFilter(name='distance_in_metres',
                                          lookup_expr='gte')
    max_distance_in_metres = NumberFilter(name='distance_in_metres',
                                          lookup_expr='lte')
    drone_name = AllValuesFilter(name='drone__name')
    pilot_name = AllValuesFilter(name='pilot__name')

    class Meta:
        model = Competition
        fields = ('distance_in_metres', 'from_achievement_date',
                  'to_achievement_date', 'min_distance_in_metres',
                  'max_distance_in_metres',
                  # drone__name will be accessed as drone_name
                  'drone_name',
                  # pilot__name will be accessed as pilot_name
                  'pilot_name',
                  )


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'
    filter_class = CompetitionFilter
    ordering_fields = (
        'distance_in_metres',
        'distance_achievement_date',
        )


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name,
                                        request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
            })
