# 📊 Algoritmos de Ordenação

Algoritmo de ordenação é um algoritmo, de manipulação de dados, que coloca os elementos de uma dada sequência em uma certa ordem, em outras palavras, efetua sua ordenação completa ou parcial. Nosso Projeto apresenta uma aplicação em python completa para a visualização interativa de algoritmos de ordenação utilizando também um gráfico.. 

# ⚙️ 1. `EstruturadeOrdenacao.py` (Visualizador de Ordenação Interativo):

O script também contém a lógica principal da aplicação GUI construída usando Tkinter.

Obs1: Aplicação GUI é um programa de computador que permite a comunicação com um computador por meio de símbolos, metáforas visuais e dispositivos apontadores.

Obs2: Tkinter é uma biblioteca da linguagem Python que acompanha a instalação padrão e permite desenvolver interfaces gráficas.

**1-Estruturas de Dados Iniciais:**

* `EXPLANATIONS`: É um dicionário que armazena os textos explicativos detalhados para cada algoritmo de ordenação.
  
*   `BAR_COLOR`, `COMPARE_COLOR`, `SWAP_COLOR`, `SORTED_COLOR`: São constantes de cores para a representação visual das barras durante a ordenação.
    
*   `STUDENT_INFO`: String multilinha contendo os créditos dos alunos responsáveis pelo projeto.
  
  **2-Classe Principal `SortingVisualizerApp`:**
  * `__init__(self, master)` (Construtor e Configuração da UI):
    
  * Inicializa a janela principal (`master`) com título, geometria e cor de fundo.
        
  *   Define variáveis de estado da aplicação (`algorithm_name`, `data`, `data_size`, `animation_speed`, `generator`, `is_sorting`, `is_paused`).
            
  *   Configura estilos `ttk` para uma aparência melhorada dos widgets.
        
  **3-Barra de Menu:**
        
  * Cria uma barra de menu com "Arquivo" (opção "Sair") e "Ajuda"
                
 **4-Frame de Controles (`controls_frame`):**
        
  *   Contém widgets para interação do usuário:
            
 *   `ttk.Combobox` (`algo_menu`): Para selecionar o algoritmo de ordenação.
                    Vinculado a `update_explanation_display`.
                    
*   `ttk.Scale` (`size_scale`): Para ajustar o tamanho da lista de dados.
                    Vinculado a `generate_data`.
                    
  *   `ttk.Scale` (`speed_scale`): Para controlar a velocidade da animação.
                
*    `ttk.Button` (`generate_button`): Para gerar uma nova lista aleatória.
                
  *   `ttk.Button` (`start_button`): Para iniciar o processo de ordenação.
                
*    `ttk.Button` (`pause_button`): Para pausar/continuar a animação.
                
  *   `ttk.Button` (`reset_button`): Para interromper a ordenação e resetar.
                
  **5-Frame de Exibição Principal (`main_display_frame`):**
        
  * `tk.Canvas` (`canvas`): Área onde as barras representando os dados são desenhadas e animadas.
            
*  Frame de Explicação (`explanation_frame`):
            
*   `ttk.Label` (`explanation_title`): Título do algoritmo selecionado.
                
*  `tk.Text` (`explanation_text_widget`): Exibe o texto explicativo do algoritmo (conteúdo de `EXPLANATIONS`).
                
  **6-Barra de Status (`status_bar`):**
        
*    `ttk.Label` no rodapé para exibir mensagens de status e contagem de comparações/trocas.
            
*   Inicializa a contagem de `comparisons` e `swaps`.
        
*   Chama `generate_data()` e `update_explanation_display()` na inicialização.
        
