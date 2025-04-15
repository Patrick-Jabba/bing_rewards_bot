import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Lista de termos de pesquisa
SEARCH_TERMS = [
    "maior roedor do mundo", "quantas cores tem no arco-íris", "melhor filme de 2023",
    "quem descobriu o Brasil", "receita de bolo de chocolate", "melhores praias do Brasil",
    "como funciona IA", "curiosidades sobre gatos", "benefícios do café", "história da internet",
    "como aprender inglês rápido", "capivara", "raças de cachorro mais inteligentes",
    "como fazer slime", "melhores livros de ficção científica", "quais são os planetas do sistema solar",
    "como economizar dinheiro", "dicas para trabalhar em casa", "melhores séries de TV",
    "como cuidar de orquídeas", "quais são as maravilhas do mundo antigo", "como montar um currículo",
    "melhores jogos de videogame", "como fazer hambúrguer caseiro", "quais são os países mais populosos",
    "como treinar para uma maratona", "curiosidades sobre tubarões", "como organizar uma festa",
    "melhores aplicativos de produtividade", "como investir na bolsa de valores", "quais são as sete maravilhas do mundo moderno",
    "como fazer pão caseiro", "melhores destinos turísticos", "como meditar", "curiosidades sobre o espaço",
    "como limpar o computador", "quais são os animais mais raros", "como fazer uma boa apresentação",
    "melhores podcasts de tecnologia", "como cuidar de peixes", "como fazer brigadeiro gourmet",
    "raças de gato mais amigáveis", "quais são os maiores oceanos", "melhores filmes de super-heróis",
    "como fazer pizza caseira", "benefícios do chá verde", "como estudar para concursos",
    "melhores cursos online gratuitos", "como limpar o celular", "curiosidades sobre dinossauros",
    "quais são os maiores lagos do mundo", "como fazer sabonete artesanal", "melhores músicas de rock",
    "como fazer vela artesanal", "benefícios do suco de limão", "como aprender a tocar violão",
    "melhores apps para meditação", "como fazer geleia caseira", "quais são os animais mais velozes",
    "como fazer cerveja artesanal", "curiosidades sobre vulcões", "melhores livros de autoajuda",
    "como fazer horta em casa", "quais são os maiores rios do mundo", "como fazer perfume caseiro",
    "melhores práticas para home office", "como fazer iogurte caseiro", "curiosidades sobre o cérebro humano",
    "quais são os maiores desertos do mundo", "como fazer shampoo caseiro", "melhores filmes de terror",
    "como fazer sabão líquido", "benefícios do ômega 3", "como organizar o guarda-roupa",
    "melhores documentários da Netflix", "como fazer velas aromáticas", "curiosidades sobre o universo",
    "quais são os maiores edifícios do mundo", "como fazer pasta de dente caseira", "melhores canais do YouTube",
    "como fazer hidratante caseiro", "benefícios do óleo de coco", "como aprender a desenhar",
    "melhores museus do mundo", "como fazer sabão líquido", "curiosidades sobre o corpo humano",
    "quais são os maiores aviões do mundo", "como fazer detergente caseiro", "melhores restaurantes do Brasil",
    "como fazer colônia caseira", "benefícios do gengibre", "como organizar o escritório",
    "melhores filmes de animação", "como fazer mousse de maracujá", "curiosidades sobre o Titanic",
    "quais são os maiores barcos do mundo", "como fazer geleia de morango", "melhores parques nacionais",
    "como fazer sabão em barra", "benefícios do chá de camomila", "como aprender a cozinhar",
    "melhores séries de ficção científica", "como fazer vinagre caseiro", "curiosidades sobre o espaço sideral",
    "quais são os maiores telescópios do mundo", "como fazer creme hidratante", "melhores livros de mistério",
    "como fazer tempero caseiro", "benefícios do mel", "como organizar a cozinha",
    "melhores filmes de comédia", "como fazer sabão esfoliante", "curiosidades sobre o sistema solar",
    "quais são os maiores navios do mundo", "como fazer geleia de uva", "melhores praias do mundo",
    "como fazer sabão líquido para roupa", "benefícios do chá de hibisco", "como aprender a fotografar",
    "melhores aplicativos para academia", "como fazer sabonete natural", "curiosidades sobre animais aquáticos",
    "quais são os maiores aviões militares", "como fazer desinfetante caseiro", "melhores filmes de drama",
    "como fazer suco detox", "melhores exercícios para perder peso", "como melhorar a memória",
    "como parar de roer unhas", "quais são os alimentos ricos em ferro", "como fazer panqueca americana",
    "como aprender matemática rápido", "curiosidades sobre lobos", "como plantar suculentas",
    "como cuidar de um hamster", "melhores filmes baseados em fatos reais", "como fazer brownie caseiro",
    "como treinar um cachorro filhote", "como fazer um currículo para primeiro emprego",
    "como economizar energia elétrica", "como fazer arroz soltinho", "como limpar vidros sem deixar manchas",
    "como acabar com mofo em casa", "como melhorar a postura", "melhores aplicativos para edição de fotos",
    "como se tornar um freelancer", "como ganhar dinheiro online", "como fazer um bolo de cenoura fofinho",
    "como aprender francês sozinho", "como aprender a tocar teclado", "quais são os maiores países do mundo",
    "como aliviar o estresse", "curiosidades sobre o Egito Antigo", "como montar uma horta vertical",
    "como fazer um currículo para estágio", "como aliviar dor nas costas", "como organizar a rotina de estudos",
    "como fazer pipoca caramelizada", "quais são os sintomas de estresse", "como fazer ioga em casa",
    "como plantar tomate em vasos", "como eliminar formigas da cozinha", "melhores filmes de romance",
    "como fazer bolo de laranja simples", "como organizar documentos em casa",
    "como fazer máscara facial caseira", "como treinar um gato para usar a caixa de areia",
    "como fazer um chá relaxante", "melhores séries para maratonar", "como dormir melhor à noite",
    "como fazer pão de queijo caseiro", "como limpar manchas de roupas brancas",
    "como aprender espanhol rapidamente", "quais são as profissões do futuro",
    "como montar um home office eficiente", "como melhorar a concentração nos estudos",
    "como fazer panetone caseiro", "como criar um hábito saudável", "como acabar com a insônia naturalmente",
    "quais são as frutas mais saudáveis", "como fazer cookies crocantes", "como aprender a desenhar rostos",
    "como se tornar um programador", "como fazer maquiagem básica para o dia a dia",
    "como cuidar da pele oleosa", "como evitar o desperdício de alimentos", "como fazer cappuccino caseiro",
    "como criar um canal no YouTube de sucesso", "como eliminar dores musculares",
    "como fazer uma apresentação profissional", "como melhorar a respiração durante o exercício",
    "como fazer sushi em casa", "como limpar prata escurecida", "como aumentar a produtividade no trabalho",
    "como se tornar um escritor", "como fazer uma sobremesa rápida", "como se organizar financeiramente",
    "como fazer exercícios sem equipamentos", "como preparar um café da manhã saudável",
    "como se livrar da ansiedade", "como criar senhas seguras", "como fazer sorvete caseiro",
    "como lidar com a procrastinação", "como limpar o forno corretamente", "como fazer crepioca",
    "como entender a linguagem corporal", "como fazer massa de pizza caseira",
    "como montar um jardim em apartamento", "como fazer uma festa infantil econômica",
    "qual a capital da Austrália",
    "previsão do tempo para amanhã",
    "cotação do dólar hoje",
    "como fazer arroz doce",
    "melhores filmes de terror psicológico",
    "o que é metaverso",
    "como declarar imposto de renda",
    "receita de lasanha",
    "melhores celulares de 2024",
    "o que é blockchain",
    "como fazer um currículo criativo",
    "melhores restaurantes italianos",
    "o que é inteligência artificial generativa",
    "como plantar manjericão",
    "melhores destinos para lua de mel",
    "o que é NFT",
    "como fazer um plano de negócios",
    "melhores museus em São Paulo",
    "o que é computação quântica",
    "como cuidar de suculentas no inverno",
    "melhores praias do Nordeste",
    "o que é realidade aumentada",
    "como escrever um bom e-mail",
    "melhores parques em Nova York",
    "o que é deep learning",
    "como fazer um terrário",
    "melhores trilhas de trekking no Brasil",
    "o que é machine learning",
    "como fazer um orçamento familiar",
    "melhores bares em Berlim",
    "o que é internet das coisas (IoT)",
    "como cuidar de cabelos cacheados",
    "melhores lugares para esquiar na América do Sul",
    "o que é 5G",
    "como fazer um roteiro de viagem",
    "melhores cafés em Paris",
    "o que é energia solar",
    "como adestrar um gato",
    "melhores musicais da Broadway",
    "o que é biotecnologia",
    "como fazer um podcast",
    "melhores ilhas gregas",
    "o que é impressão 3D",
    "como reformar um banheiro",
    "melhores cidades para mochilar na Ásia",
    "o que é agricultura orgânica",
    "como fazer um site simples",
    "melhores festivais de música no mundo",
    "o que é upcycling",
    "como pintar uma parede",
    "melhores mercados de rua em Londres",
    "o que é economia circular",
    "como escolher um bom vinho",
    "melhores rotas de carro na Europa",
    "o que é design thinking",
    "como fazer kombucha",
    "melhores lugares para observar estrelas no Chile",
    "o que é storytelling",
    "como cultivar cogumelos em casa",
    "melhores cachoeiras perto de São Paulo",
    "o que é mindfulness",
    "como fazer um bom pitch",
    "melhores baladas em Ibiza",
    "o que é branding pessoal",
    "como fazer queijo vegano",
    "melhores lugares para mergulhar na Austrália",
    "o que é marketing digital",
    "como restaurar móveis antigos",
    "melhores feiras de artesanato no Brasil",
    "o que é desenvolvimento sustentável",
    "como fazer sabão ecológico",
    "melhores trilhas de bicicleta no Rio de Janeiro",
    "o que é inteligência emocional",
    "como fazer um plano de carreira",
    "melhores livrarias em Buenos Aires",
    "o que é agilidade (metodologia)",
    "como fazer um jardim vertical pequeno",
    "melhores praias desertas no Brasil",
    "o que é pensamento crítico",
    "como fazer um vídeo tutorial",
    "melhores parques nacionais nos Estados Unidos",
    "o que é resiliência",
    "como fazer um terrário fechado",
    "melhores museus de arte moderna na Europa",
    "o que é empatia",
    "como fazer um herbário",
    "melhores lugares para surfar no Brasil"
]


