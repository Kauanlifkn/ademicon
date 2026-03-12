import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

head_match = re.search(r'<head>.*?</head>', html, re.DOTALL)
head = head_match.group(0) if head_match else ""

body_match = re.search(r'<body[^>]*>', html)
body_tag = body_match.group(0) if body_match else "<body>"

nav_match = re.search(r'<nav.*?</nav>', html, re.DOTALL)
nav = nav_match.group(0) if nav_match else ""

# Adapt Navigation
nav = re.sub(r'<div class="hidden md:flex items-center gap-8 text-sm font-medium".*?</div>', '', nav, flags=re.DOTALL)
nav = nav.replace('AETHER', 'MASTERCLASS')
nav = nav.replace('Get started now', 'Garantir minha vaga')
nav = nav.replace('route(\'landing\')', 'document.getElementById(\'hero\').scrollIntoView({behavior: \\\'smooth\\\'})')
nav = nav.replace('window.location.href=\'/contact\'', 'document.getElementById(\'cadastro\').scrollIntoView({behavior: \\\'smooth\\\'})')


hero = """
<section id="hero" class="pt-32 pr-6 pb-32 pl-6 relative overflow-hidden">
    <div class="fixed top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[600px] bg-emerald-500/20 rounded-full blur-[120px] -z-10 pointer-events-none opacity-20"></div>
    <div class="flex flex-col text-center max-w-4xl mx-auto items-center fade-in">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 text-xs text-emerald-400 mb-8 hover:bg-white/10 transition-colors cursor-default">
            <span class="px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-medium text-[10px] uppercase tracking-wider">AULA GRATUITA</span>
            <span>Exclusivo para Corretores de Imóveis</span>
        </div>
        <h1 class="leading-[1.1] md:text-7xl lg:text-6xl text-5xl font-medium text-white tracking-tight mb-8">
            Pare de perder vendas na <br class="hidden md:block"/><span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-emerald-200">mesa de crédito</span>
        </h1>
        <p class="md:text-xl leading-relaxed text-lg text-slate-400 max-w-2xl mx-auto mb-10">
            Descubra o método exato para reverter clientes com crédito reprovado e garanta suas comissões mesmo quando o banco diz não.
        </p>
        <div class="flex flex-col sm:flex-row items-center gap-4">
            <button onclick="document.getElementById('cadastro').scrollIntoView({behavior: 'smooth'})" class="group hover:bg-emerald-400 transition-all flex font-medium text-[#050505] bg-emerald-500 rounded-full pt-4 pr-8 pb-4 pl-8 gap-x-2 gap-y-2 items-center cursor-pointer">
                Quero aprender a salvar minhas vendas
                <svg aria-hidden="true" class="lucide lucide-trending-up w-4 h-4 group-hover:translate-x-1 transition-transform" data-lucide="trending-up" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M16 7h6v6"></path>
                    <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                </svg>
            </button>
        </div>
    </div>
</section>
"""