*   Configura o protocolo `WM_DELETE_WINDOW` para chamar `confirm_exit`.

  **7-Métodos de Interface e Lógica:**
        *  `show_about_dialog()`: Cria e exibe uma janela `Toplevel` modal com as informações dos alunos (`STUDENT_INFO`).
        
  *   `update_status(message)`: Atualiza o texto da barra de status.
        
  *   `update_explanation_display(event=None)`: Atualiza o painel de explicação com base no algoritmo selecionado.
        
  *   `generate_data(reset_algo=True)`: Gera uma lista de números aleatórios com base em `data_size`, redesenha e atualiza o status.
        
  *   `draw_data(color_info={})`: Limpa o canvas e desenha as barras representando os elementos da lista. `color_info` é um dicionário que especifica cores para barras específicas (comparadas, trocadas, ordenadas, etc.).
        
  *   `start_sort()`: Prepara a aplicação para a ordenação (desabilita controles, reseta contadores), seleciona o gerador do algoritmo e inicia a animação.
        
  *   `toggle_pause()`: Alterna o estado de pausa da animação.
        
  *   `animate_step()`: Núcleo da animação. Obtém o próximo estado (passo) do gerador do algoritmo, chama `draw_data` para atualizar o canvas e agenda a próxima chamada a si mesma usando `master.after()` com base na `animation_speed`. Lida com `StopIteration` para finalizar a animação.
        
  *   `reset_visualization()`: Interrompe qualquer ordenação em progresso, reabilita os controles e redesenha os dados no estado atual.
        
  *   `confirm_exit()`: Exibe um `messagebox` de confirmação antes de fechar a aplicação, especialmente se uma ordenação estiver em andamento.

  **8-Geradores de Algoritmos de Ordenação (`_gen`):**

  *   `bubble_sort_gen()`, `selection_sort_gen()`, `insertion_sort_gen()`:
    
*   Implementações dos algoritmos modificadas para funcionar como geradores.
  
 *   Usam `yield color_info` em cada passo crucial (comparação, troca) para "pausar" a execução do algoritmo e permitir que a GUI se atualize.

*   Incrementam `self.comparisons` e `self.swaps` conforme apropriado.
  
  *   O dicionário `color_info` retornado instrui `draw_data` sobre como colorir as barras para o passo atual.

  **9-Bloco `if __name__ == "__main__":`:**
  
 * Ponto de entrada padrão para iniciar a aplicação Tkinter, criando a janela raiz e instanciando `SortingVisualizerApp`.

# ❄️ **2. `setup.py` (Script de Build com `cx_Freeze`):**

Este script é usado para compilar o `EstruturadeOrdenacao.py` em um executável standalone, facilitando a distribuição.

*   **1-Importações:** `sys` e `cx_Freeze` (módulos `setup`, `Executable`).
  
*   **2-Configuração de `base`:**
  
    *   Define `base = "Win32GUI"` na plataforma Windows para suprimir a janela de console que apareceria por padrão com aplicações GUI.
*   **3-`script_principal`:**
    *   Variável que armazena o nome do arquivo Python principal a ser compilado
        (definido como "EstruturadeOrdenacao.py").
*   **4-`build_exe_options`:**
    *   Dicionário de opções para o processo de build:
        *   `packages`: Lista explicitamente os pacotes necessários (`tkinter`, `random`, `time`).
        *   `includes`, `excludes`: Para controle fino de módulos (vazios neste caso).
        *   `include_files`: Para incluir arquivos de dados adicionais (vazio aqui).
        *   `optimize`: Nível de otimização do bytecode (definido como 2).
*   **5-`executables`:**
    *   Lista contendo uma instância de `Executable`.
    *   Define o script a ser compilado (`script_principal`), a `base` configurada anteriormente, o nome do arquivo executável de saída
        (`target_name="VisualizadorOrdenacao.exe"`), e um placeholder para um ícone (atualmente `None`).
*   **6-Função `setup()`:**
    *   Chamada principal do `cx_Freeze` que configura o processo de build.
    *   Inclui metadados da aplicação como `name`, `version`, `description`, `author`.
    *   Passa as `build_exe_options` e a lista de `executables`.
*   **7-Mensagens Informativas:**
    *   Imprime instruções no console sobre como executar o build
        (`python setup.py build`).
