from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def deposite(request):
    output = """<html>
                    <head>
                        <title>BANK OF LOUDA</title>
                    </head>
                    <body>
                        <h1>deposite successfully!!!!</h1>
                        <a href="http://127.0.0.1:8000">Home</a>
                    </body>
                </html>"""
    reponse = HttpResponse(output)
    return reponse

def withdraw(request):
    output = """<html>
                    <head>
                        <title>BANK OF LOUDA</title>
                    </head>
                    <body>
                        <h1>withdraw successfully!!!!</h1>
                        <a href="http://127.0.0.1:8000/loan">Home</a>
                    </body>
                </html>"""
    reponse = HttpResponse(output)
    return reponse

def home(request):
    output = """<html>
                    <head>
                        <title>BANK OF LOUDA</title>
                    </head>
                    <body color=black>
                        <a href="http://127.0.0.1:8000/withdraw">withdraw</a>
                        <a href="http://127.0.0.1:8000/deposite">deposite</a>
                        <a href="http://127.0.0.1:8000/loan">loan</a>
                    </body>
                </html>"""
    reponse = HttpResponse(output)
    return reponse