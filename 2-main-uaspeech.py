

import pandas as pd
import os
df =pd.read_csv("./UASpeech/output.csv")

speakers = ['F02', 'F04','M05','M07']
Methods = [ 'Original','Reference', 'ASR-TTS', 'E2E-DSR','ASA-DSR',"Unit-DSR","Diff-VC","T-SAM","Text"]

final_list = []
for speaker in speakers:
    a = df["speaker"]
    filtered_df = df[df["speaker"] == speaker]
    speaker_list = []
    for Method in Methods:
        wav_list = []
        wav_list.append(Method)
        if Method == "Text":
            for index, row in filtered_df.iterrows():
                    wav_list.append(row['text'])
        else:
            for index, row in filtered_df.iterrows():
                method = row['path'].split("/")[-3]
                if Method == method:
                    wav_list.append(row['path'])
        speaker_list.append(wav_list)
    final_list.append(speaker_list)


print(final_list)
