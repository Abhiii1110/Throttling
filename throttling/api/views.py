# from . models import Student
# from . serializers import StudentSerializer
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.authentication import SessionAuthentication

# Import throttling classes
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# 1. Anon is for anoynmous/login nai kel tenchya sathi
# 2. User is for jeni register/login kelay tenchya sathi
# 3. ScopeRateThrottle mnj api chya pratyek part la time /rate limit lau shakto
# For custome user req time
# from api.throttling import CustomeUserRateThrottle



# For throttling ,changes need to be done in settings.py file
# Anon ani user (custom wala extra mdhi kelay)
# class StundentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

    # throttling ch rate mnj user kiti vela api la req taku shakto ani jo user nhiye to kiti vela req taku shakto te setting.py mdhi mention kryla lgt
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    
    # custom
    # throttle_classes = [AnonRateThrottle,CustomeUserRateThrottle]#userratethrottle sglya class sathi same setting mdhi time dilay toch use honar pn jr aplyala prtyek user sathi vegl vegl time decide krychay tr userratethrottle mdhla inherit krun use kru shakto,(Separate throttling.py file mdhi mention kryla lgt)


# SCOPE THROTTLING (Without authentication) we can use it using authentication as well
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'onlyviewAndRetrive'


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create_update_delete'


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'onlyviewAndRetrive'


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create_update_delete'


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create_update_delete'
