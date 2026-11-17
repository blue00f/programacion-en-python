import requests

def ejecutar():
    print("\n--- 4. REQUESTS ---")
    try:
        response = requests.get("https://api.github.com", timeout=5)
        print(f"Status Code: {response.status_code}")
        print("Headers (content-type):", response.headers.get("content-type"))
    except Exception as e:
        print("Error en request:", e)