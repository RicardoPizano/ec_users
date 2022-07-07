from models.responses import UserResponse, ErrorResponse

user_response = {
    200: {"model": UserResponse},
    409: {"model": ErrorResponse}
}