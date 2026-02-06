import re
import hashlib

def clean_non_numeric(raw_string):
    return re.sub(r"\D", "", raw_string)

def validate_cpf_math(cpf_numeric):
    if len(cpf_numeric) != 11 or cpf_numeric == cpf_numeric[0] * 11:
        return False
    sum_d1 = sum(int(cpf_numeric[i]) * (10 - i) for i in range(9))
    d1 = (sum_d1 * 10) % 11
    d1 = 0 if d1 == 10 else d1
    sum_d2 = sum(int(cpf_numeric[i]) * (11 - i) for i in range(10))
    d2 = (sum_d2 * 10) % 11
    d2 = 0 if d2 == 10 else d2
    return int(cpf_numeric[9]) == d1 and int(cpf_numeric[10]) == d2

def anonymize_data(raw_data):
    return hashlib.sha256(raw_data.encode()).hexdigest()

def process_match(match_string, label):
    # Se for CPF, valida matematicamente
    if label == "cpf":
        numeric_data = clean_non_numeric(match_string)
        if validate_cpf_math(numeric_data):
            return {
                "valid": True,
                "hash": anonymize_data(numeric_data),
                "masked": f"***.{numeric_data[3:6]}.***-{numeric_data[9:]}"
            }
    # Se for E-mail, apenas valida se tem o formato e masca
    elif label == "email":
        parts = match_string.split('@')
        masked = f"{parts[0][0]}***@{parts[1]}"
        return {
            "valid": True,
            "hash": anonymize_data(match_string),
            "masked": masked
        }
    
    return {"valid": False}
