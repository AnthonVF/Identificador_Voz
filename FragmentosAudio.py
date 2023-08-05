import os
import librosa
import soundfile as sf

clean_audio_directory = "D:\\Usuario\\Documents\\Python Scripts\\Inteligencia Artificial Python\\Audios\\AudiosLimpios"
fragment_duration = 1
fragment_output_directory = "D:\\Usuario\\Documents\\Python Scripts\\Inteligencia Artificial Python\\Audios\\Fragmentos"

class AudioDivider:
    def __init__(self, clean_audio_directory, fragment_duration, fragment_output_directory):
        self.clean_audio_directory = clean_audio_directory
        self.fragment_duration = fragment_duration
        self.fragment_output_directory = fragment_output_directory

    def divide_audio(self):
        audio_files = os.listdir(self.clean_audio_directory)

        for audio_file in audio_files:
            if audio_file.endswith(".wav"):
                # Ruta completa del archivo de audio limpio
                audio_path = os.path.join(self.clean_audio_directory, audio_file)

                # Cargar el audio limpio utilizando librosa
                audio, sr = librosa.load(audio_path, sr=None)

                # Calcular la duración en muestras del fragmento
                fragment_samples = int(self.fragment_duration * sr)

                # Dividir el audio en fragmentos
                num_fragments = len(audio) // fragment_samples
                for i in range(num_fragments):
                    # Obtener el fragmento de audio
                    fragment = audio[i * fragment_samples : (i + 1) * fragment_samples]

                    # Generar el nombre del fragmento de audio
                    fragment_name = os.path.splitext(audio_file)[0] + f"{i+1}"

                    # Ruta completa del fragmento de audio
                    fragment_path = os.path.join(self.fragment_output_directory, fragment_name + ".wav")

                    # Guardar el fragmento de audio
                    sf.write(fragment_path, fragment, sr)

                    print("Fragmento de Audio Limpio guardado:", fragment_path)

audio_divider = AudioDivider(clean_audio_directory, fragment_duration, fragment_output_directory)
audio_divider.divide_audio()
