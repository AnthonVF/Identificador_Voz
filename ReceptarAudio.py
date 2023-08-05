import pyaudio
import wave
import numpy as np
import os

CHUNK = 1024  # Tamaño del búfer para la captura de audio
FORMAT = pyaudio.paInt16  # Formato de los datos de audio
CHANNELS = 1  # Número de canales de audio (mono)
RATE = 16000  # Tasa de muestreo del audio (en Hz)
RECORD_SECONDS = 61  # Duración de la grabación en segundos

name = input("Ingresa el nombre del individuo: ")  # Ingresar el nombre del individuo para almacenar el audio con dicho nombre
OUTPUT_FILENAME = f"{name}_grabacion.wav"  # Nombre del archivo de salida con el nombre del individuo

# Párrafo a leer:
# En un mundo cada vez más globalizado, la diversidad cultural y étnica se ha convertido en una característica fundamental de 
# nuestras sociedades. Desde las metrópolis bulliciosas hasta los pueblos remotos, podemos encontrar personas de diferentes 
# orígenes, tradiciones y costumbres. Esta riqueza cultural nos brinda la oportunidad de aprender y crecer, al permitirnos 
# conocer y apreciar distintas perspectivas del mundo. Además, la tecnología ha jugado un papel crucial en la conectividad 
# global, permitiéndonos comunicarnos instantáneamente con personas de cualquier rincón del planeta. Por otro lado, los desafíos
# medioambientales se han vuelto cada vez más apremiantes. El cambio climático, la escasez de recursos naturales y la 
# contaminación están en el centro de atención de la comunidad global. Es necesario tomar medidas urgentes para preservar 
# nuestro planeta y garantizar un futuro sostenible para las generaciones venideras. La transición hacia fuentes de energía 
# renovable, la reducción de emisiones de gases de efecto invernadero y la adopción de prácticas sostenibles son algunas de las 
# acciones que se están llevando a cabo para abordar estos desafíos.


# Ruta para guardar el audio original
original_audio_directory = "D:\\Usuario\\Documents\\Python Scripts\\Inteligencia Artificial Python\\Audios\\AudiosSucios"

# Crear el directorio si no existe
os.makedirs(original_audio_directory, exist_ok=True)

# Inicializar el objeto PyAudio
audio = pyaudio.PyAudio()

# Configurar el stream de audio
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Grabando audio...")

frames = []

# Capturar audio en búferes y almacenarlos en una lista
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("¡Grabación finalizada!")

# Detener y cerrar el stream de audio
stream.stop_stream()
stream.close()

# Terminar el objeto PyAudio
audio.terminate()

# Guardar la grabación en un archivo WAV en la ruta del audio original
original_audio_path = os.path.join(original_audio_directory, OUTPUT_FILENAME)
wave_file = wave.open(original_audio_path, "wb")
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b"".join(frames))
wave_file.close()

print(f"Grabación de {name} guardada en {original_audio_path}")

# Ruta del archivo de audio grabado
audio_path = original_audio_path
