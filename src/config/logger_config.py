import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Pastikan folder logs ada
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Format waktu untuk nama file log per hari
log_filename = os.path.join(LOG_DIR, f"app-{datetime.now().strftime('%Y-%m-%d')}.log")

# Konfigurasi Logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "format": "[%(asctime)s] %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": log_filename,
            "when": "midnight",  # Rotasi log setiap tengah malam
            "interval": 1,
            "backupCount": 7,  # Simpan log hanya untuk 7 hari terakhir
            "encoding": "utf-8",
            "formatter": "detailed",
        }
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        },
        "app": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}

# Fungsi untuk setup logging
def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)

# Panggil setup_logging saat file di-import
setup_logging()

# Logger utama aplikasi
logger = logging.getLogger("app")
