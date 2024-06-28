from fastapi import HTTPException, status

class EnvelopException(HTTPException):
    status_code = 500
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(EnvelopException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"
        
class IncorrectEmailOrPasswordException(EnvelopException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"
        
class TokenExpiredException(EnvelopException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Срок действия токена истек"
        
class TokenAbsentException(EnvelopException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"
        
class IncorrectTokenFormatException(EnvelopException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"
        
class UserIsNotPresentException(EnvelopException):
    status_code=status.HTTP_401_UNAUTHORIZED

class RoomFullyBooked(EnvelopException):
    status_code=status.HTTP_409_CONFLICT
    detail="Не осталось свободных номеров"

class RoomCannotBeBooked(EnvelopException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось забронировать номер ввиду неизвестной ошибки"

class DateFromCannotBeAfterDateTo(EnvelopException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Дата заезда не может быть позже даты выезда"

class CannotBookHotelForLongPeriod(EnvelopException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Невозможно забронировать отель сроком более месяца"

class CannotAddDataToDatabase(EnvelopException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось добавить запись"

class CannotProcessCSV(EnvelopException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось обработать CSV файл"
