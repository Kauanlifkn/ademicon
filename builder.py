import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract head and nav
head_match = re.search(r'<head>.*?</head>', html_content, re.DOTALL)
head_content = head_match.group(0) if head_match else ""

body_match = re.search(r'<body[^>]*>', html_content)
body_tag = body_match.group(0) if body_match else "<body>"

nav_match = re.search(r'<nav.*?</nav>', html_content, re.DOTALL)
nav_content = nav_match.group(0) if nav_match else ""

# Modify nav to have anchor links to sections
nav_modified = nav_content
# Find the desktop links container
desktop_links_match = re.search(r'<div class="hidden md:flex items-center gap-8 text-sm font-medium">.*?</div>', nav_modified, re.DOTALL)
if desktop_links_match:
    new_links = """<div class="hidden md:flex items-center gap-6 text-sm font-medium">
<a class="hover:text-white transition-colors" href="#hero">Hero</a>
<a class="hover:text-white transition-colors" href="#typography">Typography</a>
<a class="hover:text-white transition-colors" href="#colors">Colors</a>
<a class="hover:text-white transition-colors" href="#components">Components</a>
<a class="hover:text-white transition-colors" href="#layout">Layout</a>
<a class="hover:text-white transition-colors" href="#motion">Motion</a>
<a class="hover:text-white transition-colors" href="#icons">Icons</a>
</div>"""
    nav_modified = nav_modified.replace(desktop_links_match.group(0), new_links)
else:
    nav_modified = nav_modified.replace('Home', 'Design System')

# Extract Hero section
hero_match = re.search(r'<section class="pt-20 pr-6 pb-32 pl-6 relative">.*?</section>', html_content, re.DOTALL)
hero_content = hero_match.group(0) if hero_match else ""
hero_content = hero_content.replace('AI solutions', 'Design System')
hero_content = hero_content.replace('designed\n    <br/>\n    for your business needs', 'living library\n    <br/>\n    for AETHER components')
hero_content = hero_content.replace('Built for efficiency and scalability, it adapts to your workflow\n    and boosts productivity across your entire organization.', 'A comprehensive guide to the visual language, elements, and motion patterns of our platform.')
hero_content = hero_content.replace('Get started now', 'Explore System')
hero_content = f'<div id="hero" class="pt-20">{hero_content}</div>'

# 1) Typography
typography_section = """
<section id="typography" class="max-w-7xl mx-auto px-6 pb-32 pt-20 border-t border-white/10">
    <div class="mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">Typography</h2>
        <p class="text-lg text-slate-400">Communicating hierarchy, scale, and rhythm.</p>
    </div>
    <div class="space-y-8 divide-y divide-white/10">
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Heading 1</div>
            <div class="flex-1 md:text-7xl lg:text-6xl text-5xl font-medium text-white tracking-tight leading-[1.1]">The quick brown fox jumps over the lazy dog</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">72px / 1.1</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Heading 2</div>
            <div class="flex-1 text-4xl md:text-5xl font-medium text-white tracking-tight mb-6">The quick brown fox jumps over the lazy dog</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">48px / 1.1</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Heading 3</div>
            <div class="flex-1 text-3xl md:text-4xl font-medium text-white mb-4 tracking-tight">The quick brown fox jumps over the lazy dog</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">36px / 1.1</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Heading 4</div>
            <div class="flex-1 text-xl font-medium text-white mb-3 tracking-tight">The quick brown fox jumps over the lazy dog</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">20px / 1.1</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Bold L</div>
            <div class="flex-1 text-lg font-bold text-white">The quick brown fox</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">18px / 1.5</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Bold M</div>
            <div class="flex-1 text-base font-bold text-white">The quick brown fox</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">16px / 1.5</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Bold S</div>
            <div class="flex-1 text-sm font-bold text-white">The quick brown fox</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">14px / 1.5</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Paragraph</div>
            <div class="flex-1 leading-relaxed text-lg text-slate-400 max-w-2xl">The quick brown fox jumps over the lazy dog. Elements like this are used for larger body text where readability is paramount over multiple lines.</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">18px / 1.625</div>
        </div>
         <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Regular L</div>
            <div class="flex-1 text-lg text-slate-300">The quick brown fox jumps over the lazy dog.</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">18px / 1.5</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Regular M</div>
            <div class="flex-1 text-base text-slate-300">The quick brown fox jumps over the lazy dog.</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">16px / 1.5</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Regular S</div>
            <div class="flex-1 text-sm text-slate-300">The quick brown fox jumps over the lazy dog.</div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">14px / 1.5</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-center justify-between py-6 gap-4">
            <div class="w-48 text-sm text-slate-500 font-mono">Gradient Text</div>
            <div class="flex-1 text-3xl font-medium tracking-tight"><span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-emerald-200">The quick brown fox</span></div>
            <div class="w-32 text-right text-xs text-slate-500 font-mono">Gradient Focus</div>
        </div>
    </div>
</section>
"""

