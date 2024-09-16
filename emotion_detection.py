import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
