
# Telegram Message Router

Sistema profissional de automação e roteamento de mensagens no Telegram usando **Telethon**.

## 📌 Visão Geral
Este projeto foi desenvolvido para monitorar múltiplos chats, identificar tópicos, tipos de conteúdo e redistribuir mensagens automaticamente para destinos específicos.

O foco é **arquitetura limpa, estabilidade e escalabilidade**, evitando forward direto (restrições de chats protegidos).

---

## 🚀 Funcionalidades
- Monitoramento de múltiplos grupos/canais
- Suporte a tópicos (Forum Topics)
- Repasse de:
  - Texto
  - Imagens
  - Vídeos
  - Stickers (com substituição automática)
- Agendamentos automáticos (bom dia / encerramento)
- Tratamento de erros e logs claros
- Compatível com chats protegidos

---

## 🧱 Arquitetura
O projeto foi dividido em módulos para facilitar manutenção:

```
src/
 ├── main.py        # Inicialização do cliente e eventos
 ├── router.py      # Lógica de roteamento
 ├── scheduler.py   # Rotinas automáticas
 ├── config.py      # IDs e configurações
 └── utils.py       # Funções auxiliares
```

Isso evita um `main.py` gigante e melhora a legibilidade.

---

## 🔒 Segurança
- Nenhuma credencial sensível incluída
- IDs e hashes isolados
- Pronto para uso com variáveis de ambiente

---

## 🛠 Tecnologias
- Python 3.10+
- Telethon
- AsyncIO

---

## ▶️ Execução
```bash
python -m src.main
```

---

## 📈 Casos de Uso
- Automação de canais pagos
- Curadoria de conteúdo
- Distribuição segmentada
- Bots de suporte

---

## 👨‍💻 Autor
Karlos Sanchez

Projeto real adaptado para portfolio técnico.
