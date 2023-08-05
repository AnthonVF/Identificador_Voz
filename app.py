from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x)) 
    return e_x / e_x.sum(axis=0)

app = Flask(__name__)
model = tf.keras.models.load_model('models/modelo_entrenado.h5')

threshold = 0.8

@app.route('/', methods=['GET', 'POST'])

def predict():
    individuos = ['Pablo' ,'Fernando' ,'Jamlilyn', 'Anthony' ,'Diego' ,'Sergio' ,'Mattew']

    if request.method == 'POST':
        if 'audioReq' in request.files:  
            audioReq = request.files['audioReq'].read()

            # Preprocesamiento del audio
            def decodificar_audio(audio_binary):
                audio, _ = tf.audio.decode_wav(contents=audio_binary)
                return tf.squeeze(audio, axis=-1)

            def obtener_spectrogram(waveform):
                input_len = 16000
                waveform = waveform[:input_len] 
                zero_padding = tf.zeros([16000] - tf.shape(waveform), dtype=tf.float32) 
                waveform = tf.cast(waveform, dtype=tf.float32)
                equal_length = tf.concat([waveform, zero_padding], 0)
                spectrogram = tf.signal.stft(equal_length, frame_length=255, frame_step=128)
                spectrogram = tf.abs(spectrogram)
                spectrogram = spectrogram[..., tf.newaxis]
                return spectrogram

            def preprocess_audio(audio_binary):
                waveform = decodificar_audio(audio_binary)
                spectrogram = obtener_spectrogram(waveform)
                return spectrogram

            spectrogram = preprocess_audio(audioReq)

            # Predicción con el modelo
            prediction = model.predict(tf.expand_dims(spectrogram, axis=0))
            prediction_softmax = softmax(prediction[0])
            predicted_index = np.argmax(prediction_softmax)
            predicted_proba = prediction_softmax[predicted_index]
            predicted_proba_formatted = round(predicted_proba * 100, 2)
            classification = individuos[predicted_index] if predicted_proba > threshold else "desconocido"

            return render_template('index.html', prediction=classification, proba=predicted_proba_formatted)
        
        else:
            return "No se envió ningún archivo de audio"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)