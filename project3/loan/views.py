from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def loan(request):
    output = """<html>
                    <head>
                        <title>BANK OF LOUDA</title>
                    </head>
                    <body color=black>
                        <h1>Outdated😒😒😒😒😒😒</h1>
                        <a href="http://127.0.0.1:8000">Home</a>
                    </body>
                </html>"""
    reponse = HttpResponse(output)
    return reponse
