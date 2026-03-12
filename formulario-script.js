// ========================================
// SCRIPT DO FORMULÁRIO - MASTERCLASS CRÉDITO
// Integração com Webhook Make/n8n
// ========================================

// Toggle mobile menu
function toggleMenu() {
    document.getElementById('mobile-menu').classList.toggle('hidden');
}

// ========================================
// CONFIGURAÇÃO DO WEBHOOK
// ========================================
// Configure seu webhook do Make/n8n aqui
// Exemplo: const WEBHOOK_URL = 'https://hook.us1.make.com/seu-webhook-id';
const WEBHOOK_URL = 'https://hook.us2.make.com/puekr3jyrmqd2pjvaitenf1lzf8dpt3m';

// ========================================
// FUNÇÕES UTILITÁRIAS
// ========================================

// Função para limpar o telefone (remover espaços, parênteses e traços)
// Isso facilita a automação via WhatsApp
function cleanPhone(phone) {
    return phone
        .replace(/\s/g, '')      // Remove espaços
        .replace(/\(/g, '')      // Remove parênteses de abertura
        .replace(/\)/g, '')      // Remove parênteses de fechamento
        .replace(/-/g, '');      // Remove traços
}

// ========================================
// LÓGICA DE ENVIO DO FORMULÁRIO
// ========================================
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inscricao-form');
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');

    if (form) {
        form.addEventListener('submit', async function (event) {
            // Prevenir comportamento padrão do formulário
            event.preventDefault();

            // Esconder mensagem de erro se estiver visível
            if (errorMessage && !errorMessage.classList.contains('hidden')) {
                errorMessage.classList.add('hidden');
            }

            // ========================================
            // CAPTURA E PREPARAÇÃO DOS DADOS
            // ========================================
            const formData = new FormData(form);
            const rawData = Object.fromEntries(formData.entries());

            // Limpar telefone para automação via WhatsApp
            const cleanedData = {
                ...rawData,
                telefone: cleanPhone(rawData.telefone)
            };

            console.log('Dados preparados para envio:', cleanedData);

            // ========================================
            // ESTADO DE LOADING (UX)
            // ========================================
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonContent = submitButton.innerHTML;

            // Desabilitar botão e mostrar estado de loading
            submitButton.disabled = true;
            submitButton.innerHTML = `
                <span class="absolute inset-[-1000%] animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#ef4444_0%,#050505_50%,#ef4444_100%)]"></span>
                <span class="inline-flex cursor-pointer items-center justify-center transition-colors group-hover:bg-[#050505]/80 text-lg font-medium text-white bg-[#050505] w-full h-full rounded-xl backdrop-blur-3xl gap-2">
                    <svg class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">
                        <path d="M12 2v4m0 12v4M4.93 4.93l2.83 2.83m8.48 8.48l2.83 2.83M2 12h4m12 0h4M4.93 19.07l2.83-2.83m8.48-8.48l2.83-2.83"></path>
                    </svg>
                    Enviando...
                </span>
            `;

            // ========================================
            // ENVIO VIA FETCH (POST)
            // ========================================
            try {
                const response = await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(cleanedData)
                });

                // ========================================
                // TRATAMENTO DE SUCESSO
                // ========================================
                if (response.ok) {
                    // Ocultar formulário
                    form.classList.add('hidden');

                    // Mostrar mensagem de sucesso
                    if (successMessage) {
                        successMessage.classList.remove('hidden');
                        // Scroll suave até a mensagem de sucesso
                        successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }

                    console.log('✅ Dados enviados com sucesso!');
                    console.log('Payload enviado:', cleanedData);

                } else {
                    // ========================================
                    // TRATAMENTO DE ERRO (STATUS HTTP)
                    // ========================================
                    throw new Error(`Status ${response.status}: ${response.statusText}`);
                }

            } catch (error) {
                // ========================================
                // TRATAMENTO DE ERRO (EXCEÇÃO)
                // ========================================
                console.error('❌ Erro ao enviar formulário:', error);

                // Restaurar botão ao estado original
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonContent;

                // Mostrar mensagem de erro discreta
                if (errorMessage) {
                    errorMessage.classList.remove('hidden');
                    // Scroll suave até a mensagem de erro
                    errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });
    }

    // Initialize Lucide icons
    lucide.createIcons();
});

// ========================================
// ESTRUTURA DO JSON ENVIADO
// ========================================
/*
{
    "nome": "João Silva",
    "telefone": "11999999999",  // Telefone limpo (sem formatação)
    "cidade": "São Paulo",
    "corretor": "sim",          // "sim" ou "nao"
    "tempo_atuacao": "2 anos"
}
*/

// ========================================
// INSTRUÇÕES DE INTEGRAÇÃO
// ========================================
/*
1. Crie um webhook no Make (Integromat) ou n8n
2. Configure o método como POST
3. Adicione os campos correspondentes no seu fluxo de automação
4. Copie a URL do webhook
5. Substitua 'COLOQUE_SEU_WEBHOOK_AQUI' pela URL real
6. Teste o formulário

Exemplo de URL do Make:
const WEBHOOK_URL = 'https://hook.us1.make.com/seu-webhook-id-unico';

Exemplo de URL do n8n:
const WEBHOOK_URL = 'https://seu-dominio.com/webhook/corretor-inscricao';
*/
