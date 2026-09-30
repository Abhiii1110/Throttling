from rest_framework.throttling import UserRateThrottle

class CustomeUserRateThrottle(UserRateThrottle):
    scope = "req_time_for_user1"#mension this 'req_time_for_user1' in settings.py