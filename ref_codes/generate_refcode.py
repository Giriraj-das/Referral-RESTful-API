import secrets


def generate_ref_code() -> str:
    """Generate urlsafe 32 bytes token (43 symbols)"""
    return secrets.token_urlsafe()
