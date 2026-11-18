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
            <p id="modalLessonBody" style="line-height: 1.6; font-size: 14px; color: var(--text-main);"></p>
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
                    task: "C++ da nomlar fazosi (namespace) qaysi kalit so'z bilan belgilanadi?", opts: ["using namespace std;", "namespace:std", "import std", "include std"], correct: 0 }
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
                    task: "Choose the correct translation for 'Dasturiy ta'minot':", opts: ["Hardware", "Software", "Firmware", "Malware"], correct: 1 }
                }
            }
        };

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
                lessonsHtml += `<div class="lesson-item" onclick="openLessonModal(idx)"><span>{les.title}</span> <b>📖 O'qish</b></div>`;
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
                document.getElementById('quizQuestion').innerText = `(currentQuizIndex+1/{data.quiz.length}) ${qData.q}`;
                
                let optsHtml = "";
                qData.opts.forEach((opt, idx) => {
                    optsHtml += `<button onclick="checkQuizAnswer(${idx}, qData.correct)">{opt}</button>`;
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
                optsHtml += `<button onclick="checkGameAnswer(${idx}, data.game.correct)">{opt}</button>`;
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
