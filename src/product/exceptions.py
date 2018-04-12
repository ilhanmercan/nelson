from rest_framework import status


class BadRequestException(Exception):
    code = 'BAD_REQUEST'
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidInputException(BadRequestException):
    code = 'INVALID_INPUT'
