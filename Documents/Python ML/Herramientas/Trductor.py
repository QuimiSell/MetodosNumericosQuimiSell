import os
import queue
import sys
import threading
import time
import wave
import numpy as np
import sounddevice as sd
import speech_recognition as sr

SAMPLE_RATE = 44100
CHANNELS = 2
FILENAME = "temp_exam_audio.wav"
q = queue.Queue()


def callback(indata, frames, time_info, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def record_audio_until_stop():
    q.queue.clear()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

    print("\n[~] Grabando audio... Reproduce el audio del examen.")
    print("[~] Presiona ENTER cuando quieras detener la grabación.")

    stop_event = threading.Event()

    def wait_for_stop():
        input()
        stop_event.set()

    stopper = threading.Thread(target=wait_for_stop, daemon=True)
    stopper.start()

    device_index = None
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if (
            "Mezcla estéreo" in dev["name"]
            or "Stereo Mix" in dev["name"]
            or "Wave Out Mix" in dev["name"]
        ) and dev["max_input_channels"] > 0:
            device_index = i
            print(f"[+] Usando dispositivo de captura: {dev['name']}")
            break

    if device_index is None:
        print(
            "[!] No se detectó 'Mezcla estéreo'. Se usará el dispositivo de entrada por defecto."
        )
        device_index = sd.default.device[0]

    try:
        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            callback=callback,
            device=device_index,
        ):
            while not stop_event.is_set():
                time.sleep(0.1)

    except Exception as e:
        print(f"[-] Error al acceder al dispositivo de audio: {e}")
        return False

    if q.empty():
        print("[-] No se captó audio durante la sesión.")
        return False

    print("[~] Guardando audio capturado...")
    with wave.open(FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        while not q.empty():
            data = q.get()
            wf.writeframes((data * 32767).astype(np.int16).tobytes())
    return True


def process_audio_and_analyze():
    recognizer = sr.Recognizer()

    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) < 44:
        print("[-] El archivo de audio está vacío o corrupto.")
        return

    with sr.AudioFile(FILENAME) as source:
        print("[~] Analizando audio...\n")
        audio_data = recognizer.record(source)

    try:
        print("[~] Transcribiendo audio en inglés...")
        text_en = recognizer.recognize_google(audio_data, language="en-US")

        print("\n" + "=" * 50)
        print("[!] ANÁLISIS DEL EXAMEN")
        print("=" * 50)
        print(f"Texto Detectado (EN):\n{text_en}\n")
        print("Prompt Sugerido para tu IA:")
        print(
            f"\"Traduce esta instrucción de examen al español e indícame qué debo hacer textualmente basándote en este texto: '{text_en}'\""
        )
        print("=" * 50)

    except sr.UnknownValueError:
        print(
            "[-] No se detectó voz clara. Asegúrate de reproducir el audio del examen mientras corre el script."
        )
    except sr.RequestError as e:
        print(f"[-] Error de red con el servidor de transcripción: {e}")
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)


def main_loop():
    print("\n=== MODO CONTINUO ===")
    print("Presiona ENTER para iniciar la grabación, ENTER para detenerla y Ctrl+C para salir.")

    while True:
        try:
            input("\nPresiona ENTER para comenzar...")
            if record_audio_until_stop():
                process_audio_and_analyze()
            else:
                print("[-] Grabación fallida o sin audio. Intenta de nuevo.")
        except KeyboardInterrupt:
            print("\n[!] Salida solicitada. Cerrando programa...")
            break


if __name__ == "__main__":
    main_loop()