# Bing Rewards Bot

Este projeto automatiza a realização de pesquisas no Bing para acumular pontos no programa Microsoft Rewards. Ele foi desenvolvido usando Python e a biblioteca Selenium para interagir com o navegador Chrome.

## 🌟 Funcionalidades
- Realiza automaticamente pesquisas no Bing para acumular pontos no Microsoft Rewards.
- Usa uma lista fixa de termos de pesquisa para evitar repetições.
- Salva o progresso em um arquivo (progress.txt) para permitir retomadas.
- Carrega um perfil específico do Chrome para manter a sessão logada no Microsoft Rewards.
- Permite configurar o número de pesquisas a serem realizadas.

## ⚙️ Requisitos
Para executar este projeto, você precisará dos seguintes itens instalados:

1. **Python 3.x**: [Download Python]
2. **Bibliotecas Python**:
- `selenium`
- `webdriver-manager`
3 **.Navegador Google Chrome**: [Download Chrome]
4. **Git** (opcional, para clonar o repositório): [Download Git]

## 🚀 Instalação
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. **Crie e ative o ambiente virtual**:
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows

3. **Instale as dependências**:
   pip install -r requirements.txt

4. **Configure o perfil do Chrome**:
Certifique-se de que o perfil correto do Chrome está configurado

5. **Atualize o caminho do diretório do perfil no código**

python bing_rewards_bot.py

## 🔧 Configuração Adicional
1. Configurar o Número de Pesquisas
Ao executar o script, ele solicitará o número de pesquisas que você deseja realizar. Insira o valor desejado.
2. Verificar o Progresso
O script salva o progresso em progress.txt. Se você interromper a execução, ele continuará de onde parou na próxima vez.
3. Adicionar ou Modificar Termos de Pesquisa
A lista de termos de pesquisa está definida na variável SEARCH_TERMS no arquivo bing_rewards_bot.py. Você pode adicionar ou modificar os termos conforme necessário.

## 🛠️ Observações Importantes
- **Perfil do Chrome** : O script carrega um perfil específico do Chrome (Profile 7). Certifique-se de que o perfil usado já esteja logado no Microsoft Rewards.
- **Chrome Aberto** : Feche todas as instâncias do Chrome antes de executar o script para evitar conflitos.
- **Limitações** :
O script foi projetado especificamente para o Bing e o Microsoft Rewards. Se o site for alterado, o código pode precisar de ajustes.
Use o script de forma responsável e dentro dos termos de serviço do Microsoft Rewards.

## 👤 Autor
Desenvolvido por [Patrick-Jabba](https://github.com/Patrick-Jabba) .

## 🛡️ Licença
Este projeto está licenciado sob a [MIT License](LICENSE).