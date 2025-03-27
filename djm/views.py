from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_api_backup(request):
    if request.method == "OPTIONS":
        # print request headers here
        print("\n================ begin request headers")
        print(json.dumps(dict(request.headers), indent=4))
        print("================ end request headers")

        # Handle preflight request
        response = HttpResponse()
        # response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Origin"] = "http://localhost:8080"
        # response["Access-Control-Allow-Methods"] = "OPTIONS, POST" # 非必须
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Max-Age"] = 5 # devtools uncheck "disable cache" to see effect

        # print response headers here
        print("================ begin response headers")
        print(json.dumps(dict(response.headers), indent=4))
        print("================ end response headers\n")

        return response

    if request.method == "POST":
        # print request headers here
        print("\n================ begin request headers")
        print(json.dumps(dict(request.headers), indent=4))
        print("================ end request headers")

        # Sample login data
        data = {
            "user_id": 1,
            "username": "sample_user",
            "email": "sample_user@example.com",
            "token": "sample_token_12345"
        }

        response = JsonResponse(data)
        # response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Origin"] = "http://localhost:8080"

        # print response headers here
        print("================ begin response headers")
        print(json.dumps(dict(response.headers), indent=4))
        print("================ end response headers")
        return response

    return HttpResponse(status=405)  # Method not allowed

@csrf_exempt
def login_api(request):
    # print request headers here
    print("\n================ begin request headers")
    print(json.dumps(dict(request.headers), indent=4))
    print("================ end request headers")

    # Sample login data
    data = {
        "user_id": 1,
        "username": "sample_user",
        "email": "sample_user@example.com",
        "token": "sample_token_12345"
    }

    response = JsonResponse(data)
    # response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Origin"] = "http://localhost:8080"

    # print response headers here
    print("================ begin response headers")
    print(json.dumps(dict(response.headers), indent=4))
    print("================ end response headers")
    return response
