from django.contrib.auth.models import User
from django.http import HttpResponse

"""
View to list all users in the system.

* Requires token authentication.
* Only admin users are able to access this view.
"""
# authentication_classes = [authentication.TokenAuthentication]
# permission_classes = [permissions.IsAdminUser]

# def get(self, request, format=None):
#     """
#     Return a list of all users.
#     """
def damn(request):
    usernames = [x for x in range(1, 10)]
    # usernames = [user.username for user in User.objects.all()]
    return HttpResponse(usernames)