agitation = """
<section class="max-w-7xl mx-auto px-6 pb-32">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div class="relative z-10">
            <h2 class="md:text-5xl text-4xl font-medium text-white tracking-tight mb-6 leading-[1.1]">
                A dor invisível do <br/>
                <span class="text-emerald-400 text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-emerald-200">corretor de imóveis</span>
            </h2>
            <p class="leading-relaxed text-lg text-slate-400 mb-8">
                Você gasta com anúncios, faz o atendimento perfeito, leva para visitar o imóvel, gasta combustível, tempo e energia. O cliente ama a casa, decide comprar... e então, <strong>o banco nega o financiamento.</strong> 
            </p>
            <div class="space-y-4">
                <div class="flex items-center gap-4 p-4 rounded-xl border border-white/10 bg-[#0A0C10]">
                    <div class="w-10 h-10 rounded-full bg-orange-500/10 border border-orange-500/20 flex items-center justify-center text-orange-400 shrink-0">
                        <svg aria-hidden="true" class="w-5 h-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    </div>
                    <div>
                        <h4 class="text-sm font-medium text-white">Semanas de trabalho perdidas</h4>
                        <p class="text-xs text-slate-500 mt-1">Todo o esforço de prospecção vai pelo ralo no último momento.</p>
                    </div>
                </div>
                <div class="flex items-center gap-4 p-4 rounded-xl border border-white/10 bg-[#0A0C10]">
                    <div class="w-10 h-10 rounded-full bg-orange-500/10 border border-orange-500/20 flex items-center justify-center text-orange-400 shrink-0">
                        <svg aria-hidden="true" class="w-5 h-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                    </div>
                    <div>
                        <h4 class="text-sm font-medium text-white">Comissões que não entram</h4>
                        <p class="text-xs text-slate-500 mt-1">Dinheiro que já era dado como certo não chega na sua conta.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="relative lg:pl-10">
            <div class="aspect-square rounded-3xl border border-white/10 bg-[#0A0C10] p-8 overflow-hidden relative flex flex-col justify-center gap-6 group hover:border-white/20 transition-all">
                <div class="absolute inset-0 bg-gradient-to-b from-white/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                
                <div class="flex items-center justify-between p-4 rounded-xl border border-white/5 bg-[#050505] relative z-10 opacity-50 grayscale">
                    <div class="flex items-center gap-3">
                        <div class="w-2 h-2 rounded-full bg-emerald-500"></div>
                        <div class="flex flex-col gap-1">
                            <span class="text-sm font-medium text-white">Financiamento Aprovado</span>
                            <span class="text-xs font-mono text-slate-500">Comissão de R$ 25.000 via Pix</span>
                        </div>
                    </div>
                </div>

                <div class="flex items-center justify-between p-4 rounded-xl border border-orange-500/30 bg-orange-500/10 relative z-10 scale-105 shadow-[0_0_20px_rgba(249,115,22,0.15)]">
                    <div class="flex items-center gap-3">
                        <div class="w-2 h-2 rounded-full bg-orange-500 animate-pulse"></div>
                        <div class="flex flex-col gap-1">
                            <span class="text-sm font-medium text-white">Financiamento Negado</span>
                            <span class="text-xs font-mono text-orange-400">Comissão perdida. Seu tempo jogado fora.</span>
                        </div>
                    </div>
                    <svg aria-hidden="true" class="w-5 h-5 text-orange-500" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </div>

            </div>
        </div>
    </div>
</section>
"""

benefits = """
<section class="max-w-7xl mx-auto px-6 pb-32">
    <div class="text-center mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">O que você vai aprender na aula</h2>
        <p class="text-lg text-slate-400">Descubra os métodos avançados que os grandes tubarões do mercado usam para contornar crédito reprovado.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Benefit 1 -->
        <div class="group relative rounded-3xl border border-white/10 bg-[#0A0C10] p-8 overflow-hidden hover:border-emerald-500/30 transition-all duration-300">
            <div class="absolute inset-0 bg-gradient-to-b from-white/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div class="h-16 w-16 mb-6 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                <svg aria-hidden="true" class="w-8 h-8" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </div>
            <h3 class="text-xl font-medium text-white mb-3 tracking-tight">O Segredo da Análise Prévia</h3>
            <p class="text-sm text-slate-400 leading-relaxed">Como identificar os riscos de reprovação antes mesmo de apresentar o imóvel para o cliente e poupar horas do seu dia.</p>
        </div>
        <!-- Benefit 2 -->
        <div class="group relative rounded-3xl border border-white/10 bg-[#0A0C10] p-8 overflow-hidden hover:border-emerald-500/30 transition-all duration-300">
            <div class="absolute inset-0 bg-gradient-to-b from-white/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div class="h-16 w-16 mb-6 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                <svg aria-hidden="true" class="w-8 h-8" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 22V12"></path><path d="m3.3 7 8.7 5 8.7-5"></path><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"></path></svg>
            </div>
            <h3 class="text-xl font-medium text-white mb-3 tracking-tight">Reestruturação do Perfil</h3>
            <p class="text-sm text-slate-400 leading-relaxed">Passo a passo prático para ajudar o cliente a adequar a renda e o score, tornando o perfil atraente para ser aprovado.</p>
        </div>
        <!-- Benefit 3 -->
        <div class="group relative rounded-3xl border border-white/10 bg-[#0A0C10] p-8 overflow-hidden hover:border-emerald-500/30 transition-all duration-300">
            <div class="absolute inset-0 bg-gradient-to-b from-white/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div class="h-16 w-16 mb-6 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                <svg aria-hidden="true" class="w-8 h-8" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"></path><path d="M12 12v9"></path><path d="m16 16-4-4-4 4"></path></svg>
            </div>
            <h3 class="text-xl font-medium text-white mb-3 tracking-tight">Alternativas de Financiamento</h3>
            <p class="text-sm text-slate-400 leading-relaxed">Instituições financeiras e modelagens de crédito além da Caixa e grandes bancos tradicionais que aprovam as pastas reprovadas.</p>
        </div>
    </div>
</section>
"""