# 2) Colors & Surfaces
colors_section = """
<section id="colors" class="max-w-7xl mx-auto px-6 pb-32 pt-20 border-t border-white/10">
    <div class="mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">Colors & Surfaces</h2>
        <p class="text-lg text-slate-400">Backgrounds, borders, and gradients.</p>
    </div>
    
    <div class="mb-12">
        <h3 class="text-xl font-medium text-white mb-6">Backgrounds</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-[#050505] border border-white/5 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-[#050505]<br>Page Background</div>
            </div>
            <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-[#0A0C10] border border-white/5 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-[#0A0C10]<br>Card Background</div>
            </div>
            <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-[#0F1115] border border-white/5 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-[#0F1115]<br>Elevated Content</div>
            </div>
            <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-white/5 border border-white/5 mb-3 backdrop-blur-md"></div>
                <div class="text-xs text-slate-400 font-mono">bg-white/5<br>Hover/Glass</div>
            </div>
            <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-white/[0.02] border border-white/5 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-white/[0.02]<br>Subtle Elements</div>
            </div>
             <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-[#050505]/80 backdrop-blur-md border border-white/5 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-[#050505]/80<br>Nav/Blur</div>
            </div>
             <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-emerald-500/10 border border-emerald-500/20 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-emerald-500/10<br>Emerald Tint</div>
            </div>
            <div class="p-4 rounded-xl border border-white/10 bg-[#050505]">
                <div class="h-16 w-full rounded-md bg-indigo-500/20 border border-indigo-500/50 mb-3"></div>
                <div class="text-xs text-slate-400 font-mono">bg-indigo-500/20<br>Avatar Tint</div>
            </div>
        </div>
    </div>
    
    <div class="mb-12">
        <h3 class="text-xl font-medium text-white mb-6">Borders & Dividers</h3>
        <div class="flex flex-col gap-6">
            <div class="p-6 rounded-xl border border-white/10 bg-[#050505] flex items-center justify-between">
                <div class="text-sm font-mono text-slate-400">border-white/5</div>
                <div class="w-1/2 border-t border-white/5"></div>
            </div>
            <div class="p-6 rounded-xl border border-white/10 bg-[#050505] flex items-center justify-between">
                <div class="text-sm font-mono text-slate-400">border-white/10</div>
                <div class="w-1/2 border-t border-white/10"></div>
            </div>
            <div class="p-6 rounded-xl border border-white/10 bg-[#050505] flex items-center justify-between">
                <div class="text-sm font-mono text-slate-400">border-white/20</div>
                <div class="w-1/2 border-t border-white/20"></div>
            </div>
             <div class="p-6 rounded-xl border border-white/10 bg-[#050505] flex items-center justify-between">
                <div class="text-sm font-mono text-slate-400">border-emerald-500/30</div>
                <div class="w-1/2 border-t border-emerald-500/30"></div>
            </div>
        </div>
    </div>
    
    <div>
        <h3 class="text-xl font-medium text-white mb-6">Gradients & Overlays</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-8 rounded-xl border border-white/10 bg-[#050505] overflow-hidden relative min-h-[160px]">
                <div class="absolute inset-0 bg-gradient-to-b from-white/[0.03] to-transparent"></div>
                <div class="relative z-10 text-sm font-mono text-slate-400">bg-gradient-to-b from-white/[0.03] to-transparent</div>
            </div>
            <div class="p-8 rounded-xl border border-white/10 bg-[#050505] overflow-hidden relative min-h-[160px] flex items-center justify-center">
                <div class="absolute inset-0 bg-emerald-500/20 rounded-full blur-[120px] opacity-20"></div>
                 <div class="relative z-10 text-sm font-mono text-slate-400 text-center">bg-emerald-500/20<br>blur-[120px]</div>
            </div>
            <div class="p-8 rounded-xl border border-white/10 bg-[#050505] overflow-hidden relative min-h-[160px] flex items-center justify-center">
                 <div class="w-full h-8 rounded-lg animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#10b981_0%,#050505_50%,#10b981_100%)]"></div>
                 <div class="absolute bottom-4 left-4 relative z-10 text-sm font-mono text-slate-400 mt-4">Conic Gradient Ring</div>
            </div>
            <div class="p-8 rounded-xl border border-white/10 bg-[#0A0C10] overflow-hidden relative min-h-[160px] flex items-center justify-center">
                <div class="w-20 h-20 rounded-full border border-white/20 bg-gradient-to-br from-white/[0.08] to-transparent flex items-center justify-center shadow-[0_0_30px_rgba(255,255,255,0.05)]"></div>
                <div class="absolute bottom-4 left-4 z-10 text-sm font-mono text-slate-400 mt-4">Node bg-gradient-to-br</div>
            </div>
        </div>
    </div>
</section>
"""

