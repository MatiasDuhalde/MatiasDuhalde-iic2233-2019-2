# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 220,
        'MAX': 382
    },
    'CARROCERIA': {
        'MIN': 150,
        'MAX': 400
    },
    'RUEDAS': {
        'MIN': 40,
        'MAX': 62
    },
    'MOTOR': {
        'MIN': 130,
        'MAX': 400
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 586,
        'MAX': 1000
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 95,
        'MAX': 115
    },
    'CARROCERIA': {
        'MIN': 85,
        'MAX': 115
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
        'MIN': 38,
        'MAX': 60
    },
    'PESO': {
        'MIN': 140,
        'MAX': 364
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 60,
        'MAX': 90
    },
    'CARROCERIA': {
        'MIN': 32,
        'MAX': 92
    },
    'RUEDAS': {
        'MIN': 15,
        'MAX': 42
    },
    'MOTOR': {
        'MIN': 30,
        'MAX': 90
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
        'MIN': 25,
        'MAX': 40
    },
    'CARROCERIA': {
        'MIN': 10,
        'MAX': 35
    },
    'RUEDAS': {
        'MIN': 5,
        'MAX': 20
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 20,
        'MAX': 40
    },
    'PESO': {
        'MIN': 78,
        'MAX': 200
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
