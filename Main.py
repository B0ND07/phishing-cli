

from API import get_prediction

# path to trained model
model_path = r"models/Malicious_URL_Prediction.h5"

# input url
url = "www.google.com/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)

