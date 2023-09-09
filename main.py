import os
from pydub import AudioSegment

def convert_webm_to_wav(input_folder, output_folder):
    # Verifica se a pasta de entrada existe
    if not os.path.exists(input_folder):
        print(f"A pasta de entrada {input_folder} não existe.")
        return

    # Cria a pasta de saída se ela não existir
    os.makedirs(output_folder, exist_ok=True)

    # Percorre todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Verifica se o arquivo é do formato webm
        if not input_path.endswith(".webm"):
            continue

        # Define o caminho do arquivo de saída
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(output_folder, output_filename)

        # Converte o arquivo de entrada para wav
        audio = AudioSegment.from_file(input_path, format="webm")
        audio = audio.set_sample_width(2) # 16 bits = 2 bytes
        audio = audio.set_channels(2) # Estéreo
        audio = audio.set_frame_rate(48000) # Taxa de amostragem de 48000 Hz
        audio.export(output_path, format="wav")

        print(f"Arquivo convertido com sucesso: {output_path}")

convert_webm_to_wav("input", "output")