# 3) UI Components
components_section = """
<section id="components" class="max-w-7xl mx-auto px-6 pb-32 pt-20 border-t border-white/10">
    <div class="mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">UI Components</h2>
        <p class="text-lg text-slate-400">Buttons, inputs, tags, and common elements.</p>
    </div>
    
    <div class="space-y-12">
        <!-- Primary Buttons -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Primary Button</h3>
            <div class="flex flex-col md:flex-row gap-8 items-center p-8 bg-[#050505] border border-white/10 rounded-2xl">
                <div class="flex flex-col gap-2 items-center">
                    <button class="group hover:bg-emerald-400 transition-all flex font-medium text-[#050505] bg-emerald-500 rounded-full pt-4 pr-8 pb-4 pl-8 gap-x-2 gap-y-2 items-center cursor-pointer">
                        Get started now
                        <svg aria-hidden="true" class="lucide lucide-trending-up w-4 h-4 group-hover:translate-x-1 transition-transform" data-lucide="trending-up" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M16 7h6v6"></path>
                            <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                        </svg>
                    </button>
                    <span class="text-xs text-slate-500 font-mono">Default / Hover</span>
                </div>
            </div>
        </div>

        <!-- Secondary Outline Buttons -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Secondary Outline Button</h3>
            <div class="flex flex-col md:flex-row gap-8 items-center p-8 bg-[#050505] border border-white/10 rounded-2xl">
                <div class="flex flex-col gap-2 items-center">
                    <button class="group border border-white/10 hover:border-emerald-500/50 hover:bg-white/5 text-white px-6 py-3 rounded-full font-medium transition-all flex items-center gap-2 text-sm">
                        Explore integrations
                        <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                            <path d="m9 18 6-6-6-6"></path>
                        </svg>
                    </button>
                    <span class="text-xs text-slate-500 font-mono">Default / Hover</span>
                </div>
            </div>
        </div>

        <!-- Subtle Action Button -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Subtle Action Button</h3>
            <div class="flex flex-col md:flex-row gap-8 items-center p-8 bg-[#050505] border border-white/10 rounded-2xl">
                <div class="flex flex-col gap-2 items-center">
                    <button class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-xs text-white transition-colors">
                        <svg aria-hidden="true" class="lucide lucide-user-plus w-3 h-3" data-lucide="user-plus" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                            <circle cx="9" cy="7" r="4"></circle>
                            <line x1="19" x2="19" y1="8" y2="14"></line>
                            <line x1="22" x2="16" y1="11" y2="11"></line>
                        </svg>
                        Invite users
                    </button>
                    <span class="text-xs text-slate-500 font-mono">Default / Hover</span>
                </div>
            </div>
        </div>

        <!-- Animated Border CTA -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Animated CTA</h3>
            <div class="flex flex-col md:flex-row gap-8 items-center p-8 bg-[#050505] border border-white/10 rounded-2xl">
                <div class="flex flex-col gap-2 items-center">
                    <button class="group relative inline-flex h-10 overflow-hidden rounded-lg p-[1px] focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:ring-offset-2 focus:ring-offset-slate-900">
                        <span class="absolute inset-[-1000%] animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#10b981_0%,#050505_50%,#10b981_100%)]"></span>
                        <span class="inline-flex cursor-pointer items-center justify-center transition-colors group-hover:bg-[#050505]/80 text-sm font-medium text-white bg-[#050505] w-full h-full rounded-lg pt-4 pr-8 pb-4 pl-8 backdrop-blur-3xl">Get started now</span>
                    </button>
                    <span class="text-xs text-slate-500 font-mono">Default / Hover</span>
                </div>
            </div>
        </div>

        <!-- Badges & Tags -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Badges & Tags</h3>
             <div class="flex flex-wrap gap-6 items-center p-8 bg-[#050505] border border-white/10 rounded-2xl">
                 <div class="flex flex-col gap-2 items-center">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 text-xs text-emerald-400 hover:bg-white/10 transition-colors cursor-pointer">
                        <span class="px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-medium text-[10px] uppercase tracking-wider">New</span>
                        <span>Feature Badge</span>
                    </div>
                 </div>
                 <div class="flex flex-col gap-2 items-center">
                    <span class="px-2 py-0.5 rounded-full bg-white/10 text-slate-300 text-xs">Processing</span>
                 </div>
                  <div class="flex flex-col gap-2 items-center">
                    <span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-xs">Success</span>
                 </div>
                  <div class="flex flex-col gap-2 items-center">
                     <span class="text-[10px] text-emerald-500 bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/20">+17.5%</span>
                 </div>
                  <div class="flex flex-col gap-2 items-center">
                     <div class="flex items-center gap-1.5 bg-white/10 px-2 py-1 rounded text-[10px] text-white font-medium border border-white/5">
                        <div class="w-2 h-2 rounded-full bg-emerald-500"></div>
                        <span>TOKENS</span>
                    </div>
                 </div>
             </div>
        </div>

        <!-- Inputs / Data Display (mockups from How it Works) -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Input / Data Read-Only Block</h3>
            <div class="flex flex-col gap-6 p-8 bg-[#0A0C10] border border-white/10 rounded-2xl">
                <div class="h-14 w-full max-w-sm bg-[#050505] border border-white/10 rounded-lg flex items-center justify-between px-3">
                    <span class="text-lg text-white font-medium font-mono">1,000</span>
                    <div class="flex items-center gap-1.5 bg-white/10 px-2 py-1 rounded text-[10px] text-white font-medium border border-white/5">
                        <div class="w-2 h-2 rounded-full bg-emerald-500"></div>
                        <span>TOKENS</span>
                    </div>
                </div>
                <div class="flex items-center gap-2 w-full max-w-sm bg-[#050505] border border-white/10 rounded-md px-3 py-1.5">
                    <span class="text-[10px] text-slate-500">Search anything...</span>
                    <div class="ml-auto bg-white text-[#050505] text-[9px] font-bold px-2 py-0.5 rounded">Research</div>
                </div>
            </div>
        </div>

        <!-- Cards -->
        <div>
            <h3 class="text-xl font-medium text-white mb-6">Card Container</h3>
            <div class="p-8 bg-[#050505] border border-white/10 rounded-2xl">
                 <div class="group relative rounded-3xl border border-white/10 bg-[#0A0C10] p-8 overflow-hidden hover:border-white/20 transition-all duration-300 max-w-md">
                    <div class="absolute inset-0 bg-gradient-to-b from-white/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10">
                        <h3 class="text-xl font-medium text-white mb-3 tracking-tight">Features Card</h3>
                        <p class="text-slate-400 leading-relaxed text-sm">Containers use subtle hover states and gradients over dark backgrounds.</p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</section>
"""

