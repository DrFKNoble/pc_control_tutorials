import serial

from django.shortcuts import render

from .models import PIN


ser = serial.Serial('COM3')


def toggle_pin(pin=13):

    ser.write('{}\n'.format(pin).encode('utf-8'))

    return 0


def index(request):
    pin_list = PIN.objects.order_by('name')[:]
    
    context = {'pin_list': pin_list}

    return render(request, 'app/index.html', context)


def toggle(request, pin_number):
    
    pin = PIN.objects.get(pin_number=pin_number)
    pin.state = False if pin.state is True else True
    pin.save()

    toggle_pin(pin.pin_number)
        
    pin_list = PIN.objects.order_by('name')[:]
    
    context = {'pin_list': pin_list}

    return render(request, 'app/index.html', context)