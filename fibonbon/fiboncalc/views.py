from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import senko.skripta as fibonacci
import json

def getFibonacci(request, number=None):
    """
    This is the main funcion for the Fibonacci web application.
    It receives an argument (any kind of argument) and transforms it to integer
    After that, a json with the input and the result is returned. 
    In case the transformation fails (for any reason), it returns a json describing the error
    """
    report = {}
    try:
        n = int(number)
    except:
        report['Error'] = 'No integer numbers given'
        return render_to_response('fibonacci.html', { 'report': json.dumps(report) }, context_instance=RequestContext(request))
    
    try:
        fib = fibonacci.Fibonacci()
        fibnum = fib.fib(n)
        report['Integer'] = number
        report['Fibonacci'] = fibnum
    except:
        report['Error'] = 'Unknown error has occured'
        return render_to_response('fibonacci.html', { 'report': json.dumps(report) }, context_instance=RequestContext(request))
    return render_to_response('fibonacci.html', { 'report': json.dumps(report) }, context_instance=RequestContext(request))