# 4) Layout & Spacing
layout_section = """
<section id="layout" class="max-w-7xl mx-auto px-6 pb-32 pt-20 border-t border-white/10">
    <div class="mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">Layout & Spacing</h2>
        <p class="text-lg text-slate-400">Common structural patterns used across the platform.</p>
    </div>

    <!-- Container Pattern -->
    <div class="mb-12">
        <h3 class="text-xl font-medium text-white mb-4">Main Container constraints</h3>
        <div class="w-full bg-[#050505] border border-white/10 h-32 flex items-center justify-center relative overflow-hidden">
            <div class="w-full max-w-7xl mx-auto px-6 h-full bg-emerald-500/10 border-x border-emerald-500/30 flex items-center justify-center text-emerald-400 text-sm font-mono">
                max-w-7xl mx-auto px-6
            </div>
        </div>
    </div>

    <!-- 3-Column Grid -->
    <div class="mb-12">
        <h3 class="text-xl font-medium text-white mb-4">3-Column Grid (Features)</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="h-24 rounded border border-white/10 bg-[#0A0C10] flex items-center justify-center text-xs font-mono text-slate-500">grid-cols-1 md:grid-cols-3 gap-6</div>
            <div class="h-24 rounded border border-white/10 bg-[#0A0C10] flex flex-col justify-center items-center text-xs font-mono text-slate-500">
                <span>p-8 rounded-3xl</span>
                <span>border-white/10</span>
            </div>
            <div class="h-24 rounded border border-white/10 bg-[#0A0C10] flex items-center justify-center text-xs font-mono text-slate-500">...</div>
        </div>
    </div>

    <!-- Asymmetric Grid -->
    <div class="mb-12">
        <h3 class="text-xl font-medium text-white mb-4">Asymmetric Grid (lg:grid-cols-3)</h3>
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
             <div class="h-24 lg:col-span-1 rounded border border-white/10 bg-[#0A0C10] flex items-center justify-center text-xs font-mono text-slate-500">lg:col-span-1</div>
             <div class="h-24 lg:col-span-2 rounded border border-white/10 bg-[#0A0C10] flex items-center justify-center text-xs font-mono text-slate-500">lg:col-span-2</div>
        </div>
    </div>

    <!-- Split Layout -->
    <div class="mb-12">
        <h3 class="text-xl font-medium text-white mb-4">Split Layout (Left content, Right visual)</h3>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 gap-x-16 gap-y-16 items-center">
            <div class="h-32 rounded border border-white/10 bg-[#050505] flex items-center justify-center text-xs font-mono text-slate-500">Content (col-span-1)</div>
            <div class="h-32 rounded border border-emerald-500/30 bg-emerald-500/10 flex items-center justify-center text-xs font-mono text-emerald-400">Visual (col-span-1)</div>
        </div>
    </div>

</section>
"""

