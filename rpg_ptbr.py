import random
"""
Jogo de Aventura Baseado em Texto
=================================

Este é um simples jogo de aventura estilo RPG baseado em texto onde o jogador assume o papel de um aventureiro errante.
O jogo é construído em torno de encontros aleatórios, tomada de decisões e um sistema de combate básico.

Características do Jogo:
------------------------
- Seleção de Gênero: Os jogadores escolhem seu gênero, o que determina o uso de pronomes ao longo da história.
- Escolha de Arma: Os jogadores escolhem entre uma Espada de Ferro ou uma Adaga de Prata no início do jogo.
- Encontros com Inimigos: Em cada rodada, o jogador encontra uma criatura selecionada aleatoriamente com uma emoção e nível atribuídos aleatoriamente.
- Sistema de Níveis: Os inimigos têm níveis variando de 1 a 5, influenciando a dificuldade da luta.
- Sistema de Combate: Os jogadores escolhem entre diferentes estratégias de combate e devem adivinhar um número nos bastidores para ter sucesso.
    - Lutas bem-sucedidas recompensam o jogador com uma vida extra.
    - Lutas fracassadas resultam em perda de vida.
- Mecânica de Fuga: Os jogadores podem fugir do combate, mas apenas até 3 vezes. Após a terceira tentativa, a fuga se torna impossível.
- Sistema de Vidas: O jogador começa com 3 vidas. Ganhar ou perder vidas depende do resultado de cada batalha.
- Feedback Narrativo: Cada ação é narrada com descrições de cenários selecionadas aleatoriamente para imersão.
- Fim de Jogo: O jogo termina quando o jogador atinge 20 rodadas, perde todas as vidas ou obtém 10 x❤️.

É um experimento leve em ficção interativa, inspirado em temas clássicos de RPG, mas mantido intencionalmente simples.
"""
bugs = [""]
space = "\n"*40
error_msg = "Erro! Opção Inválida! >:("
user_name = input("Olá, Aventureiro! Como você será chamado?\n").capitalize()
suggestions = [
    "Melhorar a estética (cores, animações com time.sleep, etc).",
    "Adicionar música de fundo usando playsound.",
    "Introduzir inimigos raros, chefes ou efeitos de habilidade.",
    "Dano de ataque multiplicado de acordo com a arma selecionada"
]
line = "=_=_=_=_=_=_=_=_=_=_=_=_=_="

if user_name in ["dev", "DEV", "Dev", "Raphael"]:
    print(f"{line}\n-=-MODO DESENVOLVEDOR-=-\n-MODO DEUS ATIVADO-\nSugestões de Melhoria:\n" +"\n".join(suggestions))
print(f"{line}")

while True:
    user_gender = input("Você é Ela ou Ele?\n1-Ela\n2-Ele\n")  # Define o gênero do jogador
    print(f"{line}")

    if user_gender == "1":
        user_gender = "ela"
        user_pos = "sua"
        user_pos2 = "ela"
        break
    elif user_gender == "2":
        user_gender = "ele"
        user_pos = "seu"
        user_pos2 = "ele"
        break
    else:
        print(f"{error_msg}")
        print(f"{line}")

small_entity = [
    "Rato", "Cão", "Mosquito", "Gremlin",
    "Ghoul", "Vampiro", "Lobisomem", "Mutante",
    "Revenant", "Demônio", "Homem-Lagarto",
    "Hiena", "Lobo", "Javali"
]

emotion_list = ["furioso", "gargarejando", "raivoso", "morto-vivo"]
level_list = [1, 2, 3, 4, 5]

while True:
    weapon_choice = input("Qual é a sua arma de escolha?\n1-Uma Espada de Ferro\n2-Uma Adaga de Prata\n")
    print(f"{line}")
    if weapon_choice == "1":
        weapon_choice = "Espada de Ferro"
        break
    elif weapon_choice == "2":
        weapon_choice = "Adaga de Prata"
        break
    else:
        print(f"{error_msg}")
        print(f"{line}")

