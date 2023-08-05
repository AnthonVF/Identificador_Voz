import os
import librosa
import soundfile as sf
import numpy as np

# Directorio donde se encuentran los archivos de audio
audio_directory = "D:\\Usuario\\Documents\\Python Scripts\\Inteligencia Artificial Python\\Audios\\AudiosSucios"

# Directorio donde se guardarán los archivos de audio limpios
clean_audio_directory = "D:\\Usuario\\Documents\\Python Scripts\\Inteligencia Artificial Python\\Audios\\AudiosLimpios"

# Obtener la lista de archivos de audio
audio_files = os.listdir(audio_directory)

# Iterar sobre cada archivo de audio
for audio_file in audio_files:
    if audio_file.endswith(".wav"):
        # Ruta completa del archivo de audio
        audio_path = os.path.join(audio_directory, audio_file)

        # Cargar el audio utilizando librosa
        audio, sr = librosa.load(audio_path, sr=None)

        # Aplicar transformada de Fourier
        audio_freq = np.fft.fft(audio)

        # Obtener la señal de audio limpia mediante la transformada inversa de Fourier
        audio_clean = np.fft.ifft(audio_freq).real

        # Guardar los audios limpios en nuevos archivos
        clean_audio_path = os.path.join(clean_audio_directory, audio_file)
        sf.write(clean_audio_path, audio_clean, sr)

        print("Audio limpio guardado:", clean_audio_path)
