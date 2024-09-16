import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": {
    "text": text_to_analyze}}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
    return response.json().get("text")
    else:
    return f"Error: {response.status_code}, {response.text}"if __name__ == "__main__":
    text = "I love this new technology."
    print(emotion_detector(text))
