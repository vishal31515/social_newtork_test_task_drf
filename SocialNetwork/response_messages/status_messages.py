
from ast import Str


class ResponseStatuses(object):
    USER_CREATED: str = "User created."
    INVALID_OTP: str = "Invalid OTP"
    LOGOUT: str = "User Successfully Logout"
    NOT_LOGIN: str = "User is not logged in"
    # UPDATED: str = "Data updated"
    # USER_NOT_EXIST: str = "User doesn't exists"
    # DATA_NOT_FOUND: str = "Data Not Found"
    # INACTIVE_USER: str = "Inactive User"
    # INVALID_PASSWORD: str = "Please enter a valid password"
    # INVALID_EMAIL: str = "Please enter a valid email"
    # INVALID_TOKEN: str = "Invalid Token"
    # DELETED: str = "Record Deleted"
    # NOT_AUTHORIZED: str = "You don't have permissions"
    # NOT_CHANGE_CURRENT: str = "You can't change your own status/role"
    # VALID_ACCESS_TOKEN: str = "Access token is valid"
    # INVALID_ACCESS_TOKEN: str = "Unauthorized / Invalid Token"
    # ACCESS_TOKEN_EXPIRED: str = "Token Expired"
    # REFRESH_TOKEN_EXPIRED: str = "Refresh Token Expired"
    # INVALID_REFRESH_TOKEN: str = "Invalid Refresh Token"
    # TOKEN_EXPIRED: str = "Token Expired"
    # METHOD_NOT_ALLOWED: str = "Method not allowed"
    # LINK_EXPIRED: str = "Link Expired"
    TRY_AGAIN: str = "Something went wrong.Please try again."
    # TOKEN_VERIFIED: str = " Token succesfully verified"
    # INVALID_API_KEY: str = "The request is missing a valid API key"
    # PHONE_VERIFIED: str = "Phone succesfully verified"
    # PROFILE_NOT_EXISTS: str = "Mobile number not exists"
    # WRONG_VERIFICATION_TYPE: str = "Wrong verification type or mobile no not match with email"
    # OTP_SENT: str = "OTP succesfully sent",
    # TEMPLATE_APPROVED: str = "Template successfully approved"


response_status = ResponseStatuses()
