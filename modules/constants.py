import enum

class HttpResponse(enum.Enum):
  
  OK = (200, "<h1>Success</h1>")
  BAD_REQUEST = (400, "<h1>No UID was found in your request</h1>")
  NOT_FOUND = (404, "<h1>UID not found</h1>")
  CONFLICT = (409, "<h1>UID already exists</h1>")
  INVALID_ARGUMENT_EXCEPTION = (422, "<h1>UID is invalid</h1>")
  INTERNAL_SERVER_ERROR = (500, "<h1>Internal server error</h1>")
  def __init__(self, code, content):
    self.code = code
    self.content = content

http_code_to_enum = {
  200: HttpResponse.OK,
  400: HttpResponse.BAD_REQUEST,
  404: HttpResponse.NOT_FOUND,
  409: HttpResponse.CONFLICT,
  422: HttpResponse.INVALID_ARGUMENT_EXCEPTION,
  500: HttpResponse.INTERNAL_SERVER_ERROR,
}