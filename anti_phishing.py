def analizar_url(url):
    palabras_sospechosas = [
        "login-verify",
        "update-account",
        "free-gift",
        "secure-bank",
        "confirmar-datos"
    ]

    url_lower = url.lower()

    amenazas_encontradas = [
        palabra for palabra in palabras_sospechosas
        if palabra in url_lower
    ]

    if amenazas_encontradas:
        print(f"[ALERTA PHISHING] La URL contiene elementos sospechosos: {amenazas_encontradas}")
    else:
        print("[SEGURO] La URL no presenta patrones obvios de phishing.")

analizar_url("https://mi-banco-seguro.com/login-verify?user=123")
analizar_url("https://www.google.com")
