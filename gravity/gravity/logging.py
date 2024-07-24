from os import path

LOGS_DIR = "logs"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s [%(asctime)s] %(message)s'
        },
    },
    "handlers": {
        "client_file_handler": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': path.join(LOGS_DIR, 'client.log'),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "client": {
            'level': 'DEBUG',
            "handlers": ["client_file_handler"]
        },
    },
}
