from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import xarray
import matplotlib.pyplot as plt

era5 = xarray.open_zarr(
    "gs://gcp-public-data-arco-era5/ar/1959-2022-full_37-1h-0p25deg-chunk-1.zarr-v2",
    chunks={'time': 48},
    consolidated=True,
)



type coord = tuple[float, float]
type Time = list[str]

# Create your views here.
def Home(request):
    return JsonResponse({})

def u10(request,latitude: str, longitude: str, time: str):
    '''
    Componente U (este-oeste) del viento a 10 metros sobre la superficie
    latitude: Arreglo con pares inicio-fin
    longitud: Arreglo con pares inicio-fin
    time: Fecha inicio a fecha final  
    '''

    lat = latitude.split(',')
    long = longitude.split(',')
    t = time.split(',')

    if (len(lat) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Latitud mal ingresada, deben ser dos valores entre [-90,90], separados por una coma'})
    elif (len(long) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Longitud mal ingresada, deben ser dos valores entre [0,359.8], separados por una coma'})

    try:
        latitudeInitial = int(lat[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud inicial no es un entero'})
        
    try:
        latitudeFinal = int(lat[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud final no es un entero'})
    
    try:
        longitudeInitial = int(long[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud inicial no es un entero'})
    
    try:
        longitudeFinal = int(long[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud final no es un entero'})

    timeInitial = t[0]
    
    timeFinal = 0
    if(len(t)>1):
        timeFinal= t[1]
    
    try:
        data = era5['10m_u_component_of_wind'].loc[dict(latitude=slice(latitudeInitial,latitudeFinal), 
                                                        longitude=slice(longitudeInitial,longitudeFinal), 
                                                        time=(slice(timeInitial,timeFinal) if timeFinal != 0 else timeInitial))].values.tolist()
    except:
        return JsonResponse({'Mensaje del Servidor': 'Hubo un error al obtener los datos'})

    response = {'coords': {'latitudeInitial':latitudeInitial, 
                                'latitudeFinal':latitudeFinal, 
                                'longitudeInitial':longitudeInitial, 
                                'longitudeFinal':longitudeFinal}, 
                 'time': {'timeInitial': timeInitial, 
                            'timeFinal':timeFinal},
                 'data': data,
                 'units': 'm*s**-1'}

    return JsonResponse(response)

def v10(request,latitude: str, longitude: str, time: str):
    '''
    Componente V (norte-sur) del viento a 10 metros sobre la superficie
    latitude: Arreglo con pares inicio-fin
    longitud: Arreglo con pares inicio-fin
    time: Fecha inicio a fecha final  
    '''

    lat = latitude.split(',')
    long = longitude.split(',')
    t = time.split(',')

    if (len(lat) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Latitud mal ingresada, deben ser dos valores entre [-90,90], separados por una coma'})
    elif (len(long) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Longitud mal ingresada, deben ser dos valores entre [0,359.8], separados por una coma'})

    try:
        latitudeInitial = int(lat[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud inicial no es un entero'})
        
    try:
        latitudeFinal = int(lat[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud final no es un entero'})
    
    try:
        longitudeInitial = int(long[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud inicial no es un entero'})
    
    try:
        longitudeFinal = int(long[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud final no es un entero'})

    timeInitial = t[0]
    
    timeFinal = 0
    if(len(t)>1):
        timeFinal= t[1]
    
    try:
        data = era5['10m_v_component_of_wind'].loc[dict(latitude=slice(latitudeInitial,latitudeFinal), 
                                                        longitude=slice(longitudeInitial,longitudeFinal), 
                                                        time=(slice(timeInitial,timeFinal) if timeFinal != 0 else timeInitial))].values.tolist()
    except:
        return JsonResponse({'Mensaje del Servidor': 'Hubo un error al obtener los datos'})

    response = {'coords': {'latitudeInitial':latitudeInitial, 
                                'latitudeFinal':latitudeFinal, 
                                'longitudeInitial':longitudeInitial, 
                                'longitudeFinal':longitudeFinal}, 
                 'time': {'timeInitial': timeInitial, 
                            'timeFinal':timeFinal},
                 'data': data,
                 'units': 'm*s**-1'}

    return JsonResponse(response)

def t2m(request,latitude: str, longitude: str):
    '''
    Indica la temperatura a 2 metros sobre la superficie
    latitude: Arreglo con pares inicio-fin
    longitud: Arreglo con pares inicio-fin
    '''

    lat = latitude.split(',')
    long = longitude.split(',')

    if (len(lat) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Latitud mal ingresada, deben ser dos valores entre [-90,90], separados por una coma'})
    elif (len(long) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Longitud mal ingresada, deben ser dos valores entre [0,359.8], separados por una coma'})

    try:
        latitudeInitial = int(lat[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud inicial no es un entero'})
        
    try:
        latitudeFinal = int(lat[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud final no es un entero'})
    
    try:
        longitudeInitial = int(long[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud inicial no es un entero'})
    
    try:
        longitudeFinal = int(long[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud final no es un entero'})

    try:
        data = era5['2m_temperature'].loc[dict(latitude=slice(latitudeInitial,latitudeFinal), 
                                                        longitude=slice(longitudeInitial,longitudeFinal))].values.tolist()
    except:
        return JsonResponse({'Mensaje del Servidor': 'Hubo un error al obtener los datos'})

    response = {'coords': {'latitudeInitial':latitudeInitial, 
                                'latitudeFinal':latitudeFinal, 
                                'longitudeInitial':longitudeInitial, 
                                'longitudeFinal':longitudeFinal}, 
                 'data': data,
                 'units': 'K'}

    return JsonResponse(response)

def anor(request,latitude: str, longitude: str):
    '''
    Ángulo de la orografía a escala subcuadrícula
    latitude: Arreglo con pares inicio-fin
    longitud: Arreglo con pares inicio-fin
    '''

    lat = latitude.split(',')
    long = longitude.split(',')

    if (len(lat) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Latitud mal ingresada, deben ser dos valores entre [-90,90], separados por una coma'})
    elif (len(long) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Longitud mal ingresada, deben ser dos valores entre [0,359.8], separados por una coma'})

    try:
        latitudeInitial = int(lat[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud inicial no es un entero'})
        
    try:
        latitudeFinal = int(lat[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud final no es un entero'})
    
    try:
        longitudeInitial = int(long[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud inicial no es un entero'})
    
    try:
        longitudeFinal = int(long[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud final no es un entero'})

    try:
        data = era5['2m_temperature'].loc[dict(latitude=slice(latitudeInitial,latitudeFinal), 
                                                        longitude=slice(longitudeInitial,longitudeFinal))].values.tolist()
    except:
        return JsonResponse({'Mensaje del Servidor': 'Hubo un error al obtener los datos'})

    response = {'coords': {'latitudeInitial':latitudeInitial, 
                                'latitudeFinal':latitudeFinal, 
                                'longitudeInitial':longitudeInitial, 
                                'longitudeFinal':longitudeFinal}, 
                 'data': data,
                 'units': 'radians'}

    return JsonResponse(response)

def isor(request,latitude: str, longitude: str):
    '''
    Describe la anisotropía de la orografía a escala subcuadrícula.
    latitude: Arreglo inicio-fin
    longitud: Arreglo inicio-fin
    '''

    lat = latitude.split(',')
    long = longitude.split(',')

    if (len(lat) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Latitud mal ingresada, deben ser dos valores entre [-90,90], separados por una coma'})
    elif (len(long) < 1):
        return JsonResponse({'Mensaje del Servidor': 'Longitud mal ingresada, deben ser dos valores entre [0,359.8], separados por una coma'})

    try:
        latitudeInitial = int(lat[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud inicial no es un entero'})
        
    try:
        latitudeFinal = int(lat[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La latitud final no es un entero'})
    
    try:
        longitudeInitial = int(long[0])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud inicial no es un entero'})
    
    try:
        longitudeFinal = int(long[1])
    except:
        return JsonResponse({'Mensaje del Servidor': 'La longitud final no es un entero'})

    try:
        data = era5['2m_temperature'].loc[dict(latitude=slice(latitudeInitial,latitudeFinal), 
                                                        longitude=slice(longitudeInitial,longitudeFinal))].values.tolist()
    except:
        return JsonResponse({'Mensaje del Servidor': 'Hubo un error al obtener los datos'})

    response = {'coords': {'latitudeInitial':latitudeInitial, 
                                'latitudeFinal':latitudeFinal, 
                                'longitudeInitial':longitudeInitial, 
                                'longitudeFinal':longitudeFinal}, 
                 'data': data,
                 'units': 'not specified'}

    return JsonResponse(response)