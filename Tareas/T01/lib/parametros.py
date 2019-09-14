# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 154,
        'MAX': 212
    },
    'CARROCERIA': {
        'MIN': 425,
        'MAX': 598
    },
    'RUEDAS': {
        'MIN': 243,
        'MAX': 367
    },
    'MOTOR': {
        'MIN': 559,
        'MAX': 724
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 1680,
        'MAX': 2420
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 462,
        'MAX': 550
    },
    'CARROCERIA': {
        'MIN': 120,
        'MAX': 150
    },
    'RUEDAS': {
        'MIN': 270,
        'MAX': 405
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 502,
        'MAX': 623
    },
    'PESO': {
        'MIN': 3020,
        'MAX': 3980
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 92,
        'MAX': 143
    },
    'CARROCERIA': {
        'MIN': 235,
        'MAX': 291
    },
    'RUEDAS': {
        'MIN': 240,
        'MAX': 566
    },
    'MOTOR': {
        'MIN': 345,
        'MAX': 489
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 193,
        'MAX': 378
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 42,
        'MAX': 95
    },
    'CARROCERIA': {
        'MIN': 178,
        'MAX': 233
    },
    'RUEDAS': {
        'MIN': 792,
        'MAX': 960
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 843,
        'MAX': 1024
    },
    'PESO': {
        'MIN': 10,
        'MAX': 28
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 600,
        'EFECTO': 2
    },
    'CARROCERIA': {
        'COSTO': 260,
        'EFECTO': 2
    },
    'RUEDAS': {
        'COSTO': 320,
        'EFECTO': 2
    },
    'MOTOR': {
        'COSTO': 280,
        'EFECTO': 2
    },
    'ZAPATILLAS': {
        'COSTO': 280,
        'EFECTO': 2
    }
}


# Características de los pilotos de los diferentes equipos
# PERSONALIDAD is list so it can be used in random.choice()
# Values in Enunciado.pdf
# Supuesto: se le colocó tilde a 'HÍBRIDOS' por consistencia con enunciado y 
# savefiles


EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': ['precavido']
    },
    'HÍBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': ['osado', 'precavido']
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': ['osado']
    }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 30

# Velocidad intencional
EFECTO_OSADO = 2
EFECTO_PRECAVIDO = 1

# Dificultad de control del vehículo
PESO_MEDIO = 80
EQUILIBRIO_PRECAVIDO = 2

# Tiempo pits
TIEMPO_MINIMO_PITS = 5
VELOCIDAD_PITS = 5

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 2
BONIFICACION_OSADO = 1

# Ponderacion efectos
POND_EFECT_HIELO = 2
POND_EFECT_ROCAS = 2
POND_EFECT_DIFICULTAD = 3


# Paths de los archivos
# Contain lists, to be used in os.path.join(*PATHS[index])
PATHS = {
    'PISTAS': ['databases', 'static', 'pistas.csv'],
    'CONTRINCANTES': ['databases', 'static', 'contrincantes.csv'],
    'PILOTOS': ['databases', 'pilotos.csv'],
    'VEHICULOS': ['databases', 'vehículos.csv']
}

# Precios de los vehículos

PRECIOS = {
    'AUTOMOVIL' : 550,
    'MOTOCICLETA' : 900,
    'TRONCOMOVIL' : 370,
    'BICICLETA' : 1050
}

# Cantidad contrincantes (https://github.com/IIC2233/syllabus/issues/123)
NUMERO_CONTRINCANTES = 7

# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