# 5) Motion & Interaction
motion_section = """
<section id="motion" class="max-w-7xl mx-auto px-6 pb-32 pt-20 border-t border-white/10">
    <div class="mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">Motion & Interaction</h2>
        <p class="text-lg text-slate-400">Entrance animations, hover lifts, and glows.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Hover Glow -->
        <div class="flex flex-col gap-4">
             <div class="aspect-square rounded-3xl border border-white/10 bg-[#0A0C10] p-8 flex items-center justify-center group hover:border-emerald-500/30 transition-all duration-300">
                <div class="w-16 h-16 rounded-lg bg-emerald-500/10 border border-emerald-500/30 group-hover:bg-emerald-500/20 transition-all duration-300 group-hover:shadow-[0_0_15px_rgba(16,185,129,0.2)]"></div>
             </div>
             <div>
                <h4 class="text-sm font-medium text-white">Hover Glow</h4>
                <p class="text-xs font-mono text-slate-500 mt-1">hover:border-emerald-500/30<br>group-hover:shadow-...</p>
             </div>
        </div>

        <!-- Float Rotate -->
        <div class="flex flex-col gap-4">
             <div class="aspect-square rounded-3xl border border-white/10 bg-[#0A0C10] p-8 flex items-center justify-center group">
                 <svg class="text-slate-700 group-hover:text-emerald-500/50 transition-colors duration-500 origin-center group-hover:rotate-45" height="60" viewbox="0 0 120 120" width="60" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="60" cy="60" r="40" stroke-dasharray="20 10" />
                    <line x1="20" y1="60" x2="100" y2="60" />
                    <line x1="60" y1="20" x2="60" y2="100" />
                 </svg>
             </div>
             <div>
                <h4 class="text-sm font-medium text-white">Transform Rotate</h4>
                <p class="text-xs font-mono text-slate-500 mt-1">transition-transform duration-700<br>group-hover:rotate-45</p>
             </div>
        </div>

        <!-- Fill/Height Growth -->
        <div class="flex flex-col gap-4">
             <div class="aspect-square rounded-3xl border border-white/10 bg-[#0A0C10] p-8 flex items-end justify-center gap-3 pb-8 group">
                <div class="w-6 bg-white/5 border border-white/10 rounded-t-lg h-8 group-hover:h-16 transition-all duration-500 ease-out delay-75"></div>
                <div class="w-6 bg-emerald-500/20 border border-emerald-500/30 rounded-t-lg h-12 group-hover:h-24 transition-all duration-500 ease-out shadow-[0_0_20px_rgba(16,185,129,0.2)]"></div>
                <div class="w-6 bg-white/5 border border-white/10 rounded-t-lg h-10 group-hover:h-20 transition-all duration-500 ease-out delay-150"></div>
             </div>
             <div>
                <h4 class="text-sm font-medium text-white">Animated Bars</h4>
                <p class="text-xs font-mono text-slate-500 mt-1">transition-all duration-500 ease-out<br>delay-75</p>
             </div>
        </div>

        <!-- Marquee Infinite -->
        <div class="flex flex-col gap-4">
             <div class="aspect-[2/1] rounded-3xl border border-white/10 bg-[#0A0C10] p-4 flex items-center justify-center overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_10%,black_90%,transparent)]">
                 <div class="flex gap-4 w-max animate-[marquee-left_10s_linear_infinite]">
                    <div class="px-4 py-2 border border-white/10 bg-white/5 rounded">Card 1</div>
                    <div class="px-4 py-2 border border-white/10 bg-white/5 rounded">Card 2</div>
                    <div class="px-4 py-2 border border-white/10 bg-white/5 rounded">Card 3</div>
                    <div class="px-4 py-2 border border-white/10 bg-white/5 rounded">Card 1</div>
                    <div class="px-4 py-2 border border-white/10 bg-white/5 rounded">Card 2</div>
                    <div class="px-4 py-2 border border-white/10 bg-white/5 rounded">Card 3</div>
                 </div>
                 <style>
                    @keyframes marquee-left { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
                 </style>
             </div>
             <div>
                <h4 class="text-sm font-medium text-white">Continuous Marquee</h4>
                <p class="text-xs font-mono text-slate-500 mt-1">Infinite linear scroll animation</p>
             </div>
        </div>

        <!-- Fade-in Page -->
        <div class="flex flex-col gap-4">
             <div class="aspect-square rounded-3xl border border-white/10 bg-[#0A0C10] p-8 flex items-center justify-center group">
                 <div class="px-6 py-4 bg-white/5 border border-white/10 rounded-lg opacity-0 group-hover:opacity-100 transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 ease-in-out">
                    Fade In
                 </div>
             </div>
             <div>
                <h4 class="text-sm font-medium text-white">Entrance / slideUp</h4>
                <p class="text-xs font-mono text-slate-500 mt-1">opacity: 1; transform: translateY(0);</p>
             </div>
        </div>

    </div>
</section>
"""

