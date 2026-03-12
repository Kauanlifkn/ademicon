# 📋 Integração do Formulário com Webhook (Make/n8n)

## 🎯 Visão Geral

Este formulário envia dados capturados da landing page para um webhook (Make/n8n) que pode ser usado para:
- Salvar leads em banco de dados
- Enviar mensagens automáticas via WhatsApp
- Integrar com CRM
- Disparar e-mails de confirmação

---

## 🚀 Como Configurar

### 1. Criar o Webhook

#### No Make (Integromat):
1. Acesse [make.com](https://make.com)
2. Crie um novo cenário
3. Adicione um trigger "Webhooks" → "Custom webhook"
4. Clique em "Add" para criar um novo webhook
5. Configure como método **POST**
6. Copie a URL gerada

#### No n8n:
1. Acesse sua instância do n8n
2. Crie um novo workflow
3. Adicione o nó "Webhook"
4. Configure como método **POST**
5. Copie a URL gerada

---

### 2. Configurar a URL no Código

No arquivo `landing-corretores-formulario.html`, localize a linha:

```javascript
const WEBHOOK_URL = 'COLOQUE_SEU_WEBHOOK_AQUI';
```

Substitua pela URL do seu webhook:

```javascript
const WEBHOOK_URL = 'https://hook.us1.make.com/seu-webhook-id-unico';
// ou
const WEBHOOK_URL = 'https://seu-dominio.com/webhook/corretor-inscricao';
```

---

## 📦 Estrutura dos Dados Recebidos

O webhook recebe um JSON com a seguinte estrutura:

```json
{
    "nome": "João Silva",
    "telefone": "11999999999",
    "cidade": "São Paulo",
    "corretor": "sim",
    "tempo_atuacao": "2 anos"
}
```

### Campo Especial: `telefone`

O telefone é **automaticamente limpo** antes do envio:
- Remove espaços: `(11) 99999-9999` → `(11)99999-9999`
- Remove parênteses: `(11)99999-9999` → `1199999999`
- Remove traços: `1199999999` → `1199999999`

Isso facilita integrações diretas com APIs de WhatsApp.

---

## 🎨 Comportamento da UI

### Estado Inicial
- Formulário visível com todos os campos
- Botão "Garantir minha vaga" habilitado

### Loading State
Ao clicar no botão:
- Texto muda para **"Enviando..."**
- Botão é **desabilitado** (evita cliques duplos)
- Spinner animado aparece no botão

### Sucesso (Status 200)
- Formulário é **ocultado**
- Mensagem de sucesso aparece:
  ```
  Em breve você receberá
  o link da aula.
  Até breve!
  ```
- Scroll suave até a mensagem

### Erro
- Botão retorna ao estado original
- Mensagem de erro discreta aparece:
  ```
  ⚠️ Ocorreu um erro ao enviar. Por favor, tente novamente.
  ```
- Scroll suave até a mensagem de erro

---

## 🔧 Troubleshooting

### Formulário não envia dados:
- Verifique se a `WEBHOOK_URL` está configurada corretamente
- Confirme que o webhook está **ativo** no Make/n8n
- Verifique o console do navegador (F12) para erros

### Recebendo dados vazios:
- Confirme que os campos do formulário têm os atributos `name` corretos
- Verifique se a validação HTML5 (`required`) está funcionando

### Integração com WhatsApp não funciona:
- Certifique-se de que o telefone está sendo limpo corretamente
- Teste o número de telefone manualmente
- Verifique se a API de WhatsApp está configurada corretamente

---

## 📝 Exemplo de Integração com WhatsApp

No Make/n8n, após receber o webhook:

1. Adicione um nó "HTTP Request"
2. Configure para a API do WhatsApp
3. Use o campo `telefone` do webhook
4. Envie mensagem automática de confirmação

Exemplo de payload para WhatsApp API:

```json
{
    "phone": "55{{telefone}}",
    "message": "Olá {{nome}}! Sua inscrição na Masterclass Crédito foi confirmada. Em breve você receberá o link da aula. 🎓"
}
```

---

## 🔐 Segurança

- Todos os dados são enviados via HTTPS (se o webhook usar HTTPS)
- O formulário usa validação HTML5 no frontend
- Considerar adicionar rate-limiting no webhook
- Usar autenticação no webhook se necessário

---

## 📚 Arquivos do Projeto

1. **`landing-corretores-formulario.html`** - Landing page completa com formulário integrado
2. **`formulario-script.js`** - Script JavaScript isolado e documentado
3. **`formulario-html.html`** - HTML da seção do formulário para referência
4. **Este arquivo** - Instruções de integração

---

## 🎓 Design System

O formulário mantém todas as características do Design System:
- **Cor de destaque**: VERMELHA (`red-500`, `red-400`)
- **Tema**: Dark (`#050505`)
- **Fonte**: Inter
- **Bordas e Focus**: Vermelho com blur e gradientes
- **Ícones**: Lucide
- **Responsivo**: Mobile-first

---

## 💡 Dicas Adicionais

1. **Teste o webhook** antes de colocar em produção usando ferramentas como Postman
2. **Adicione logs** no Make/n8n para monitorar os dados recebidos
3. **Configure notificações** de erro no webhook para saber quando falhar
4. **Use variáveis de ambiente** para a URL do webhook em produção
5. **Considere adicionar CAPTCHA** para evitar spam

---

## 📞 Suporte

Para dúvidas sobre a integração:
- Verifique a documentação do Make: [docs.make.com](https://docs.make.com)
- Verifique a documentação do n8n: [docs.n8n.io](https://docs.n8n.io)
- Revise o console do navegador para erros JavaScript

---

**Desenvolvido com 💜 usando Design System personalizado**
