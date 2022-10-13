print("Testando...ANNEX \n")

import speech_recognition as sr
import os
import psutil
from datetime import datetime


def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 
battery = psutil.sensors_battery() 


#Funcao para ouvir e rwconhecer a fala
def ouvir_microfone():
    microfone = sr.Recognizer() #habilita o microfone do usuario

    with sr.Microphone() as source:

        #chama um algoritmo de reducao de ruidos de som
        microfone.adjust_for_ambient_noise(source)
        
        #frase para o usuario dizer algo
        print("Diga alguma coisa.\n ")

        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        #Passa a variavel para o algoritmo reconhecer de padroes
        frase = microfone.recognize_google(audio, language ='pt-BR')

        #retorna a frase pronunciada
        print("Você disse:" + frase)

        if "bateria" in frase: #Verificações da carga de bateria
            print("Porcentagem de Bateria : ", battery.percent) 
            print("Conectado ao carregador : ", battery.power_plugged) 
            print("Tempo de carga(horas) : ", convertTime(battery.secsleft)) 

        elif "navegador" in frase:
                os.system("start chrome.exe")
        elif "Excel" in frase:
                os.system("start Excel.exe")
        elif "Bateria" in frase:
                os.system ()

    except sr.UnkownValueError: #Se nao reconhecer o padrao de fala, exibixa a mensagem
       print("Não entendi")
 
 

    return frase
ouvir_microfone()      