form = """
<section id="cadastro" class="max-w-7xl mx-auto px-6 pb-32">
    <div class="border border-white/10 bg-[#0A0C10] rounded-3xl overflow-hidden shadow-2xl flex flex-col md:flex-row relative">
        <div class="absolute bottom-0 right-0 w-[400px] h-[300px] bg-emerald-500/10 rounded-full blur-[100px] pointer-events-none"></div>
        <div class="md:w-1/2 p-10 md:p-16 border-b md:border-b-0 md:border-r border-white/10 flex flex-col justify-center">
            <div class="inline-flex max-w-max items-center gap-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 text-xs text-emerald-400 mb-6 font-medium">
                <div class="w-2 h-2 rounded-full bg-emerald-500 animate-[spin_2s_linear_infinite]"></div>
                VAGAS LIMITADAS
            </div>
            <h2 class="text-4xl lg:text-5xl font-medium text-white mb-6 tracking-tight leading-[1.1]">
                Garanta seu lugar <br/> na Masterclass
            </h2>
            <p class="text-slate-400 text-lg leading-relaxed">
                Preencha o formulário abaixo com atenção para receber o link de acesso exclusivo da aula gratuita no seu E-mail e WhatsApp.
            </p>
        </div>
        <div class="md:w-1/2 p-10 md:p-16 bg-[#050505] relative z-10">
            <form onsubmit="event.preventDefault(); alert('Cadastro realizado com sucesso! Verifique seu e-mail e WhatsApp.')" class="space-y-6">
                <div class="space-y-2">
                    <label class="text-sm font-medium text-slate-300">Seu nome completo</label>
                    <input type="text" placeholder="Ex: João da Silva" class="h-14 w-full bg-[#050505] border border-white/10 rounded-lg px-4 text-white placeholder-slate-600 outline-none focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:border-transparent transition-all" required>
                </div>
                <div class="space-y-2">
                    <label class="text-sm font-medium text-slate-300">E-mail principal</label>
                    <input type="email" placeholder="Ex: corretor@imobiliaria.com.br" class="h-14 w-full bg-[#050505] border border-white/10 rounded-lg px-4 text-white placeholder-slate-600 outline-none focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:border-transparent transition-all" required>
                </div>
                <div class="space-y-2">
                    <label class="text-sm font-medium text-slate-300">WhatsApp</label>
                    <input type="tel" placeholder="(11) 90000-0000" class="h-14 w-full bg-[#050505] border border-white/10 rounded-lg px-4 text-white placeholder-slate-600 outline-none focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:border-transparent transition-all" required>
                </div>
                
                <button type="submit" class="group relative inline-flex w-full h-14 overflow-hidden rounded-lg p-[1px] focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:ring-offset-2 focus:ring-offset-slate-900 mt-4 rounded-xl">
                    <span class="absolute inset-[-1000%] animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#10b981_0%,#050505_50%,#10b981_100%)]"></span>
                    <span class="inline-flex cursor-pointer items-center justify-center transition-colors group-hover:bg-[#050505]/80 text-lg font-medium text-white bg-[#050505] w-full h-full rounded-xl backdrop-blur-3xl gap-2">
                        Garantir minha vaga gratuita
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                    </span>
                </button>

                <div class="flex items-center gap-2 justify-center text-xs text-slate-500 mt-4">
                    <svg class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    <span>Seus dados estão 100% seguros conosco.</span>
                </div>
            </form>
        </div>
    </div>
</section>
"""

footer = """
<footer class="border-t border-white/10 bg-[#020617] pt-16 pb-8">
    <div class="max-w-7xl mx-auto px-6">
        <div class="flex flex-col items-center gap-4 mb-16 text-center">
            <div class="text-emerald-400">
                <svg aria-hidden="true" class="lucide lucide-triangle w-8 h-8 fill-current rotate-180" data-lucide="triangle" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13.73 4a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path>
                </svg>
            </div>
            <span class="text-white text-2xl font-medium tracking-tight">
                MASTERCLASS CRÉDITO
            </span>
            <p class="text-slate-500 text-sm max-w-md">
                Transformando corretores de imóveis em especialistas absolutos em aprovação financeira e conversão.
            </p>
        </div>
        <div class="border-t border-white/5 pt-8 flex justify-center text-center">
            <p class="text-slate-500 text-xs text-center">
                © 2026 Masterclass Crédito. Todos os direitos reservados.
            </p>
        </div>
    </div>
</footer>
"""

landing_html = f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
{head}
{body_tag}
{nav}
<main class="pt-20 min-h-screen relative overflow-hidden bg-[#050505]">
{hero}
{agitation}
{benefits}
{form}
</main>
{footer}
</body>
</html>"""

with open('landing-corretores.html', 'w', encoding='utf-8') as f:
    f.write(landing_html)

print("Generated landing page successfully.")
