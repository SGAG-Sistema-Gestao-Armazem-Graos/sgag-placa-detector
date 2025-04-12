# SGAG - Sistema de Gestão de Armazém de Grãos

O **SGAG** é um sistema automatizado desenvolvido para gerenciar o processo logístico de armazém de grãos. O sistema utiliza técnicas de **Visão Computacional** com **OpenCV** para captura de imagens de caminhões e **OCR (Reconhecimento Óptico de Caracteres)** com **Tesseract** para ler as placas dos veículos. Além disso, o sistema gerencia informações sobre os veículos, motoristas, tipos de grãos e movimentação no armazém.

## Estrutura do Repositório

Abaixo está a estrutura do repositório com uma breve descrição de cada diretório e arquivo:

```
sgag-placa-detector/
│
├── crud_db/                          # Funções CRUD para manipulação de dados no banco de dados
│   ├── cargo_vehicle_crud.py          # CRUD para veículos de carga
│   ├── cargo_vehicle_type_CRUD.py     # CRUD para tipos de veículos de carga
│   ├── driver_license_crud.py
│   ├── driver_crud.py
│   ├── driver_license_crud.py
│   ├── grain_load_crud.py
│   ├── grain_type_crud.py
│   ├── load_crud.py
│   ├── responsible_person_crud.py
│   ├── storage_location_crud.py
│   
├── display/                           # Exibição de informações e relatórios
│   ├── display_cargo_vehicle_type.py  # Exibição de tipos de veículos de carga
│   ├── display_cargo_vehicle.py       # Exibição de veículos de carga
│   
├── leitura_placa/                     # Processamento de imagem e leitura de placa
│   ├── captura_imagem.py              # Captura de imagem dos caminhões
│
├── ai_plate_recognition/
│   ├── __init__.py
│   ├── main.py               # App principal (interface ou terminal)
│   ├── detector.py           # Responsável por detectar a placa e extrair texto
│   ├── camera.py             # Captura imagens da câmera ou vídeo
│   ├── plate_reader.py       # Lógica de OCR (Tesseract ou EasyOCR)
│   ├── driver_manager.py     # CRUD para motoristas (você já tem)
│   ├── driver.py             # Classe Driver
│   └── images/               # Pasta para armazenar imagens
│       └── (vazia por enquanto)
├── manager/                           # Lógica de gerenciamento de dados
│   ├── cargo_vehicle_type.py          # Gerenciamento de tipos de veículos de carga
│   ├── cargo_vehicle.py               # Gerenciamento de veículos de carga
│   ├── driver_license.py              # Gerenciamento de licenças de motoristas
│   ├── driver.py                      # Gerenciamento de motoristas
│   ├── grain_load_type.py             # Gerenciamento de tipos de carregamento de grãos
│   ├── grain_type.py                  # Gerenciamento de tipos de grãos
│   ├── load.py                        # Gerenciamento de carregamentos
│   ├── movement_forecast.py           # Previsão de movimentação
│   ├── movement.py                    # Gerenciamento de movimentação
│   ├── responsible_person.py          # Gerenciamento de responsáveis
│   ├── stock_history.py               # Histórico de estoque
│   ├── storage_location.py            # Localização de armazenamento
│   ├── weather_forecast.py            # Previsão do tempo
│
├── oracle_db/                         # Conexão com o banco de dados Oracle
│   ├── oracle_db.py                   # Arquivo de configuração de banco de dados Oracle
│   
├── script_logistica_oracle/           # Scripts logísticos e de integração com Oracle
│   ├── script_logistic_oracle.sql     # Outros scripts logísticos
│   
├── test/                              # Testes automatizados
│   ├── test_crud/                     # Testes dos CRUDs
│   ├── test_cargo_vehicle_type.py     # Testes para tipos de veículos de carga
│   ├── test_cargo_vehicle.py          # Testes para veículos de carga
│   ├── test_driver_license.py         # Testes para licenças de motoristas
│   ├── test_driver.py                 # Testes para motoristas
│   ├── test_grain_load_type.py        # Testes para tipos de carregamento de grãos
│   ├── test_grain_type.py             # Testes para tipos de grãos
│   ├── test_load.py                   # Testes para carregamentos
│   ├── test_movement_forecast.py      # Testes para previsões de movimentação
│   ├── test_movement.py               # Testes para movimentação
│   ├── test_responsible_person.py     # Testes para responsáveis
│   ├── test_stock_history.py          # Testes para histórico de estoque
│   ├── test_storage_location.py       # Testes para localização de armazenamento
│   ├── test_weather_forecast.py       # Testes para previsão do tempo
│   
├── main.py                            # Arquivo principal de execução
│   
├── README.md                          # Este arquivo de documentação
└── requirements.txt                   # Dependências do projeto
```

## Funcionalidades

### 1. Captura e Leitura de Placas
A funcionalidade principal do **SGAG** é a captura automática de imagens de caminhões e a leitura das placas utilizando **OpenCV** e **Tesseract** (OCR). Isso permite a identificação rápida de veículos no processo de carregamento e descarregamento de grãos.

### 2. Gerenciamento de Veículos e Motoristas
O sistema gerencia informações sobre os veículos de carga, incluindo tipo de veículo, dados do motorista e suas licenças. Através do sistema, é possível registrar novos veículos, atualizar suas informações e consultar o histórico de movimentações.

### 3. Gerenciamento de Grãos e Movimentações
O **SGAG** também lida com os tipos de grãos, tipos de carregamento e a movimentação dentro do armazém, realizando previsões de estoque e armazenamento com base em dados históricos e previsão do tempo.

### 4. Banco de Dados Oracle
A integração com o banco de dados Oracle permite que todas as informações do sistema sejam armazenadas de forma segura e consultadas conforme necessário. Scripts específicos fazem a integração entre o sistema e o banco de dados.

## Requisitos

Para rodar o projeto, você precisa das seguintes dependências:

- Python 3.x
- cx_Oracle==8.3.0
- numpy==2.2.4
- opencv-python==4.11.0.86
- pillow==11.1.0

As dependências podem ser instaladas com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/SGAG-Sistema-Gestao-Armazem-Graos/sgag-placa-detector
```

2. Navegue até o diretório do projeto:

```bash
cd sgag-placa-detector
```

3. Execute o script principal:

```bash
python main.py
```

## Testes

Os testes unitários estão localizados na pasta **`test/`**. Para rodá-los, basta executar o seguinte comando:

```bash
python -m unittest discover -s test
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou fazer **pull requests** para melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