# 6) Icons
icons_section = """
<section id="icons" class="max-w-7xl mx-auto px-6 pb-32 pt-20 border-t border-white/10">
    <div class="mb-16">
        <h2 class="md:text-5xl text-3xl font-medium text-white tracking-tight mb-4">Icons</h2>
        <p class="text-lg text-slate-400">Lucide icons used with minimal strokes and clear intent.</p>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">
        <!-- Icon 1 -->
        <div class="flex flex-col gap-3 items-center justify-center p-6 bg-[#050505] border border-white/10 rounded-2xl text-slate-400">
            <svg aria-hidden="true" class="lucide lucide-triangle w-6 h-6 rotate-180 fill-current" data-lucide="triangle" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.73 4a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path>
            </svg>
            <span class="text-[10px] font-mono">Triangle Filled</span>
        </div>
        
        <!-- Icon 2 -->
        <div class="flex flex-col gap-3 items-center justify-center p-6 bg-[#050505] border border-white/10 rounded-2xl text-slate-400 hover:text-emerald-400 transition-colors">
            <svg aria-hidden="true" class="lucide lucide-trending-up w-6 h-6" data-lucide="trending-up" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 7h6v6"></path>
                <path d="m22 7-8.5 8.5-5-5L2 17"></path>
            </svg>
            <span class="text-[10px] font-mono">Trending Up</span>
        </div>

        <!-- Icon 3 -->
        <div class="flex flex-col gap-3 items-center justify-center p-6 bg-[#050505] border border-white/10 rounded-2xl text-slate-400 hover:text-emerald-400 transition-colors">
            <svg aria-hidden="true" class="lucide lucide-user-plus w-6 h-6" data-lucide="user-plus" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <line x1="19" x2="19" y1="8" y2="14"></line>
                <line x1="22" x2="16" y1="11" y2="11"></line>
            </svg>
            <span class="text-[10px] font-mono">User Plus</span>
        </div>

        <!-- Icon 4 -->
         <div class="flex flex-col gap-3 items-center justify-center p-6 bg-[#050505] border border-white/10 rounded-2xl text-slate-400 hover:text-emerald-400 transition-colors">
            <svg class="w-6 h-6" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="m9 18 6-6-6-6"></path>
            </svg>
            <span class="text-[10px] font-mono">Chevron Right</span>
        </div>

         <!-- Icon 5 -->
         <div class="flex flex-col gap-3 items-center justify-center p-6 bg-[#050505] border border-white/10 rounded-2xl text-slate-400 hover:text-emerald-400 transition-colors">
            <svg class="w-6 h-6" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2a10 10 0 1 0 10 10H12V2z"></path>
                <path d="M12 2a10 10 0 0 1 10 10h-10V2z"></path>
                <path d="m9 12 5.09-5.09L12 19l5.09-5.09"></path>
            </svg>
            <span class="text-[10px] font-mono">Globe Outline</span>
        </div>

    </div>
</section>
"""

# Assemble
body_content = f"{nav_modified}\n<main class=\"pt-20 min-h-screen relative overflow-hidden\">\n{hero_content}\n{typography_section}\n{colors_section}\n{components_section}\n{layout_section}\n{motion_section}\n{icons_section}\n</main>"

final_html = f"<!DOCTYPE html>\n<html class=\"scroll-smooth\" lang=\"en\">\n{head_content}\n{body_tag}\n{body_content}\n</body>\n</html>"

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Created design-system.html successfully.")