fight_options = f"O que {user_name} deve fazer?\n1-Lutar\n2-Fugir\n"


enter_sm = f"Pressione ENTER para continuar...\n{line}\n"

def fight_sys(entity, life, emotion, level):
    #: Handles combat mechanics, determining win or loss scenarios.
    while True:
        fight_choice = input(
            "Hora de lutar! Escolha seu próximo movimento para prosseguir.\n1-Golpe de precisão\n2-Esquivar e contra-atacar\n3-Ataque de força bruta\n")
        print(f"{line}")

        if level < 3:
            fight_numbers = ["1", "2", "3"]
        elif level == 3:
            fight_numbers = ["1", "2", "3", "4"]
        elif level == 4:
            fight_numbers = ["1", "2", "3", "4", "5"]
        else:
            fight_numbers = ["1", "2", "3", "4", "5", "6"]

        fight_number = random.choice(fight_numbers)

        win_scenarios = [
            f"{user_name} franze a testa e balança {user_pos} {weapon_choice} em direção ao {emotion} {entity}, derrubando-o.",
            f"{user_name} domina o {entity} com um golpe limpo, fazendo-o fugir.",
            f"{user_name} esquiva rapidamente e contra-ataca, derrubando o {emotion} {entity}.",
            f"{user_name} encara o {emotion} {entity}, segurando {user_pos} {weapon_choice} firmemente.\nCom um golpe rápido e poderoso, {user_gender} corta o ar, a força do ataque levantando poeira.\nO {entity} hesita, sentindo que não é páreo para {user_name}.\nCom um último rosnado desafiador, a criatura foge, escolhendo viver mais um dia. {user_name} observa enquanto ela vai, vitorioso mas sempre cauteloso.",
            f"O {emotion} {entity} rosna e se prepara para atacar, mas {user_name} não perde tempo.\nCom uma explosão de velocidade, {user_name} balança {user_pos} {weapon_choice} com toda a força, acertando a criatura bem no peito.\nO impacto faz o {entity} rolar para trás, atordoado e choramingando.\nEle se levanta e foge para a escuridão, derrotado. {user_name} limpa {user_pos} arma e continua a jornada, inabalado."
        ]

        lose_scenarios = [
            f"{user_name} balança mas o {emotion} {entity} esquiva e morde de volta, forçando uma retirada.",
            f"{user_name} calcula mal um ataque e o {entity} retaliou ferozmente, tornando a fuga a única opção.",
            f"{user_name} é dominado e derrubado, mal conseguindo fugir.",
            f"{user_name} segura {user_pos} {weapon_choice} firmemente e ataca o {emotion} {entity}. Mas a criatura é implacável, esquivando-se de cada ataque com facilidade.\nApós uma luta feroz, {user_name} está exausto.\n{user_pos.capitalize()} pernas estão fracas, e {user_pos} visão fica embaçada. A única escolha é fugir antes que seja tarde demais.",
            f"{user_name} corta o {emotion} {entity}, mas o golpe mal o atinge. A criatura retaliou com um golpe violento, derrubando {user_name} no chão.\nEnquanto {user_pos} arma escapa de {user_pos} mãos, o pânico toma conta.\nNão há escolha a não ser se levantar e escapar antes que seja tarde demais."
        ]

        if fight_choice in fight_numbers:
            if level == 1 or fight_choice == fight_number or user_name in ["Raphael", "dev", "DEV", "Dev"]:
                life += 1
                print(random.choice(win_scenarios))
                print(f"{line}\n{user_name} GANHOU 1 x❤️ e agora tem {life} x❤️.")
                print(f"{line}")
                input(f"{enter_sm}")
            else:
                print(random.choice(lose_scenarios))
                life -= 1
                print(f"{line}\n{user_name} PERDEU 1 x❤️ e agora tem {life} x❤️.")
                print(f"{line}")
                input(f"{enter_sm}")
            return life
        else:
            print(f"{error_msg}")


