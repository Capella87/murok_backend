from django.http import HttpResponse
from django.views.decorators.http import require_GET
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

@require_GET
def robots_txt(request):
    return HttpResponse(robots_txt_content, content_type="text/plain")


robots_txt_content = """\
User-Agent: *
Disallow: /

User-agent: GPTBot
Disallow: /
"""


class MainView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request) -> Response:
        # Return JSON
        data = {
            "Message": "Welcome back!",
            "Status": "Success"
        }

        return Response(data=data, status=status.HTTP_200_OK)
