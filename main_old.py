<!DOCTYPE html>
<html lang="ko" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SonicLog - 아티스트 포트폴리오 & 협업 스페이스</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Pretendard', 'sans-serif'],
                    },
                    colors: {
                        dark: {
                            950: '#090d16',
                            900: '#0f172a',
                            800: '#1e293b',
                            700: '#334155',
                        },
                        accent: {
                            purple: '#8b5cf6',
                            indigo: '#6366f1',
                            cyan: '#06b6d4',
                            pink: '#ec4899',
                        }
                    },
                    animation: {
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                        'float': 'float 4s ease-in-out infinite',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-6px)' },
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body {
            font-family: 'Pretendard', sans-serif;
            background-color: #090d16;
            color: #f8fafc;
        }
        /* Custom glassmorphism & scrollbar */
        .glass-panel {
            background: rgba(30, 41, 59, 0.70);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-card {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #090d16;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-accent-purple selection:text-white">

    <header class="sticky top-0 z-50 glass-panel border-b border-slate-800/80 px-4 lg:px-8 py-3.5 transition-all">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <!-- Brand Logo -->
            <div class="flex items-center gap-3 w-full sm:w-auto justify-between sm:justify-start">
                <div class="flex items-center gap-2.5 cursor-pointer" onclick="switchView('portfolio')">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-accent-purple via-accent-indigo to-accent-cyan flex items-center justify-center shadow-lg shadow-purple-500/20">
                        <i class="fa-solid fa-waveform-lines text-white text-lg"></i>
                    </div>
                    <div>
                        <span class="text-lg font-bold tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">SonicLog</span>
                        <span class="block text-[10px] text-accent-cyan font-medium tracking-widest uppercase">Creator & Collab OS</span>
                    </div>
                </div>
                <!-- Mobile view indicator badge -->
                <div class="sm:hidden px-2.5 py-1 rounded-full bg-slate-800 border border-slate-700 text-xs text-slate-300" id="mobileViewIndicator">
                    포트폴리오
                </div>
            </div>

            <!-- View Switcher Tabs -->
            <nav class="flex items-center bg-slate-900/90 p-1.5 rounded-2xl border border-slate-800 shadow-inner w-full sm:w-auto overflow-x-auto">
                <button onclick="switchView('portfolio')" id="nav-portfolio" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-2 bg-gradient-to-r from-accent-purple to-accent-indigo text-white shadow-md">
                    <i class="fa-solid fa-address-card"></i>
                    <span>[1] 아티스트 포트폴리오</span>
                </button>
                <button onclick="switchView('workspace')" id="nav-workspace" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs sm:text-sm font-medium text-slate-400 hover:text-white transition-all flex items-center justify-center gap-2">
                    <i class="fa-solid fa-sliders"></i>
                    <span>[2] 협업 스페이스</span>
                </button>
                <button onclick="switchView('upload')" id="nav-upload" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs sm:text-sm font-medium text-slate-400 hover:text-white transition-all flex items-center justify-center gap-2">
                    <i class="fa-solid fa-cloud-arrow-up"></i>
                    <span>[3] 곡 업로드 & 갱신</span>
                </button>
            </nav>

            <!-- Quick Action / Profile Switcher -->
            <div class="hidden lg:flex items-center gap-3">
                <div class="flex items-center gap-2 bg-slate-900/80 px-3 py-1.5 rounded-full border border-slate-800">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="text-xs text-slate-300 font-medium">EXEL (Pro Tier)</span>
                </div>
                <button onclick="openCollabModal()" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold border border-slate-700 text-slate-200 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-paper-plane text-accent-cyan"></i>
                    <span>협업 문의</span>
                </button>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">

        <!-- ================= VIEW 1: PUBLIC ARTIST PORTFOLIO (Link-in-Bio View) ================= -->
        <section id="view-portfolio" class="view-section space-y-8 animate-fade-in">
            <!-- Artist Bio Hero Header -->
            <div class="glass-panel rounded-3xl p-6 sm:p-10 relative overflow-hidden">
                <div class="absolute -right-20 -top-20 w-80 h-80 bg-accent-purple/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -left-20 -bottom-20 w-80 h-80 bg-accent-cyan/10 rounded-full blur-3xl pointer-events-none"></div>

                <div class="relative z-10 flex flex-col md:flex-row items-center gap-6 sm:gap-8 text-center md:text-left">
                    <div class="relative group">
                        <div class="w-28 h-28 sm:w-36 sm:h-36 rounded-2xl overflow-hidden border-2 border-accent-purple/50 shadow-2xl shadow-purple-900/40">
                            <img src="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400&auto=format&fit=crop&q=80" alt="Artist Profile" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        </div>
                        <span class="absolute bottom-2 right-2 bg-emerald-500 text-slate-950 font-bold text-[10px] px-2 py-0.5 rounded-full shadow-md flex items-center gap-1">
                            <i class="fa-solid fa-circle text-[6px]"></i> 작업가능
                        </span>
                    </div>

                    <div class="flex-1 space-y-3">
                        <div class="flex flex-wrap items-center justify-center md:justify-start gap-2">
                            <h1 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white">EXEL (엑셀)</h1>
                            <span class="bg-accent-purple/20 text-accent-purple border border-accent-purple/30 text-xs px-2.5 py-0.5 rounded-full font-semibold">Verified Producer</span>
                        </div>
                        <p class="text-slate-300 text-sm sm:text-base max-w-2xl font-light leading-relaxed">
                            Hyperpop & Alternative R&B Producer / Sound Designer. 서울과 LA를 오가며 감정적인 사운드스케이프를 만듭니다. 다운로드 없는 고음질 스트리밍과 투명한 크레딧 DB를 공유합니다.
                        </p>
                        <!-- Tags & Social Links -->
                        <div class="flex flex-wrap items-center justify-center md:justify-start gap-2 pt-1">
                            <span class="text-xs bg-slate-800 text-slate-300 px-3 py-1 rounded-xl border border-slate-700/60">#Hyperpop</span>
                            <span class="text-xs bg-slate-800 text-slate-300 px-3 py-1 rounded-xl border border-slate-700/60">#AlternativeRnB</span>
                            <span class="text-xs bg-slate-800 text-slate-300 px-3 py-1 rounded-xl border border-slate-700/60">#SoundDesign</span>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex flex-row md:flex-col gap-3 w-full md:w-auto">
                        <button onclick="openCollabModal()" class="flex-1 md:flex-initial px-6 py-3 rounded-2xl bg-gradient-to-r from-accent-purple to-accent-indigo hover:opacity-95 text-white font-semibold text-sm shadow-lg shadow-purple-600/30 transition flex items-center justify-center gap-2">
                            <i class="fa-solid fa-handshake"></i>
                            <span>협업 / 외주 문의하기</span>
                        </button>
                        <a href="#portfolio-tracks" class="flex-1 md:flex-initial px-6 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-sm border border-slate-700 transition flex items-center justify-center gap-2">
                            <i class="fa-solid fa-headphones"></i>
                            <span>대표 트랙 재생</span>
                        </a>
                    </div>
                </div>
            </div>

            <div id="portfolio-tracks" class="space-y-4">
                <div class="flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-2 text-white">
                        <i class="fa-solid fa-compact-disc text-accent-purple animate-spin-slow"></i>
                        <span>포트폴리오 대표 트랙 (In-Page Stream)</span>
                    </h2>
                    <span class="text-xs text-slate-400">다운로드 없이 링크 안에서 즉시 재생</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="trackListContainer">
                    <!-- Track Card 1 -->
                    <div class="glass-card rounded-2xl p-5 hover:border-slate-700 transition space-y-4">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-600 to-pink-600 flex items-center justify-center text-white font-bold shadow-md">
                                    <i class="fa-solid fa-music"></i>
                                </div>
                                <div>
                                    <h3 class="font-bold text-white text-base">Neon Rain (Feat. Sumin)</h3>
                                    <p class="text-xs text-slate-400">Single • Released 2026.03</p>
                                </div>
                            </div>
                            <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2.5 py-1 rounded-full font-medium">Official Master</span>
                        </div>

                        <!-- Waveform Mockup & Player -->
                        <div class="space-y-2 bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/80">
                            <div class="flex items-center justify-between text-xs text-slate-400">
                                <div class="flex items-center gap-2">
                                    <button onclick="togglePlay(this, 'track1')" class="w-9 h-9 rounded-full bg-accent-purple hover:bg-accent-indigo text-white flex items-center justify-center transition shadow-md play-btn">
                                        <i class="fa-solid fa-play ml-0.5"></i>
                                    </button>
                                    <span class="font-mono text-slate-200 time-display">0:00 / 2:45</span>
                                </div>
                                <!-- Version Selector -->
                                <select onchange="changeVersion('track1', this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-300 rounded-lg px-2.5 py-1 outline-none">
                                    <option value="final">Final Master (v3)</option>
                                    <option value="mix">Rough Mix (v2)</option>
                                    <option value="demo">Demo Sketch (v1)</option>
                                </select>
                            </div>
                            <!-- Visual Waveform representation -->
                            <div class="h-10 flex items-center gap-0.5 cursor-pointer waveform-bar px-1" onclick="seekAudio(event, this)">
                                <!-- Generated dummy waveform bars -->
                                <div class="w-1 bg-accent-purple/60 hover:bg-accent-cyan h-3/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/80 hover:bg-accent-cyan h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple hover:bg-accent-cyan h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/70 hover:bg-accent-cyan h-2/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/90 hover:bg-accent-cyan h-3/4 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/60 hover:bg-accent-cyan h-1/2 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/80 hover:bg-accent-cyan h-5/6 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple hover:bg-accent-cyan h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/50 hover:bg-accent-cyan h-3/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/90 hover:bg-accent-cyan h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/70 hover:bg-accent-cyan h-2/3 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple hover:bg-accent-cyan h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/80 hover:bg-accent-cyan h-5/6 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/60 hover:bg-accent-cyan h-3/4 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/40 hover:bg-accent-cyan h-1/2 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/80 hover:bg-accent-cyan h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple hover:bg-accent-cyan h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/70 hover:bg-accent-cyan h-3/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/50 hover:bg-accent-cyan h-2/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/90 hover:bg-accent-cyan h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple hover:bg-accent-cyan h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/70 hover:bg-accent-cyan h-3/4 rounded-full transition"></div>
                                <div class="w-1 bg-accent-purple/60 hover:bg-accent-cyan h-1/2 rounded-full transition"></div>
                            </div>
                        </div>

                        <div class="flex items-center justify-between text-xs text-slate-400 pt-1">
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-users text-accent-cyan"></i> 참여 크레딧: 프로듀서, 작곡, 믹스</span>
                            <span class="text-accent-purple font-medium">상호검증 완료 ✓</span>
                        </div>
                    </div>

                    <!-- Track Card 2 -->
                    <div class="glass-card rounded-2xl p-5 hover:border-slate-700 transition space-y-4">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-600 to-cyan-600 flex items-center justify-center text-white font-bold shadow-md">
                                    <i class="fa-solid fa-music"></i>
                                </div>
                                <div>
                                    <h3 class="font-bold text-white text-base">Cyber Blue (Remix)</h3>
                                    <p class="text-xs text-slate-400">EP Track • Released 2026.01</p>
                                </div>
                            </div>
                            <span class="text-xs bg-accent-purple/10 text-accent-purple border border-accent-purple/20 px-2.5 py-1 rounded-full font-medium">Collab Track</span>
                        </div>

                        <!-- Waveform Mockup & Player -->
                        <div class="space-y-2 bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/80">
                            <div class="flex items-center justify-between text-xs text-slate-400">
                                <div class="flex items-center gap-2">
                                    <button onclick="togglePlay(this, 'track2')" class="w-9 h-9 rounded-full bg-accent-purple hover:bg-accent-indigo text-white flex items-center justify-center transition shadow-md play-btn">
                                        <i class="fa-solid fa-play ml-0.5"></i>
                                    </button>
                                    <span class="font-mono text-slate-200 time-display">0:00 / 3:12</span>
                                </div>
                                <select onchange="changeVersion('track2', this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-300 rounded-lg px-2.5 py-1 outline-none">
                                    <option value="final">Final Master (v2)</option>
                                    <option value="demo">Demo (v1)</option>
                                </select>
                            </div>
                            <div class="h-10 flex items-center gap-0.5 cursor-pointer waveform-bar px-1" onclick="seekAudio(event, this)">
                                <div class="w-1 bg-accent-cyan/60 hover:bg-accent-purple h-2/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/80 hover:bg-accent-purple h-3/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan hover:bg-accent-purple h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/70 hover:bg-accent-purple h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/90 hover:bg-accent-purple h-3/4 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/60 hover:bg-accent-purple h-1/2 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/80 hover:bg-accent-purple h-5/6 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan hover:bg-accent-purple h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/50 hover:bg-accent-purple h-3/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/90 hover:bg-accent-purple h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/70 hover:bg-accent-purple h-2/3 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan hover:bg-accent-purple h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/80 hover:bg-accent-purple h-5/6 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/60 hover:bg-accent-purple h-3/4 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/40 hover:bg-accent-purple h-1/2 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/80 hover:bg-accent-purple h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan hover:bg-accent-purple h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/70 hover:bg-accent-purple h-3/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/50 hover:bg-accent-purple h-2/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/90 hover:bg-accent-purple h-4/5 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan hover:bg-accent-purple h-full rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/70 hover:bg-accent-purple h-3/4 rounded-full transition"></div>
                                <div class="w-1 bg-accent-cyan/60 hover:bg-accent-purple h-1/2 rounded-full transition"></div>
                            </div>
                        </div>

                        <div class="flex items-center justify-between text-xs text-slate-400 pt-1">
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-users text-accent-cyan"></i> 참여 크레딧: 리믹스 프로듀서, 마스터링</span>
                            <span class="text-accent-purple font-medium">상호검증 완료 ✓</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Verified Credits DB -->
                <div class="lg:col-span-1 glass-panel rounded-3xl p-6 space-y-5">
                    <div class="flex items-center justify-between">
                        <h3 class="font-bold text-base text-white flex items-center gap-2">
                            <i class="fa-solid fa-shield-check text-emerald-400"></i>
                            <span>공식 검증 크레딧 DB</span>
                        </h3>
                        <span class="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded-lg">4건</span>
                    </div>

                    <div class="space-y-3">
                        <div class="p-3.5 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                            <div>
                                <h4 class="font-semibold text-sm text-white">Neon Rain</h4>
                                <p class="text-xs text-slate-400">Producer & Co-Writer</p>
                            </div>
                            <span class="text-[10px] bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2.5 py-1 rounded-full font-medium">검증됨 ✓</span>
                        </div>

                        <div class="p-3.5 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                            <div>
                                <h4 class="font-semibold text-sm text-white">Cyber Blue</h4>
                                <p class="text-xs text-slate-400">Mixing & Mastering</p>
                            </div>
                            <span class="text-[10px] bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2.5 py-1 rounded-full font-medium">검증됨 ✓</span>
                        </div>

                        <div class="p-3.5 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                            <div>
                                <h4 class="font-semibold text-sm text-white">Lost in Seoul (OST)</h4>
                                <p class="text-xs text-slate-400">Sound Design</p>
                            </div>
                            <span class="text-[10px] bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2.5 py-1 rounded-full font-medium">검증됨 ✓</span>
                        </div>
                    </div>
                </div>

                <!-- Process Stories & References (Qualitative Diary) -->
                <div class="lg:col-span-2 glass-panel rounded-3xl p-6 space-y-5">
                    <div class="flex items-center justify-between">
                        <h3 class="font-bold text-base text-white flex items-center gap-2">
                            <i class="fa-solid fa-book-open text-accent-cyan"></i>
                            <span>작업 과정 스토리 & 레퍼런스 아카이브</span>
                        </h3>
                        <span class="text-xs text-slate-400">비하인드 노트 & 샘플링 소스</span>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div class="glass-card rounded-2xl p-4 space-y-3 border border-slate-800">
                            <div class="flex items-center justify-between text-xs text-accent-cyan font-medium">
                                <span>#Diary Note</span>
                                <span class="text-slate-400">2026.03.10</span>
                            </div>
                            <h4 class="font-semibold text-sm text-white">신디사이저 앰비언스 레이어링 비하인드</h4>
                            <p class="text-xs text-slate-300 leading-relaxed font-light">
                                "Neon Rain 곡의 후반부 비 오는 소리는 홍대 골목에서 직접 채집한 필드 녹음과 Moog 서브 베이스를 겹쳐서 몽환적인 질감을 연출했습니다."
                            </p>
                        </div>

                        <div class="glass-card rounded-2xl p-4 space-y-3 border border-slate-800">
                            <div class="flex items-center justify-between text-xs text-accent-purple font-medium">
                                <span>#Reference Mood</span>
                                <span class="text-slate-400">2026.01.20</span>
                            </div>
                            <h4 class="font-semibold text-sm text-white">90년대 로파이 감성 샘플 소스</h4>
                            <p class="text-xs text-slate-300 leading-relaxed font-light">
                                "8비트 아날로그 패드 사운드를 참고하여 레트로하면서도 미래지향적인 톤을 잡기 위해 사용한 메인 레퍼런스 보드입니다."
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ================= VIEW 2: INTERNAL WORKSPACE VIEW (Collab & Version Control) ================= -->
        <section id="view-workspace" class="view-section hidden space-y-6 animate-fade-in">
            <!-- Workspace Header / Project Selector -->
            <div class="glass-panel rounded-3xl p-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-accent-indigo to-accent-cyan flex items-center justify-center text-white text-lg shadow-lg">
                        <i class="fa-solid fa-sliders"></i>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <h2 class="text-xl font-bold text-white">Neon Rain (Album Project)</h2>
                            <span class="bg-purple-500/10 text-accent-purple text-xs px-2.5 py-0.5 rounded-full font-semibold border border-purple-500/20">실시간 협업 중</span>
                        </div>
                        <p class="text-xs text-slate-400 mt-0.5">참여 멤버: EXEL (Lead), Sumin (Vocal), Jinu (Mixing)</p>
                    </div>
                </div>

                <!-- Project Switcher & Actions -->
                <div class="flex items-center gap-2.5 w-full md:w-auto">
                    <select class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-xl px-3 py-2.5 outline-none font-medium">
                        <option>프로젝트: Neon Rain</option>
                        <option>프로젝트: Cyber Blue Remix</option>
                        <option>프로젝트: Lost in Seoul OST</option>
                    </select>
                    <button onclick="showToast('새로운 작업 공간이 생성되었습니다.')" class="px-4 py-2.5 rounded-xl bg-accent-purple hover:bg-accent-indigo text-white text-xs font-semibold shadow-md transition flex items-center gap-1.5">
                        <i class="fa-solid fa-plus"></i>
                        <span>새 프로젝트</span>
                    </button>
                </div>
            </div>

            <!-- Main Workspace Grid: Version Control & SoundCloud Timestamp Comments -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Left 2 Cols: Version Control & Audio Waveform + Timestamped Comments -->
                <div class="lg:col-span-2 space-y-6">
                    <!-- Version Control Timeline -->
                    <div class="glass-panel rounded-3xl p-6 space-y-4">
                        <div class="flex items-center justify-between">
                            <h3 class="font-bold text-base text-white flex items-center gap-2">
                                <i class="fa-solid fa-code-branch text-accent-cyan"></i>
                                <span>트랙 버전 관리 (Version Control)</span>
                            </h3>
                            <span class="text-xs text-slate-400">클라우드 실시간 동기화</span>
                        </div>

                        <div class="space-y-3">
                            <div class="p-3.5 rounded-2xl bg-slate-900/90 border border-accent-purple/40 flex items-center justify-between shadow-md">
                                <div class="flex items-center gap-3">
                                    <span class="w-8 h-8 rounded-xl bg-accent-purple/20 text-accent-purple font-bold text-xs flex items-center justify-center">v3</span>
                                    <div>
                                        <h4 class="font-semibold text-sm text-white">Neon_Rain_Final_Master.mp3</h4>
                                        <p class="text-[11px] text-slate-400">Jinu 믹스 마스터 완료 • 2시간 전 업로드</p>
                                    </div>
                                </div>
                                <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-3 py-1 rounded-full font-medium">현재 활성 버전</span>
                            </div>

                            <div class="p-3.5 rounded-2xl bg-slate-900/50 border border-slate-800 flex items-center justify-between opacity-80 hover:opacity-100 transition">
                                <div class="flex items-center gap-3">
                                    <span class="w-8 h-8 rounded-xl bg-slate-800 text-slate-400 font-bold text-xs flex items-center justify-center">v2</span>
                                    <div>
                                        <h4 class="font-semibold text-sm text-slate-300">Neon_Rain_Rough_Mix_v2.mp3</h4>
                                        <p class="text-[11px] text-slate-500">EXEL 보컬 튜닝 수정 • 어제</p>
                                    </div>
                                </div>
                                <button onclick="showToast('v2 버전으로 오디오 프리뷰가 전환되었습니다.')" class="text-xs text-accent-cyan hover:underline font-medium">전환하기</button>
                            </div>

                            <div class="p-3.5 rounded-2xl bg-slate-900/50 border border-slate-800 flex items-center justify-between opacity-80 hover:opacity-100 transition">
                                <div class="flex items-center gap-3">
                                    <span class="w-8 h-8 rounded-xl bg-slate-800 text-slate-400 font-bold text-xs flex items-center justify-center">v1</span>
                                    <div>
                                        <h4 class="font-semibold text-sm text-slate-300">Neon_Rain_Demo_Sketch.mp3</h4>
                                        <p class="text-[11px] text-slate-500">초기 아이디어 스케치 • 3일 전</p>
                                    </div>
                                </div>
                                <button onclick="showToast('v1 버전으로 오디오 프리뷰가 전환되었습니다.')" class="text-xs text-accent-cyan hover:underline font-medium">전환하기</button>
                            </div>
                        </div>
                    </div>

                    <!-- SoundCloud Style Timestamp Comment Feed -->
                    <div class="glass-panel rounded-3xl p-6 space-y-4">
                        <div class="flex items-center justify-between">
                            <h3 class="font-bold text-base text-white flex items-center gap-2">
                                <i class="fa-solid fa-comments text-accent-purple"></i>
                                <span>구간별 코멘트 피드 (SoundCloud Style)</span>
                            </h3>
                            <span class="text-xs text-slate-400">타임스탬프 실시간 피드백</span>
                        </div>

                        <!-- Comment input box -->
                        <div class="flex gap-2 bg-slate-900/80 p-2 rounded-2xl border border-slate-800">
                            <input type="text" id="workspaceCommentInput" placeholder="1:23 구간에 남길 피드백을 입력하세요... (예: 베이스라인 살짝 키우면 좋을듯)" class="flex-1 bg-transparent border-none text-xs text-white px-3 py-2 outline-none placeholder-slate-500">
                            <button onclick="addWorkspaceComment()" class="px-4 py-2 bg-accent-purple hover:bg-accent-indigo text-white rounded-xl text-xs font-semibold transition">
                                코멘트 남기기
                            </button>
                        </div>

                        <!-- Comments list -->
                        <div class="space-y-3 pt-2" id="workspaceCommentsList">
                            <div class="p-3.5 rounded-2xl bg-slate-900/60 border border-slate-800 flex items-start gap-3">
                                <div class="w-8 h-8 rounded-full bg-accent-cyan/20 text-accent-cyan font-bold text-xs flex items-center justify-center shrink-0">S</div>
                                <div class="flex-1">
                                    <div class="flex items-center justify-between">
                                        <span class="font-semibold text-xs text-white">Sumin (Vocal)</span>
                                        <span class="font-mono text-xs bg-slate-800 text-accent-cyan px-2 py-0.5 rounded-md">1:24</span>
                                    </div>
                                    <p class="text-xs text-slate-300 mt-1 font-light">"이 부분 보컬 리버브 양을 살짝 줄이고 드라이하게 가져가면 코러스가 더 살 것 같아요!"</p>
                                </div>
                            </div>

                            <div class="p-3.5 rounded-2xl bg-slate-900/60 border border-slate-800 flex items-start gap-3">
                                <div class="w-8 h-8 rounded-full bg-accent-purple/20 text-accent-purple font-bold text-xs flex items-center justify-center shrink-0">J</div>
                                <div class="flex-1">
                                    <div class="flex items-center justify-between">
                                        <span class="font-semibold text-xs text-white">Jinu (Mastering)</span>
                                        <span class="font-mono text-xs bg-slate-800 text-accent-purple px-2 py-0.5 rounded-md">2:05</span>
                                    </div>
                                    <p class="text-xs text-slate-300 mt-1 font-light">"아웃트로 스네어 테일 깔끔하게 정리했습니다. 최종 마스터 확인 부탁해요."</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Col: Reference Board & Credit Sign-off Panel -->
                <div class="space-y-6">
                    <!-- Reference Board (Moodboard / Samples) -->
                    <div class="glass-panel rounded-3xl p-6 space-y-4">
                        <div class="flex items-center justify-between">
                            <h3 class="font-bold text-base text-white flex items-center gap-2">
                                <i class="fa-solid fa-thumbtack text-accent-pink"></i>
                                <span>참조 레퍼런스 보드</span>
                            </h3>
                            <button onclick="showToast('레퍼런스 파일이 추가되었습니다.')" class="text-xs text-accent-cyan hover:underline font-medium">+ 추가</button>
                        </div>

                        <div class="space-y-3">
                            <div class="p-3 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center gap-3">
                                <div class="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-400 flex items-center justify-center">
                                    <i class="fa-solid fa-image"></i>
                                </div>
                                <div class="flex-1 min-w-0">
                                    <h4 class="font-semibold text-xs text-white truncate">Bladee_Style_Synth_Mood.png</h4>
                                    <p class="text-[10px] text-slate-400">비주얼 레퍼런스</p>
                                </div>
                            </div>

                            <div class="p-3 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center gap-3">
                                <div class="w-10 h-10 rounded-xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center">
                                    <i class="fa-solid fa-volume-high"></i>
                                </div>
                                <div class="flex-1 min-w-0">
                                    <h4 class="font-semibold text-xs text-white truncate">808_Bass_Reference_Loop.wav</h4>
                                    <p class="text-[10px] text-slate-400">오디오 샘플 레퍼런스</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Credit Sign-off Panel (Mutual Verification) -->
                    <div class="glass-panel rounded-3xl p-6 space-y-4">
                        <div class="flex items-center justify-between">
                            <h3 class="font-bold text-base text-white flex items-center gap-2">
                                <i class="fa-solid fa-file-signature text-emerald-400"></i>
                                <span>크레딧 상호 동의 (Sign-off)</span>
                            </h3>
                            <span class="text-xs bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded-md">2/3 동의</span>
                        </div>
                        <p class="text-xs text-slate-400 leading-relaxed font-light">
                            곡 완성 후 참여자들의 상호 검증이 완료되면 각 아티스트의 공식 포트폴리오 크레딧 DB에 자동 누적됩니다.
                        </p>

                        <div class="space-y-2 pt-1">
                            <div class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/90 text-xs">
                                <span class="text-white font-medium">EXEL (Prod/Song)</span>
                                <span class="text-emerald-400 font-semibold"><i class="fa-solid fa-check"></i> 동의 완료</span>
                            </div>
                            <div class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/90 text-xs">
                                <span class="text-white font-medium">Sumin (Vocal/Feat)</span>
                                <span class="text-emerald-400 font-semibold"><i class="fa-solid fa-check"></i> 동의 완료</span>
                            </div>
                            <div class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/90 text-xs">
                                <span class="text-white font-medium">Jinu (Mastering)</span>
                                <span class="text-amber-400 font-semibold"><i class="fa-solid fa-clock"></i> 대기 중...</span>
                            </div>
                        </div>

                        <button onclick="showToast('크레딧 최종 확정 및 포트폴리오 동기화 요청이 전송되었습니다!')" class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:opacity-95 text-white font-semibold text-xs shadow-lg shadow-emerald-600/30 transition">
                            크레딧 최종 확정 및 포트폴리오에 반영하기
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ================= VIEW 3: UPLOAD & PORTFOLIO SYNC BUILDER ================= -->
        <section id="view-upload" class="view-section hidden space-y-6 animate-fade-in max-w-4xl mx-auto">
            <div class="glass-panel rounded-3xl p-6 sm:p-10 space-y-8">
                <div class="text-center space-y-2">
                    <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-accent-purple via-accent-indigo to-accent-cyan mx-auto flex items-center justify-center text-white text-2xl shadow-xl shadow-purple-500/20">
                        <i class="fa-solid fa-cloud-arrow-up"></i>
                    </div>
                    <h2 class="text-2xl font-bold text-white">새로운 곡 업로드 및 포트폴리오 갱신</h2>
                    <p class="text-xs sm:text-sm text-slate-400 max-w-lg mx-auto">
                        창작물을 업로드하고 정성적인 과정 메모와 레퍼런스를 첨부하면, 인스타그램 바이오 링크 및 아티스트 포트폴리오에 즉시 시각화되어 반영됩니다.
                    </p>
                </div>

                <form onsubmit="handleUploadSync(event)" class="space-y-6">
                    <!-- Track Title & Genre -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div class="space-y-2">
                            <label class="text-xs font-semibold text-slate-300">트랙 제목 (Track Title)</label>
                            <input type="text" required placeholder="예: Cybernetic Dream" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-4 py-3 text-sm text-white outline-none focus:border-accent-purple transition">
                        </div>
                        <div class="space-y-2">
                            <label class="text-xs font-semibold text-slate-300">장르 / 태그</label>
                            <input type="text" required placeholder="예: Hyperpop, Synthwave" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-4 py-3 text-sm text-white outline-none focus:border-accent-purple transition">
                        </div>
                    </div>

                    <!-- Audio File Drag & Drop Zone -->
                    <div class="space-y-2">
                        <label class="text-xs font-semibold text-slate-300">오디오 파일 업로드 (MP3 / WAV)</label>
                        <div class="border-2 border-dashed border-slate-700 hover:border-accent-purple rounded-2xl p-8 text-center bg-slate-900/50 cursor-pointer transition group">
                            <div class="w-12 h-12 rounded-full bg-slate-800 text-accent-purple flex items-center justify-center mx-auto mb-3 group-hover:scale-110 transition">
                                <i class="fa-solid fa-file-audio text-xl"></i>
                            </div>
                            <p class="text-sm font-medium text-white">오디오 파일을 여기에 드래그하거나 클릭하여 업로드</p>
                            <p class="text-xs text-slate-400 mt-1">다운로드 없이 링크 내에서 고음질로 재생됩니다 (최대 50MB)</p>
                        </div>
                    </div>

                    <!-- Process Story & Behind-the-scenes Notes -->
                    <div class="space-y-2">
                        <label class="text-xs font-semibold text-slate-300">과정적 스토리 및 비하인드 노트 (Process Story)</label>
                        <textarea rows="4" placeholder="작업 과정에서의 고민, 샘플링 출처, 혹은 리스너들에게 들려주고 싶은 제작 비하인드를 적어보세요..." class="w-full bg-slate-900 border border-slate-700/80 rounded-xl p-4 text-sm text-white outline-none focus:border-accent-purple transition resize-none"></textarea>
                    </div>

                    <!-- Portfolio Link Sync Toggle -->
                    <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-xl bg-emerald-500/10 text-emerald-400 flex items-center justify-center">
                                <i class="fa-solid fa-link"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-sm text-white">인스타그램 포트폴리오 링크 즉시 동기화</h4>
                                <p class="text-xs text-slate-400">업로드 완료 즉시 퍼블릭 바이오 페이지에 플레이어 카드가 생성됩니다.</p>
                            </div>
                        </div>
                        <input type="checkbox" checked class="w-5 h-5 accent-accent-purple rounded cursor-pointer">
                    </div>

                    <!-- Submit Button -->
                    <button type="submit" class="w-full py-4 rounded-2xl bg-gradient-to-r from-accent-purple via-accent-indigo to-accent-cyan text-white font-bold text-sm shadow-xl shadow-purple-600/30 hover:opacity-95 transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-rocket"></i>
                        <span>업로드 및 포트폴리오에 즉시 반영하기</span>
                    </button>
                </form>
            </div>
        </section>

    </main>

    <!-- Collab Inquiry Modal -->
    <div id="collabModal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="glass-panel rounded-3xl p-6 sm:p-8 max-w-md w-full space-y-6 relative animate-scale-up">
            <button onclick="closeCollabModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white text-lg">
                <i class="fa-solid fa-xmark"></i>
            </button>

            <div class="space-y-2">
                <div class="w-12 h-12 rounded-2xl bg-accent-purple/20 text-accent-purple flex items-center justify-center text-xl">
                    <i class="fa-solid fa-handshake"></i>
                </div>
                <h3 class="text-xl font-bold text-white">EXEL 아티스트 협업 문의</h3>
                <p class="text-xs text-slate-400">프로젝트 외주, 피처링, 믹싱 작업 의뢰를 남겨주세요.</p>
            </div>

            <form onsubmit="submitCollabInquiry(event)" class="space-y-4">
                <div class="space-y-1.5">
                    <label class="text-xs font-semibold text-slate-300">성함 또는 팀명</label>
                    <input type="text" required placeholder="예: 프로듀서 민수" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2.5 text-xs text-white outline-none">
                </div>
                <div class="space-y-1.5">
                    <label class="text-xs font-semibold text-slate-300">연락처 / 이메일</label>
                    <input type="email" required placeholder="name@email.com" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2.5 text-xs text-white outline-none">
                </div>
                <div class="space-y-1.5">
                    <label class="text-xs font-semibold text-slate-300">문의 유형</label>
                    <select class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2.5 text-xs text-slate-200 outline-none">
                        <option>비트메이킹 및 프로듀싱 외주</option>
                        <option>보컬 피처링 및 탑라인 협업</option>
                        <option>믹싱 및 마스터링 엔지니어링</option>
                        <option>기타 상호 협업</option>
                    </select>
                </div>
                <div class="space-y-1.5">
                    <label class="text-xs font-semibold text-slate-300">상세 내용</label>
                    <textarea rows="3" required placeholder="작업 예산, 일정, 곡 레퍼런스 등을 간략히 적어주세요." class="w-full bg-slate-900 border border-slate-700 rounded-xl p-3.5 text-xs text-white outline-none resize-none"></textarea>
                </div>

                <button type="submit" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-accent-purple to-accent-indigo text-white font-semibold text-xs shadow-lg shadow-purple-600/30 hover:opacity-95 transition">
                    협업 문의 전송하기
                </button>
            </form>
        </div>
    </div>

    <!-- Custom Toast Notification -->
    <div id="toastNotification" class="fixed bottom-6 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 glass-card px-5 py-3.5 rounded-2xl border border-accent-purple/40 shadow-2xl flex items-center gap-3">
        <div class="w-8 h-8 rounded-full bg-accent-purple/20 text-accent-purple flex items-center justify-center">
            <i class="fa-solid fa-bell text-sm"></i>
        </div>
        <div>
            <h4 class="font-bold text-xs text-white">SonicLog 알림</h4>
            <p id="toastMessage" class="text-xs text-slate-300">성공적으로 처리되었습니다.</p>
        </div>
    </div>

    <script>
        // View Switching Logic
        function switchView(viewName) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.add('hidden'));
            document.getElementById('view-' + viewName).classList.remove('hidden');

            // Reset tab styling
            const tabs = ['portfolio', 'workspace', 'upload'];
            tabs.forEach(tab => {
                const btn = document.getElementById('nav-' + tab);
                if (tab === viewName) {
                    btn.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-2 bg-gradient-to-r from-accent-purple to-accent-indigo text-white shadow-md";
                } else {
                    btn.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs sm:text-sm font-medium text-slate-400 hover:text-white transition-all flex items-center justify-center gap-2";
                }
            });

            // Update mobile indicator text
            const indicator = document.getElementById('mobileViewIndicator');
            if (viewName === 'portfolio') indicator.innerText = "포트폴리오";
            else if (viewName === 'workspace') indicator.innerText = "협업 스페이스";
            else if (viewName === 'upload') indicator.innerText = "곡 업로드";

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Audio Player Simulation state
        let activeIntervals = {};

        function togglePlay(btn, trackId) {
            const card = btn.closest('.glass-card');
            const timeDisplay = card.querySelector('.time-display');
            const icon = btn.querySelector('i');
            
            if (icon.classList.contains('fa-play')) {
                // Pause any other playing tracks
                document.querySelectorAll('.play-btn i').forEach(i => {
                    i.className = "fa-solid fa-play ml-0.5";
                });

                icon.className = "fa-solid fa-pause";
                showToast(trackId === 'track1' ? 'Neon Rain 스트리밍 재생 중...' : 'Cyber Blue 스트리밍 재생 중...');

                // Simulate progress timer
                let seconds = 0;
                if (activeIntervals[trackId]) clearInterval(activeIntervals[trackId]);
                
                activeIntervals[trackId] = setInterval(() => {
                    seconds++;
                    let mins = Math.floor(seconds / 60);
                    let secs = seconds % 60;
                    let formatted = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
                    let maxDuration = trackId === 'track1' ? '2:45' : '3:12';
                    timeDisplay.innerText = `${formatted} / ${maxDuration}`;
                    
                    if (seconds >= 165) { // Reset at end
                        clearInterval(activeIntervals[trackId]);
                        icon.className = "fa-solid fa-play ml-0.5";
                    }
                }, 1000);

            } else {
                icon.className = "fa-solid fa-play ml-0.5";
                if (activeIntervals[trackId]) clearInterval(activeIntervals[trackId]);
                showToast('일시정지되었습니다.');
            }
        }

        function seekAudio(event, bar) {
            showToast('오디오 타임라인이 이동되었습니다.');
        }

        function changeVersion(trackId, version) {
            showToast(`${trackId.toUpperCase()} 버일이 [${version.toUpperCase()}] 버전으로 변경되었습니다.`);
        }

        // Modal Controls
        function openCollabModal() {
            const modal = document.getElementById('collabModal');
            modal.classList.remove('hidden');
            modal.classList.add('flex');
        }

        function closeCollabModal() {
            const modal = document.getElementById('collabModal');
            modal.classList.add('hidden');
            modal.classList.remove('flex');
        }

        function submitCollabInquiry(e) {
            e.preventDefault();
            closeCollabModal();
            showToast('협업 및 외주 문의가 성공적으로 아티스트에게 전송되었습니다!');
        }

        // Workspace Comment Addition
        function addWorkspaceComment() {
            const input = document.getElementById('workspaceCommentInput');
            const val = input.value.trim();
            if(!val) return;

            const list = document.getElementById('workspaceCommentsList');
            const newComment = document.createElement('div');
            newComment.className = "p-3.5 rounded-2xl bg-slate-900/60 border border-slate-800 flex items-start gap-3 animate-fade-in";
            newComment.innerHTML = `
                <div class="w-8 h-8 rounded-full bg-accent-purple/20 text-accent-purple font-bold text-xs flex items-center justify-center shrink-0">E</div>
                <div class="flex-1">
                    <div class="flex items-center justify-between">
                        <span class="font-semibold text-xs text-white">EXEL (Lead)</span>
                        <span class="font-mono text-xs bg-slate-800 text-accent-purple px-2 py-0.5 rounded-md">1:25</span>
                    </div>
                    <p class="text-xs text-slate-300 mt-1 font-light">"${val}"</p>
                </div>
            `;
            list.prepend(newComment);
            input.value = '';
            showToast('타임스탬프 코멘트가 실시간 등록되었습니다.');
        }

        // Upload & Sync Handler
        function handleUploadSync(e) {
            e.preventDefault();
            showToast('곡이 업로드되고 인스타그램 포트폴리오에 성공적으로 동기화되었습니다!');
            switchView('portfolio');
        }

        // Toast Notification Helper
        function showToast(message) {
            const toast = document.getElementById('toastNotification');
            const msgEl = document.getElementById('toastMessage');
            msgEl.innerText = message;

            toast.classList.remove('translate-y-24', 'opacity-0');
            toast.classList.add('translate-y-0', 'opacity-100');

            setTimeout(() => {
                toast.classList.remove('translate-y-0', 'opacity-100');
                toast.classList.add('translate-y-24', 'opacity-0');
            }, 3500);
        }
    </script>
</body>
</html>