# Arquivo para salvar o progresso
PROGRESS_FILE = "progress.txt"

def load_progress():
    """Carrega o progresso salvo."""
    try:
        with open(PROGRESS_FILE, "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0

def save_progress(progress):
    """Salva o progresso atual."""
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(progress))

def perform_searches(num_searches):
    """Realiza pesquisas no Google Chrome."""
    # Carrega o progresso anterior
    start_index = load_progress()

    # Configuração do WebDriver para Chrome com perfil existente
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=C:\\Users\\Patrick\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument("--profile-directory=Profile 7")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.com")

    try:
        # Abre a página do Microsoft Rewards
        driver.get("https://rewards.bing.com/status/pointsbreakdown")
        time.sleep(5)  # Tempo para carregar a página

        # Acessa a página de pesquisa (PC Search)
        search_url = "https://www.bing.com/news/?form=ml11z9&crea=ml11z9&wt.mc_id=ml11z9&rnoreward=1&rnoreward=1"
        driver.get(search_url)
        time.sleep(3)  # Tempo para carregar a página

        for i in range(start_index, start_index + num_searches):
            if i >= len(SEARCH_TERMS):
                print("Todas as pesquisas disponíveis foram concluídas.")
                break

            search_term = SEARCH_TERMS[i]
            print(f"Realizando pesquisa {i + 1}: {search_term}")
            
            # Insere o termo de pesquisa na barra de busca
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(search_term)
            search_box.send_keys(Keys.RETURN)
            
            time.sleep(random.uniform(2, 5))  # Pausa entre pesquisas
            
            # Volta para a página inicial do Bing News
            driver.get(search_url)
            time.sleep(random.uniform(2, 5))  # Pausa antes da próxima pesquisa

            # Salva o progresso
            save_progress(i + 1)

        print("Todas as pesquisas foram concluídas!")

    finally:
        # Fecha o navegador ao final
        driver.quit()

if __name__ == "__main__":
    # Solicita ao usuário o número de pesquisas
    num_searches = int(input("Quantas pesquisas você deseja realizar? "))
    
    # Executa as pesquisas
    perform_searches(num_searches)