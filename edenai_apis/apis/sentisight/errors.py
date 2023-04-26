from edenai_apis.utils.exception import (
    ProviderErrorLists,
    ProviderInternalServerError,
    ProviderInvalidInputError,
)

# NOTE: error messages should be regex patterns
ERRORS: ProviderErrorLists = {
    ProviderInvalidInputError: [
        r"HTTP 404 Not Found",
        r"invalid url or image",
    ],
    ProviderInternalServerError: [
        r"Internal Server Error",
        r"504 Gateway Time-out",
    ],
}