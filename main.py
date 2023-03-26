import time
import subprocess
from playsound import playsound


'''
        Atenção, esse pomodoro é com base nos meus parâmetros, então nele você tem incluso,
    sistema de seleção de recompensa, mostra qual recompensa ele deve lhe oferecer, sistema 
    de bloqueio de site, durante o tempo que você estiver usando ele, ele faz o bloqueio de
    site, não pare o software me hipotese alguma, assim você tera os sites bloqueados para 
    sempre, caso não saiba resolver.
'''
print("Bem-vindo ao programa de pomodoro!")

print("Vamos testar o audio, por favor, coloque bem baixo o seu audio e verifique depois da mensagem \"Testando o audio\" se está saindo corretamente!")

time.sleep(10)

print("Testando o audio!")

time.sleep(2)

for i in range(4):
        for y in range(2):
            playsound("beep.mp3")
        time.sleep(2)

study_time = int(input("Insira o tempo de estudo: ")) # Tempo de estudo em minutos

break_time = int(input("Insira o tempo de descanso: ")) # Tempo de descanso em minutos

pomo = int(input("Insira a quantidade de pomodoros que você quer: ")) # Quantidade de pomodoros

rewards = ["Descansar na cama por 5 minutos", "Mexer no cubo mágico por 5 minutos"] # Lista de recompensas possíveis

# Inicie o ciclo de estudo e descanso
for i in range(1,pomo):
    print("{}º pomodoro!".format(i))
    print("Comece a estudar!")

    # Inicie o cronômetro
    start_time = time.time()

    # Cria a variável minuto e tempo
    minutos = 0
    segundos = 0
    # Execute o loop enquanto o tempo de estudo não for alcançado
    while time.time() < start_time + study_time * 60:
        if(segundos == 60):
            segundos = 0
            minutos += 1
        print("Tempo: {:02}:{:02}".format(minutos,segundos),end='\r')
        segundos += 1
        # Continuar estudando
        time.sleep(1)
        
    # Tocar um beep por três vezes
    for i in range(2):
        for y in range(2):
            playsound("beep.mp3")
        time.sleep(2)

    # Mostre uma recompensa aleatória quando o tempo de estudo for alcançado
    import random
    print("Parabéns por terminar o seu tempo de estudo! Como recompensa, você pode desfrutar de:", random.choice(rewards))

    # Inicie o período de descanso
    print("Agora é hora de um descanso de", break_time, "minutos!")

    # Inicie o cronômetro
    start_time = time.time()

    # Cria a variável minuto e tempo
    minutos = 0
    segundos = 0
    # Execute o loop enquanto o tempo de descanso não for alcançado
    while time.time() < start_time + break_time * 60:
        if(segundos == 60):
            segundos = 0
            minutos += 1
        print("Tempo: {:02}:{:02}".format(minutos,segundos),end='\r')
        segundos += 1
        # Continuar descansando
        time.sleep(1)
    for i in range(2):
        for y in range(2):
            playsound("beep.mp3")
        time.sleep(2)
