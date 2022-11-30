def sound_process(path_file: str,
                  *,
                  # Использовал сторого ключевые параметры, т.к. все следующие аргументы являются цифровыми и однотипными
                  audio_format: int | str,
                  channels: int | str,
                  sampling: int | str,
                  bit_depth: int | str) -> str:
    """Проверяет корректность переданных аргументов и выводит результат проверки"""
    
    sampl_corr = (8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000)
    bit_depth_corr = (8, 16, 24, 32)
    
    res = ''
    res += f"{path_file = } {['INCORRECT','CORRECTLY'][path_file.endswith('.wav')]}\n"
    res += f"{audio_format = } {['INCORRECT','CORRECTLY'][1 <= int(audio_format) <= 999]}\n"
    res += f"{channels = } {['INCORRECT','CORRECTLY'][1 <= int(channels) <= 10]}\n"
    res += f"{sampling = } {['INCORRECT','CORRECTLY'][int(sampling) in sampl_corr]}\n"
    res += f"{bit_depth = } {['INCORRECT','CORRECTLY'][int(bit_depth) in bit_depth_corr]}"
    
    return res
 
#stdin 
print(sound_process("/Homeworks/Miftakhov/07.10/sound.wav", audio_format=378, channels='9', sampling=192000, bit_depth=16))

#stdout
# path_file = '/Homeworks/Miftakhov/07.10/sound.wav' CORRECTLY
# audio_format = 378 CORRECTLY
# channels = '9' CORRECTLY
# sampling = 192000 CORRECTLY
# bit_depth = 16 CORRECTLY

#stdin
print(sound_process("/Homeworks/Miftakhov/07.10/sound.mp3", audio_format='1001', channels=15, sampling='10000', bit_depth='25'))

#stdout
# path_file = '/Homeworks/Miftakhov/07.10/sound.mp3' INCORRECT
# audio_format = '1001' INCORRECT
# channels = 15 INCORRECT
# sampling = '10000' INCORRECT
# bit_depth = '25' INCORRECT