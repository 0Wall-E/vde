from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def mp(request):
    index = """<!DOCTYPE html>
    <html>
    <h1>Hello from django</h1>
    </html>"""
    return HttpResponse(index)
