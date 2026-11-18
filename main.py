
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>0 dan Pro - Shaxsiy Ta'lim Akademiyasi</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --accent: #38bdf8;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --success: #22c55e;
            --warning: #f59e0b;
            --danger: #ef4444;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 20px;
        }
        h2 {
            text-align: center;
            color: var(--accent);
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            color: var(--text-sub);
            font-size: 14px;
            margin-bottom: 25px;
        }
        .container {
            max-width: 650px;
            margin: 0 auto;
        }
        .section-title {
            color: var(--warning);
            font-size: 16px;
            margin: 20px 0 10px 0;
            font-weight: bold;
        }
        .card {
            background: var(--card-bg);
            padding: 16px;
            margin-bottom: 12px;
            border-radius: 14px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
            cursor: pointer;
            display: flex;
            align-items: center;
            transition: 0.3s;
            border-left: 5px solid var(--accent);
        }
        .card:hover {
            transform: translateY(-3px);
            background: #27354f;
        }
        .icon {
            font-size: 34px;
            margin-right: 15px;
        }
        .info h3 {
            margin: 0 0 4px 0;
            font-size: 17px;
            color: #fff;
        }
        .info p {
            margin: 0;
            color: var(--text-sub);
            font-size: 12px;
        }
        .badge {
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent);
            padding: 3px 7px;
            border-radius: 6px;
            font-size: 10px;
            font-weight: bold;
            display: inline-block;
            margin-top: 5px;
        }
        .hidden {
            display: none !important;
        }
        .back-btn {
            background: #334155;
            color: #fff;
            border: none;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            margin-bottom: 20px;
            font-weight: bold;
        }
        .back-btn:hover {
            background: #475569;
        }
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        .tab-btn {
            flex: 1;
            padding: 10px;
            background: #1e293b;
            color: var(--text-sub);
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.2s;
        }
        .tab-btn.active {
            background: var(--accent);
            color: #0f172a;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        .lesson-item {
            background: #1e293b;
            padding: 12px 15px;
            margin-bottom: 10px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 14px;
            cursor: pointer;
            transition: 0.2s;
        }
        .lesson-item:hover {
            background: #27354f;
            border-left: 4px solid var(--accent);
        }
        #lessonModal {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.9);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        .modal-content {
            background: var(--card-bg);
            padding: 25px;
            border-radius: 14px;
            max-width: 500px;
            max-height: 85vh;
            overflow-y: auto;
            width: 90%;
            box-shadow: 0 5px 20px rgba(0,0,0,0.5);
            border: 1px solid #334155;
        }
        .close-modal {
            background: var(--danger);
            color: #fff;
            border: none;
            padding: 8px 15px;
            border-radius: 6px;
            cursor: pointer;
            float: right;
            font-weight: bold;
        }
        .quiz-box, .game-box {
            background: #1e293b;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
        }
        .quiz-options button {
            display: block;
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            background: #334155;
            color: #fff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-align: left;
            font-size: 14px;
            transition: 0.2s;
        }
        .quiz-options button:hover {
            background: #475569;
        }
        .ai-box {
            background: #0f172a;
            border: 1px solid #334155;
            padding: 15px;
            border-radius: 12px;
            margin-top: 20px;
        }
        .ai-box input[type="text"] {
            width: 65%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #475569;
            background: #1e293b;
            color: #fff;
        }
        .ai-box input[type="file"] {
            margin-top: 8px;
            width: 100%;
            color: var(--text-sub);
            font-size: 12px;
        }
        .ai-box button {
            width: 30%;
            padding: 10px;
            border-radius: 8px;
            border: none;
            background: var(--accent);
            color: #0f172a;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <!-- ASOSIY MENYU -->
    <div id="mainMenu" class="container">
        <h2>🚀 0 dan Pro Akademiya</h2>
        <div class="subtitle">Dasturlash va Xorijiy Tillar Markazi</div>

        <div class="section-title">💻 Dasturlash Yo'nalishlari (0 dan Pro)</div>

        <div class="card" onclick="openCourse('C')">
            <div class="icon">💻</div>
            <div class="info">
                <h3>C Dasturlash Tili</h3>
                <p>Tizimli dasturlash va xotira boshqaruvi</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('Cpp')">
            <div class="icon">⚡</div>
            <div class="info">
                <h3>C++ Dasturlash Tili</h3>
                <p>OOP, Algoritmlar va O'yinlar</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('CSharp')">
            <div class="icon">🔷</div>
            <div class="info">
                <h3>C# (.NET)</h3>
                <p>OOP, Unity va Backend</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('Java')">
            <div class="icon">☕</div>
            <div class="info">
                <h3>Java Dasturlash</h3>
                <p>Spring Boot va Android</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('Frontend')">
            <div class="icon">🎨</div>
            <div class="info">
                <h3>Frontend Dasturlash</h3>
                <p>HTML, CSS, JavaScript, React JS</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('DataAnalytica')">
            <div class="icon">📊</div>
            <div class="info">
                <h3>Backend & Data Analitika</h3>
                <p>Python, SQL, Ma'lumotlar tahlili</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="section-title">🌍 Xorijiy Tillar (Grammatika va Talaffuz)</div>

        <div class="card" onclick="openCourse('EnglishIT')">
            <div class="icon">🇬🇧</div>
            <div class="info">
                <h3>Ingliz tili (0 dan Pro gacha)</h3>
                <p>Grammatika, Talaffuz va IT Ingliz tili</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('RussianLang')">
            <div class="icon">🇷🇺</div>
            <div class="info">
                <h3>Rus tili (0 dan Pro gacha)</h3>
                <p>Grammatika, O'qilishi va So'zlashuv</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('ChineseLang')">
            <div class="icon">🇨🇳</div>
            <div class="info">
                <h3>Xitoy tili (Mandarin)</h3>
                <p>Pinyin (O'qilishi), Ierogliflar va Grammatika</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>

        <div class="card" onclick="openCourse('JapaneseLang')">
            <div class="icon">🇯🇵</div>
            <div class="info">
                <h3>Yapon tili (Hiragana/Katakana)</h3>
                <p>Grammatika, O'qilishi va Kanijilar</p>
                <span class="badge">Darslar, Test va O'yin</span>
            </div>
        </div>
    </div>

    <!-- KURSA ICHKI SAHifasi -->
    <div id="courseView" class="container hidden">
        <button class="back-btn" onclick="goBack()">⬅️ Ortga qaytish</button>
        <h2 id="courseTitle">Kurs Nomi</h2>
        <div class="subtitle">0 dan Pro darajagacha o'quv tizimi</div>

        <!-- TABLAR -->
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('lessons', this)">📚 Darslar</button>
            <button class="tab-btn" onclick="switchTab('tests', this)">🧠 Testlar</button>
            <button class="tab-btn" onclick="switchTab('game', this)">🎮 Kod O'yini (Debug)</button>
        </div>

        <!-- Darslar Tab -->
        <div id="lessonsTab" class="tab-content active">
            <div id="lessonsList"></div>
        </div>

        <!-- Testlar Tab -->
        <div id="testsTab" class="tab-content">
            <div class="quiz-box">
                <div id="quizContainer">
                    <h4 id="quizQuestion">Savol yuklanmoqda...</h4>
                    <div class="quiz-options" id="quizOptions"></div>
                </div>
                <div id="quizResultArea" class="hidden" style="text-align: center;">
                    <h3>🎉 Test yakunlandi!</h3>
                    <p id="finalScoreText" style="font-size: 16px; margin: 15px 0;"></p>
                    <button class="back-btn" onclick="restartQuiz()">Qaytadan topshirish</button>
                </div>
            </div>
        </div>

        <!-- Mini-O'yin Tab -->
        <div id="gameTab" class="tab-content">
            <div class="game-box">
                <h4>🎯 Mini-O'yin: Kodni Xatosini Topish (Bug Fixing)</h4>
                <p style="font-size: 13px; color: var(--text-sub);">Quyidagi kodda xatolik bor, uni to'g'ri variantini toping:</p>
                <div id="gameContainer">
                    <p id="gameTask" style="font-weight: bold; color: var(--accent); margin: 15px 0;"></p>
                    <div class="quiz-options" id="gameOptions"></div>
                </div>
                <div id="gameResultArea" class="hidden" style="text-align: center;">
                    <h3>🏆 O'yin yakunlandi!</h3>
                    <p id="finalGameScore" style="font-size: 16px; margin: 15px 0;"></p>
                    <button class="back-btn" onclick="restartGame()">O'yinni qayta boshlash</button>
                </div>
            </div>
        </div>

        <!-- AI YORDAMCHI BO'LIMI -->
        <div class="ai-box">
            <h4>🤖 Groq AI Repetitor</h4>
            <p style="font-size: 12px; color: var(--text-sub);">Tanlangan mavzu bo'yicha savol bering yoki fayl yuklang:</p>
            
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <input type="text" id="aiQuery" placeholder="Savolni yozing...">
                <button onclick="askAI()">Yuborish</button>
            </div>
            
            <input type="file" id="aiFile" accept="image/*,.txt,.pdf,.cpp,.c,.java,.cs">
            <p id="aiResponse" style="margin-top: 10px; font-size: 13px; color: var(--accent);"></p>
        </div>
    </div>

    <!-- Darsni o'qish uchun Modal Oyna -->
    <div id="lessonModal" class="hidden">
        <div class="modal-content">
            <button class="close-modal" onclick="closeLessonModal()">Yopish ❌</button>
            <h3 id="modalLessonTitle" style="color: var(--accent); margin-top: 0;"></h3>
            <p id="modalLessonBody" style="white-space: pre-wrap; line-height: 1.6; font-size: 14px; color: var(--text-main);"></p>
        </div>
    </div>

    <script>
        const coursesData = {
            'C': {
                title: "C Dasturlash Tili (0 dan Pro)",
                lessons: [
                    { title: "1-Dars: Kirish va GCC muhitni sozlash", content: "C tili 1972-yilda Dennis Ritchi tomonidan yaratilgan. Bu tizimli til bo'lib, operatsion tizimlar va drayverlar yozishda ishlatiladi. GCC — C tili kodlarini mashina tiliga tarjima qiluvchi kompilyator." },
                    { title: "2-Dars: O'zgaruvchilar va ma'lumot turlari", content: "C tilida ma'lumot turlari: int (butun son), float (o'nlik son), char (belgi). O'zgaruvchi e'lon qilish uchun turi yozilib, nomi beriladi: int x = 10;" },
                    { title: "3-Dars: Shart operatorlari (if, switch)", content: "Shart operatorlari dasturda mantiqiy qarorlar qabul qilish uchun kerak. 'if (x > 5)' sharti bajarilsa, ichidagi kod ishlaydi." },
                    { title: "4-Dars: Sikllar (for, while, do-while)", content: "Bir xil amalni bir necha marta takrorlash uchun sikllardan foydalaniladi. Masalan, 'for(int i=0; i<10; i++)' sikli 10 marta aylanadi." }
                ],
                quiz: [
                    { q: "C tilida ekranga chiqarish funksiyasi qaysi?", opts: ["print()", "printf()", "cout", "Console.Write"], correct: 1 },
                    { q: "C tilida butun sonlarni saqlash uchun qaysi kalit so'z ishlatiladi?", opts: ["float", "char", "int", "double"], correct: 2 },
                    { q: "C tilida bir qatorli izoh qanday belgilanadi?", opts: ["// izoh", "/* izoh */", "# izoh", "-- izoh"], correct: 0 },
                    { q: "C dasturi qaysi funksiyadan ishga tushadi?", opts: ["start()", "run()", "main()", "begin()"], correct: 2 }
                ],
                game: {
                    task: "Xatoni toping: printf(\"Salom Dunyo\"); — bu yerda nima yetishmayapti?",
                    opts: ["Nuqta-vergul (;)", "Qavs", "Qo'shtirnoq", "Hech qanday xato yo'q"],
                    correct: 0
                }
            },
            'Cpp': {
                title: "C++ Dasturlash Tili (0 dan Pro)",
                lessons: [
                    { title: "1-Dars: C++ ga kirish va cout/cin", content: "C++ tili C tilining davomi bo'lib, obyektga yo'naltirilgan dasturlash (OOP) imkoniyatlarini qo'shadi. Ekranga chiqarish uchun std::cout ishlatiladi." },
                    { title: "2-Dars: OOP va Klasslar, Obyektlar", content: "Klass — bu shablon, obyekt esa o'sha shablon asosida yaratilgan real nusxa. OOP asosiy to'rt ustunga ega: Inkapsulyatsiya, Vorislik, Polimorfizm, Abstraksiya." }
                ],
                quiz: [
                    { q: "C++ da obyekt yaratish uchun nima ishlatiladi?", opts: ["class", "new", "struct", "object"], correct: 0 },
                    { q: "C++ da ma'lumot kiritish uchun nima ishlatiladi?", opts: ["cin", "cout", "scanf", "print"], correct: 0 }
                ],
                game: {
                    task: "C++ da nomlar fazosi (namespace) qaysi kalit so'z bilan belgilanadi?", opts: ["using namespace std;", "namespace:std", "import std", "include std"], correct: 0
                }
            },
            'EnglishIT': {
                title: "Ingliz tili (0 dan Pro & IT)",
                lessons: [
                    { title: "1-Dars: Alifbo, Talaffuz va Transkripsiya", content: "Ingliz tilida 26 ta harf bor. Harflarning o'qilishi so'z ichidagi o'rniga qarab o'zgaradi. Transkripsiya so'zlarning to'g'ri talaffuzini ko'rsatadi." },
                    { title: "2-Dars: Grammatika: Present Simple va To be", content: "Present Simple hozirgi oddiy zamon. 'To be' fe'li (am, is, are) holatni bildiradi: I am a programmer." }
                ],
                quiz: [
                    { q: "What does 'Debugging' mean?", opts: ["Writing code", "Finding and fixing errors", "Running server", "UI design"], correct: 1 },
                    { q: "Choose the correct form: 'He ... a developer.'", opts: ["am", "is", "are", "be"], correct: 1 }
                ],
                game: {
                    task: "Choose the correct translation for 'Dasturiy ta'minot':", opts: ["Hardware", "Software", "Firmware", "Malware"], correct: 1
                }
            }
        };

        const L = (title, content) => ({ title, content });
        const Q = (q, opts, correct) => ({ q, opts, correct });

        Object.assign(coursesData, {
            'CSharp': {
                title: "C# (.NET) Kursi",
                lessons: [
                    L("1-Dars: C# va .NET ga kirish", "C# — Microsoft yaratgan zamonaviy OOP tili. .NET platformasida veb, desktop va Unity o'yinlari yoziladi.\n\nConsole.WriteLine(\"Salom\");"),
                    L("2-Dars: O'zgaruvchilar", "Asosiy turlar: int, double, string, bool.\n\nint yosh = 20;\nstring ism = \"Ali\";"),
                    L("3-Dars: Klasslar va obyektlar", "Klass — obyekt shabloni. new kalit so'zi obyekt yaratadi.\n\nclass Avto { public string Nom; }\nvar a = new Avto();")
                ],
                quiz: [Q("C# da ekranga chiqarish buyrug'i?", ["Console.WriteLine()", "printf()", "cout", "echo"], 0), Q("C# da matn turi qaysi?", ["char[]", "string", "text", "str"], 1)],
                game: { task: "Xatoni toping: int x = \"5\"; — nima noto'g'ri?", opts: ["int ga matn berilgan", "Nuqta-vergul yo'q", "x nomi xato", "Xato yo'q"], correct: 0 }
            },
            'Java': {
                title: "Java Dasturlash Kursi",
                lessons: [
                    L("1-Dars: Java va JVM", "Java kodi JVM (virtual mashina) orqali ishlaydi va Android ilovalarida ham keng qo'llanadi.\n\nSystem.out.println(\"Salom\");"),
                    L("2-Dars: Ma'lumot turlari", "int, double, boolean va String. String katta harf bilan yoziladi.\n\nint son = 5;\nString matn = \"Java\";"),
                    L("3-Dars: Metodlar", "Metod — kodni qayta ishlatish uchun nomlangan blok.\n\nstatic int qosh(int a, int b) {\n    return a + b;\n}")
                ],
                quiz: [Q("Java kodi qaysi muhitda ishlaydi?", ["JVM", "CLR", "GCC", "DOM"], 0), Q("Java dasturi qaysi metoddan boshlanadi?", ["main", "start", "init", "run"], 0)],
                game: { task: "Xatoni toping: string ism = \"Ali\"; — Java da nima noto'g'ri?", opts: ["string kichik harf bilan yozilgan", "Qo'shtirnoq", "Nuqta-vergul", "Xato yo'q"], correct: 0 }
            },
            'Frontend': {
                title: "Frontend Dasturlash Kursi",
                lessons: [
                    L("1-Dars: HTML asoslari", "HTML sahifa tuzilishini belgilaydi.\n\n<h1>Salom</h1>\n<p>Matn</p>\n<a href=\"#\">Havola</a>"),
                    L("2-Dars: CSS bilan bezash", "CSS rang, o'lcham va joylashuvni boshqaradi.\n\nh1 {\n  color: blue;\n  font-size: 32px;\n}"),
                    L("3-Dars: JavaScript", "JavaScript sahifani jonlantiradi: tugma bosilganda amal bajaradi.\n\nlet x = 5;\nbtn.onclick = () => alert(x);")
                ],
                quiz: [Q("Sahifa rangini o'zgartirish uchun nima ishlatiladi?", ["CSS", "SQL", "C++", "XML"], 0), Q("Eng katta sarlavha tegi qaysi?", ["<h1>", "<h6>", "<head>", "<title>"], 0)],
                game: { task: "Xatoni toping: <p>Salom<p> — nima noto'g'ri?", opts: ["Yopuvchi </p> yo'q", "Matn xato", "Teg nomi xato", "Xato yo'q"], correct: 0 }
            },
            'DataAnalytica': {
                title: "Backend & Data Analitika Kursi",
                lessons: [
                    L("1-Dars: Python asoslari", "Python oddiy sintaksisli til bo'lib, ma'lumotlar tahlilida eng mashhur.\n\nprint(\"Salom\")\nx = 10"),
                    L("2-Dars: SQL so'rovlari", "SQL ma'lumotlar bazasidan ma'lumot oladi.\n\nSELECT ism FROM talabalar\nWHERE yosh > 18;"),
                    L("3-Dars: Ro'yxat va sikl", "Ro'yxat bir nechta qiymatni saqlaydi.\n\nson = [1, 2, 3]\nfor s in son:\n    print(s)")
                ],
                quiz: [Q("Ma'lumot tanlash uchun SQL buyrug'i?", ["SELECT", "GET", "PULL", "TAKE"], 0), Q("Python da ekranga chiqarish?", ["print()", "printf()", "cout", "echo"], 0)],
                game: { task: "Xatoni toping: SELCT * FROM users; — nima noto'g'ri?", opts: ["SELECT xato yozilgan", "FROM kerak emas", "* belgisi xato", "Xato yo'q"], correct: 0 }
            },
            'RussianLang': {
                title: "Rus tili Kursi",
                lessons: [
                    L("1-Dars: Alifbo", "Rus alifbosida 33 ta harf bor: А (a), Б (b), В (v), Г (g), Д (d).\n\nПривет — Salom\nСпасибо — Rahmat"),
                    L("2-Dars: Salomlashish", "Доброе утро — Xayrli tong\nДобрый день — Xayrli kun\nДо свидания — Xayr"),
                    L("3-Dars: O'zini tanishtirish", "Меня зовут Али. — Mening ismim Ali.\nЯ из Узбекистана. — Men O'zbekistondanman.")
                ],
                quiz: [Q("«Спасибо» nima degani?", ["Rahmat", "Salom", "Xayr", "Iltimos"], 0), Q("Rus alifbosida nechta harf bor?", ["33", "26", "28", "30"], 0)],
                game: { task: "«Привет» so'zining tarjimasini toping:", opts: ["Salom", "Xayr", "Rahmat", "Kechirasiz"], correct: 0 }
            },
            'ChineseLang': {
                title: "Xitoy tili (Mandarin) Kursi",
                lessons: [
                    L("1-Dars: Pinyin va ohanglar", "Xitoy tilida 4 ta asosiy ohang bor. Pinyin — ierogliflarning lotin harflaridagi o'qilishi.\n\nmā, má, mǎ, mà"),
                    L("2-Dars: Salomlashish", "你好 (nǐ hǎo) — Salom\n谢谢 (xièxie) — Rahmat\n再见 (zàijiàn) — Xayr"),
                    L("3-Dars: Sonlar", "一 (yī) — 1\n二 (èr) — 2\n三 (sān) — 3\n十 (shí) — 10")
                ],
                quiz: [Q("«你好» nima degani?", ["Salom", "Xayr", "Rahmat", "Ha"], 0), Q("Pinyin nima?", ["Lotin harflaridagi o'qilishi", "Ohang", "Gap", "Son"], 0)],
                game: { task: "«谢谢» so'zining tarjimasini toping:", opts: ["Rahmat", "Salom", "Xayr", "Iltimos"], correct: 0 }
            },
            'JapaneseLang': {
                title: "Yapon tili Kursi",
                lessons: [
                    L("1-Dars: Hiragana", "Hiragana — yapon tilining asosiy 46 belgili alifbosi.\n\nあ (a), い (i), う (u), え (e), お (o)"),
                    L("2-Dars: Salomlashish", "こんにちは (konnichiwa) — Salom\nありがとう (arigatō) — Rahmat\nさようなら (sayōnara) — Xayr"),
                    L("3-Dars: Katakana", "Katakana chet so'zlarni yozish uchun ishlatiladi.\n\nコンピュータ (kompyūta) — kompyuter")
                ],
                quiz: [Q("«ありがとう» nima degani?", ["Rahmat", "Salom", "Xayr", "Ha"], 0), Q("Chet so'zlar qaysi alifboda yoziladi?", ["Katakana", "Hiragana", "Pinyin", "Kirill"], 0)],
                game: { task: "«こんにちは» so'zining tarjimasini toping:", opts: ["Salom", "Rahmat", "Xayr", "Uzr"], correct: 0 }
            }
        });

        coursesData.Cpp.lessons[0].content = "C++ tili C tilining davomi bo'lib, OOP imkoniyatlarini qo'shadi. Dastur main() funksiyasidan boshlanadi.\n\nBirinchi dastur:\n\n#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Salom, Dunyo!\" << endl;\n    return 0;\n}\n\nTushuntirish:\n• #include <iostream> — kiritish/chiqarish kutubxonasi\n• cout — ekranga chiqaradi\n• cin — klaviaturadan o'qiydi\n• endl — yangi qatorga o'tadi\n• return 0 — dastur muvaffaqiyatli tugadi\n\nMa'lumot kiritish:\n\nint yosh;\ncout << \"Yoshingiz: \";\ncin >> yosh;\ncout << \"Siz \" << yosh << \" yoshdasiz\";";
        coursesData.Cpp.lessons[1].content = "Klass — shablon, obyekt — undan yaratilgan nusxa.\n\nclass Talaba {\npublic:\n    string ism;\n    int yosh;\n    void salom() {\n        cout << \"Men \" << ism << endl;\n    }\n};\n\nint main() {\n    Talaba t;\n    t.ism = \"Ali\";\n    t.salom();\n}\n\nOOP ning 4 ustuni:\n• Inkapsulyatsiya — ma'lumotni himoyalash (private)\n• Vorislik — klassdan meros olish\n• Polimorfizm — bir nom, turli xatti-harakat\n• Abstraksiya — keraksiz tafsilotni yashirish";
        coursesData.C.lessons[0].content = "C tili 1972-yilda Dennis Ritchi tomonidan yaratilgan. Operatsion tizimlar va drayverlar shu tilda yoziladi. GCC — C kodini mashina tiliga o'giruvchi kompilyator.\n\nBirinchi dastur:\n\n#include <stdio.h>\n\nint main() {\n    printf(\"Salom, Dunyo!\\n\");\n    return 0;\n}\n\nKompilyatsiya va ishga tushirish:\n\ngcc salom.c -o salom\n./salom";
        coursesData.C.lessons[1].content = "O'zgaruvchi — ma'lumot saqlovchi xotira joyi. Asosiy turlar:\n• int — butun son (5)\n• float — o'nlik son (3.14)\n• char — bitta belgi ('A')\n\nint x = 10;\nfloat narx = 2.5;\nchar harf = 'A';\nprintf(\"%d %.1f %c\", x, narx, harf);\n\n%d — int, %f — float, %c — char uchun format belgisi.";
        coursesData.C.lessons[2].content = "if (shart) bajarilsa ichidagi kod ishlaydi, aks holda else qismi.\n\nint x = 7;\nif (x > 5) {\n    printf(\"Katta\");\n} else {\n    printf(\"Kichik\");\n}\n\nKo'p variant bo'lsa switch ishlatiladi:\n\nswitch (kun) {\n    case 1: printf(\"Dushanba\"); break;\n    case 2: printf(\"Seshanba\"); break;\n    default: printf(\"Boshqa\");\n}";
        coursesData.C.lessons[3].content = "Sikl bir xil amalni takrorlaydi.\n\nfor — soni ma'lum bo'lsa:\nfor (int i = 0; i < 5; i++) {\n    printf(\"%d \", i);\n}\n\nwhile — shart to'g'ri bo'lguncha:\nint n = 3;\nwhile (n > 0) {\n    n--;\n}\n\ndo-while — kamida bir marta bajariladi:\ndo {\n    n++;\n} while (n < 3);";
        coursesData.EnglishIT.lessons[0].content = "Ingliz alifbosida 26 ta harf bor: 5 ta unli (A, E, I, O, U) va 21 ta undosh.\n\nHarflarning nomi:\n• A — [ei]\n• E — [i:]\n• I — [ai]\n• O — [ou]\n• U — [ju:]\n\nTranskripsiya so'zning o'qilishini [ ] ichida ko'rsatadi: computer [kəmˈpjuːtər]. Yangi so'zni o'rganganda lug'atdagi transkripsiyaga qarang.";
        coursesData.EnglishIT.lessons[1].content = "To be fe'li: I am, he/she/it is, you/we/they are.\n\nI am a programmer.\nHe is a developer.\nWe are students.\n\nPresent Simple — odatiy ish-harakat. he/she/it bilan fe'lga -s qo'shiladi:\n\nI code every day.\nShe codes every day.\n\nSo'roq: Do you code? / Does she code?\nInkor: I do not code. / She does not code.";

        coursesData.C.lessons.push(L("5-Dars: Funksiyalar", "Funksiya — kodni qayta ishlatish uchun nomlangan blok.\n\nint kvadrat(int x) {\n    return x * x;\n}"));
        coursesData.Cpp.lessons.push(
            L("3-Dars: Shart va sikllar", "if/else qaror qabul qiladi, for va while takrorlaydi.\n\nfor (int i = 0; i < 5; i++) {\n    cout << i << endl;\n}"),
            L("4-Dars: Massiv va funksiyalar", "Massiv — bir turdagi qiymatlar to'plami.\n\nint a[3] = {1, 2, 3};\nint qosh(int x, int y) { return x + y; }")
        );
        coursesData.EnglishIT.lessons.push(L("3-Dars: IT so'zlari", "bug — xato\ncode — kod\nserver — server\ndatabase — ma'lumotlar bazasi\nupdate — yangilash"));

        coursesData.Cpp.lessons = [
            coursesData.Cpp.lessons[0],
            L("2-Dars: O'zgaruvchilar va operatorlar", `Asosiy turlar:
int — butun son, double — o'nlik son, char — belgi, bool — true/false, string — matn.

int yosh = 20;
double narx = 9.99;
char harf = 'A';
bool tayyor = true;
string ism = "Ali";
const double PI = 3.14;

Operatorlar:
• Arifmetik: + - * / % (qoldiq)
• Taqqoslash: == != < > <= >=
• Mantiqiy: && (va), || (yoki), ! (emas)

int a = 7, b = 2;
cout << a / b;            // 3 (butun bo'lish)
cout << a % b;            // 1
cout << (double)a / b;    // 3.5`),
            L("3-Dars: Shart operatorlari", `if / else if / else dastur yo'lini tanlaydi.

int ball = 85;
if (ball >= 90) cout << "A'lo";
else if (ball >= 70) cout << "Yaxshi";
else cout << "Qoniqarli";

Ternar operator (qisqa shart):
string r = (ball >= 56) ? "O'tdi" : "Yiqildi";

switch — aniq qiymatlar uchun:
switch (kun) {
    case 1: cout << "Dushanba"; break;
    case 2: cout << "Seshanba"; break;
    default: cout << "Boshqa kun";
}
break yozmasangiz keyingi case ham bajariladi.`),
            L("4-Dars: Sikllar", `for — soni ma'lum, while — shart to'g'ri bo'lguncha, do-while — kamida bir marta.

1 dan 10 gacha yig'indi:
int s = 0;
for (int i = 1; i <= 10; i++) s += i;
cout << s;   // 55

int n = 3;
while (n > 0) { cout << n << " "; n--; }

break — siklni to'xtatadi, continue — keyingi qadamga o'tadi.

Ichma-ich sikl (ko'paytirish jadvali):
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++)
        cout << i * j << " ";
    cout << endl;
}

Mashq: 1 dan 100 gacha juft sonlar yig'indisini toping.`),
            L("5-Dars: Massivlar va stringlar", `Massiv — bir turdagi qiymatlar ketma-ketligi. Indeks 0 dan boshlanadi.

int a[5] = {4, 8, 15, 16, 23};
for (int i = 0; i < 5; i++) cout << a[i] << " ";

Eng katta element:
int mx = a[0];
for (int i = 1; i < 5; i++) if (a[i] > mx) mx = a[i];

2 o'lchamli massiv: int m[3][3];

string:
string s = "Salom";
cout << s.length();   // 5
s += " Dunyo";
cout << s[0];         // S

Diqqat: massiv chegarasidan tashqariga chiqish xavfli xatodir.`),
            L("6-Dars: Funksiyalar", `Funksiya kodni qayta ishlatish imkonini beradi.

int qosh(int a, int b) { return a + b; }
void salom(string ism) { cout << "Salom, " << ism; }

Havola (&) orqali asl o'zgaruvchi o'zgaradi:
void almashtir(int &x, int &y) {
    int t = x; x = y; y = t;
}

Overloading — bir xil nom, turli parametr:
int kv(int x) { return x * x; }
double kv(double x) { return x * x; }

Rekursiya — funksiya o'zini chaqiradi:
int fakt(int n) { return n <= 1 ? 1 : n * fakt(n - 1); }`),
            L("7-Dars: Ko'rsatkichlar va xotira", `Ko'rsatkich — o'zgaruvchi manzilini saqlaydi. & — manzil, * — manzildagi qiymat.

int x = 10;
int *p = &x;
cout << *p;    // 10
*p = 20;       // x endi 20

Dinamik xotira:
int *a = new int[3];
a[0] = 5;
delete[] a;    // bo'shatish shart!

new bilan olingan xotirani delete qilmasangiz, xotira oqishi (memory leak) yuz beradi. Zamonaviy C++ da unique_ptr (#include <memory>) buni avtomatik qiladi. Bo'sh ko'rsatkich: nullptr.`),
            L("8-Dars: Klasslar va inkapsulyatsiya", `Klass ma'lumot va metodlarni birlashtiradi. private — tashqaridan yopiq, public — ochiq.

class Talaba {
private:
    int yosh;
public:
    string ism;
    Talaba(string i, int y) { ism = i; yosh = y; }
    int getYosh() { return yosh; }
    void setYosh(int y) { if (y > 0) yosh = y; }
};

Talaba t("Ali", 20);
t.setYosh(21);
cout << t.getYosh();

Konstruktor obyekt yaratilganda ishlaydi, destruktor (~Talaba) o'chirilganda. Inkapsulyatsiya: ma'lumotga faqat metodlar orqali kiriladi.`),
            L("9-Dars: Vorislik va polimorfizm", `Vorislik — yangi klass mavjud klassdan xususiyat oladi.

class Hayvon {
public:
    virtual void ovoz() { cout << "..."; }
};
class It : public Hayvon {
public:
    void ovoz() override { cout << "Vov"; }
};

Hayvon *h = new It();
h->ovoz();   // Vov

virtual metod polimorfizmni beradi: bir xil chaqiruv, obyekt turiga qarab turli natija. Abstrakt klass: virtual void f() = 0; — bunday klassdan obyekt yaratib bo'lmaydi, faqat voris klass orqali ishlatiladi.`),
            L("10-Dars: STL — vector va map", `STL tayyor ma'lumotlar tuzilmalari va algoritmlarni beradi.

#include <vector>
#include <map>
#include <algorithm>

vector<int> v = {5, 2, 9};
v.push_back(1);
sort(v.begin(), v.end());
for (int x : v) cout << x << " ";   // 1 2 5 9
cout << v.size();

map<string, int> ball;
ball["Ali"] = 90;
ball["Vali"] = 75;
cout << ball["Ali"];

vector — o'lchami o'zgaruvchan massiv, map — kalit-qiymat juftliklari.`),
            L("11-Dars: Fayllar va xatolarni boshqarish", `#include <fstream>

Yozish:
ofstream f("data.txt");
f << "Salom";
f.close();

O'qish:
ifstream g("data.txt");
string s;
getline(g, s);

Xatolarni ushlash (#include <stdexcept>):
try {
    if (b == 0) throw runtime_error("0 ga bo'lib bo'lmaydi");
    cout << a / b;
} catch (exception &e) {
    cout << e.what();
}`),
            L("12-Dars: Algoritmlar", `Saralash (bubble sort) — murakkabligi O(n²):
for (int i = 0; i < n - 1; i++)
    for (int j = 0; j < n - i - 1; j++)
        if (a[j] > a[j + 1]) swap(a[j], a[j + 1]);

Ikkilik qidiruv (massiv saralangan bo'lishi kerak) — O(log n):
int l = 0, r = n - 1;
while (l <= r) {
    int m = (l + r) / 2;
    if (a[m] == x) return m;
    if (a[m] < x) l = m + 1;
    else r = m - 1;
}
return -1;

Katta ma'lumotda murakkablik muhim: 1 000 000 ta elementda ikkilik qidiruv taxminan 20 qadamda topadi.`),
            L("13-Dars: Mini loyiha va keyingi yo'l", `Ro'yxat dasturi (menyu + vector):

vector<string> royxat;
int t;
do {
    cout << "1-Qo'shish 2-Ko'rish 0-Chiqish: ";
    cin >> t;
    if (t == 1) { string n; cin >> n; royxat.push_back(n); }
    else if (t == 2) for (auto &n : royxat) cout << n << endl;
} while (t != 0);

Pro darajaga yo'l:
• Har kuni 1-2 ta masala yeching (LeetCode, Codeforces)
• Ma'lumotlar tuzilmalarini o'rganing: stack, queue, daraxt, graf
• Kichik loyihalar yozing: kalkulyator, bank tizimi, matn o'yini
• Keyin Qt yoki SFML bilan oyna va o'yin yarating`)
        ];
        coursesData.Cpp.quiz.push(
            Q("int a = 7, b = 2; a / b natijasi nima?", ["3.5", "3", "4", "2"], 1),
            Q("Massiv indeksi nechadan boshlanadi?", ["1", "0", "-1", "2"], 1),
            Q("Funksiyada o'zgaruvchining o'zi o'zgarishi uchun nima ishlatiladi?", ["const", "static", "Havola (&)", "void"], 2),
            Q("O'zgaruvchi manzilini olish operatori qaysi?", ["*", "->", "&", "::"], 2),
            Q("new bilan olingan xotira nima bilan bo'shatiladi?", ["free", "delete", "remove", "clear"], 1),
            Q("Polimorfizm uchun metod qaysi kalit so'z bilan e'lon qilinadi?", ["static", "const", "inline", "virtual"], 3)
        );

        coursesData.Frontend.lessons = [
            L("1-Dars: HTML sahifa tuzilishi", `Har bir veb-sahifa HTML dan boshlanadi.

<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Mening saytim</title>
</head>
<body>
  <h1>Salom</h1>
  <p>Birinchi sahifam.</p>
</body>
</html>

head — ko'rinmas ma'lumotlar (sarlavha, kodlash), body — ko'rinadigan qism.
Asosiy teglar: h1–h6 (sarlavha), p (abzas), a (havola), img (rasm), ul/ol/li (ro'yxat), div va span (guruhlash).`),
            L("2-Dars: Havola, rasm, jadval va forma", `<a href="https://example.com">Saytga o'tish</a>
<img src="rasm.jpg" alt="Rasm tavsifi">

<ul>
  <li>Birinchi</li>
  <li>Ikkinchi</li>
</ul>

<table>
  <tr><th>Ism</th><th>Ball</th></tr>
  <tr><td>Ali</td><td>90</td></tr>
</table>

<form>
  <input type="text" placeholder="Ismingiz">
  <input type="email" placeholder="Email">
  <button type="submit">Yuborish</button>
</form>

alt matni rasm ochilmaganda va ko'zi ojizlar uchun kerak.`),
            L("3-Dars: CSS asoslari", `CSS sahifani bezaydi. Alohida fayl (style.css) qilib head ichida ulanadi:
<link rel="stylesheet" href="style.css">

Sintaksis: selektor { xususiyat: qiymat; }

h1 {
  color: #2563eb;
  font-size: 32px;
  text-align: center;
}
.karta { background: #f1f5f9; }   /* class — nuqta bilan */
#logo { width: 120px; }           /* id — # bilan */

HTML da: <div class="karta">Matn</div>
Bir elementga bir nechta class berish mumkin, id esa sahifada bitta bo'ladi.`),
            L("4-Dars: Box model va joylashuv", `Har bir element quti: content → padding (ichki masofa) → border (chiziq) → margin (tashqi masofa).

.karta {
  width: 300px;
  padding: 16px;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  margin: 20px auto;     /* markazga joylash */
  box-sizing: border-box;
}

display: block (qatorni to'liq egallaydi), inline (matn ichida), none (yashirish).
position: relative, absolute, fixed — elementni aniq joyga qo'yish uchun.`),
            L("5-Dars: Flexbox va Grid", `Flexbox — bir o'lchamli joylashuv:

.qator {
  display: flex;
  justify-content: space-between;  /* gorizontal */
  align-items: center;             /* vertikal */
  gap: 12px;
}

Grid — jadval ko'rinishidagi joylashuv:

.panjara {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

Qoida: bir qator yoki ustun bo'lsa flex, kataklar to'plami bo'lsa grid ishlating.`),
            L("6-Dars: Responsive dizayn", `Sayt telefon va kompyuterda ham chiroyli ko'rinishi kerak. Birinchi qadam — head ichida:
<meta name="viewport" content="width=device-width, initial-scale=1.0">

Media query ekran kengligiga qarab uslub o'zgartiradi:

.panjara { display: grid; grid-template-columns: 1fr; }
@media (min-width: 768px) {
  .panjara { grid-template-columns: repeat(3, 1fr); }
}

Maslahatlar:
• px o'rniga %, rem, vw birliklarini ishlating
• img { max-width: 100%; }
• Avval telefon uchun yozing (mobile first)`),
            L("7-Dars: JavaScript asoslari", `JavaScript sahifani jonlantiradi. HTML oxirida script tegi bilan ulanadi (src="app.js").

let ism = "Ali";
const yosh = 20;
console.log("Salom, " + ism);

function qosh(a, b) { return a + b; }
const kv = (x) => x * x;      // arrow funksiya

if (yosh >= 18) console.log("Katta");

let sonlar = [3, 7, 9];
sonlar.push(12);
for (let s of sonlar) console.log(s);
let ikki = sonlar.map(s => s * 2);

let talaba = { ism: "Vali", ball: 88 };
console.log(talaba.ism);`),
            L("8-Dars: DOM va hodisalar", `DOM — JavaScript orqali sahifa elementlarini boshqarish.

HTML:
<button id="btn">Bos</button>
<p id="matn">Salom</p>

JS:
const btn = document.getElementById("btn");
const matn = document.querySelector("#matn");

btn.addEventListener("click", function () {
  matn.textContent = "Tugma bosildi!";
  matn.classList.toggle("qizil");
  matn.style.color = "blue";
});

Yangi element yaratish:
const li = document.createElement("li");
li.textContent = "Yangi band";
document.querySelector("ul").appendChild(li);`),
            L("9-Dars: API, localStorage va mini loyiha", `Serverdan ma'lumot olish:

fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then(r => r.json())
  .then(data => console.log(data.title));

Brauzerda saqlash:
localStorage.setItem("ism", "Ali");
let ism = localStorage.getItem("ism");

Mini loyiha — vazifalar ro'yxati (To-Do):
1. input va "Qo'shish" tugmasi yarating
2. Tugma bosilganda yangi li qo'shing
3. Ro'yxatni localStorage ga saqlang
4. O'chirish tugmasini qo'shing

Pro yo'l: Git va GitHub, React, GitHub Pages yoki Netlify da joylash. Kichik bizneslarga bir sahifali sayt (landing) yasab berish — birinchi real tajriba bo'ladi.`)
        ];
        coursesData.Frontend.quiz.push(
            Q("CSS da class selektori qanday yoziladi?", ["#nom", ".nom", "nom", "*nom"], 1),
            Q("Elementlarni bir qatorda joylash uchun qaysi display ishlatiladi?", ["block", "none", "flex", "table"], 2),
            Q("Elementni JavaScript da id bo'yicha topish funksiyasi?", ["getElementById", "findId", "selectId", "getId"], 0),
            Q("O'zgarmas qiymat e'lon qilish uchun qaysi kalit so'z?", ["var", "let", "set", "const"], 3)
        );

        coursesData.DataAnalytica.lessons = [
            L("1-Dars: Python kirish", `Python — o'qish oson, ma'lumotlar tahlili va backend uchun mashhur til.

print("Salom, Dunyo!")

ism = input("Ismingiz: ")
yosh = 20            # int
narx = 9.99          # float
faol = True          # bool
print("Salom,", ism)

Turni o'zgartirish: int("5"), str(10), float("2.5")
Izoh # belgisi bilan yoziladi. Blok chegarasi { } emas, probel (4 ta) bilan belgilanadi.`),
            L("2-Dars: Shart va sikllar", `ball = 85
if ball >= 90:
    print("A'lo")
elif ball >= 70:
    print("Yaxshi")
else:
    print("Qoniqarli")

for i in range(5):        # 0,1,2,3,4
    print(i)

n = 3
while n > 0:
    print(n)
    n -= 1

Operatorlar: and, or, not, ==, !=, in
Misol: if "a" in "salom": print("bor")`),
            L("3-Dars: Ro'yxat, lug'at, to'plam", `Ro'yxat (list):
sonlar = [5, 2, 9]
sonlar.append(1)
sonlar.sort()
print(sonlar[0], len(sonlar))

Lug'at (dict) — kalit: qiymat:
talaba = {"ism": "Ali", "ball": 90}
talaba["yosh"] = 20
for k, v in talaba.items():
    print(k, v)

To'plam (set) — takrorlanmaydigan qiymatlar:
s = {1, 2, 2, 3}   # {1, 2, 3}

List comprehension:
kvadrat = [x * x for x in range(5)]`),
            L("4-Dars: Funksiyalar va modullar", `def qosh(a, b=0):
    return a + b

print(qosh(2, 3))

kv = lambda x: x * x

Modul — tayyor kod to'plami:
import math
print(math.sqrt(16))

from random import randint
print(randint(1, 10))

Tashqi kutubxonani o'rnatish (terminalda):
pip install pandas

Yaxshi odat: bitta funksiya bitta vazifani bajarsin.`),
            L("5-Dars: Fayllar va xatolar", `with open("data.txt", "w") as f:
    f.write("Salom")

with open("data.txt") as f:
    matn = f.read()
    print(matn)

Xatolarni ushlash:
try:
    x = int(input("Son: "))
    print(10 / x)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
except ValueError:
    print("Son kiriting")

CSV bilan ishlash:
import csv
with open("ball.csv") as f:
    for qator in csv.reader(f):
        print(qator)`),
            L("6-Dars: SQL asoslari", `SQL — ma'lumotlar bazasi bilan ishlash tili.

CREATE TABLE talabalar (
    id INTEGER PRIMARY KEY,
    ism TEXT,
    yosh INTEGER,
    ball INTEGER
);

INSERT INTO talabalar (ism, yosh, ball) VALUES ('Ali', 20, 90);

SELECT * FROM talabalar;
SELECT ism, ball FROM talabalar WHERE ball > 80 ORDER BY ball DESC;
SELECT * FROM talabalar LIMIT 5;

Qoida: WHERE — filtr, ORDER BY — saralash, LIMIT — nechta qator.`),
            L("7-Dars: SQL: yangilash, guruhlash, JOIN", `UPDATE talabalar SET ball = 95 WHERE ism = 'Ali';
DELETE FROM talabalar WHERE id = 3;   -- WHERE ni unutmang!

Agregat funksiyalar: COUNT, SUM, AVG, MIN, MAX
SELECT COUNT(*), AVG(ball) FROM talabalar;

Guruhlash:
SELECT guruh, AVG(ball) FROM talabalar GROUP BY guruh;

JOIN — ikki jadvalni bog'lash:
SELECT t.ism, f.nom
FROM talabalar t
JOIN fanlar f ON t.fan_id = f.id;

DELETE va UPDATE da WHERE yozmasangiz, barcha qatorlar o'zgaradi.`),
            L("8-Dars: pandas bilan tahlil", `pandas jadval ma'lumotlarini tahlil qiladi (pip install pandas).

import pandas as pd

df = pd.read_csv("sotuv.csv")
print(df.head())          # dastlabki 5 qator
print(df.describe())      # statistika

yuqori = df[df["narx"] > 100]       # filtr
print(df["narx"].mean())            # o'rtacha
print(df.groupby("shahar")["narx"].sum())

df["jami"] = df["narx"] * df["soni"]
df.sort_values("jami", ascending=False).to_csv("natija.csv")

Ma'lumotni tahlildan oldin tozalang: bo'sh qiymatlar (df.dropna()) va takroriylar (df.drop_duplicates()).`),
            L("9-Dars: Mini loyiha va keyingi yo'l", `Loyiha: sotuv ma'lumotlarini tahlil qilish.
1. CSV faylni pandas bilan o'qing
2. Ma'lumotni tozalang
3. Eng ko'p sotilgan 5 mahsulotni toping
4. Natijani grafik qiling:
   import matplotlib.pyplot as plt
   df.groupby("mahsulot")["jami"].sum().plot(kind="bar")
   plt.show()

Pro yo'l:
• Flask yoki FastAPI bilan backend yozing
• Telegram bot yaratish (aiogram kutubxonasi)
• SQLite yoki PostgreSQL bilan haqiqiy loyiha qiling
• Har kuni kichik masala yeching va natijani GitHub ga joylang`)
        ];
        coursesData.DataAnalytica.quiz.push(
            Q("Python da ro'yxatga element qo'shish metodi?", ["add()", "append()", "push()", "insert_end()"], 1),
            Q("SQL da shart bo'yicha filtrlash uchun nima ishlatiladi?", ["FILTER", "IF", "WHERE", "FIND"], 2),
            Q("Python da blok chegarasi nima bilan belgilanadi?", ["Probel (indent)", "{ }", "begin/end", "( )"], 0),
            Q("pandas da dastlabki qatorlarni ko'rish metodi?", ["top()", "first()", "head()", "show()"], 2)
        );

        coursesData.C.lessons = coursesData.C.lessons.slice(0, 4).concat([
            L("5-Dars: Massivlar va satrlar", `Massiv — bir turdagi qiymatlar ketma-ketligi. Indeks 0 dan boshlanadi.

int a[5] = {4, 8, 15, 16, 23};
for (int i = 0; i < 5; i++) printf("%d ", a[i]);

Satr — char massivi, oxiri '\\0' bilan tugaydi:
char ism[20] = "Ali";
printf("%s", ism);

#include <string.h>
strlen(ism);          // uzunlik
strcpy(ism, "Vali");  // nusxalash
strcmp(ism, "Ali");   // solishtirish (0 bo'lsa teng)

Ma'lumot o'qish:
int x;
scanf("%d", &x);      // int uchun & shart
Chegaradan chiqish — C da eng ko'p uchraydigan xato.`),
            L("6-Dars: Funksiyalar", `Funksiya kodni qayta ishlatish imkonini beradi.

#include <stdio.h>

int qosh(int a, int b) {
    return a + b;
}

void salom(void) {
    printf("Salom\\n");
}

int main() {
    salom();
    printf("%d", qosh(2, 3));
    return 0;
}

Funksiyani main dan oldin e'lon qilish (prototip):
int qosh(int a, int b);

C da parametr qiymat bo'yicha uzatiladi: funksiya ichida o'zgarish asl o'zgaruvchiga ta'sir qilmaydi. Buning uchun ko'rsatkich kerak.`),
            L("7-Dars: Ko'rsatkichlar va xotira", `Ko'rsatkich — o'zgaruvchi manzilini saqlaydi. & — manzil, * — manzildagi qiymat.

int x = 10;
int *p = &x;
printf("%d", *p);   // 10
*p = 20;            // x endi 20

Ko'rsatkich orqali o'zgartirish:
void almashtir(int *a, int *b) {
    int t = *a; *a = *b; *b = t;
}
almashtir(&x, &y);

Dinamik xotira (#include <stdlib.h>):
int *m = malloc(5 * sizeof(int));
m[0] = 7;
free(m);   // bo'shatish shart!

malloc dan keyin NULL ekanini tekshiring, free qilmasangiz xotira oqadi.`),
            L("8-Dars: struct va fayllar", `struct bir nechta ma'lumotni birlashtiradi.

struct Talaba {
    char ism[30];
    int ball;
};

struct Talaba t = {"Ali", 90};
printf("%s %d", t.ism, t.ball);

Faylga yozish va o'qish:
FILE *f = fopen("data.txt", "w");
fprintf(f, "%s %d", t.ism, t.ball);
fclose(f);

f = fopen("data.txt", "r");
char s[30]; int b;
fscanf(f, "%s %d", s, &b);
fclose(f);

Fayl ochilmasa fopen NULL qaytaradi — doim tekshiring.`)
        ]);
        coursesData.C.quiz.push(
            Q("C da satr qaysi belgi bilan tugaydi?", ["'\\n'", "'\\0'", "';'", "' '"], 1),
            Q("scanf da int o'zgaruvchi oldiga nima yoziladi?", ["*", "#", "&", "@"], 2),
            Q("malloc bilan olingan xotira nima bilan bo'shatiladi?", ["delete", "free", "clear", "remove"], 1)
        );

        coursesData.CSharp.lessons = [
            L("1-Dars: C# va .NET ga kirish", `C# — Microsoft yaratgan zamonaviy OOP tili. Veb, desktop, mobil va Unity o'yinlari uchun ishlatiladi.

Muhit: .NET SDK va Visual Studio (yoki VS Code) o'rnating. Terminalda:
dotnet new console -n Salom
dotnet run

Birinchi dastur:
using System;

class Program {
    static void Main() {
        Console.WriteLine("Salom, Dunyo!");
    }
}

Dastur Main metodidan boshlanadi. Console.WriteLine — chiqarish, Console.ReadLine() — o'qish.`),
            L("2-Dars: O'zgaruvchilar va operatorlar", `Turlar: int, double, bool, char, string.

int yosh = 20;
double narx = 9.99;
string ism = "Ali";
bool faol = true;
var son = 5;            // tur avtomatik aniqlanadi
const double PI = 3.14;

Kiritish:
Console.Write("Yoshingiz: ");
int y = int.Parse(Console.ReadLine());

Matn ichiga qiymat qo'yish:
Console.WriteLine($"Salom, {ism}! Siz {yosh} yoshdasiz.");

Operatorlar: + - * / %, == != < > <= >=, && || !`),
            L("3-Dars: Shart va sikllar", `int ball = 85;
if (ball >= 90) Console.WriteLine("A'lo");
else if (ball >= 70) Console.WriteLine("Yaxshi");
else Console.WriteLine("Qoniqarli");

switch (kun) {
    case 1: Console.WriteLine("Dushanba"); break;
    default: Console.WriteLine("Boshqa"); break;
}

for (int i = 0; i < 5; i++) Console.WriteLine(i);

int n = 3;
while (n > 0) { n--; }

foreach (var x in new int[] {1, 2, 3}) Console.WriteLine(x);

break siklni to'xtatadi, continue keyingi qadamga o'tadi.`),
            L("4-Dars: Massiv, List va string", `int[] a = {4, 8, 15};
Console.WriteLine(a[0] + " " + a.Length);

List — o'lchami o'zgaruvchan ro'yxat:
using System.Collections.Generic;
var royxat = new List<string>();
royxat.Add("Ali");
royxat.Add("Vali");
Console.WriteLine(royxat.Count);
royxat.Remove("Ali");

string metodlari:
string s = "Salom Dunyo";
s.Length;
s.ToUpper();
s.Substring(0, 5);   // Salom
s.Contains("Dunyo");
s.Split(' ');`),
            L("5-Dars: Metodlar", `static int Qosh(int a, int b) {
    return a + b;
}

static void Salom(string ism) {
    Console.WriteLine("Salom, " + ism);
}

Standart qiymat:
static double Narx(double summa, double chegirma = 0) {
    return summa - chegirma;
}

ref va out — qiymatni asl o'zgaruvchiga qaytarish:
static void Almashtir(ref int x, ref int y) {
    int t = x; x = y; y = t;
}
Almashtir(ref a, ref b);

Bitta metod bitta vazifani bajarsin.`),
            L("6-Dars: Klasslar va obyektlar", `class Talaba {
    public string Ism;
    private int yosh;

    public Talaba(string ism, int yosh) {
        Ism = ism;
        this.yosh = yosh;
    }

    public int Yosh {            // property
        get { return yosh; }
        set { if (value > 0) yosh = value; }
    }

    public void Salom() {
        Console.WriteLine("Men " + Ism);
    }
}

var t = new Talaba("Ali", 20);
t.Salom();
t.Yosh = 21;

private — tashqaridan yopiq, public — ochiq.`),
            L("7-Dars: Vorislik va interfeys", `class Hayvon {
    public virtual void Ovoz() { Console.WriteLine("..."); }
}
class It : Hayvon {
    public override void Ovoz() { Console.WriteLine("Vov"); }
}

Hayvon h = new It();
h.Ovoz();   // Vov

Interfeys — majburiy metodlar ro'yxati:
interface IUchish {
    void Uch();
}
class Qush : IUchish {
    public void Uch() { Console.WriteLine("Uchyapti"); }
}

Bir klass bitta klassdan meros oladi, lekin bir nechta interfeysni qo'llay oladi.`),
            L("8-Dars: Xatolar, LINQ va keyingi yo'l", `try {
    int x = int.Parse("abc");
} catch (FormatException e) {
    Console.WriteLine("Son emas: " + e.Message);
} finally {
    Console.WriteLine("Doim bajariladi");
}

LINQ — kolleksiyalar bilan qisqa ishlash:
using System.Linq;
var sonlar = new List<int> {5, 2, 9, 1};
var katta = sonlar.Where(x => x > 2).OrderBy(x => x).ToList();
Console.WriteLine(sonlar.Sum());

Keyingi yo'l: fayllar bilan ishlash, ASP.NET Core (veb), Unity (o'yinlar). Mini loyiha: konsolda talabalar ro'yxati dasturi.`)
        ];
        coursesData.CSharp.quiz.push(
            Q("C# da matn ichiga qiymat qo'yish usuli?", ["\"Salom \" % ism", "$\"Salom {ism}\"", "f\"Salom {ism}\"", "\"Salom ${ism}\""], 1),
            Q("Mavjud metodni voris klassda o'zgartirish uchun nima yoziladi?", ["new", "static", "override", "sealed"], 2),
            Q("O'lchami o'zgaruvchan ro'yxat qaysi?", ["List<T>", "int[]", "string", "var"], 0)
        );

        coursesData.Java.lessons = [
            L("1-Dars: Java va JVM", `Java — "bir marta yoz, hamma joyda ishlat" tamoyilidagi til. Kod bayt-kodga (.class) o'giriladi va JVM orqali ishlaydi. Android, veb-serverlar, bank tizimlarida keng qo'llanadi.

O'rnatish: JDK, muhit: IntelliJ IDEA yoki VS Code.

Salom.java:
public class Salom {
    public static void main(String[] args) {
        System.out.println("Salom, Dunyo!");
    }
}

Ishga tushirish (terminalda):
javac Salom.java
java Salom

Fayl nomi public klass nomi bilan bir xil bo'lishi kerak.`),
            L("2-Dars: O'zgaruvchilar va kiritish", `Turlar: int, long, double, boolean, char va String (katta harf bilan).

int yosh = 20;
double narx = 9.99;
boolean faol = true;
String ism = "Ali";
final double PI = 3.14;

Kiritish:
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
System.out.print("Ismingiz: ");
String ism = sc.nextLine();
int y = sc.nextInt();

Operatorlar: + - * / %, == != < > <= >=, && || !
Butun sonlarni bo'lish: 7 / 2 = 3, (double) 7 / 2 = 3.5`),
            L("3-Dars: Shart va sikllar", `int ball = 85;
if (ball >= 90) System.out.println("A'lo");
else if (ball >= 70) System.out.println("Yaxshi");
else System.out.println("Qoniqarli");

switch (kun) {
    case 1: System.out.println("Dushanba"); break;
    default: System.out.println("Boshqa");
}

for (int i = 0; i < 5; i++) System.out.println(i);

int n = 3;
while (n > 0) { n--; }

do { n++; } while (n < 3);

Satrlarni solishtirishda == emas, equals ishlating:
if (ism.equals("Ali")) { ... }`),
            L("4-Dars: Massiv va String", `int[] a = {4, 8, 15, 16};
System.out.println(a[0] + " " + a.length);
for (int x : a) System.out.println(x);

int[] b = new int[5];   // 0 bilan to'ldirilgan

String metodlari:
String s = "Salom Dunyo";
s.length();
s.toUpperCase();
s.substring(0, 5);   // Salom
s.contains("Dunyo");
s.split(" ");

String o'zgarmas (immutable): har o'zgarishda yangi obyekt yaratiladi. Ko'p qo'shish uchun StringBuilder ishlating.`),
            L("5-Dars: Metodlar", `public static int qosh(int a, int b) {
    return a + b;
}

public static void salom(String ism) {
    System.out.println("Salom, " + ism);
}

Overloading — bir xil nom, turli parametr:
static int kv(int x) { return x * x; }
static double kv(double x) { return x * x; }

Rekursiya:
static int fakt(int n) {
    return n <= 1 ? 1 : n * fakt(n - 1);
}

Java da parametr qiymat bo'yicha uzatiladi; obyektlarda esa havola nusxasi uzatiladi.`),
            L("6-Dars: Klasslar va obyektlar", `public class Talaba {
    private String ism;
    private int yosh;

    public Talaba(String ism, int yosh) {
        this.ism = ism;
        this.yosh = yosh;
    }

    public String getIsm() { return ism; }
    public int getYosh() { return yosh; }
    public void setYosh(int yosh) {
        if (yosh > 0) this.yosh = yosh;
    }

    public void salom() {
        System.out.println("Men " + ism);
    }
}

Talaba t = new Talaba("Ali", 20);
t.salom();

private maydonlarga faqat getter/setter orqali kiriladi (inkapsulyatsiya).`),
            L("7-Dars: Vorislik va interfeys", `class Hayvon {
    void ovoz() { System.out.println("..."); }
}
class It extends Hayvon {
    @Override
    void ovoz() { System.out.println("Vov"); }
}

Hayvon h = new It();
h.ovoz();   // Vov (polimorfizm)

interface Uchuvchi {
    void uch();
}
class Qush implements Uchuvchi {
    public void uch() { System.out.println("Uchyapti"); }
}

abstract class — to'liq bo'lmagan klass, undan obyekt yaratib bo'lmaydi. Bir klass bitta klassdan extends qiladi, bir nechta interfeysni implements qila oladi.`),
            L("8-Dars: Kolleksiyalar va xatolar", `import java.util.*;

ArrayList<String> royxat = new ArrayList<>();
royxat.add("Ali");
royxat.add("Vali");
System.out.println(royxat.size());
royxat.remove("Ali");

HashMap<String, Integer> ball = new HashMap<>();
ball.put("Ali", 90);
System.out.println(ball.get("Ali"));

Xatolarni ushlash:
try {
    int x = Integer.parseInt("abc");
} catch (NumberFormatException e) {
    System.out.println("Son emas");
} finally {
    System.out.println("Doim bajariladi");
}

Keyingi yo'l: fayllar, Spring Boot (veb), Android. Mini loyiha: konsolda talabalar ro'yxati.`)
        ];
        coursesData.Java.quiz.push(
            Q("Java da satrlarni solishtirish uchun nima ishlatiladi?", ["==", "equals()", "compare", "="], 1),
            Q("Java da o'zgarmas qiymat e'lon qilish kalit so'zi?", ["const", "static", "final", "let"], 2),
            Q("Klass boshqa klassdan meros olishi uchun nima yoziladi?", ["extends", "inherits", "implements", "super"], 0)
        );

        coursesData.Cpp.lessons.push(
            L("14-Dars (O'rta): const, havola va ko'rsatkichlar", `const o'zgarmaslikni ta'minlaydi:
const int N = 10;
void chiqar(const string &s) { cout << s; }   // nusxa olinmaydi, o'zgartirib ham bo'lmaydi

Katta obyektlarni funksiyaga const havola (&) bilan uzating — bu tez va xavfsiz.

Ko'rsatkich arifmetikasi:
int a[3] = {10, 20, 30};
int *p = a;
cout << *(p + 1);   // 20
p++;                // keyingi elementga

Ko'rsatkich turlari:
const int *p1;   // qiymatni o'zgartirib bo'lmaydi
int *const p2 = &x;   // manzilni o'zgartirib bo'lmaydi

Havola — o'zgaruvchining boshqa nomi: int &r = x; Havola nullptr bo'lolmaydi va qayta bog'lanmaydi.`),
            L("15-Dars (O'rta): string va stringstream", `#include <string>
#include <sstream>

string s = "Salom Dunyo";
s.find("Dunyo");        // 6 (topilmasa string::npos)
s.substr(0, 5);         // Salom
s.replace(0, 5, "Hay");
s.erase(0, 1);
s.push_back('!');
s.size();

Bo'sh joyli qatorni o'qish:
string qator;
getline(cin, qator);

Sonni matnga va aksincha:
int n = stoi("123");
string t = to_string(45);

Matnni so'zlarga bo'lish:
stringstream ss("men C++ o'rganyapman");
string so;
while (ss >> so) cout << so << endl;`),
            L("16-Dars (O'rta): enum, namespace va constexpr", `enum class Rang { Qizil, Yashil, Kok };
Rang r = Rang::Yashil;
if (r == Rang::Yashil) cout << "Yashil";

enum class turlari bir-biriga aralashib ketmaydi.

namespace — nomlar to'qnashuvini oldini oladi:
namespace Matem {
    int qosh(int a, int b) { return a + b; }
}
cout << Matem::qosh(2, 3);

constexpr — kompilyatsiya vaqtida hisoblanadi:
constexpr int kv(int x) { return x * x; }
constexpr int N = kv(5);   // 25

auto — kompilyator turni o'zi aniqlaydi:
auto x = 3.14;
for (auto &el : royxat) { ... }

#define o'rniga const yoki constexpr ishlating.`),
            L("17-Dars (O'rta): Klasslar chuqurroq", `class Nuqta {
    int x, y;
    static int soni;          // barcha obyektlarga umumiy
public:
    Nuqta() : x(0), y(0) { soni++; }            // default
    Nuqta(int x, int y) : x(x), y(y) { soni++; }  // initializer list
    Nuqta(const Nuqta &b) : x(b.x), y(b.y) { soni++; }  // nusxa
    int getX() const { return x; }              // const metod
    static int nechta() { return soni; }
};
int Nuqta::soni = 0;

Nuqta a(1, 2);
Nuqta b = a;                    // nusxa konstruktori
cout << Nuqta::nechta();       // 2

const metod obyektni o'zgartirmaydi. Initializer list — maydonlarni tez va to'g'ri boshlash usuli.`),
            L("18-Dars (O'rta): Operator overloading", `Operatorni o'z klassimiz uchun ma'no berish:

class Vektor {
public:
    int x, y;
    Vektor(int x = 0, int y = 0) : x(x), y(y) {}
    Vektor operator+(const Vektor &b) const {
        return Vektor(x + b.x, y + b.y);
    }
    bool operator==(const Vektor &b) const {
        return x == b.x && y == b.y;
    }
};

Vektor a(1, 2), b(3, 4);
Vektor c = a + b;     // (4, 6)

cout uchun << operatori (friend):
ostream& operator<<(ostream &os, const Vektor &v) {
    return os << "(" << v.x << ", " << v.y << ")";
}
cout << c;

Faqat tabiiy ma'no beradigan joyda overload qiling.`),
            L("19-Dars (O'rta): RAII va smart pointerlar", `RAII: resursni konstruktorda olamiz, destruktorda qaytaramiz. Shunda xotira oqmaydi.

#include <memory>

unique_ptr<int> p = make_unique<int>(5);
cout << *p;        // o'zi o'chadi, delete shart emas

shared_ptr<int> a = make_shared<int>(10);
shared_ptr<int> b = a;        // egalar soni 2
cout << a.use_count();

unique_ptr — bitta egasi bor, nusxalanmaydi (move bilan o'tkaziladi):
auto q = move(p);

Qoida: yangi kodda xom new/delete o'rniga make_unique va make_shared ishlating. Agar klassingiz xotira olsa, destruktor, nusxa konstruktori va nusxa operatorini birga yozing (Rule of three).`),
            L("20-Dars (O'rta): Shablonlar (template)", `Shablon bir kodni turli turlar uchun ishlatadi.

template <typename T>
T katta(T a, T b) {
    return a > b ? a : b;
}
cout << katta(3, 7);        // int
cout << katta(2.5, 1.2);    // double

Klass shabloni:
template <typename T>
class Quti {
    T qiymat;
public:
    Quti(T q) : qiymat(q) {}
    T ol() const { return qiymat; }
};
Quti<string> q("Salom");
cout << q.ol();

STL ning hammasi (vector, map...) shablonlardan qurilgan. Shablon kodi odatda header faylda yoziladi.`),
            L("21-Dars (O'rta): STL konteynerlar", `#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <stack>
#include <queue>

set<int> s = {3, 1, 3, 2};          // {1, 2, 3}, takrorlanmaydi, saralangan
unordered_map<string, int> m;       // tezroq qidiruv
m["Ali"] = 90;
if (m.count("Ali")) cout << m["Ali"];

stack<int> st;  st.push(1);  st.push(2);  cout << st.top();   // 2 (oxirgi kirgan birinchi chiqadi)
queue<int> q;   q.push(1);   q.push(2);   cout << q.front();  // 1 (birinchi kirgan birinchi chiqadi)

Iterator:
for (auto it = s.begin(); it != s.end(); ++it) cout << *it;

Tanlash: ketma-ketlik uchun vector, kalit bo'yicha qidiruv uchun unordered_map, saralangan to'plam uchun set/map.`),
            L("22-Dars (O'rta): Algoritmlar va lambda", `#include <algorithm>
#include <numeric>

vector<int> v = {5, 2, 9, 1};
sort(v.begin(), v.end());
sort(v.begin(), v.end(), greater<int>());    // kamayish tartibida
reverse(v.begin(), v.end());
auto it = find(v.begin(), v.end(), 9);
int yig = accumulate(v.begin(), v.end(), 0);
int mx = *max_element(v.begin(), v.end());

Lambda — nomsiz funksiya:
sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
auto juft = count_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
for_each(v.begin(), v.end(), [](int x) { cout << x << " "; });

[ ] ichida tashqi o'zgaruvchini olish mumkin: [&] havola bilan, [=] nusxa bilan.`),
            L("23-Dars (O'rta): Istisnolar va fayllar", `O'z istisnoingiz:
#include <stdexcept>

class BalansXato : public runtime_error {
public:
    BalansXato() : runtime_error("Mablag' yetarli emas") {}
};

void yech(double &balans, double s) {
    if (s > balans) throw BalansXato();
    balans -= s;
}

try {
    yech(balans, 500);
} catch (const BalansXato &e) {
    cout << e.what();
} catch (const exception &e) {
    cout << "Boshqa xato: " << e.what();
}

Qatorlab o'qish:
ifstream f("data.txt");
if (!f) { cout << "Fayl ochilmadi"; return 1; }
string qator;
while (getline(f, qator)) cout << qator << endl;

Faylga qo'shib yozish: ofstream f("log.txt", ios::app);`),
            L("24-Dars (O'rta): Ko'p fayli loyiha", `Katta dastur bir nechta faylga bo'linadi.

talaba.h:
#ifndef TALABA_H
#define TALABA_H
#include <string>
class Talaba {
    std::string ism;
public:
    Talaba(std::string i);
    void salom() const;
};
#endif

talaba.cpp:
#include "talaba.h"
#include <iostream>
Talaba::Talaba(std::string i) : ism(i) {}
void Talaba::salom() const { std::cout << ism; }

main.cpp:
#include "talaba.h"
int main() { Talaba t("Ali"); t.salom(); }

Kompilyatsiya:
g++ main.cpp talaba.cpp -o dastur -std=c++17

#ifndef — include guard, headerning ikki marta qo'shilishini oldini oladi. Katta loyihada CMake ishlatiladi.`),
            L("25-Dars (O'rta): Mini loyiha — Bank tizimi", `Maqsad: o'rganganlarni birlashtirish.

Talablar:
1. Hisob klassi: egasi (string), balans (double), yech() va qosh() metodlari
2. Balans yetmasa BalansXato istisnosi
3. Hisoblar vector<Hisob> da saqlanadi
4. Menyu: hisob ochish, pul qo'yish, yechish, ro'yxat
5. Ma'lumotlar data.txt ga saqlanadi va dastur ishga tushganda o'qiladi
6. Kodni hisob.h, hisob.cpp va main.cpp ga bo'ling

Boshlang'ich qismi:
class Hisob {
    string ega;
    double balans;
public:
    Hisob(string e, double b = 0) : ega(e), balans(b) {}
    void qosh(double s) { balans += s; }
    void yech(double s) {
        if (s > balans) throw runtime_error("Yetarli emas");
        balans -= s;
    }
    double getBalans() const { return balans; }
};

Qo'shimcha vazifa: hisoblarni balans bo'yicha sort() va lambda bilan saralang.`)
        );
        coursesData.Cpp.quiz.push(
            Q("Katta obyektni nusxa olmasdan va o'zgartirmasdan uzatish usuli?", ["T obj", "const T &obj", "T *obj", "static T obj"], 1),
            Q("Klass shabloni qaysi kalit so'z bilan boshlanadi?", ["generic", "class", "template", "type"], 2),
            Q("Bitta egasi bor smart pointer qaysi?", ["unique_ptr", "shared_ptr", "weak_ptr", "auto_ptr"], 0),
            Q("Takrorlanmaydigan, saralangan to'plam qaysi konteyner?", ["vector", "set", "queue", "stack"], 1),
            Q("Headerning ikki marta qo'shilishini nima oldini oladi?", ["#define faqat", "namespace", "#ifndef guard", "static"], 2)
        );

        coursesData.Cpp.lessons.push(
            L("26-Dars (Yuqori): Move semantics", `Nusxalash qimmat, ko'chirish (move) esa resursni "o'g'irlab" oladi.

lvalue — nomi bor ob'ekt (a). rvalue — vaqtinchalik qiymat (a + b, f()). T&& — rvalue havola.

class Bufer {
    int *d; size_t n;
public:
    Bufer(size_t n) : d(new int[n]), n(n) {}
    ~Bufer() { delete[] d; }
    Bufer(Bufer &&b) noexcept : d(b.d), n(b.n) {   // ko'chirish konstruktori
        b.d = nullptr; b.n = 0;
    }
    Bufer& operator=(Bufer &&b) noexcept {
        if (this != &b) { delete[] d; d = b.d; n = b.n; b.d = nullptr; b.n = 0; }
        return *this;
    }
};

Bufer a(1000);
Bufer b = move(a);   // a endi bo'sh, nusxa olinmadi

Rule of five: destruktor, nusxa va ko'chirish konstruktor/operatorlarini birga ko'rib chiqing. vector kabi konteynerlar move bo'lsa tezroq ishlaydi.`),
            L("27-Dars (Yuqori): Ko'p oqimlilik", `#include <thread>
#include <mutex>
#include <atomic>
#include <future>

void ish(int id) { cout << "Oqim " << id << endl; }

thread t1(ish, 1), t2(ish, 2);
t1.join();
t2.join();

Umumiy ma'lumotga bir vaqtda yozish — data race. Mutex bilan himoya:
mutex m;
int sanagich = 0;
void oshir() {
    for (int i = 0; i < 1000; i++) {
        lock_guard<mutex> q(m);
        sanagich++;
    }
}

Oddiy sonlar uchun atomic: atomic<int> a(0); a++;

async — natijani kutish:
future<int> f = async(launch::async, []{ return 42; });
cout << f.get();

Deadlock xavfi: bir nechta mutexni doim bir xil tartibda oling yoki scoped_lock ishlating.`),
            L("28-Dars (Yuqori): Zamonaviy C++ (17/20)", `#include <optional>
#include <variant>
#include <string_view>

optional<int> top(const vector<int> &v) {
    if (v.empty()) return nullopt;
    return v[0];
}
if (auto x = top(v)) cout << *x;

variant<int, string> val = "matn";
cout << get<string>(val);

string_view — nusxasiz matn ko'rinishi:
void chiqar(string_view s) { cout << s; }

Structured binding:
map<string, int> m = {{"Ali", 90}};
for (auto &[ism, ball] : m) cout << ism << ball;

if constexpr (shablon ichida kompilyatsiya vaqtida tanlash):
template <typename T>
void f(T x) { if constexpr (is_integral_v<T>) cout << "butun"; else cout << "boshqa"; }

C++20: concepts, ranges, modullar, std::format. Kompilyatsiya: g++ -std=c++20`),
            L("29-Dars (Yuqori): Dizayn andozalari", `Andoza — tez-tez uchraydigan muammoning sinalgan yechimi.

Singleton — bitta obyekt:
class Sozlama {
    Sozlama() {}
public:
    static Sozlama& ol() { static Sozlama s; return s; }
    Sozlama(const Sozlama&) = delete;
};

Factory — obyekt yaratishni yashirish:
unique_ptr<Hayvon> yarat(const string &tur) {
    if (tur == "it") return make_unique<It>();
    return make_unique<Mushuk>();
}

Observer — o'zgarishdan xabardor qilish:
class Kuzatuvchi { public: virtual void yangila(int) = 0; };
class Mavzu {
    vector<Kuzatuvchi*> r;
public:
    void qosh(Kuzatuvchi *k) { r.push_back(k); }
    void xabar(int x) { for (auto k : r) k->yangila(x); }
};

Andozani kerakli joydagina qo'llang, ortiqcha murakkablik yaratmang.`),
            L("30-Dars (Yuqori): Optimallashtirish", `Qoida: avval to'g'ri, keyin tez. Taxmin qilmang, o'lchang.

• Kompilyator: g++ -O2 (yoki -O3)
• vector ga ko'p element qo'shsangiz: v.reserve(n);
• Nusxa o'rniga: push_back(x) → emplace_back(args), uzatishda const T& yoki move
• Xotirada ketma-ket joylashuv (vector) bog'langan ro'yxatdan (list) tezroq: cache samaradorligi
• Sikl ichida bir xil hisobni qayta qilmang
• Tez kirish/chiqish:
  ios::sync_with_stdio(false); cin.tie(nullptr);

Vaqtni o'lchash:
#include <chrono>
auto t0 = chrono::steady_clock::now();
// ... kod ...
auto t1 = chrono::steady_clock::now();
cout << chrono::duration_cast<chrono::milliseconds>(t1 - t0).count();

Murakkablik: O(1) < O(log n) < O(n) < O(n log n) < O(n²). Yaxshi algoritm yomon kodni ham tezroq qilishi mumkin. Profiler: perf, gprof, Valgrind (xotira xatolari uchun).`),
            L("31-Dars (Yuqori): Daraxt va graf", `Binar qidiruv daraxti (BST):

struct Tugun {
    int q; Tugun *chap = nullptr, *ong = nullptr;
    Tugun(int q) : q(q) {}
};
Tugun* qosh(Tugun *t, int x) {
    if (!t) return new Tugun(x);
    if (x < t->q) t->chap = qosh(t->chap, x);
    else t->ong = qosh(t->ong, x);
    return t;
}
void chiqar(Tugun *t) {          // saralangan tartibda
    if (!t) return;
    chiqar(t->chap); cout << t->q << " "; chiqar(t->ong);
}

Graf — qo'shni ro'yxat va BFS (eng qisqa yo'l):
vector<vector<int>> g(n);
g[a].push_back(b); g[b].push_back(a);
queue<int> q; vector<int> uz(n, -1);
q.push(0); uz[0] = 0;
while (!q.empty()) {
    int v = q.front(); q.pop();
    for (int u : g[v]) if (uz[u] < 0) { uz[u] = uz[v] + 1; q.push(u); }
}

DFS rekursiya bilan, BFS navbat bilan yoziladi.`),
            L("32-Dars (Yuqori): Dinamik dasturlash", `DP — masalani kichik qismlarga bo'lib, natijalarni saqlash.

Fibonachchi (xotirali):
long long memo[100];
long long fib(int n) {
    if (n < 2) return n;
    if (memo[n]) return memo[n];
    return memo[n] = fib(n - 1) + fib(n - 2);
}
Oddiy rekursiya O(2^n), memo bilan O(n).

Ryukzak (0/1 knapsack):
vector<int> dp(W + 1, 0);
for (int i = 0; i < n; i++)
    for (int w = W; w >= og[i]; w--)
        dp[w] = max(dp[w], dp[w - og[i]] + narx[i]);
cout << dp[W];

Dijkstra (og'irlikli graf, eng qisqa yo'l): priority_queue bilan O((V+E) log V).

Mashq uchun: LeetCode va Codeforces da "Climbing Stairs", "Coin Change", "Longest Common Subsequence".`),
            L("33-Dars (Yuqori): Test, build va yakuniy loyiha", `CMakeLists.txt:
cmake_minimum_required(VERSION 3.16)
project(Dastur)
set(CMAKE_CXX_STANDARD 17)
add_executable(dastur main.cpp talaba.cpp)

Qurish:
cmake -B build
cmake --build build

Oddiy test:
#include <cassert>
assert(qosh(2, 3) == 5);

Professional testlash uchun GoogleTest yoki Catch2 ishlatiladi. Git: git init, git add ., git commit, GitHub ga joylash.

Yakuniy loyiha (portfolio uchun):
1. Konsolli yoki Qt/SFML bilan grafik dastur (masalan, Tic-Tac-Toe, to'p o'yini, vazifalar menejeri)
2. Klasslar va smart pointerlar, STL, istisnolar
3. Kamida bitta algoritm (qidiruv yoki saralash)
4. CMake bilan qurish, README yozish
5. GitHub ga joylash

Shu bosqichdan keyin siz C++ da Junior darajadagi loyihalarda ishlay olasiz.`)
        );
        coursesData.Cpp.quiz.push(
            Q("rvalue havola qanday yoziladi?", ["T&", "T&&", "T*", "const T"], 1),
            Q("Ikki oqim bir vaqtda umumiy o'zgaruvchiga yozsa nima yuz beradi?", ["Data race", "Kompilyatsiya xatosi", "Hech narsa", "Xotira kengayadi"], 0),
            Q("Qiymat bo'lmasligi mumkin bo'lgan natija uchun qaysi tur?", ["variant", "optional", "any", "tuple"], 1),
            Q("BFS qaysi ma'lumotlar tuzilmasidan foydalanadi?", ["stack", "set", "queue", "map"], 2)
        );

        coursesData.DataAnalytica.lessons.push(
            L("10-Dars (O'rta): Python OOP", `class Hisob:
    def __init__(self, ega, balans=0):
        self.ega = ega
        self.balans = balans

    def qosh(self, s):
        self.balans += s

    def __str__(self):
        return f"{self.ega}: {self.balans}"

h = Hisob("Ali", 100)
h.qosh(50)
print(h)   # Ali: 150

Vorislik:
class Jamgarma(Hisob):
    def foiz(self):
        self.balans *= 1.1

self — obyektning o'zi. __init__ konstruktor, __str__ chiqarish ko'rinishi. f"..." — matn ichiga qiymat qo'yish (f-string).`),
            L("11-Dars (O'rta): Generator va dekorator", `Generator — qiymatlarni birma-bir beradi, xotirani tejaydi:
def sanash(n):
    for i in range(n):
        yield i

for x in sanash(3):
    print(x)

sum(x * x for x in range(1000000))   # generator ifodasi

Dekorator — funksiyaga qo'shimcha xatti-harakat beradi:
import time

def vaqt(f):
    def ichki(*a, **k):
        t = time.time()
        natija = f(*a, **k)
        print("Vaqt:", time.time() - t)
        return natija
    return ichki

@vaqt
def sekin():
    return sum(range(10**6))

*args — ixtiyoriy sondagi parametr, **kwargs — nomli parametrlar.`),
            L("12-Dars (O'rta): Virtual muhit va loyiha tuzilishi", `Har loyiha uchun alohida muhit:

python -m venv venv
venv\\Scripts\\activate        # Windows
source venv/bin/activate     # Linux/Mac

pip install pandas requests
pip freeze > requirements.txt
pip install -r requirements.txt

Loyiha tuzilishi:
loyiha/
  main.py
  tahlil/
    __init__.py
    tozalash.py
  requirements.txt

Import: from tahlil.tozalash import tozala

Fayl boshqa joydan import qilinganda emas, to'g'ridan-to'g'ri ishga tushirilganda ishlashi uchun:
if __name__ == "__main__":
    main()`),
            L("13-Dars (O'rta): JSON va API", `import json, requests

JSON bilan ishlash:
data = {"ism": "Ali", "ball": [90, 85]}
matn = json.dumps(data, ensure_ascii=False)
asl = json.loads(matn)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

API dan ma'lumot olish:
r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
if r.status_code == 200:
    print(r.json()["title"])

Xatolarni ushlash:
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
except requests.RequestException as e:
    print("Xato:", e)

API kalitini kod ichiga yozmang, muhit o'zgaruvchisida saqlang (os.environ).`),
            L("14-Dars (O'rta): SQLite va Python", `import sqlite3

con = sqlite3.connect("talaba.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, ism TEXT, ball INT)")
cur.execute("INSERT INTO t (ism, ball) VALUES (?, ?)", ("Ali", 90))
con.commit()

for q in cur.execute("SELECT ism, ball FROM t WHERE ball > ?", (80,)):
    print(q)
con.close()

Doim ? bilan parametr bering, matnni qo'shib yozmang (SQL injection xavfi).

SQL chuqurroq:
CREATE INDEX idx_ball ON t(ball);       -- qidiruvni tezlashtiradi
BEGIN; UPDATE ...; COMMIT;              -- tranzaksiya
SELECT guruh, COUNT(*) c FROM t GROUP BY guruh HAVING c > 5;`),
            L("15-Dars (O'rta): pandas chuqurroq", `import pandas as pd

a = pd.read_csv("sotuv.csv")
b = pd.read_csv("mijoz.csv")

Jadvallarni birlashtirish:
df = a.merge(b, on="mijoz_id", how="left")

Pivot jadval:
p = df.pivot_table(index="shahar", columns="oy", values="summa", aggfunc="sum")

Ustun ustida amal:
df["soliq"] = df["summa"].apply(lambda x: x * 0.12)
df["sana"] = pd.to_datetime(df["sana"])
df["oy"] = df["sana"].dt.month

Bo'sh va takroriy qiymatlar:
df = df.dropna(subset=["summa"]).drop_duplicates()
df["summa"] = df["summa"].fillna(0)

Guruhlash va bir nechta natija:
df.groupby("shahar")["summa"].agg(["sum", "mean", "count"])`),
            L("16-Dars (O'rta): Mini loyiha — ma'lumotlar quvuri", `Maqsad: API dan ma'lumot olib, bazaga saqlash va tahlil qilish.

Qadamlar:
1. requests bilan ochiq API dan ma'lumot oling
2. pandas.DataFrame ga o'tkazing va tozalang
3. SQLite ga yozing: df.to_sql("malumot", con, if_exists="replace", index=False)
4. SQL bilan so'rov qiling: pd.read_sql("SELECT ... GROUP BY ...", con)
5. Grafik chizing va rasmga saqlang:
   import matplotlib.pyplot as plt
   df.plot(kind="bar"); plt.savefig("grafik.png")
6. Kodni funksiyalarga bo'ling: yukla(), tozala(), saqla(), tahlil()

Qo'shimcha vazifa: dasturni har kuni avtomatik ishga tushiring (cron yoki Windows Task Scheduler) va natijani faylga yozing.`)
        );
        coursesData.DataAnalytica.quiz.push(
            Q("Python da generator qiymat qaytarishda qaysi kalit so'z ishlatiladi?", ["return", "yield", "give", "emit"], 1),
            Q("SQL injection dan himoyalanish uchun nima qilinadi?", ["Parametrli so'rov (?)", "Matnni qo'shib yozish", "Katta harflar", "COMMIT"], 0),
            Q("Ikki DataFrame ni bog'lash metodi?", ["join_all()", "merge()", "link()", "attach()"], 1)
        );

        coursesData.Frontend.lessons.push(
            L("10-Dars (O'rta): Semantik HTML va qulaylik", `Ma'noli teglar qidiruv tizimlari va ekran o'quvchilariga sahifani tushunishga yordam beradi.

<header>
  <nav><a href="/">Bosh sahifa</a></nav>
</header>
<main>
  <section>
    <h2>Xizmatlar</h2>
    <article>...</article>
  </section>
</main>
<footer>Aloqa: info@sayt.uz</footer>

div o'rniga: header, nav, main, section, article, aside, footer.

Formada label:
<label for="ism">Ismingiz</label>
<input id="ism" type="text" required>

Qoidalar:
• Sahifada bitta h1, sarlavhalar tartibda (h1 → h2 → h3)
• Barcha rasmlarda alt
• Tugma uchun button, havola uchun a ishlating
• Matn va fon rangi o'rtasida yetarli kontrast bo'lsin`),
            L("11-Dars (O'rta): CSS: o'zgaruvchilar va animatsiya", `CSS o'zgaruvchilari:
:root {
  --asosiy: #2563eb;
  --radius: 12px;
}
.tugma { background: var(--asosiy); border-radius: var(--radius); }

Pseudo-class va element:
.tugma:hover { opacity: 0.85; }
li:nth-child(odd) { background: #f1f5f9; }
.sarlavha::after { content: " ★"; }
input:focus { outline: 2px solid var(--asosiy); }

Silliq o'tish va transformatsiya:
.karta { transition: transform 0.3s; }
.karta:hover { transform: translateY(-4px) scale(1.02); }

Animatsiya:
@keyframes paydo {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: none; }
}
.blok { animation: paydo 0.6s ease; }

position: sticky; top: 0; — sahifa aylanganda tepada qoladigan menyu.`),
            L("12-Dars (O'rta): Zamonaviy layout va qorong'u rejim", `Grid bilan o'zi moslashadigan kartalar:
.panjara {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

Shrift o'lchami ekranga qarab:
h1 { font-size: clamp(1.5rem, 4vw, 3rem); }

Grid maydonlari:
.sahifa {
  display: grid;
  grid-template-areas:
    "tepa tepa"
    "yon  asosiy"
    "past past";
  grid-template-columns: 200px 1fr;
}
.tepa { grid-area: tepa; }

Qorong'u rejim:
@media (prefers-color-scheme: dark) {
  :root { --fon: #0f172a; --matn: #f8fafc; }
}

Foydali: aspect-ratio: 16 / 9; gap, min(), max(), object-fit: cover (rasm uchun).`),
            L("13-Dars (O'rta): JavaScript chuqurroq", `Massiv metodlari:
const sonlar = [1, 2, 3, 4, 5];
const juft = sonlar.filter(x => x % 2 === 0);      // [2, 4]
const kv = sonlar.map(x => x * x);                  // [1, 4, 9, 16, 25]
const yig = sonlar.reduce((a, x) => a + x, 0);      // 15
const topildi = sonlar.find(x => x > 3);            // 4
sonlar.some(x => x > 4);  sonlar.every(x => x > 0);

Destructuring va spread:
const { ism, yosh } = { ism: "Ali", yosh: 20 };
const [a, b] = [10, 20];
const yangi = [...sonlar, 6];
const nusxa = { ...{ ism: "Ali" }, yosh: 21 };

Ixtiyoriy zanjir:
const shahar = foydalanuvchi?.manzil?.shahar ?? "Noma'lum";

Modullar:
// matem.js
export function qosh(a, b) { return a + b; }
// app.js
import { qosh } from "./matem.js";

== emas, === ishlating (turni ham solishtiradi).`),
            L("14-Dars (O'rta): Asinxron JavaScript", `Server javobini kutayotganda sahifa qotib qolmasligi kerak.

Promise va async/await:
async function yukla() {
  try {
    const r = await fetch("https://jsonplaceholder.typicode.com/users");
    if (!r.ok) throw new Error("Server xatosi: " + r.status);
    const users = await r.json();
    return users;
  } catch (e) {
    console.error(e.message);
  }
}

POST so'rov:
await fetch("/api/yubor", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ ism: "Ali" })
});

Bir nechta so'rovni parallel:
const [a, b] = await Promise.all([fetch(u1), fetch(u2)]);

Foydalanuvchiga yuklanish holatini (loading) va xatoni ko'rsating.`),
            L("15-Dars (O'rta): Formalar va hodisalar", `const forma = document.querySelector("#forma");

forma.addEventListener("submit", (e) => {
  e.preventDefault();                       // sahifa yangilanmasin
  const ism = forma.elements.ism.value.trim();
  if (ism.length < 2) {
    xato.textContent = "Ism kamida 2 harf bo'lsin";
    return;
  }
  royxat.push(ism);
  localStorage.setItem("royxat", JSON.stringify(royxat));
});

Saqlanganini o'qish:
const royxat = JSON.parse(localStorage.getItem("royxat") || "[]");

Event delegation — ko'p elementga bitta tinglovchi:
ul.addEventListener("click", (e) => {
  if (e.target.matches("button.ochir")) {
    e.target.closest("li").remove();
  }
});

HTML tomonidan tekshirish: required, minlength, type="email", pattern.`),
            L("16-Dars (O'rta): Mini loyiha — Valyuta kursi ilovasi", `Maqsad: API, DOM va localStorage ni birlashtirish.

Talablar:
1. Ikki ro'yxat (qaysi valyutadan va qaysi valyutaga) va summa kiritish maydoni
2. "Hisoblash" bosilganda API dan kurs olinadi (async/await)
3. Natija sahifada ko'rinadi, xato bo'lsa tushunarli xabar chiqadi
4. Oxirgi 5 ta hisob localStorage da saqlanadi va ro'yxatda ko'rinadi
5. Telefonda ham chiroyli (responsive), qorong'u rejim bilan

Papka:
valyuta/
  index.html
  style.css
  app.js

GitHub Pages ga joylash:
1. GitHub da yangi repo yarating
2. Fayllarni yuklang (yoki git push)
3. Settings → Pages → branch: main
4. Havola tayyor: foydalanuvchi.github.io/valyuta`)
        );
        coursesData.Frontend.quiz.push(
            Q("Sahifaning asosiy mazmuni qaysi semantik tegda bo'ladi?", ["<div>", "<main>", "<span>", "<body2>"], 1),
            Q("JavaScript da massivdan shartga mos elementlarni ajratish metodi?", ["map", "reduce", "filter", "push"], 2),
            Q("Formani yuborganda sahifa yangilanishini nima to'xtatadi?", ["e.stop()", "e.preventDefault()", "return null", "e.block()"], 1)
        );

        coursesData.Frontend.lessons.push(
            L("17-Dars (Yuqori): Git, GitHub va npm", `Git — kod versiyalarini boshqarish tizimi.

git init
git add .
git commit -m "Birinchi versiya"
git branch funksiya
git checkout funksiya     # yangi shoxda ishlash
git checkout main
git merge funksiya
git remote add origin https://github.com/ism/loyiha.git
git push -u origin main

Ish jarayoni: har yangi funksiya uchun alohida branch → GitHub da Pull Request → tekshiruvdan keyin main ga qo'shish.

.gitignore ga node_modules va maxfiy fayllarni (.env) yozing.

npm — JavaScript paketlari:
npm create vite@latest loyiha
cd loyiha
npm install
npm run dev       # ishlab chiqish serveri
npm run build     # tayyor versiya (dist papkasi)`),
            L("18-Dars (Yuqori): React asoslari", `React interfeysni komponentlarga bo'ladi.

function Salom({ ism }) {
  return <h1>Salom, {ism}!</h1>;
}

function App() {
  const royxat = ["HTML", "CSS", "JS"];
  return (
    <div>
      <Salom ism="Ali" />
      <ul>
        {royxat.map(t => <li key={t}>{t}</li>)}
      </ul>
    </div>
  );
}

Qoidalar:
• Komponent nomi katta harf bilan boshlanadi
• JSX da {} ichida JavaScript ifodasi yoziladi
• class o'rniga className ishlatiladi
• Ro'yxatdagi har elementga noyob key beriladi
• props — komponentga tashqaridan beriladigan ma'lumot (o'zgartirilmaydi)`),
            L("19-Dars (Yuqori): React: state va effect", `import { useState, useEffect } from "react";

function Sanagich() {
  const [n, setN] = useState(0);
  return <button onClick={() => setN(n + 1)}>Bosildi: {n}</button>;
}

Forma bilan:
const [ism, setIsm] = useState("");
<input value={ism} onChange={(e) => setIsm(e.target.value)} />

Ma'lumot yuklash (useEffect):
function Foydalanuvchilar() {
  const [data, setData] = useState([]);
  const [yuklanmoqda, setYuklanmoqda] = useState(true);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(r => r.json())
      .then(d => { setData(d); setYuklanmoqda(false); });
  }, []);       // [] — faqat birinchi chizilganda

  if (yuklanmoqda) return <p>Yuklanmoqda...</p>;
  return <ul>{data.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

State ni to'g'ridan-to'g'ri o'zgartirmang, doim setN kabi funksiya orqali yangilang.`),
            L("20-Dars (Yuqori): Router, Context va custom hook", `React Router — sahifalar o'rtasida o'tish:
npm install react-router-dom

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
<BrowserRouter>
  <Link to="/">Bosh</Link> <Link to="/haqida">Haqida</Link>
  <Routes>
    <Route path="/" element={<Bosh />} />
    <Route path="/haqida" element={<Haqida />} />
  </Routes>
</BrowserRouter>

Context — props zanjirisiz umumiy ma'lumot:
const Mavzu = createContext("yorug");
<Mavzu.Provider value="qorong'u"><App /></Mavzu.Provider>
const m = useContext(Mavzu);

Custom hook — qayta ishlatiladigan mantiq:
function useFetch(url) {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData);
  }, [url]);
  return data;
}

Katta ilovada holat boshqaruvi uchun Zustand yoki Redux Toolkit ishlatiladi.`),
            L("21-Dars (Yuqori): Tezlik va SEO", `Sayt sekin bo'lsa mijoz ketadi, qidiruvda ham pastga tushadi.

Tekshirish: Chrome DevTools → Lighthouse.

Tezlashtirish:
• Rasmni siqing va WebP formatidan foydalaning
• <img loading="lazy" width="400" height="300"> — kechiktirilgan yuklash
• CSS va JS ni minify qiling (Vite build buni o'zi qiladi)
• Keraksiz kutubxonalarni olib tashlang
• Shriftlarni kamroq oling (font-display: swap)

SEO uchun head da:
<title>Aniq va qisqa sarlavha</title>
<meta name="description" content="Sahifa haqida 150 belgigacha tavsif">
<meta property="og:title" content="Ulashganda ko'rinadigan sarlavha">
<meta property="og:image" content="https://sayt.uz/rasm.jpg">

Core Web Vitals: LCP (asosiy kontent tezligi), CLS (sakrab ketmaslik), INP (javob tezligi).`),
            L("22-Dars (Yuqori): Xavfsizlik, deploy va portfolio", `XSS dan himoya: foydalanuvchi kiritgan matnni innerHTML ga qo'ymang.
el.textContent = foydalanuvchiMatni;    // xavfsiz
el.innerHTML = foydalanuvchiMatni;      // xavfli!

Boshqa qoidalar:
• Faqat HTTPS ishlating
• API kalitlari va parollarni frontend kodiga yozmang — ular serverda turadi
• .env fayllarini GitHub ga yuklamang
• Kutubxonalarni yangilab turing: npm audit

Joylash (deploy): Netlify, Vercel yoki GitHub Pages. Repo ni ulang — har git push da sayt avtomatik yangilanadi. Domen (.uz yoki .com) alohida olinadi.

TypeScript — JavaScript ga turlar qo'shadi va xatolarni oldindan topadi: let yosh: number = 20;

Portfolio uchun 3 ta loyiha:
1. Biznes uchun landing sahifa (responsive, tez, SEO)
2. React bilan API ga ulangan ilova
3. Forma va saqlash bilan to'liq ishlaydigan vazifalar menejeri
Har biri GitHub da README bilan bo'lsin. Shundan so'ng frilanserda va mahalliy mijozlar bilan ishlashni boshlash mumkin.`)
        );
        coursesData.Frontend.quiz.push(
            Q("Foydalanuvchi matnini xavfsiz chiqarish uchun nima ishlatiladi?", ["innerHTML", "textContent", "outerHTML", "document.write"], 1),
            Q("React da holat (state) qaysi hook bilan saqlanadi?", ["useEffect", "useRef", "useState", "useMemo"], 2),
            Q("Rasmni kechiktirib yuklash atributi?", ["loading=\"lazy\"", "defer", "async", "preload"], 0)
        );

        coursesData.Java.lessons.push(
            L("9-Dars (O'rta): Generics va kolleksiyalar", `Generics — turni oldindan belgilash, xatolarni kompilyatsiyada topish.

List<Integer> sonlar = new ArrayList<>();
Set<String> set = new HashSet<>();            // takrorlanmaydi
Map<String, Integer> m = new HashMap<>();
Deque<Integer> navbat = new ArrayDeque<>();   // stack va queue uchun

for (Map.Entry<String, Integer> e : m.entrySet()) {
    System.out.println(e.getKey() + " " + e.getValue());
}

Saralash:
Collections.sort(sonlar);
list.sort(Comparator.comparing(Talaba::getBall).reversed());

Comparable — klassning tabiiy tartibi:
class Talaba implements Comparable<Talaba> {
    public int compareTo(Talaba b) { return Integer.compare(ball, b.ball); }
}

Generik metod:
static <T> void chiqar(List<T> r) { for (T x : r) System.out.println(x); }

Tanlash: ArrayList — tez o'qish, LinkedList — ko'p qo'shish/o'chirish, HashMap — tez qidiruv, TreeMap — saralangan.`),
            L("10-Dars (O'rta): OOP chuqurroq", `Obyektni solishtirish va chiqarish uchun metodlarni qayta yozing:

class Nuqta {
    final int x, y;
    Nuqta(int x, int y) { this.x = x; this.y = y; }

    @Override public boolean equals(Object o) {
        if (!(o instanceof Nuqta)) return false;
        Nuqta n = (Nuqta) o;
        return x == n.x && y == n.y;
    }
    @Override public int hashCode() { return Objects.hash(x, y); }
    @Override public String toString() { return "(" + x + ", " + y + ")"; }
}

equals qayta yozilsa, hashCode ham yoziladi (HashMap/HashSet to'g'ri ishlashi uchun).

enum:
enum Kun { DUSHANBA, SESHANBA, CHORSHANBA }
Kun k = Kun.DUSHANBA;

record — o'zgarmas ma'lumot klassi (Java 16+):
record Talaba(String ism, int ball) {}
var t = new Talaba("Ali", 90);
System.out.println(t.ism());

Interfeysda default metod:
interface Salom { default void ayt() { System.out.println("Salom"); } }`),
            L("11-Dars (O'rta): Istisnolar chuqurroq", `Checked istisnolar (IOException) — ushlash yoki throws bilan e'lon qilish shart.
Unchecked (RuntimeException, NullPointerException) — majburiy emas.

O'z istisnoingiz:
class BalansXato extends Exception {
    BalansXato(String xabar) { super(xabar); }
}

void yech(double s) throws BalansXato {
    if (s > balans) throw new BalansXato("Mablag' yetarli emas");
    balans -= s;
}

try {
    yech(500);
} catch (BalansXato e) {
    System.out.println(e.getMessage());
} finally {
    System.out.println("Doim bajariladi");
}

try-with-resources — resurs o'zi yopiladi:
try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
    System.out.println(br.readLine());
} catch (IOException e) {
    e.printStackTrace();
}

Bo'sh catch yozmang: xatoni hech bo'lmasa log ga yozing.`),
            L("12-Dars (O'rta): Fayllar (NIO) va vaqt", `import java.nio.file.*;
import java.util.*;

Faylni o'qish va yozish:
Path p = Path.of("data.txt");
List<String> qatorlar = Files.readAllLines(p);
Files.writeString(p, "Salom\\nDunyo");
Files.write(p, List.of("a", "b"), StandardOpenOption.APPEND);

if (Files.exists(p)) System.out.println(Files.size(p));

Katta fayl uchun qatorma-qator:
try (Stream<String> s = Files.lines(p)) {
    s.filter(q -> q.contains("xato")).forEach(System.out::println);
}

Sana va vaqt (java.time):
LocalDate bugun = LocalDate.now();
LocalDate d = LocalDate.of(2026, 11, 18);
System.out.println(bugun.plusDays(7));
long kun = ChronoUnit.DAYS.between(d, bugun);

Eski Date va SimpleDateFormat o'rniga doim java.time ishlating.`),
            L("13-Dars (O'rta): Lambda va Stream API", `Lambda — qisqa funksiya:
Comparator<String> c = (a, b) -> a.length() - b.length();
Runnable r = () -> System.out.println("Ishga tushdi");

Stream — ma'lumotlarni zanjir bilan qayta ishlash:
List<Integer> s = List.of(5, 2, 8, 1, 9);

List<Integer> juft = s.stream().filter(x -> x % 2 == 0).toList();
int yig = s.stream().mapToInt(Integer::intValue).sum();
List<Integer> kv = s.stream().map(x -> x * x).sorted().toList();
Optional<Integer> eng = s.stream().max(Integer::compare);
long soni = s.stream().filter(x -> x > 3).count();

Talabalarni guruhlash:
Map<String, List<Talaba>> g = talabalar.stream()
    .collect(Collectors.groupingBy(Talaba::getGuruh));

Metod havolasi: Talaba::getIsm (x -> x.getIsm() ning qisqasi).
Stream ni qayta ishlatib bo'lmaydi va asl ro'yxatni o'zgartirmaydi.`),
            L("14-Dars (O'rta): Optional, StringBuilder, text block", `Optional — null dan qochish:
Optional<String> ism = Optional.ofNullable(topIsm());
System.out.println(ism.orElse("Noma'lum"));
ism.ifPresent(i -> System.out.println(i));
String katta = ism.map(String::toUpperCase).orElse("");

NullPointerException oldini olish: metod null qaytarishi mumkin bo'lsa Optional qaytaring.

StringBuilder — ko'p qo'shish uchun tez:
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 5; i++) sb.append(i).append(", ");
sb.reverse();
System.out.println(sb.toString());

String.format va formatted:
String q = String.format("%s: %.2f so'm", "Narx", 12.5);

Text block (Java 15+):
String json = """
    {
      "ism": "Ali"
    }
    """;

var — turni kompilyator aniqlaydi (faqat lokal o'zgaruvchi): var royxat = new ArrayList<String>();`),
            L("15-Dars (O'rta): Mini loyiha — Kutubxona tizimi", `Maqsad: o'rganganlarni birlashtirish.

Klasslar:
• record Kitob(int id, String nom, String muallif)
• class Azo (ism, olgan kitoblar ro'yxati)
• class Kutubxona (kitoblar: Map<Integer, Kitob>, azolar: List<Azo>)

Imkoniyatlar:
1. Kitob qo'shish va o'chirish
2. Kitobni azoga berish va qaytarib olish (olingan kitobni ikkinchi marta berib bo'lmaydi: istisno)
3. Muallif yoki nom bo'yicha qidirish (Stream va filter)
4. Eng ko'p kitob olgan azolarni topish (sorted, limit)
5. Ma'lumotlar Files orqali faylga saqlanadi va ishga tushganda o'qiladi
6. Menyu Scanner orqali

Boshlang'ich qism:
Optional<Kitob> top(String nom) {
    return kitoblar.values().stream()
        .filter(k -> k.nom().equalsIgnoreCase(nom))
        .findFirst();
}

Qo'shimcha vazifa: kitoblarni muallif bo'yicha guruhlab (groupingBy) chiqaring.`)
        );
        coursesData.Java.quiz.push(
            Q("equals() qayta yozilsa, yana qaysi metodni yozish shart?", ["toString()", "hashCode()", "clone()", "finalize()"], 1),
            Q("Ro'yxatdan shart bo'yicha elementlarni tanlash Stream metodi?", ["map", "filter", "sorted", "limit"], 1),
            Q("Resurs avtomatik yopilishi uchun qaysi konstruksiya ishlatiladi?", ["try-with-resources", "finally faqat", "synchronized", "assert"], 0)
        );

        coursesData.Java.lessons.push(
            L("16-Dars (Yuqori): Maven va JUnit", `Maven — loyihani qurish va kutubxonalarni boshqarish.

pom.xml ga kutubxona qo'shish:
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>5.10.0</version>
  <scope>test</scope>
</dependency>

Buyruqlar:
mvn compile
mvn test
mvn package        # jar fayl yaratadi

Papka tuzilishi: src/main/java (kod), src/test/java (testlar).

JUnit test:
class HisobTest {
    @Test
    void yechish() {
        Hisob h = new Hisob(100);
        h.yech(30);
        assertEquals(70, h.getBalans());
    }
    @Test
    void yetarliEmas() {
        assertThrows(BalansXato.class, () -> new Hisob(10).yech(50));
    }
}

Qoida: yangi funksiya yozsangiz, uning testini ham yozing. Mockito — tashqi bog'liqlikni soxtalashtirish uchun.`),
            L("17-Dars (Yuqori): Ko'p oqimlilik", `Thread bilan:
Thread t = new Thread(() -> System.out.println("Oqim"));
t.start();
t.join();

Umumiy ma'lumotni himoyalash:
class Sanagich {
    private int n = 0;
    public synchronized void oshir() { n++; }
}
AtomicInteger a = new AtomicInteger();
a.incrementAndGet();

Oqimlar havzasi (ExecutorService):
ExecutorService ex = Executors.newFixedThreadPool(4);
Future<Integer> f = ex.submit(() -> 21 * 2);
System.out.println(f.get());
ex.shutdown();

CompletableFuture — zanjirli asinxron ish:
CompletableFuture.supplyAsync(() -> yukla())
    .thenApply(m -> m.toUpperCase())
    .thenAccept(System.out::println);

ConcurrentHashMap — ko'p oqimli xarita. Deadlock: bir nechta qulfni doim bir tartibda oling. Java 21 da virtual oqimlar: Thread.startVirtualThread(...)`),
            L("18-Dars (Yuqori): JVM ichki tuzilishi", `JVM xotirasi:
• Stack — metod chaqiruvlari va lokal o'zgaruvchilar (har oqimda alohida)
• Heap — barcha obyektlar (new bilan yaratilganlar)
• Metaspace — klass ma'lumotlari

Garbage Collector (GC) kerak bo'lmagan obyektlarni o'zi o'chiradi. Obyektga hech qanday havola qolmasa, u o'chirishga yaroqli bo'ladi.

Xotira oqishi (memory leak) Java da ham bo'ladi: static ro'yxatga qo'shib, hech qachon olib tashlamaslik, yopilmagan resurslar.

Sozlash:
java -Xms256m -Xmx1g -jar dastur.jar

Tahlil vositalari: jconsole, VisualVM, jstack (oqimlar), jmap (heap).

StackOverflowError — cheksiz rekursiya, OutOfMemoryError — heap to'lgan.

Tavsiya: GC ni qo'lda boshqarishga urinmang, avval kodni va ma'lumotlar tuzilmasini tekshiring.`),
            L("19-Dars (Yuqori): Spring Boot REST API", `Spring Boot — tayyor sozlangan veb-ilova.

start.spring.io da loyiha yarating: Spring Web, Spring Data JPA, H2 yoki PostgreSQL.

Entity:
@Entity
public class Talaba {
    @Id @GeneratedValue
    private Long id;
    private String ism;
    private int ball;
    // getter va setterlar
}

Repository (SQL yozmasdan):
public interface TalabaRepo extends JpaRepository<Talaba, Long> {
    List<Talaba> findByBallGreaterThan(int ball);
}

Controller:
@RestController
@RequestMapping("/api/talabalar")
public class TalabaController {
    private final TalabaRepo repo;
    public TalabaController(TalabaRepo repo) { this.repo = repo; }

    @GetMapping
    public List<Talaba> hammasi() { return repo.findAll(); }

    @PostMapping
    public Talaba qosh(@RequestBody Talaba t) { return repo.save(t); }
}

Ishga tushirish: mvn spring-boot:run, so'ng brauzerda localhost:8080/api/talabalar. Konstruktor orqali berilgan repo — dependency injection.`),
            L("20-Dars (Yuqori): SOLID va dizayn andozalari", `SOLID — toza kod tamoyillari:
• S — bir klass bitta vazifa
• O — kengaytirishga ochiq, o'zgartirishga yopiq
• L — voris klass ota klassning o'rnini bosa olsin
• I — katta interfeysni kichiklarga bo'ling
• D — aniq klassga emas, interfeysga bog'lanish

Qaramlikni inversiya qilish:
interface Xabarchi { void yubor(String m); }
class Email implements Xabarchi { public void yubor(String m) { ... } }
class Buyurtma {
    private final Xabarchi x;
    Buyurtma(Xabarchi x) { this.x = x; }   // Email yoki SMS berilishi mumkin
}

Builder andozasi:
Talaba t = new Talaba.Builder().ism("Ali").ball(90).build();

Strategy — algoritmni almashtirish:
interface Chegirma { double hisobla(double s); }
Chegirma oddiy = s -> s * 0.9;

Andozani kerak joyda ishlating; oddiy masalani murakkablashtirmang.`),
            L("21-Dars (Yuqori): Yakuniy loyiha va Pro yo'l", `Portfolio loyiha — Vazifalar menejeri (REST API):

1. Spring Boot + PostgreSQL
2. Foydalanuvchi, Vazifa entitylari (OneToMany bog'lanish)
3. CRUD endpointlar, xatolarni @ControllerAdvice bilan qaytarish
4. Kirish uchun Spring Security va JWT
5. JUnit testlar (kamida 10 ta)
6. Docker:
   FROM eclipse-temurin:21
   COPY target/app.jar app.jar
   ENTRYPOINT ["java", "-jar", "app.jar"]
7. README, GitHub ga joylash

Keyingi yo'l:
• Android uchun Kotlin va Jetpack Compose
• Mikroservislar, Kafka, Redis
• Bulut: AWS yoki Azure asoslari
• Oracle Java sertifikati

Shu darajadan keyin Junior Java Developer lavozimlariga murojaat qilish mumkin.`)
        );
        coursesData.Java.quiz.push(
            Q("Java da obyektlar qaysi xotira qismida saqlanadi?", ["Stack", "Heap", "Registr", "Metaspace faqat"], 1),
            Q("Spring Boot da REST kontroller qaysi annotatsiya bilan belgilanadi?", ["@Entity", "@Service", "@RestController", "@Component faqat"], 2),
            Q("SOLID dagi D harfi nimani bildiradi?", ["Interfeysga bog'lanish (inversiya)", "Ma'lumot", "Dizayn", "Delegatsiya"], 0)
        );

        coursesData.CSharp.lessons.push(
            L("9-Dars (O'rta): Kolleksiyalar va generics", `using System.Collections.Generic;

var sonlar = new List<int> { 5, 2, 9 };
var lugat = new Dictionary<string, int> { ["Ali"] = 90, ["Vali"] = 75 };
var set = new HashSet<string> { "a", "b", "a" };     // takrorlanmaydi
var navbat = new Queue<int>();  navbat.Enqueue(1);  navbat.Dequeue();
var stek = new Stack<int>();    stek.Push(1);       stek.Pop();

foreach (var juft in lugat) Console.WriteLine(juft.Key + " " + juft.Value);

if (lugat.TryGetValue("Ali", out int ball)) Console.WriteLine(ball);   // xavfsiz o'qish

Saralash:
sonlar.Sort();
talabalar.Sort((a, b) => b.Ball.CompareTo(a.Ball));

Generik metod va klass:
static T Katta<T>(T a, T b) where T : IComparable<T> {
    return a.CompareTo(b) > 0 ? a : b;
}
class Quti<T> { public T Qiymat { get; set; } }

IEnumerable<T> — foreach bilan aylanadigan har qanday ketma-ketlik.`),
            L("10-Dars (O'rta): OOP chuqurroq", `Abstrakt klass va interfeys:
abstract class Shakl {
    public abstract double Yuza();
    public override string ToString() => "Yuza: " + Yuza();
}
class Doira : Shakl {
    public double R { get; init; }
    public override double Yuza() => Math.PI * R * R;
}

Avtomatik property:
public string Ism { get; set; }
public int Yosh { get; private set; }

record — o'zgarmas ma'lumot turi (qiymat bo'yicha solishtiriladi):
public record Talaba(string Ism, int Ball);
var a = new Talaba("Ali", 90);
var b = a with { Ball = 95 };     // nusxa, bitta maydon o'zgargan

struct (qiymat turi) va class (havola turi) farqi:
• struct nusxalanadi, kichik ma'lumotlar uchun
• class havola orqali uzatiladi

static klass — obyekt yaratilmaydi (yordamchi metodlar uchun).
sealed class — undan meros olib bo'lmaydi.`),
            L("11-Dars (O'rta): Delegate, event va lambda", `Delegate — metodga havola:
delegate int Amal(int a, int b);
Amal qosh = (a, b) => a + b;
Console.WriteLine(qosh(2, 3));

Tayyor delegatlar:
Func<int, int> kv = x => x * x;          // qiymat qaytaradi
Action<string> chiqar = s => Console.WriteLine(s);   // qaytarmaydi
Predicate<int> juftmi = x => x % 2 == 0;

Event — "biror narsa yuz berdi" xabari:
class Hisob {
    public event Action<double> BalansOzgardi;
    private double balans;
    public void Qosh(double s) {
        balans += s;
        BalansOzgardi?.Invoke(balans);
    }
}

var h = new Hisob();
h.BalansOzgardi += b => Console.WriteLine("Yangi balans: " + b);
h.Qosh(100);

?. — obuna bo'lmagan bo'lsa xato bermaydi. Observer andozasining tayyor ko'rinishi shu.`),
            L("12-Dars (O'rta): LINQ chuqurroq", `using System.Linq;

var t = new List<Talaba> { new("Ali", "A", 90), new("Vali", "B", 70), new("Sami", "A", 85) };

var yaxshi = t.Where(x => x.Ball >= 80).OrderByDescending(x => x.Ball);
var ismlar = t.Select(x => x.Ism).ToList();
bool bormi = t.Any(x => x.Ball < 60);
int soni = t.Count(x => x.Guruh == "A");
double ort = t.Average(x => x.Ball);
var birinchi = t.FirstOrDefault(x => x.Ism == "Vali");   // topilmasa null

Guruhlash:
var guruh = t.GroupBy(x => x.Guruh)
             .Select(g => new { Guruh = g.Key, Ortacha = g.Average(x => x.Ball) });

Birlashtirish:
var natija = t.Join(fanlar, x => x.Id, f => f.TalabaId, (x, f) => new { x.Ism, f.Nom });

Muhim: LINQ kechiktirib bajariladi. Natijani darhol olish uchun ToList() yoki ToArray() chaqiring.`),
            L("13-Dars (O'rta): Istisnolar, fayllar va JSON", `O'z istisnoingiz:
class BalansXato : Exception {
    public BalansXato(string xabar) : base(xabar) { }
}

try {
    if (s > balans) throw new BalansXato("Mablag' yetarli emas");
} catch (BalansXato e) {
    Console.WriteLine(e.Message);
} catch (Exception e) {
    Console.WriteLine("Kutilmagan xato: " + e.Message);
} finally {
    Console.WriteLine("Doim bajariladi");
}

Fayllar:
File.WriteAllText("data.txt", "Salom");
string matn = File.ReadAllText("data.txt");
foreach (var q in File.ReadLines("data.txt")) Console.WriteLine(q);

using — resurs o'zi yopiladi:
using var sr = new StreamReader("data.txt");

JSON:
using System.Text.Json;
string json = JsonSerializer.Serialize(talaba);
Talaba t = JsonSerializer.Deserialize<Talaba>(json);`),
            L("14-Dars (O'rta): Zamonaviy C# imkoniyatlari", `Nullable:
int? son = null;
Console.WriteLine(son ?? 0);          // null bo'lsa 0
string? ism = null;
Console.WriteLine(ism?.Length);       // null bo'lsa null

Pattern matching:
object o = 42;
if (o is int n && n > 10) Console.WriteLine("Katta son: " + n);

switch ifodasi:
string baho = ball switch {
    >= 90 => "A'lo",
    >= 70 => "Yaxshi",
    _ => "Qoniqarli"
};

Tuple:
(int min, int max) Chegara(int[] a) => (a.Min(), a.Max());
var (mn, mx) = Chegara(new[] { 3, 1, 7 });

Qisqa konstruktor va using:
Talaba t = new("Ali", 90);
List<int> r = [1, 2, 3];       // C# 12 kolleksiya ifodasi

Top-level statements: Main metodini yozmasdan to'g'ridan-to'g'ri kod yozish mumkin.`),
            L("15-Dars (O'rta): Mini loyiha — Ombor tizimi", `Maqsad: o'rganganlarni birlashtirish.

Modellar:
• record Mahsulot(int Id, string Nom, decimal Narx, int Soni)
• class Ombor (Dictionary<int, Mahsulot>)

Imkoniyatlar:
1. Mahsulot qo'shish, o'chirish, sonini o'zgartirish
2. Sotib olish: soni yetmasa MahsulotXato istisnosi
3. Qidirish va narx bo'yicha saralash (LINQ)
4. Soni 5 tadan kam mahsulotlar haqida event orqali ogohlantirish
5. Jami ombor qiymati: Sum(x => x.Narx * x.Soni)
6. Ma'lumotlar JSON faylga saqlanadi va dastur ochilganda o'qiladi
7. Konsol menyusi

Boshlang'ich qism:
public event Action<Mahsulot> KamQoldi;

public void Sot(int id, int soni) {
    var m = mahsulotlar[id];
    if (m.Soni < soni) throw new MahsulotXato("Omborda yetarli emas");
    mahsulotlar[id] = m with { Soni = m.Soni - soni };
    if (mahsulotlar[id].Soni < 5) KamQoldi?.Invoke(mahsulotlar[id]);
}

Qo'shimcha vazifa: sotuvlar tarixini yozib boring va eng ko'p sotilgan mahsulotni toping.`)
        );
        coursesData.CSharp.quiz.push(
            Q("Qiymat qaytaradigan tayyor delegat turi qaysi?", ["Action", "Func", "Predicate faqat", "Event"], 1),
            Q("LINQ so'rovini darhol bajarish uchun nima chaqiriladi?", ["Run()", "Execute()", "ToList()", "Start()"], 2),
            Q("record turining asosiy xususiyati?", ["Qiymat bo'yicha solishtiriladi", "Faqat static", "Meros olib bo'lmaydi faqat", "Xotirada saqlanmaydi"], 0)
        );

        coursesData.CSharp.lessons.push(
            L("16-Dars (Yuqori): async/await va Task", `Server yoki fayldan ma'lumot kutayotganda dastur qotmasligi kerak.

static async Task<string> YuklaAsync(string url) {
    using var http = new HttpClient();
    return await http.GetStringAsync(url);
}

string matn = await YuklaAsync("https://jsonplaceholder.typicode.com/todos/1");

Parallel bajarish:
var t1 = YuklaAsync(u1);
var t2 = YuklaAsync(u2);
string[] natija = await Task.WhenAll(t1, t2);

Bekor qilish:
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(5));
await http.GetStringAsync(url, cts.Token);

Qoidalar:
• Asinxron metod nomi Async bilan tugaydi
• async void faqat event tinglovchida ishlating, boshqa joyda Task qaytaring
• .Result va .Wait() bilan bloklamang (deadlock xavfi)
• CPU ni band qiladigan ish uchun Task.Run(...)`),
            L("17-Dars (Yuqori): Entity Framework Core", `EF Core — SQL yozmasdan bazaga murojaat qilish (ORM).

dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet tool install --global dotnet-ef

Model va kontekst:
public class Talaba {
    public int Id { get; set; }
    public string Ism { get; set; } = "";
    public int Ball { get; set; }
}

public class MalumotDb : DbContext {
    public DbSet<Talaba> Talabalar => Set<Talaba>();
    protected override void OnConfiguring(DbContextOptionsBuilder o)
        => o.UseSqlite("Data Source=talaba.db");
}

Migratsiya:
dotnet ef migrations add Boshlangich
dotnet ef database update

Ishlatish:
using var db = new MalumotDb();
db.Talabalar.Add(new Talaba { Ism = "Ali", Ball = 90 });
await db.SaveChangesAsync();
var yaxshi = await db.Talabalar.Where(t => t.Ball > 80).ToListAsync();

Bog'lanish: bitta Guruhda ko'p Talaba — List<Talaba> navigatsiya property orqali. Include(...) bilan bog'liq ma'lumot olinadi.`),
            L("18-Dars (Yuqori): ASP.NET Core Web API", `dotnet new webapi -n TalabaApi
dotnet run

Minimal API:
var app = WebApplication.CreateBuilder(args).Build();
app.MapGet("/api/salom", () => "Salom");
app.MapPost("/api/talaba", (Talaba t) => Results.Created("/api/talaba/1", t));
app.Run();

Controller:
[ApiController]
[Route("api/[controller]")]
public class TalabalarController : ControllerBase {
    private readonly MalumotDb db;
    public TalabalarController(MalumotDb db) { this.db = db; }   // DI

    [HttpGet]
    public async Task<IEnumerable<Talaba>> Hammasi() => await db.Talabalar.ToListAsync();

    [HttpGet("{id}")]
    public async Task<ActionResult<Talaba>> Bitta(int id) {
        var t = await db.Talabalar.FindAsync(id);
        return t is null ? NotFound() : t;
    }
}

Dependency Injection: builder.Services.AddDbContext<MalumotDb>(); Middleware — so'rov yo'lidagi qatlamlar (autentifikatsiya, xatolarni ushlash, log). Swagger orqali API ni brauzerda sinash mumkin.`),
            L("19-Dars (Yuqori): Testlash, SOLID va DI", `xUnit bilan test:
dotnet new xunit -n Testlar

public class HisobTests {
    [Fact]
    public void Yechish_BalansKamayadi() {
        var h = new Hisob(100);
        h.Yech(30);
        Assert.Equal(70, h.Balans);
    }

    [Theory]
    [InlineData(5, 3, 8)]
    [InlineData(-1, 1, 0)]
    public void Qosh(int a, int b, int kutilgan) => Assert.Equal(kutilgan, Hisoblagich.Qosh(a, b));

    [Fact]
    public void Yetmasa_XatoBeradi() =>
        Assert.Throws<BalansXato>(() => new Hisob(10).Yech(50));
}

Moq bilan soxta bog'liqlik:
var m = new Mock<IXabarchi>();
var b = new Buyurtma(m.Object);
b.Tasdiqla();
m.Verify(x => x.Yubor(It.IsAny<string>()), Times.Once);

Interfeysga bog'langan kod oson test qilinadi — SOLID ning D tamoyili. Servislarni Program.cs da ro'yxatdan o'tkazing: AddScoped<IXabarchi, EmailXabarchi>();`),
            L("20-Dars (Yuqori): Unity bilan o'yin yaratish", `Unity da o'yin mantig'i C# skriptlarida yoziladi.

using UnityEngine;

public class Oyinchi : MonoBehaviour {
    public float tezlik = 5f;
    private Rigidbody2D rb;

    void Start() {                       // bir marta, boshida
        rb = GetComponent<Rigidbody2D>();
    }

    void Update() {                      // har kadrda
        float x = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(x * tezlik, rb.velocity.y);
        if (Input.GetKeyDown(KeyCode.Space)) rb.AddForce(Vector2.up * 300f);
    }

    void OnCollisionEnter2D(Collision2D c) {
        if (c.gameObject.CompareTag("Dushman")) Destroy(gameObject);
    }
}

Tushunchalar: GameObject, Component, Prefab (qayta ishlatiladigan obyekt), Scene, Collider, Rigidbody. public maydonlar Inspector da ko'rinadi.

Maslahat: Update ichida og'ir hisob va har kadrda GetComponent chaqirmang. Boshlash uchun kichik 2D o'yin (platformer yoki to'p o'yini) yarating.`),
            L("21-Dars (Yuqori): Yakuniy loyiha va Pro yo'l", `Portfolio loyiha — Vazifalar menejeri (Web API):

1. ASP.NET Core Web API + EF Core + PostgreSQL yoki SQLite
2. Foydalanuvchi va Vazifa modellari, CRUD endpointlar
3. JWT orqali kirish (autentifikatsiya) va rollar
4. Xatolarni umumiy middleware orqali qaytarish
5. xUnit testlar (kamida 10 ta)
6. Docker:
   FROM mcr.microsoft.com/dotnet/aspnet:8.0
   COPY publish/ .
   ENTRYPOINT ["dotnet", "TalabaApi.dll"]
7. README va GitHub ga joylash

Keyingi yo'l:
• Blazor — C# da veb-interfeys (JavaScript siz)
• .NET MAUI — Android va iOS ilovalari
• Azure asoslari, CI/CD (GitHub Actions)
• Mikroservislar va xabarlar navbati (RabbitMQ)
• Microsoft sertifikatlari (AZ-204)

Shu darajadan keyin Junior .NET Developer lavozimlariga murojaat qilish mumkin.`)
        );
        coursesData.CSharp.quiz.push(
            Q("Asinxron metod nima qaytaradi?", ["void faqat", "Task yoki Task<T>", "Thread", "Event"], 1),
            Q("EF Core da jadvalni ifodalovchi tur?", ["DbSet<T>", "List<T> faqat", "DataGrid", "Table<T>"], 0),
            Q("Unity da har kadrda chaqiriladigan metod?", ["Start", "Awake", "Update", "OnEnable"], 2)
        );

        coursesData.C.lessons.push(
            L("9-Dars (O'rta): Preprotsessor va ko'p fayli loyiha", `Preprotsessor kompilyatsiyadan oldin matnni qayta ishlaydi.

#define MAX 100
#define KV(x) ((x) * (x))       // makro, argumentni qavsga oling
#include <stdio.h>               // standart kutubxona
#include "hisob.h"               // o'zingizning fayl

Shartli kompilyatsiya:
#ifdef DEBUG
    printf("Sinov rejimi\\n");
#endif

hisob.h:
#ifndef HISOB_H
#define HISOB_H
int qosh(int a, int b);
#endif

hisob.c:
#include "hisob.h"
int qosh(int a, int b) { return a + b; }

main.c:
#include <stdio.h>
#include "hisob.h"
int main() { printf("%d\\n", qosh(2, 3)); return 0; }

Kompilyatsiya:
gcc main.c hisob.c -o dastur

static — o'zgaruvchi/funksiya faqat shu fayl ichida ko'rinadi, extern — boshqa fayldagi o'zgaruvchini ishlatish.`),
            L("10-Dars (O'rta): Ko'rsatkichlar chuqurroq", `Massiv nomi — birinchi elementga ko'rsatkich:
int a[3] = {10, 20, 30};
int *p = a;
printf("%d %d\\n", *p, *(p + 2));   // 10 30
p++;                                // keyingi element

Ko'rsatkichga ko'rsatkich:
int x = 5;
int *p1 = &x;
int **p2 = &p1;
printf("%d\\n", **p2);               // 5

Funksiya ko'rsatkichi:
int qosh(int a, int b) { return a + b; }
int (*amal)(int, int) = qosh;
printf("%d\\n", amal(2, 3));

Ikki o'lchamli dinamik massiv:
int **m = malloc(3 * sizeof(int*));
for (int i = 0; i < 3; i++) m[i] = malloc(4 * sizeof(int));
for (int i = 0; i < 3; i++) free(m[i]);
free(m);

const:
const int *p3;      // qiymatni o'zgartirib bo'lmaydi
int *const p4 = &x; // manzilni o'zgartirib bo'lmaydi`),
            L("11-Dars (O'rta): struct, union, enum, typedef", `typedef bilan qisqa nom:
typedef struct {
    char ism[30];
    int ball;
} Talaba;

Talaba t = {"Ali", 90};
Talaba *p = &t;
printf("%s %d\\n", p->ism, p->ball);     // ko'rsatkich orqali -> bilan

Talabalar massivi va saralash (qsort):
int solishtir(const void *a, const void *b) {
    return ((Talaba*)b)->ball - ((Talaba*)a)->ball;
}
qsort(royxat, n, sizeof(Talaba), solishtir);

union — bir xotira joyi, turli ko'rinish (bir vaqtda bittasi):
union Qiymat { int i; float f; };

enum — nomlangan sonlar:
typedef enum { DUSHANBA, SESHANBA, CHORSHANBA } Kun;
Kun k = SESHANBA;

sizeof(Talaba) — struct hajmi maydonlar yig'indisidan katta bo'lishi mumkin (hizalash, padding).`),
            L("12-Dars (O'rta): Bog'langan ro'yxat", `Massivdan farqli, bog'langan ro'yxat o'lchami o'zgaruvchan.

typedef struct Tugun {
    int q;
    struct Tugun *keyingi;
} Tugun;

Boshiga qo'shish:
Tugun* boshigaQosh(Tugun *bosh, int x) {
    Tugun *yangi = malloc(sizeof(Tugun));
    if (!yangi) return bosh;
    yangi->q = x;
    yangi->keyingi = bosh;
    return yangi;
}

Chiqarish:
for (Tugun *t = bosh; t != NULL; t = t->keyingi) printf("%d ", t->q);

O'chirish (qiymat bo'yicha):
Tugun* ochir(Tugun *bosh, int x) {
    if (!bosh) return NULL;
    if (bosh->q == x) { Tugun *k = bosh->keyingi; free(bosh); return k; }
    bosh->keyingi = ochir(bosh->keyingi, x);
    return bosh;
}

Hammasini bo'shatish: har tugunni free qiling. Stack va queue shu asosda quriladi.`),
            L("13-Dars (O'rta): Fayllar chuqurroq va argumentlar", `Ikkilik (binary) fayl:
Talaba t = {"Ali", 90};
FILE *f = fopen("data.bin", "wb");
fwrite(&t, sizeof(Talaba), 1, f);
fclose(f);

f = fopen("data.bin", "rb");
Talaba o;
while (fread(&o, sizeof(Talaba), 1, f) == 1) printf("%s\\n", o.ism);
fclose(f);

Fayl ichida yurish: fseek(f, 0, SEEK_END); long n = ftell(f); rewind(f);

Xatoni aniqlash:
#include <errno.h>
FILE *g = fopen("yoq.txt", "r");
if (!g) { perror("Fayl ochilmadi"); return 1; }

Buyruq qatori argumentlari:
int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) printf("%s\\n", argv[i]);
    return 0;
}
./dastur salom dunyo

Qator o'qishda fgets(satr, hajm, stdin) ishlating, gets ishlatmang (xavfli).`),
            L("14-Dars (O'rta): Mini loyiha — Talabalar bazasi", `Maqsad: struct, massiv, fayl va menyuni birlashtirish.

Talablar:
1. typedef struct Talaba { int id; char ism[30]; int ball; }
2. Dinamik massiv (malloc/realloc) da talabalar saqlanadi
3. Menyu: qo'shish, ko'rish, qidirish (ism bo'yicha), o'chirish, ball bo'yicha saralash (qsort)
4. Chiqishda ma'lumotlar data.bin ga yoziladi, ishga tushganda o'qiladi
5. Kiritishni tekshirish: scanf natijasi, ball 0-100 oralig'ida
6. Kod ikki-uch faylga bo'lingan: talaba.h, talaba.c, main.c

Boshlang'ich qism:
Talaba *royxat = NULL;
int n = 0, sigim = 0;

void qosh(Talaba t) {
    if (n == sigim) {
        sigim = sigim ? sigim * 2 : 4;
        royxat = realloc(royxat, sigim * sizeof(Talaba));
    }
    royxat[n++] = t;
}

Qo'shimcha vazifa: o'rtacha ball va eng yuqori ball egasini chiqaring.`)
        );
        coursesData.C.quiz.push(
            Q("Ko'rsatkich orqali struct maydoniga murojaat operatori?", [".", "->", "::", "&&"], 1),
            Q("Header faylning ikki marta qo'shilishini nima oldini oladi?", ["#ifndef guard", "static", "extern", "typedef"], 0),
            Q("Ikkilik faylga yozish funksiyasi?", ["fprintf", "fputs", "fwrite", "puts"], 2)
        );

        coursesData.C.lessons.push(
            L("15-Dars (Yuqori): Bit operatsiyalari", `Operatorlar: & (va), | (yoki), ^ (XOR), ~ (inkor), << va >> (siljitish).

unsigned char b = 0b00001100;     // 12
b |= (1 << 0);                    // 0-bitni yoqish
b &= ~(1 << 2);                   // 2-bitni o'chirish
b ^= (1 << 3);                    // 3-bitni almashtirish
int yoniqmi = (b >> 1) & 1;       // 1-bit qiymati

Misollar:
• x << 1 — ikkiga ko'paytirish, x >> 1 — ikkiga bo'lish
• (x & 1) — son toqmi
• (x & (x - 1)) == 0 — son 2 ning darajasimi

Bayroqlar (flag):
#define O_QILISH 1
#define YOZISH   2
#define ISHGA    4
int ruxsat = O_QILISH | YOZISH;
if (ruxsat & YOZISH) printf("Yozish mumkin\\n");

Bit maydon:
struct Bayroq { unsigned a : 1; unsigned b : 3; };

Endianness: sonning baytlari xotirada qanday tartibda turishi (little-endian: avval kichik bayt). Tarmoq va fayl formatlarida muhim. Embedded dasturlashda registrlar aynan bitlar orqali boshqariladi.`),
            L("16-Dars (Yuqori): Xotira xatolari va tahlil", `C da xavfsizlikni dasturchi o'zi ta'minlaydi. Tipik xatolar:

• Buffer overflow: char s[5]; strcpy(s, "juda uzun matn");   // xotirani buzadi
  To'g'risi: snprintf(s, sizeof(s), "%s", manba);
• Dangling pointer: free(p); *p = 1;   // o'chirilgan xotiraga murojaat
  free(p); p = NULL;
• Double free: bitta xotirani ikki marta free qilish
• Memory leak: malloc qilib free qilmaslik
• Initsializatsiya qilinmagan o'zgaruvchi: int x; printf("%d", x);
• Massiv chegarasidan chiqish

Vositalar:
gcc -g -fsanitize=address,undefined main.c -o dastur
./dastur           # xatoni aniq qatori bilan ko'rsatadi

valgrind --leak-check=full ./dastur    # xotira oqishini topadi

Yaxshi odatlar:
• Har malloc dan keyin NULL tekshirish
• Har malloc ga mos free
• Satr funksiyalarida hajmni cheklaydigan variantlar: strncpy, snprintf
• Ko'rsatkichni free dan keyin NULL qilish`),
            L("17-Dars (Yuqori): Jarayonlar va oqimlar (POSIX)", `Linux/macOS da. Jarayon yaratish:
#include <unistd.h>
#include <sys/wait.h>

pid_t p = fork();
if (p == 0) {
    printf("Bola jarayon\\n");
    return 0;
} else {
    wait(NULL);
    printf("Ota jarayon tugadi\\n");
}

Boshqa dastur ishga tushirish: execlp("ls", "ls", "-l", NULL);
Jarayonlar aloqasi: pipe(fd) — bir tomondan yozilib, ikkinchi tomondan o'qiladi.

Oqimlar (pthread):
#include <pthread.h>
pthread_mutex_t qulf = PTHREAD_MUTEX_INITIALIZER;
int sanagich = 0;

void *ish(void *arg) {
    for (int i = 0; i < 1000; i++) {
        pthread_mutex_lock(&qulf);
        sanagich++;
        pthread_mutex_unlock(&qulf);
    }
    return NULL;
}

pthread_t t1, t2;
pthread_create(&t1, NULL, ish, NULL);
pthread_create(&t2, NULL, ish, NULL);
pthread_join(t1, NULL);
pthread_join(t2, NULL);

Kompilyatsiya: gcc main.c -pthread. Mutex bo'lmasa, sanagich noto'g'ri chiqadi (data race).`),
            L("18-Dars (Yuqori): Tarmoq dasturlash (socket)", `Oddiy TCP server (Linux):

#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>

int s = socket(AF_INET, SOCK_STREAM, 0);

struct sockaddr_in a = {0};
a.sin_family = AF_INET;
a.sin_port = htons(8080);
a.sin_addr.s_addr = INADDR_ANY;

bind(s, (struct sockaddr*)&a, sizeof(a));
listen(s, 5);

int mijoz = accept(s, NULL, NULL);
char bufer[256];
int n = read(mijoz, bufer, sizeof(bufer) - 1);
bufer[n] = 0;
const char *javob = "Salom, mijoz!\\n";
write(mijoz, javob, strlen(javob));
close(mijoz);
close(s);

Klient: socket → connect → write/read → close.
Sinash: terminalda nc localhost 8080.

htons — sonni tarmoq bayt tartibiga o'tkazadi. Ko'p mijoz uchun har mijozga alohida oqim yoki select/poll/epoll ishlatiladi. Har bir funksiya natijasini (-1) tekshiring.`),
            L("19-Dars (Yuqori): Makefile, gdb va gcc bayroqlari", `Makefile:
CC = gcc
CFLAGS = -Wall -Wextra -g -O2
dastur: main.o hisob.o
\t$(CC) $(CFLAGS) -o dastur main.o hisob.o
%.o: %.c
\t$(CC) $(CFLAGS) -c $<
tozala:
\trm -f *.o dastur

Buyruq: make, make tozala. (Buyruq satri oldidan Tab belgisi bo'lishi shart.)

Foydali bayroqlar:
• -Wall -Wextra — ogohlantirishlarni yoqish (ularga e'tibor bering)
• -g — nosozlikni tuzatish ma'lumoti
• -O2 — optimallashtirish
• -std=c11

gdb bilan nosozlikni topish:
gdb ./dastur
break main
run
next          # keyingi qator
step          # funksiya ichiga kirish
print x       # qiymatni ko'rish
backtrace     # chaqiruvlar zanjiri

Segmentation fault chiqsa: gdb da run, so'ng backtrace — xato qaysi qatorda ekani ko'rinadi.`),
            L("20-Dars (Yuqori): Yakuniy loyiha va Pro yo'l", `Portfolio loyiha — kichik HTTP server yoki oddiy shell:

HTTP server:
1. TCP socket ochish va mijoz so'rovini o'qish
2. So'rovdan GET yo'lini ajratib olish
3. Mos faylni o'qib, HTTP javob sarlavhasi bilan qaytarish (200 va 404)
4. Har mijozga alohida oqim
5. Xotira oqishsiz: valgrind va AddressSanitizer dan toza o'tsin
6. Makefile, README, GitHub ga joylash

Oddiy shell: qatorni o'qish → so'zlarga bo'lish → fork va execvp → wait; ichki buyruqlar (cd, exit).

Keyingi yo'l:
• Embedded: Arduino, STM32 — C da mikrokontrollerlar dasturlash
• Linux tizim dasturlash va drayverlar, yadro (kernel) ga hissa
• Ma'lumotlar tuzilmalari va algoritmlarni C da mustahkamlash
• C++ ga o'tish (siz allaqachon asosni bilasiz)
• Xavfsizlik va reverse engineering (xotira, assembler bilimi)

Shu darajadan keyin sistemali dasturlash yo'nalishidagi Junior lavozimlarga tayyor bo'lasiz.`)
        );
        coursesData.C.quiz.push(
            Q("Sonning toq ekanini tekshirish bit ifodasi?", ["x | 1", "x & 1", "x ^ 1", "x << 1"], 1),
            Q("Xotira oqishini topuvchi vosita?", ["Valgrind", "make", "strcpy", "typedef"], 0),
            Q("Yangi jarayon yaratuvchi funksiya?", ["exec()", "spawn()", "fork()", "create()"], 2)
        );

        coursesData.DataAnalytica.lessons.push(
            L("17-Dars (Yuqori): Toza Python", `Tur ko'rsatmalari kodni tushunarli qiladi va xatolarni oldindan topadi (mypy):

def narx_hisobla(narx: float, soni: int = 1) -> float:
    return narx * soni

dataclass — kam kod bilan ma'lumot klassi:
from dataclasses import dataclass, field

@dataclass
class Talaba:
    ism: str
    ball: int = 0
    fanlar: list[str] = field(default_factory=list)

t = Talaba("Ali", 90)
print(t)          # Talaba(ism='Ali', ball=90, fanlar=[])

pathlib va logging:
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

p = Path("data") / "natija.txt"
p.parent.mkdir(exist_ok=True)
p.write_text("Salom", encoding="utf-8")
log.info("Fayl yozildi: %s", p)

Buyruq qatori dasturi:
import argparse
a = argparse.ArgumentParser()
a.add_argument("fayl")
a.add_argument("--soni", type=int, default=5)
args = a.parse_args()

print() o'rniga logging ishlating: darajalari bor, faylga yozish mumkin.`),
            L("18-Dars (Yuqori): asyncio, oqimlar va GIL", `Python da GIL bir vaqtda faqat bitta oqim kodni bajarishiga yo'l qo'yadi.

• Kutish ko'p ishlar (tarmoq, fayl): asyncio yoki threading
• Hisoblash ko'p ishlar: multiprocessing

asyncio:
import asyncio, aiohttp

async def yukla(sess, url):
    async with sess.get(url) as r:
        return await r.text()

async def main():
    async with aiohttp.ClientSession() as sess:
        sahifalar = await asyncio.gather(*(yukla(sess, u) for u in urllar))
    print(len(sahifalar))

asyncio.run(main())

Ko'p jarayon:
from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor() as ex:
    natija = list(ex.map(og_ir_hisob, range(10)))

Ko'p oqim:
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=8) as ex:
    javoblar = list(ex.map(yukla_oddiy, urllar))

Qoida: asyncio da bloklaydigan funksiya (time.sleep, requests) chaqirmang, await asyncio.sleep() ishlating.`),
            L("19-Dars (Yuqori): FastAPI bilan backend", `pip install fastapi uvicorn

main.py:
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Talaba(BaseModel):
    ism: str
    ball: int

db: list[Talaba] = []

@app.post("/talaba")
def qosh(t: Talaba):
    db.append(t)
    return t

@app.get("/talaba/{i}")
def bitta(i: int):
    if i >= len(db):
        raise HTTPException(status_code=404, detail="Topilmadi")
    return db[i]

Ishga tushirish: uvicorn main:app --reload
Hujjatlar o'zi chiqadi: localhost:8000/docs

pydantic kiruvchi ma'lumotni avtomatik tekshiradi (turi noto'g'ri bo'lsa 422 xato qaytadi).

Bazaga ulash: SQLAlchemy yoki sqlite3 + Depends orqali sessiya berish. Autentifikatsiya uchun JWT (python-jose) ishlatiladi. Parollarni faqat xesh (hash) holida saqlang.`),
            L("20-Dars (Yuqori): Testlash va sifat", `pytest bilan test:
pip install pytest

hisob.py:
def foiz(summa, p):
    if p < 0:
        raise ValueError("Foiz manfiy bo'lmasin")
    return summa * p / 100

test_hisob.py:
import pytest
from hisob import foiz

def test_oddiy():
    assert foiz(200, 10) == 20

def test_xato():
    with pytest.raises(ValueError):
        foiz(100, -5)

@pytest.mark.parametrize("s,p,kutilgan", [(100, 10, 10), (50, 50, 25)])
def test_koproq(s, p, kutilgan):
    assert foiz(s, p) == kutilgan

Ishga tushirish: pytest -v

Fixture va mock:
@pytest.fixture
def talaba():
    return Talaba("Ali", 90)

from unittest.mock import patch
with patch("modul.requests.get") as m:
    m.return_value.json.return_value = {"kurs": 12500}

Kod sifati: ruff yoki black (format), mypy (turlar). Docker:
FROM python:3.12-slim
COPY . /app
RUN pip install -r /app/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]`),
            L("21-Dars (Yuqori): Ma'lumotlar tahlili Pro", `NumPy — tez sonli hisob:
import numpy as np
a = np.array([1, 2, 3, 4])
print(a * 2, a.mean(), a.std())
m = np.arange(6).reshape(2, 3)

Vizualizatsiya:
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(df["narx"])
sns.boxplot(x="shahar", y="narx", data=df)
plt.savefig("grafik.png")

Tahlil bosqichlari: savol qo'yish → ma'lumot yig'ish → tozalash → o'rganish (EDA) → xulosa. df.corr() — o'zgaruvchilar orasidagi bog'liqlik.

Mashina o'rganishiga kirish (scikit-learn):
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[["maydon", "xona"]]
y = df["narx"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_tr, y_tr)
print(model.score(X_te, y_te))      # 1 ga yaqin bo'lsa yaxshi

Muhim: modelni o'qitilmagan (test) ma'lumotda tekshiring, aks holda natija aldaydi (overfitting).

pandas tezlashtirish: for sikl o'rniga vektorli amallar, kerakli ustunlarnigina o'qing (usecols), turlarni kichraytiring.`),
            L("22-Dars (Yuqori): SQL Pro va yakuniy loyiha", `CTE (WITH) — murakkab so'rovni qismlarga bo'lish:
WITH oylik AS (
    SELECT strftime('%Y-%m', sana) AS oy, SUM(summa) AS jami
    FROM sotuv GROUP BY oy
)
SELECT oy, jami FROM oylik WHERE jami > 1000000;

Oyna funksiyalari:
SELECT ism, guruh, ball,
       RANK() OVER (PARTITION BY guruh ORDER BY ball DESC) AS orin,
       AVG(ball) OVER (PARTITION BY guruh) AS guruh_ortacha
FROM talabalar;

Qism so'rov:
SELECT ism FROM talabalar WHERE ball > (SELECT AVG(ball) FROM talabalar);

Indeks va tahlil:
CREATE INDEX idx_sana ON sotuv(sana);
EXPLAIN QUERY PLAN SELECT * FROM sotuv WHERE sana > '2026-01-01';

Normalizatsiya: ma'lumotni takrorlamang, alohida jadvallarga bo'ling va FOREIGN KEY bilan bog'lang.

Yakuniy loyiha — Sotuv tahlili va hisobot tizimi:
1. API/CSV dan ma'lumot yig'ish va tozalash (pandas)
2. SQLite yoki PostgreSQL ga saqlash
3. FastAPI orqali natijani qaytarish (/hisobot endpointi)
4. pytest testlar, Docker, README, GitHub
5. Qo'shimcha: Telegram bot (aiogram) orqali kunlik hisobotni yuborish

Shundan keyin Junior Python/Data Analyst lavozimlariga murojaat qilish mumkin.`)
        );
        coursesData.DataAnalytica.quiz.push(
            Q("Python da hisoblash og'ir ishlarni parallel bajarish uchun nima mos?", ["asyncio", "multiprocessing", "logging", "dataclass"], 1),
            Q("FastAPI da kiruvchi ma'lumotni tekshiruvchi kutubxona?", ["pydantic", "pytest", "numpy", "argparse"], 0),
            Q("SQL da guruh ichida o'rin berish funksiyasi?", ["COUNT", "RANK() OVER", "LIMIT", "MERGE"], 1)
        );

        coursesData.EnglishIT.lessons.push(
            L("4-Dars: Salomlashish va tanishuv", `Hello [həˈləʊ] — Salom
Hi [hai] — Salom (do'stona)
Good morning [gʊd ˈmɔːnɪŋ] — Xayrli tong
Good evening [gʊd ˈiːvnɪŋ] — Xayrli kech
Goodbye [gʊdˈbai] — Xayr
Thank you [θæŋk juː] — Rahmat
Please [pliːz] — Iltimos
Sorry [ˈsɒri] — Kechirasiz

[θ] tovushi: tilni tishlar orasiga qo'yib havo chiqaring (thank, three, think).

Tanishuv:
— What is your name? [wɒt iz jɔː neim] — Ismingiz nima?
— My name is Ali. — Mening ismim Ali.
— How are you? — Yaxshimisiz?
— I am fine, thank you. And you? — Yaxshiman, rahmat. O'zingiz-chi?
— Nice to meet you. [nais tə miːt juː] — Tanishganimdan xursandman.
— Where are you from? — Qayerdansiz?
— I am from Uzbekistan. — Men O'zbekistondanman.

Mashq: o'zingiz haqingizda 4 ta gap yozing va ovoz chiqarib ayting.`),
            L("5-Dars: Sonlar, vaqt, kun va oylar", `Sonlar:
1 one, 2 two, 3 three, 4 four, 5 five, 6 six, 7 seven, 8 eight, 9 nine, 10 ten
11 eleven, 12 twelve, 13 thirteen (13-19 da -teen), 20 twenty, 30 thirty, 100 a hundred, 1000 a thousand

Farqlang: thirteen [θɜːˈtiːn] (urg'u oxirida) va thirty [ˈθɜːti] (urg'u boshida).

Hafta kunlari: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
Oylar: January, February, March, April, May, June, July, August, September, October, November, December

Vaqt:
What time is it? — Soat necha?
It is 5 o'clock. — Soat 5.
It is half past six. — Olti yarim.
It is a quarter to nine. — Nolga chorak qoldi (8:45).

Sana: Today is Wednesday, 18th of November.
Kun qismlari: morning, afternoon, evening, night`),
            L("6-Dars: Artikllar, ko'plik va ko'rsatish olmoshlari", `Artikl:
• a — undosh tovushdan oldin: a book, a car
• an — unli tovushdan oldin: an apple, an hour
• the — aniq narsa: The book is on the table.

Ko'plik:
book → books, car → cars
box → boxes, bus → buses (s, x, ch, sh dan keyin -es)
city → cities (undosh + y)
Qoidasiz: man → men, woman → women, child → children, foot → feet, person → people

this / that / these / those:
This is a laptop. — Bu noutbuk (yaqin, bitta).
That is a server. — Anavi server (uzoq, bitta).
These are books. — Bular kitoblar (yaqin, ko'p).
Those are computers. — Anavilar kompyuterlar (uzoq, ko'p).

Sanalmaydigan otlar (a/an yo'q): water, information, advice, money, software.
Noto'g'ri: an information. To'g'ri: some information.`),
            L("7-Dars: Present Continuous va Past Simple", `Present Continuous — hozir bo'layotgan ish: am/is/are + fe'l-ing
I am learning English. — Men ingliz tilini o'rganyapman.
She is writing code. — U kod yozyapti.
They are not working. — Ular ishlamayapti.
Are you listening? — Tinglayapsizmi?

Past Simple — o'tgan zamon.
To'g'ri fe'llar: fe'l + ed
work → worked, play → played, study → studied

Noto'g'ri fe'llar (yodlash kerak):
go — went, see — saw, have — had, do — did, make — made
write — wrote, eat — ate, buy — bought, take — took, come — came

Gap tuzish:
I went to the office yesterday. — Kecha ofisga bordim.
Did you see the error? — Xatoni ko'rdingizmi?
I did not write the code. — Men kodni yozmadim.

did dan keyin fe'l asl holida: Did you go? (went emas).

-ed oxiri: worked [wɜːkt], played [pleid], wanted [ˈwɒntɪd].`),
            L("8-Dars: Kelasi zamon va modal fe'llar", `Kelasi zamon:
will + fe'l — joyida qilingan qaror: I will help you.
am/is/are going to + fe'l — oldindan reja: I am going to study tomorrow.

Modal fe'llar (keyingi fe'l asl holida, -s yo'q):
can — qila olish: I can code in C++.
could — qila olardi / iltimos: Could you help me?
must — majburiyat: You must save the file.
should — maslahat: You should test your code.
may — ruxsat/ehtimol: May I come in?
have to — zaruriyat: I have to work on Monday.

Inkor: cannot (can't), must not (mustn't), should not (shouldn't)

Savol: Can you help me? Should I restart the server?

Mashq: kelasi hafta uchun 5 ta rejangizni going to bilan yozing.`),
            L("9-Dars: Kundalik so'zlashuv iboralari", `Yo'l so'rash:
Excuse me, where is the bank? — Kechirasiz, bank qayerda?
Turn left / right. — Chapga / o'ngga buring.
Go straight. — To'g'riga yuring.
It is next to the hotel. — U mehmonxonaning yonida.

Do'kon va restoran:
How much is it? — Bu qancha turadi?
Can I pay by card? — Karta bilan to'lasam bo'ladimi?
I would like a cup of tea. — Men bir choy olmoqchiman.
The bill, please. — Hisobni olib keling.

Tushunmaganda:
Sorry, I don't understand. — Kechirasiz, tushunmadim.
Could you repeat that, please? — Takrorlay olasizmi?
Could you speak more slowly? — Sekinroq gapira olasizmi?
What does this word mean? — Bu so'z nimani anglatadi?

Yordam so'rash:
Can you help me, please? — Menga yordam bera olasizmi?
I need a doctor. — Menga shifokor kerak.

Maslahat: har kuni 5 ta yangi ibora yodlang va ularni ovoz chiqarib takrorlang.`),
            L("10-Dars: IT ingliz tili va ish suhbati", `Dasturchilar uchun asosiy so'zlar:
function — funksiya, variable — o'zgaruvchi, array — massiv
loop — sikl, condition — shart, class — klass, object — obyekt
bug — xato, fix — tuzatish, deploy — joylash, release — chiqarish
request — so'rov, response — javob, database — ma'lumotlar bazasi
repository — ombor, commit — saqlash, branch — shox, merge — qo'shish

Hujjat (documentation) o'qish iboralari:
Required — majburiy, Optional — ixtiyoriy, Deprecated — eskirgan
Returns — qaytaradi, Throws — xato beradi, Parameters — parametrlar

Ish suhbatida:
Tell me about yourself. — O'zingiz haqingizda gapirib bering.
I have experience with C++ and web development. — C++ va veb dasturlashda tajribam bor.
I am learning Python and SQL. — Python va SQL ni o'rganyapman.
I can work in a team. — Jamoada ishlay olaman.

Email yozish:
Dear Mr. Smith, — Hurmatli janob Smit,
I am writing to ask about the job. — Ish haqida so'rash uchun yozyapman.
Thank you for your time. — Vaqtingiz uchun rahmat.
Best regards, Ali — Hurmat bilan, Ali

Maslahat: GitHub README va Stack Overflow javoblarini har kuni o'qing, shunda texnik ingliz tili tez rivojlanadi.`)
        );
        coursesData.EnglishIT.quiz.push(
            Q("Unli tovushdan oldin qaysi artikl ishlatiladi?", ["a", "an", "the faqat", "hech qaysi"], 1),
            Q("'go' fe'lining Past Simple shakli?", ["goed", "gone", "went", "going"], 2),
            Q("'Could you repeat that, please?' qanday ma'noda?", ["Takrorlay olasizmi?", "Xayr", "Rahmat", "Qayerdansiz?"], 0),
            Q("'Deploy' so'zining ma'nosi?", ["Xato", "Joylash (ishga tushirish)", "Shox", "Funksiya"], 1)
        );

        function getCourseData(key) {
            if (coursesData[key]) return coursesData[key];
            return {
                title: key + " Kursi",
                lessons: [
                    { title: "1-Dars: Kirish va asosiy tushunchalar", content: "Bu darslik orqali siz asosiy boshlang'ich bilimga ega bo'lasiz va bosqichma-bosqich Pro darajaga chiqasiz." },
                    { title: "2-Dars: Amaliy mashg'ulotlar", content: "Amaliyot davomida real vazifalarni bajarishni o'rganasiz." }
                ],
                quiz: [
                    { q: "Ushbu yo'nalish bo'yicha asosiy tushuncha nima?", opts: ["Mantiq", "Tezlik", "Xotira", "Barchasi to'g'ri"], correct: 3 },
                    { q: "Pro darajaga chiqish uchun nima qilish kerak?", opts: ["Ko'p amaliyot", "Faqat o'qish", "Dam olish", "Hech narsa"], correct: 0 }
                ],
                game: { task: "Mantiqiy topshiriq: To'g'ri variantni tanlang.", opts: ["Variant A", "Variant B", "Variant C", "Variant D"], correct: 0 }
            };
        }

        let currentCourseKey = '';
        let currentQuizIndex = 0;
        let score = 0;

        function openCourse(courseKey) {
            currentCourseKey = courseKey;
            currentQuizIndex = 0;
            score = 0;

            document.getElementById('mainMenu').classList.add('hidden');
            document.getElementById('courseView').classList.remove('hidden');
            
            let data = getCourseData(courseKey);
            document.getElementById('courseTitle').innerText = data.title;

            let lessonsHtml = "";
            data.lessons.forEach((les, idx) => {
                lessonsHtml += `<div class="lesson-item" onclick="openLessonModal(${idx})"><span>${les.title}</span> <b>📖 O'qish</b></div>`;
            });
            document.getElementById('lessonsList').innerHTML = lessonsHtml;

            loadQuizQuestion();
            loadGame();

            switchTab('lessons', document.querySelector('.tab-btn'));
        }

        function openLessonModal(index) {
            let data = getCourseData(currentCourseKey);
            let les = data.lessons[index];
            document.getElementById('modalLessonTitle').innerText = les.title;
            document.getElementById('modalLessonBody').innerText = les.content;
            document.getElementById('lessonModal').classList.remove('hidden');
        }

        function closeLessonModal() {
            document.getElementById('lessonModal').classList.add('hidden');
        }

        function loadQuizQuestion() {
            let data = getCourseData(currentCourseKey);
            if (currentQuizIndex < data.quiz.length) {
                let qData = data.quiz[currentQuizIndex];
                document.getElementById('quizQuestion').innerText = `(${currentQuizIndex+1}/${data.quiz.length}) ${qData.q}`;
                
                let optsHtml = "";
                qData.opts.forEach((opt, idx) => {
                    optsHtml += `<button onclick="checkQuizAnswer(${idx}, ${qData.correct})">${opt}</button>`;
                });
                document.getElementById('quizOptions').innerHTML = optsHtml;
                document.getElementById('quizContainer').classList.remove('hidden');
                document.getElementById('quizResultArea').classList.add('hidden');
            } else {
                document.getElementById('quizContainer').classList.add('hidden');
                document.getElementById('quizResultArea').classList.remove('hidden');
                let total = data.quiz.length;
                let percent = Math.round((score / total) * 100);
                document.getElementById('finalScoreText').innerText = `Siz ${total} ta savoldan ${score} tasiga to'g'ri javob berdingiz! Natijangiz: ${percent}%.`;
            }
        }

        function checkQuizAnswer(selected, correct) {
            if (selected === correct) {
                score += 1;
            }
            currentQuizIndex++;
            loadQuizQuestion();
        }

        function restartQuiz() {
            currentQuizIndex = 0;
            score = 0;
            loadQuizQuestion();
        }

        function loadGame() {
            let data = getCourseData(currentCourseKey);
            document.getElementById('gameTask').innerText = data.game.task;
            let optsHtml = "";
            data.game.opts.forEach((opt, idx) => {
                optsHtml += `<button onclick="checkGameAnswer(${idx}, ${data.game.correct})">${opt}</button>`;
            });
            document.getElementById('gameOptions').innerHTML = optsHtml;
            document.getElementById('gameContainer').classList.remove('hidden');
            document.getElementById('gameResultArea').classList.add('hidden');
        }

        function checkGameAnswer(selected, correct) {
            let resArea = document.getElementById('gameResultArea');
            let resText = document.getElementById('finalGameScore');
            document.getElementById('gameContainer').classList.add('hidden');
            resArea.classList.remove('hidden');

            if (selected === correct) {
                resText.style.color = "var(--success)";
                resText.innerText = "🎉 Ajoyib! Topshiriq muvaffaqiyatli bajarildi va xato topildi! (+20 ball)";
            } else {
                resText.style.color = "var(--danger)";
                resText.innerText = "❌ Xato javob! Qaytadan urinib ko'ring.";
            }
        }

        function restartGame() {
            loadGame();
        }

        function switchTab(tabName, btn) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

            if(tabName === 'lessons') document.getElementById('lessonsTab').classList.add('active');
            if(tabName === 'tests') document.getElementById('testsTab').classList.add('active');
            if(tabName === 'game') document.getElementById('gameTab').classList.add('active');

            if(btn) btn.classList.add('active');
        }

        function goBack() {
            document.getElementById('courseView').classList.add('hidden');
            document.getElementById('mainMenu').classList.remove('hidden');
            document.getElementById('aiResponse').innerText = '';
            document.getElementById('aiQuery').value = '';
            document.getElementById('aiFile').value = '';
        }

        function askAI() {
            let query = document.getElementById('aiQuery').value;
            let fileInput = document.getElementById('aiFile');
            let responseField = document.getElementById('aiResponse');
            
            if(query.trim() === "" && fileInput.files.length === 0) {
                responseField.innerText = "Iltimos, savol yozing yoki fayl yuklang!";
                return;
            }

            responseField.innerText = "Groq AI tahlil qilmoqda... Tez orada javob beriladi!";
            
            setTimeout(() => {
                responseField.innerText = "AI Javobi: Tanlangan mavzu va grammatika bo'yicha tushuntirish tayyorlandi.";
            }, 1200);
        }
    </script>

</body>
</html>