def run_away_sys(entity, emotion, life):
    #: Manages the scenario where the player runs away from an enemy.
    run_scenarios = [
    f"{user_name} vira-se e corre o mais rápido que {user_pos} pernas conseguem carregar {user_pos2}, deixando o {emotion} {entity} para trás.",
    f"{user_name} mal esquiva das garras do {emotion} {entity} e corre, coração acelerado.",
    f"{user_name} joga terra nos olhos do {entity}, usando a distração para escapar rapidamente.",
    f"Quando o {entity} avança, {user_name} pula para o lado e corre para a floresta.",
    f"O {emotion} {entity} rosna, mas {user_name} desaparece atrás das ruínas antes que ele possa reagir.",
    f"{user_name} tropeça mas rapidamente se levanta, escapando por pouco do alcance do {entity}.",
    f"O {entity} solta um rugido ensurdecedor, mas {user_name} já está longe, correndo por sua vida.",
    f"Sem pensar duas vezes, {user_name} dispara, ouvindo o {entity} quebrando o mato atrás.",
    f"{user_name} pula sobre uma árvore caída e corre pela névoa, escapando do {emotion} {entity}.",
    f"O {entity} avança, mas {user_name} mergulha em um rio, deixando a correnteza levar {user_pos2} para a segurança.",
    f"{user_name} chuta uma caixa de madeira em direção ao {emotion} {entity}, criando um atraso suficiente para fugir.",
    f"Com uma explosão de adrenalina, {user_name} escala uma borda rochosa, deixando o {entity} rosnando abaixo.",
    f"{user_name} não vê outra opção e corre para uma caverna próxima, esperando que o {entity} não siga.",
    f"O {emotion} {entity} uiva, mas {user_name} já está desaparecendo no horizonte, recusando-se a olhar para trás."
    ]

    print(random.choice(run_scenarios))
    print(f"Você fugiu com segurança. Suas vidas permanecem as mesmas: {life} x❤️")
    print(f"{line}")
    input(f"{enter_sm}")

def game():
    #: Main function controlling the game loop, enemy encounters, and player choices.
    rounds = 0
    run_attempts = 0
    life = 3

    while rounds < 20 and life > 0:
        rounds += 1
        entity = random.choice(small_entity)
        emotion = random.choice(emotion_list)
        level = random.choice(level_list)
        print(f"{space}{line}\n {user_name} está caminhando pela estrada quando de repente um {emotion} {entity} de nível {level} aparece! \n{line}\nNº de ❤️:{life}\n{line}\n")

        while True:
            choice1 = input(fight_options)
            print(f"{line}")

            if choice1 == "1":
                life = fight_sys(entity, life, emotion, level)
                break
            elif choice1 == "2":
                run_attempts += 1
                if run_attempts >= 4:
                    print("Você machucou os pés e não pode mais correr.")
                    life = fight_sys(entity, life, emotion, level)
                    break
                run_away_sys(entity, emotion, life)
                break
            else:
                print(f"{error_msg}")
                print(f"{line}")

        print(f"Rodadas Jogadas: {rounds}")
        print(f"{line}")
        if life == 0:
            print(f"Você foi derrotado pelo {entity} de nível {level}...\n{line}\n OBRIGADO POR JOGAR! :)")
            input(f"{enter_sm}")
            break
        elif rounds == 20 and life > 0:
            print(f"PARABÉNS!!! VOCÊ VENCEU!!!\n Nº de vidas ❤️:{life}\nOBRIGADO POR JOGAR! :)")
            input(f"{enter_sm}")
            break
        elif life >= 10:
            print(f"PARABÉNS!!! VOCÊ VENCEU!!!\n Nº de vidas ❤️:{life}\nOBRIGADO POR JOGAR! :)")
            input(f"{enter_sm}")
            break



game()
