import json_log_formatter
import logging
from django.utils.timezone import now


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord):
        extra['name'] = record.name
        extra['filename'] = record.filename
        extra['funcName'] = record.funcName
        extra['msecs'] = record.msecs
        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return {
            'message': message,
            'timestamp': now(),
            'level': record.levelname,
            'context': extra
        }
