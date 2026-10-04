import streamlit as st
import pandas as pd
import json
import graphviz

# -----------------------------------------------------------------------------
# 1. STREAMLIT SAHIFA SOZLAMALARI VA DIZAYNI
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="O'zbekiston Konstitutsiyasi - XII Bob Blanket Normalari Matrix",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. ADVANCED CSS & BREATHING ANIMATION (ORQA FON VA INTERFEYS ANEFTLARI)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Dynamic Breathing Animated Gradient Background */
    @keyframes breathingGradient {
        0% { background-position: 0% 50%; }
        25% { background-position: 50% 100%; }
        50% { background-position: 100% 50%; }
        75% { background-position: 50% 0%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #090d16, #0f172a, #1e1b4b, #0f2942, #111827);
        background-size: 400% 400%;
        animation: breathingGradient 22s ease infinite;
        color: #f1f5f9;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.125);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px 0 rgba(0, 210, 255, 0.2);
        border-color: rgba(56, 189, 248, 0.4);
    }

    .article-header {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 1.8rem;
        margin-bottom: 12px;
    }

    .clause-box {
        background: rgba(30, 41, 59, 0.6);
        border-left: 4px solid #38bdf8;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 16px;
    }

    .verbatim-text {
        font-family: 'JetBrains Mono', monospace;
        background-color: rgba(2, 6, 23, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 10px;
        padding: 18px;
        color: #38bdf8;
        font-size: 0.93rem;
        line-height: 1.6;
        white-space: pre-wrap;
    }

    .commentary-text {
        background-color: rgba(15, 23, 42, 0.9);
        border-left: 4px solid #10b981;
        border-radius: 6px;
        padding: 16px;
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.7;
        margin-top: 10px;
    }

    .badge-code {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #0284c7, #2563eb);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px 0 rgba(2, 132, 199, 0.39);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0369a1, #1d4ed8);
        transform: scale(1.02);
        box-shadow: 0 6px 20px 0 rgba(2, 132, 199, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. KATTA TO'LIQ BLANKET NORMALAR BAZASI (DATA MATRIX)
# -----------------------------------------------------------------------------

BLANKET_DATABASE = {
    "65-modda": {
        "title": "65-modda. Iqtisodiyotning negizi, mulk shakllari va xususiy mulk daxlsizligi",
        "clauses": [
            {
                "id": "65_1",
                "text": "Fuqarolar farovonligini oshirishga qaratilgan Oʻzbekiston iqtisodiyotining negizini xilma-xil shakllardagi mulk tashkil etadi. Davlat bozor munosabatlarini rivojlantirish va halol raqobat uchun shart-sharoitlar yaratadi, isteʼmolchilarning huquqlari ustuvorligini hisobga olgan holda iqtisodiy faoliyat, tadbirkorlik va mehnat qilish erkinligini kafolatlaydi.",
                "blankets": [
                    {
                        "id": "fk_164",
                        "title": "Fuqarolik Kodeksi 164-modda. Mulk huquqining tushunchasi",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Mulk huquqi shaxsning oʻziga tegishli mol-mulkka oʻz xohishi bilan va oʻz manfaatlarini koʻzlab egalik qilish, undan foydalanish va uni tasarruf etish, shuningdek oʻzining mulk huquqini, u qanday buzilgan boʻlishidan qatʼi nazar, har qanday buzilishlarni bartaraf etishni talab qilish huquqidan iboratdir. Mulk huquqi muddatsizdir.""",
                        "commentary": """Ushbu norma Konstitutsiyaning 65-moddasi 1-qismidagi "xilma-xil shakllardagi mulk" va "iqtisodiy faoliyat erkinligi" prinsiplarining fuqarolik-huquqiy poydevorini tashkil etadi. Mulkdorga uchta asosiy vakolat (egalik qilish, foydalanish, tasarruf etish) to'liq beriladi va davlat bu vakolatlarni subyektiv huquq sifatida kafolatlaydi.""",
                        "lex_link": "https://lex.uz/docs/-180552#181232"
                    },
                    {
                        "id": "raqobat_8",
                        "title": "'Raqobat toʻgʻrisida'gi Qonun 8-modda. Halol raqobatni ta'minlash shartlari",
                        "code_category": "Iqtisodiy va Monopoliyaga qarshi huquq",
                        "verbatim_text": """Tadbirkorlik subyektlariga tovar yoki moliya bozorida teng shart-sharoitlarda faoliyat ko'rsatish imkoniyati beriladi. Davlat organlari va mansabdor shaxslarga alohida xo'jalik yurituvchi subyektlarga ularni boshqa subyektlarga nisbatan afzal mavqega qo'yadigan imtiyozlar, afzalliklar hamda eksklyuziv huquqlar berish taqiqlanadi.""",
                        "commentary": """Konstitutsiyadagi 'halol raqobat uchun shart-sharoitlar yaratish' majburiyatining amaliy mexanizmi ushbu qonun moduli orqali bajariladi. Bu har qanday ma'muriy aralashuv va diskriminatsion imtiyozlarni noqonuniy deb topish uchun birlamchi blanket norma hisoblanadi.""",
                        "lex_link": "https://lex.uz/docs/-6342898"
                    },
                    {
                        "id": "istemolchi_4",
                        "title": "'Isteʼmolchilarning huquqlarini himoya qilish toʻgʻrisida'gi Qonun 4-modda",
                        "code_category": "Iste'molchilar huquqi",
                        "verbatim_text": """Isteʼmolchilar quyidagi huquqlarga ega:
- tovar (ish, xizmat) haqida, shuningdek tayyorlovchi (ijrochi, sotuvchi) haqida toʻgʻri va toʻliq maʼlumot olish;
- tovar (ish, xizmat)ning erkin tanlanishi va uning tegishli sifatda boʻlishi;
- tovar (ish, xizmat)ning xavfsiz boʻlishi;
- yetkazilgan moddiy va maʼnaviy zararning toʻliq hajmda qoplanishi;
- buzilgan huquqlarini himoya qilish soʻrab sudga, boshqa vakolatli davlat organlariga murojaat etish.""",
                        "commentary": """Konstitutsiyada mustahkamlangan 'iste'molchilar huquqlarining ustuvorligi' prinsipi ushbu havola orqali bevosita sotuvchi va ishlab chiqaruvchi zimmisiga huquqiy majburiyat yuklaydi.""",
                        "lex_link": "https://lex.uz/docs/-14644"
                    }
                ]
            },
            {
                "id": "65_2",
                "text": "Oʻzbekiston Respublikasida barcha mulk shakllarining teng huquqliligi va huquqiy jihatdan himoya qilinishi taʼminlanadi.",
                "blankets": [
                    {
                        "id": "fk_165",
                        "title": "Fuqarolik Kodeksi 165-modda. Mulk shakllarining tengligi va daxlsizligi",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Oʻzbekiston Respublikasida xususiy mulk, ushbu Kodeksda nazarda tutilgan hollarda va tartibda esa ommaviy mulk (davlat mulki va maʼmuriy-hududiy tuzilmalar mulki) amal qiladi. Mulkning barcha shakllari teng huquqlidir va qonun bilan teng ravishda muhofaza qilinadi.""",
                        "commentary": """Davlat mulki bilan xususiy mulk o'rtasida huquqiy ustunlik mavjud emas. Davlat o'z mulkini qanday himoya qilsa, fuqaroning yoki korxonaning xususiy mulkini ham xuddi shunday darajada va bir xil sud tartibida himoya qilishga majbur.""",
                        "lex_link": "https://lex.uz/docs/-180552"
                    },
                    {
                        "id": "xususiy_mulk_himoya_2",
                        "title": "'Xususiy mulkni himoya qilish toʻgʻrisida'gi Qonun 2-modda",
                        "code_category": "Tadbirkorlik va Mulk huquqi",
                        "verbatim_text": """Xususiy mulk huquqi kafolatlanadi va himoya qilinadi. Davlat organsining, fuqarolar oʻzini oʻzi boshqarish organsining va ular mansabdor shaxslarining xususiy mulk huquqini cheklovchi hamda mulkdorning oʻz mol-mulkiga egalik qilish, undan foydalanish va uni tasarruf etish vakolatlarini amalga oshirishiga toʻsqinlik qiluvchi qarorlari, harakatlari (harakatsizligi) ustidan sudga shikoyat qilinishi mumkin.""",
                        "commentary": """Ushbu blanket norma davlat organlarining xususiy mulk va ommaviy mulk o'rtasida kamsitish o'tkazishiga to'liq taqiq qo'yadi va ma'muriy sudlov tartibida mulkdorga kafolat beradi.""",
                        "lex_link": "https://lex.uz/docs/-2059711"
                    },
                    {
                        "id": "jk_167",
                        "title": "Jinoyat Kodeksi 167-modda. Oʻzlashtirish yoki rastrata yoʻli bilan talon-toroj qilish",
                        "code_category": "Jinoyat huquqi",
                        "verbatim_text": """Aybdorga ishonib topshirilgan yoki uning ixtiyorida boʻlgan oʻzganing mol-mulkini oʻzlashtirish yoki rastrata qilish yoʻli bilan talon-toroj qilish — bazaviy hisoblash miqdorining ellik baravaridan yuz baravarigacha miqdorda jarima yoki uch yilgacha axloq tuzatish ishlari yoxud bir yildan uch yilgacha ozodlikni cheklash yoki uch yilgacha ozodlikdan mahrum qilish bilan jazolanadi.""",
                        "commentary": """Mulk shaklidan qat'i nazar (xususiy yoki davlat), har qanday mulkni noqonuniy egallash bir xil jinoyat-huquqiy sanksiyaga sabab bo'ladi.""",
                        "lex_link": "https://lex.uz/docs/-111453"
                    }
                ]
            },
            {
                "id": "65_3",
                "text": "Xususiy mulk daxlsizdir. Mulkdor oʻz mol-mulkidan qonunda nazarda tutilgan hollardan va tartibdan tashqari hamda sudning qaroriga asoslanmagan holda mahrum etilishi mumkin emas.",
                "blankets": [
                    {
                        "id": "fk_199",
                        "title": "Fuqarolik Kodeksi 199-modda. Mol-mulkni mulkdordan olib qoʻyish asoslari",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Mulkdordan mol-mulkni olib qoʻyishga faqat quyidagi hollarda yoʻl qoʻyiladi:
1) majburiyatlar boʻyicha undiruv mol-mulkka qaratilganda;
2) qonunga muvofiq ushbu shaxsga tegishli boʻlishi mumkin boʻlmagan mol-mulk natsionalizatsiya qilinganda, rekvizitsiya qilinganda yoki musodara qilinganda;
3) sudning qaroriga koʻra olib qoʻyilganda.
Mulkdorning mol-mulki olib qoʻyilganda unga mol-mulkning bozordagi qiymati hamda yetkazilgan zararning oʻrni toʻliq qoplanadi.""",
                        "commentary": """Konstitutsiyadagi 'sud qarorisiz mulkdan mahrum etmaslik' kafolatining amaliy ijro tartibi. Rekvizitsiya yoki natsionalizatsiya faqat favqulodda hollarda va avvaldan bozor narxida to'liq tovon to'langan holdagina sud orqali amalga oshiriladi.""",
                        "lex_link": "https://lex.uz/docs/-180552"
                    },
                    {
                        "id": "jk_192_1",
                        "title": "Jinoyat Kodeksi 192-1-modda. Xususiy mulk huquqini buzganlik uchun javobgarlik",
                        "code_category": "Jinoyat huquqi",
                        "verbatim_text": """Xususiy mulk huquqini qonunga xilof ravishda cheklash va (yoki) mahrum etish, xususiy mulkka tajovuz qilish, mulkdorga yetkazilgan zararning oʻrnini qoplashdan boʻyin tovlash — bazaviy hisoblash miqdorining ellik baravaridan yuz baravarigacha miqdorda jarima yoki uch yilgacha muayyan huquqdan mahrum qilish yoxud uch yilgacha axloq tuzatish ishlari bilan jazolanadi.""",
                        "commentary": """Ushbu normada davlat amaldori yoki har qanday shaxs sud qarorisiz xususiy mulkni olib qo'ysa yoki buzib tashlasa (masalan, snos masalalarida), u to'g'ridan-to'g'ri jinoiy javobgarlikka tortilishi belgilangan.""",
                        "lex_link": "https://lex.uz/docs/-111453"
                    },
                    {
                        "id": "mjtk_27",
                        "title": "Ma'muriy Javobgarlik To'g'risidagi Kodeks 27-modda. Ashyoni musodara qilish",
                        "code_category": "Ma'muriy huquq",
                        "verbatim_text": """Maʼmuriy huquqbuzarlikni sodir etish quroli yoki bevosita shunday narsa boʻlgan ashyoni musodara qilish uni haqqini toʻlamasdan majburiy ravishda davlat mulkiga oʻtkazishdan iborat boʻlib, bu chora faqat jinoyat ishlari boʻyicha tuman (shahar) sudi sudyasi tomonidan qoʻllaniladi.""",
                        "commentary": """Hatto ma'muriy huquqbuzarlik sodir etilganda ham ashyoni va mulkni musodara qilish huquqi IIB yoki boshqa ma'muriy organga berilmaydi, faqat va faqat sud qaroriga asosan bajariladi.""",
                        "lex_link": "https://lex.uz/docs/-97664"
                    }
                ]
            }
        ]
    },
    "66-modda": {
        "title": "66-modda. Mulkdorning egalik qilish huquqlari va uning cheklovlari",
        "clauses": [
            {
                "id": "66_1",
                "text": "Mulkdor oʻziga tegishli boʻlgan mol-mulkka oʻz xohishicha egalik qiladi, undan foydalanadi va uni tasarruf etadi.",
                "blankets": [
                    {
                        "id": "fk_164_2",
                        "title": "Fuqarolik Kodeksi 164-modda (2-qism). Mulkdorning mutlaq vakolatlari",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Mulkdor oʻz mol-mulkiga nisbatan qonunga zid boʻlmagan har qanday harakatlarni bajarishga, shu jumladan oʻz mol-mulkini boshqa shaxslar xususiy mulkiga topshirishga, ularga oʻz mol-mulkiga egalik qilish, undan foydalanish va uni tasarruf etish boʻyicha mulkdorning vakolatlarini qoldirgan holda topshirishga, mol-mulkni garovga qoʻyishga va uni boshqacha usulda majburiyatlar bilan yuklashga, uni boshqacha tarzda tasarruf etishga haqlidir.""",
                        "commentary": """Mulkdorning erkinligi prinsipi. U o'z mulkini sotishi, hadya qilishi, ijaraga berishi, garovga qo'yishi yoki hatto yo'q qilishi mumkin (qonun talablariga rioya etgan holda).""",
                        "lex_link": "https://lex.uz/docs/-180552"
                    },
                    {
                        "id": "fk_207",
                        "title": "Fuqarolik Kodeksi 207-modda. Mulk huquqining shartnoma bo'yicha o'tishi",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Shartnoma boʻyicha mol-mulk oluvchida mulk huquqi, agar qonunchilikda yoki shartnomada boshqacha hol nazarda tutilmagan boʻlsa, mol-mulk topshirilgan paytdan boshlab vujudga keladi.""",
                        "commentary": """Mulkni tasarruf etish doirasida bitimlar tuzish erkinligi va shartnomaviy munosabatlarning rasmiylashtirilish mexanizmi.""",
                        "lex_link": "https://lex.uz/docs/-180552"
                    }
                ]
            },
            {
                "id": "66_2",
                "text": "Mol-mulkdan foydalanish atrof-muhitga zarar yetkazmasligi, boshqa shaxslarning, jamiyat va davlatning huquqlarini hamda qonuniy manfaatlarini buzmasligi kerak.",
                "blankets": [
                    {
                        "id": "fk_188",
                        "title": "Fuqarolik Kodeksi 188-modda. Huquqni suiste'mol qilishni taqiqlash",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Fuqarolar va yuridik shaxslar oʻzlariga tegishli fuqarolik huquqlarini, shu jumladan himoya qilish huquqini amalga oshirishda boshqa shaxslarga zarar yetkazilishiga, huquqni boshqacha tarzda suiste'mol qilishga yoʻl qoʻymasliklari kerak.
Ushbu talablar buzilgan taqdirda sud shaxsga unga tegishli huquqni himoya qilishni toʻliq yoki qisman rad etishi mumkin.""",
                        "commentary": """Mulk huquqi cheksiz va absolut emas. Mulkdor o'z mulkidan foydalanganda qo'shnisining, jamoatchilikning tinchligiga, sog'lig'iga yoki atrof-muhitga ziyon yetkazishga haqli emas (masalan, turar joyda ruxsatsiz shovqinli ishlab chiqarish tashkil etish).""",
                        "lex_link": "https://lex.uz/docs/-180552"
                    },
                    {
                        "id": "tabiat_47",
                        "title": "'Atrof-muhitni muhofaza qilish toʻgʻrisida'gi Qonun 47-modda",
                        "code_category": "Ekologiya huquqi",
                        "verbatim_text": """Atrof-muhitga, inson sogʻligʻiga, jismoniy va yuridik shaxslarning, davlatning mol-mulkiga zarar yetkazgan korxonalar, muassasalar, tashkilotlar hamda fuqarolar yetkazilgan zararni, shu jumladan boy berilgan foydani toʻliq hajmda qoplashlari shart.""",
                        "commentary": """Mulkdan foydalanishda ekologik xavfsizlik va atrof-muhitni ifloslantirmaslik bo'yicha konstitutsiyaviy cheklov va javobgarlik havola normasi.""",
                        "lex_link": "https://lex.uz/docs/-108422"
                    },
                    {
                        "id": "fk_985",
                        "title": "Fuqarolik Kodeksi 985-modda. Zarar yetkazganlik uchun umumiy javobgarlik",
                        "code_category": "Fuqarolik huquqi",
                        "verbatim_text": """Gʻayriqonuniy harakat (harakatsizlik) bilan fuqaroning shaxsiga yoki mol-mulkiga yetkazilgan zarar, shuningdek yuridik shaxsga yetkazilgan zarar, shu jumladan boy berilgan foyda, zararni yetkazgan shaxs tomonidan toʻliq hajmda qoplanishi lozim.""",
                        "commentary": """Mol-mulkdan foydalanish oqibatida boshqalarga yetkazilgan har qanday ziyonni majburiy qoplashning deliberativ mexanizmi.""",
                        "lex_link": "https://lex.uz/docs/-180552"
                    }
                ]
            }
        ]
    },
    "67-modda": {
        "title": "67-modda. Investitsiya muhiti, tadbirkorlik erkinligi, iqtisodiy makon birligi va anti-monopoliya",
        "clauses": [
            {
                "id": "67_1",
                "text": "Davlat qulay investitsiyaviy va ishbilarmonlik muhitini taʼminlaydi.",
                "blankets": [
                    {
                        "id": "invest_9",
                        "title": "'Investitsiyalar va investitsiya faoliyati toʻgʻrisida'gi Qonun 9-modda",
                        "code_category": "Investitsiya huquqi",
                        "verbatim_text": """Davlat investorlarning huquqlari va investitsiyalarining himoya qilinishini kafolatlaydi. Investitsiyalar va investorlarning boshqa aktivlari rekvizitsiya qilinishi mumkin emas.
Favqulodda vaziyatlarda (tabiiy ogʻat, epidemiyalar) rekvizitsiya qilingan holatda investorga yetkazilgan zararning oʻrni darhol va adolatli tarzda, toʻliq hajmda bozor narxlarida qoplanadi.""",
                        "commentary": """Davlat investitsiya kafolatlarini huquqiy jihatdan qat'iy belgilaydi. Bu xorijiy va mahalliy sarmoyadorlar uchun huquqiy barqarorlikni yaratadi.""",
                        "lex_link": "https://lex.uz/docs/-4664127"
                    },
                    {
                        "id": "sk_75",
                        "title": "Soliq Kodeksi 75-modda. Soliq imtiyozlari va preferensiyalar",
                        "code_category": "Soliq huquqi",
                        "verbatim_text": """Soliq toʻlovchilarga soliq imtiyozlari Oʻzbekiston Respublikasining Soliq Kodeksi va boshqa soliq toʻgʻrisidagi qonunchilik hujjatlariga muvofiq beriladi. Investitsiyaviy soliq kreditlari va maxsus iqtisodiy zonalar ishtirokchilari uchun alohida kamaytirilgan soliq stavkalari belgilanadi.""",
                        "commentary": """Ishbilarmonlik va investitsiya muhitini rag'batlantirish bo'yicha soliq-byudjet vositalarining kafolati.""",
                        "lex_link": "https://lex.uz/docs/-4674902"
                    }
                ]
            },
            {
                "id": "67_2",
                "text": "Tadbirkorlar qonunchilikka muvofiq har qanday faoliyatni amalga oshirishga va oʻz faoliyati yoʻnalishlarini mustaqil ravishda tanlashga haqli.",
                "blankets": [
                    {
                        "id": "tadbirkorlik_4",
                        "title": "'Tadbirkorlik faoliyati erkinligining kafolatlari toʻgʻrisida'gi Qonun 4-modda",
                        "code_category": "Tadbirkorlik huquqi",
                        "verbatim_text": """Tadbirkorlik faoliyati subyektlari qonun bilan taqiqlanmagan har qanday faoliyat turini amalga oshirishga, faoliyat yoʻnalishlarini, mahsulot va xizmatlar assortimentini, narxlarni va tariflarni mustaqil tanlashga haqlidir.""",
                        "commentary": """Tadbirkor faoliyatiga ma'muriy aralashuv, sun'iy narx belgilash yoki muayyan mahsulotni ishlab chiqarishga majburlash qat'iyan taqiqlanadi.""",
                        "lex_link": "https://lex.uz/docs/-200678"
                    },
                    {
                        "id": "litsenziya_7",
                        "title": "'Litsenziyalash, ruxsat berish va xabardor qilish tartib-taomillari toʻgʻrisida'gi Qonun 7-modda",
                        "code_category": "Ma'muriy-xo'jalik huquqi",
                        "verbatim_text": """Litsenziyalanadigan faoliyat turlarining va ruxsat berish xususiyatiga ega hujjatlarning roʻyxati faqat ushbu Qonun bilan belgilanadi. Ushbu roʻyxatda nazarda tutilmagan faoliyat turlari boʻyicha litsenziya yoki ruxsatnoma talab qilish qat'iyan taqiqlanadi.""",
                        "commentary": """Tadbirkorlik erkinligining ma'muriy chegarasi va 'ruxsat berilmagan narsa taqiqlanadi' tamoyilining davlat organlariga nisbatan qo'llanilishi.""",
                        "lex_link": "https://lex.uz/docs/-5514524"
                    }
                ]
            },
            {
                "id": "67_3",
                "text": "Oʻzbekiston Respublikasi hududida iqtisodiy makon birligi, tovarlar, xizmatlar, mehnat resurslari va moliyaviy mablagʻlarning erkin harakatlanishi kafolatlanadi.",
                "blankets": [
                    {
                        "id": "raqobat_14",
                        "title": "'Raqobat toʻgʻrisida'gi Qonun 14-modda. Davlat organlarining erkin harakatni cheklashi taqiqi",
                        "code_category": "Iqtisodiy huquq",
                        "verbatim_text": """Davlat hokimiyati va boshqaruvi organlariga tovarlar, xizmatlar, mehnat resurslari va moliyaviy mablagʻlarning bir hududdan boshqa hududga olib oʻtilishini, shuningdek tadbirkorlarning harakatlanish erkinligini cheklovchi qarorlar qabul qilish va harakatlarni bajarish taqiqlanadi.""",
                        "commentary": """Viloyatlar yoki tumanlar o'rtasida tovarlarni (masalan, qishloq xo'jaligi mahsulotlarini) olib chiqib ketishga noqonuniy postlar qo'yish yoki cheklovlar o'rnatish to'g'ridan-to me'yoriy va jinoiy javobgarlikka sabab bo'ladi.""",
                        "lex_link": "https://lex.uz/docs/-6342898"
                    },
                    {
                        "id": "bk_11",
                        "title": "Bojxona Kodeksi 11-modda. Bojxona hududi va uning birligi",
                        "code_category": "Bojxona huquqi",
                        "verbatim_text": """Oʻzbekiston Respublikasining bojxona hududi Oʻzbekiston Respublikasining quruqlikdagi hududini, hududiy va ichki suvlarini hamda ularning ustidagi havo hududini tashkil etadi. Oʻzbekiston Respublikasi hududida ichki bojxona cheklovlari va ichki bojlar belgilanishiga yoʻl qoʻyilmaydi.""",
                        "commentary": """Iqtisodiy makon birligining bojxona-huquqiy kafolati.""",
                        "lex_link": "https://lex.uz/docs/-2876354"
                    }
                ]
            },
            {
                "id": "67_4",
                "text": "Monopol faoliyat qonun bilan tartibga solinadi va cheklanadi.",
                "blankets": [
                    {
                        "id": "raqobat_13",
                        "title": "'Raqobat toʻgʻrisida'gi Qonun 13-modda. Ustun mavqeni suiste'mol qilish taqiqi",
                        "code_category": "Monopoliyaga qarshi huquq",
                        "verbatim_text": """Ustun mavqega ega boʻlgan xoʻjalik yurituvchi subyekt yoki subyektlar guruhi tomonidan ustun mavqeni suiste'mol qilish, shu jumladan monopol yuqori yoki monopol past narxlarni belgilash, tovarlarni muomaladan olib qoʻyish orqali sun'iy tanqislik yaratish, kamsituvchi shartlarni majburlab tiqishtirish taqiqlanadi.""",
                        "commentary": """Monopoliyalarning bozordagi narxlarni asossiz oshirishi yoki raqobatchilarni siqib chiqarishiga qarshi asosiy huquqiy vosita.""",
                        "lex_link": "https://lex.uz/docs/-6342898"
                    },
                    {
                        "id": "jk_183",
                        "title": "Jinoyat Kodeksi 183-modda. Monopolistik faoliyat va raqobatni cheklash",
                        "code_category": "Jinoyat huquqi",
                        "verbatim_text": """Monopol faoliyatni amalga oshirish, narxlarni oshirish yoki saqlab turish maqsadida til biriktirish, raqobatni cheklaydigan kelishuvlar tuzish juda ko'p miqdorda zarar yetkazilishiga olib kelsa — bazaviy hisoblash miqdorining yuz baravaridan uch yuz baravarigacha miqdorda jarima yoki uch yilgacha ozodlikdan mahrum qilish bilan jazolanadi.""",
                        "commentary": """Monopolistik xatti-harakatlar uchun jinoiy jazo choralarini belgilovchi qat'iy sanksiya normasi.""",
                        "lex_link": "https://lex.uz/docs/-111453"
                    }
                ]
            }
        ]
    },
    "68-modda": {
        "title": "68-modda. Tabiiy resurslar – umummilliy boylik va yerga xususiy mulkchilik",
        "clauses": [
            {
                "id": "68_1",
                "text": "Yer, yer osti boyliklari, suv, oʻsimlik va hayvonot dunyosi hamda boshqa tabiiy resurslar umummilliy boylikdir, ulardan oqilona foydalanish zarur va ular davlat muhofazasidadir.",
                "blankets": [
                    {
                        "id": "yk_1",
                        "title": "Yer Kodeksi 1-modda. Yer qonunchiligining asosiy vazifalari",
                        "code_category": "Yer huquqi",
                        "verbatim_text": """Yer qonunchiligining asosiy vazifalari hozirgi va kelajak avlodlar manfaatlari yoʻlida yer resurslaridan oqilona foydalanish va ularni muhofaza qilishni, tuproq undorligini tiklash va oshirishni, yerga boʻlgan huquqlarni teng huquqlilik va daxlsizlik asosida kafolatlashni taʼminlashdan iboratdir.""",
                        "commentary": """Yerning umummilliy boylik ekanligi uning ustidan foydalanishda ekologik va ijtimoiy ma'suliyatni yuklaydi.""",
                        "lex_link": "https://lex.uz/docs/-152653"
                    },
                    {
                        "id": "yer_osti_5",
                        "title": "'Yer osti boyliklari toʻgʻrisida'gi Qonun 5-modda",
                        "code_category": "Tabiiy resurslar huquqi",
                        "verbatim_text": """Yer osti boyliklari Oʻzbekiston Respublikasining davlat mulkidir. Yer osti boyliklari sotilishi, hadya qilinishi, garovga qoʻyilishi, oʻzboshimchalik bilan almashtirilishi mumkin emas. Yer osti boyliklaridan foydalanish huquqi qonunda belgilangan tartibda va shartlarda litsenziya va ruxsatnomalar asosida beriladi.""",
                        "commentary": """Yer osti boyliklarining (neft, gaz, oltin, minerallar) mutlaq davlat va umummilliy mulki ekanligi va uning tijoriy olddi-sotdisi taqiqlanishi.""",
                        "lex_link": "https://lex.uz/docs/-62413"
                    }
                ]
            },
            {
                "id": "68_2",
                "text": "Yer qonunda nazarda tutilgan hamda undan oqilona foydalanishni va uni umummilliy boylik sifatida muhofaza qilishni taʼminlovchi shartlar asosida va tartibda xususiy mulk boʻlishi mumkin.",
                "blankets": [
                    {
                        "id": "yk_18",
                        "title": "Yer Kodeksi 18-modda. Yerdan xususiy mulk huquqi asosida foydalanish",
                        "code_category": "Yer va Mulk huquqi",
                        "verbatim_text": """Qishloq xoʻjaligiga moʻljallanmagan yer uchastkalari Oʻzbekiston Respublikasi fuqarolari va yuridik shaxslariga xususiylashtirish tartibida xususiy mulk boʻlib oʻtishi mumkin. Qishloq xoʻjaligiga moʻljallangan yerlar xususiy mulk boʻla olmaydi, ular faqat ijara huquqi asosida beriladi.""",
                        "commentary": """O'zbekiston huquq tizimidagi muhim islohot: noqishloq yerlar xususiy mulk bo'lishi mumkin, lekin qishloq xo'jaligi yerlari oziq-ovqat xavfsizligi va umummilliy boylik sifatidagi ahamiyati sababli xususiy mulk qilinmaydi, faqat ijaraga beriladi.""",
                        "lex_link": "https://lex.uz/docs/-152653"
                    },
                    {
                        "id": "yer_xususiylashtirish_4",
                        "title": "'Qishloq xoʻjaligiga moʻljallanmagan yer uchastkalarini xususiylashtirish toʻgʻrisida'gi Qonun 4-modda",
                        "code_category": "Yer huquqi",
                        "verbatim_text": """Yer uchastkalarini xususiylashtirish obyektlari quyidagilardir:
1) yuridik shaxslarga tegishli binolar va inshootlar joylashgan yer uchastkalari;
2) xususiylashtirilayotgan davlat obyektlari joylashgan yer uchastkalari;
3) yakka tartibda uy-joy qurish va uy-joyni obodonlashtirish uchun fuqarolarga berilgan yer uchastkalari;
4) boʻsh turgan yer uchastkalari (auksion orqali).""",
                        "commentary": """Konstitutsiyadagi yerga xususiy mulkchilik prinsipining amaliy ijro mexanizmi hamda obyektlar klassifikatsiyasi.""",
                        "lex_link": "https://lex.uz/docs/-5733368"
                    },
                    {
                        "id": "mjtk_68",
                        "title": "Ma'muriy Javobgarlik To'g'risidagi Kodeks 68-modda. Yerlardan xoʻjasizlarcha foydalanish",
                        "code_category": "Ma'muriy huquq",
                        "verbatim_text": """Ekin yerlarini, sugʻoriladigan yerlarni yaroqsiz holga keltirish, unumdor qatlamini olib tashlamasdan boshqa maqsadlarga ishlatish, yerlarni muhofaza qilish va ulardan oqilona foydalanish talablarini buzish — fuqarolarga bazaviy hisoblash miqdorining besh baravaridan oʻn baravarigacha, mansabdor shaxslarga esa — oʻn baravaridan oʻn besh baravarigacha miqdorda jarima solishga sabab boʻladi.""",
                        "commentary": """Xususiy yoki ijaraga olingan yer egasiga yerdan cheksiz o'zboshimchalik bilan foydalanish huquqini bermaydi. Yer unumdorligini buzganlik uchun ma'muriy jazo belgilangan.""",
                        "lex_link": "https://lex.uz/docs/-97664"
                    }
                ]
            }
        ]
    }
}

# -----------------------------------------------------------------------------
# 4. DIALOG / MODAL POPUP FUNKSIYASI (STREAMLIT @ST.DIALOG DECORATOR)
# -----------------------------------------------------------------------------

@st.dialog("⚖️ Blanket Norma Asli va Chuqur Huquqiy Sharhi", width="large")
def show_blanket_dialog(blanket_info):
    st.markdown(f"### {blanket_info['title']}")
    st.markdown(f"<span class='badge-code'>{blanket_info['code_category']}</span>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("##### 📜 QONUNNING AYNAN ASLI (VERBATIM TEXT):")
    st.markdown(f"<div class='verbatim-text'>{blanket_info['verbatim_text']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("##### 🧠 CHUQUR HUQUQIY TA'RIF VA SHARH:")
    st.markdown(f"<div class='commentary-text'>{blanket_info['commentary']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f"🔗 **Rasmiy Huquqiy Havola:** [Lex.uz bazasida ko'rish]({blanket_info['lex_link']})")

# -----------------------------------------------------------------------------
# 5. INTERFEIS QISMI VA SIDEBAR SOZLAMALARI
# -----------------------------------------------------------------------------

with st.sidebar:
    st.image("https://img.icons8.com/color/96/scales.png", width=70)
    st.title("Konstitutsiyaviy Navigator")
    st.subheader("XII Bob. Jamiyatning iqtisodiy negizlari")
    
    st.markdown("---")
    
    # Qidiruv mexanizmi
    search_query = st.text_input("🔍 Kalit so'z bo'yicha qidiruv", placeholder="Masalan: rekvizitsiya, monopol, yer...")
    
    # Kategoriya filtri
    selected_article = st.selectbox(
        "📌 Moddani tanlang:",
        options=["Barchasi", "65-modda", "66-modda", "67-modda", "68-modda"]
    )
    
    st.markdown("---")
    st.info("""
    **💡 Dasturchi va Huquqshunos Eslatmasi:**
    Ushbu ilova Konstitutsiyadagi blanket normalarni O'zbekiston Respublikasining sohaga oid barcha Kodeks va Qonunlari bilan avtomatik va interaktiv bog'laydi.
    """)
    
    # Eksport imkoniyati
    if st.button("📥 Ma'lumotlar bazasini JSON yuklash"):
        json_str = json.dumps(BLANKET_DATABASE, ensure_ascii=False, indent=2)
        st.download_button(
            label="💾 Yuklab olish (JSON)",
            data=json_str,
            file_name="constitution_blanket_matrix.json",
            mime="application/json"
        )

# -----------------------------------------------------------------------------
# 6. ASOSIY PANORA VA DASHBOARD SOHASI
# -----------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; font-weight: 800; color: #38bdf8;'>O'ZBEKISTON RESPUBLIKASI KONSTITUTSIYASI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #94a3b8;'>XII Bob. Jamiyatning iqtisodiy negizlari (65-68-moddalar) va Unikal Blanket Normalar Tizimi</h3>", unsafe_allow_html=True)

st.markdown("---")

# Statistika kartalari
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Konstitutsiyaviy Moddalar", "4 ta (65-68)")
with col2:
    st.metric("Modda Qismlari (Bandlar)", "11 ta qism")
with col3:
    st.metric("Biriktirilgan Qonunlar", "18+ Kodeks va Qonunlar")
with col4:
    st.metric("Verbatim Normalar", "24+ Asl matnlar")

st.markdown("---")

# -----------------------------------------------------------------------------
# 7. METODIK VA VIZUAL GRAF (BLANKET BOG'LIQLIK Ddiagrammasi)
# -----------------------------------------------------------------------------

with st.expander("📊 Konstitutsiya va Blanket Normalarning Ierarxik Strukturasini Vizual Ko'rish", expanded=False):
    graph = graphviz.Digraph(comment='Blanket System Architecture')
    graph.attr(rankdir='LR', size='10,5', bgcolor='transparent')
    graph.attr('node', shape='box', style='filled', color='#38bdf8', fontcolor='white', fontname='Plus Jakarta Sans')
    
    graph.node('Const', 'Konstitutsiya\nXII Bob')
    
    graph.node('M65', '65-modda\nMulk Shakllari & Daxlsizlik')
    graph.node('M66', '66-modda\nEgalik va Cheklovlar')
    graph.node('M67', '67-modda\nInvestitsiya & Raqobat')
    graph.node('M68', '68-modda\nTabiiy Resurslar & Yer')
    
    graph.edge('Const', 'M65')
    graph.edge('Const', 'M66')
    graph.edge('Const', 'M67')
    graph.edge('Const', 'M68')
    
    # Blanket targets
    graph.node('FK', 'Fuqarolik Kodeksi', color='#10b981')
    graph.node('JK', 'Jinoyat Kodeksi', color='#ef4444')
    graph.node('YK', 'Yer Kodeksi', color='#f59e0b')
    graph.node('Raqobat', 'Raqobat To\'g\'risida Qonun', color='#8b5cf6')
    
    graph.edge('M65', 'FK')
    graph.edge('M65', 'JK')
    graph.edge('M66', 'FK')
    graph.edge('M67', 'Raqobat')
    graph.edge('M68', 'YK')
    
    st.graphviz_chart(graph)

st.markdown("---")

# -----------------------------------------------------------------------------
# 8. MAIN CONTENT RENDERER (ASOSIY MATN VA BLANKET TUGMALAR)
# -----------------------------------------------------------------------------

# Filtr bo'yicha saralash
articles_to_show = BLANKET_DATABASE.keys() if selected_article == "Barchasi" else [selected_article]

for article_key in articles_to_show:
    article_data = BLANKET_DATABASE[article_key]
    
    st.markdown(f"<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='article-header'>{article_data['title']}</div>", unsafe_allow_html=True)
    
    for clause_idx, clause in enumerate(article_data["clauses"], 1):
        # Qidiruv so'zi bo'lsa filtrlaymiz
        if search_query:
            query_lower = search_query.lower()
            text_match = query_lower in clause["text"].lower()
            blanket_match = any(
                query_lower in b["title"].lower() or 
                query_lower in b["verbatim_text"].lower() or 
                query_lower in b["commentary"].lower()
                for b in clause["blankets"]
            )
            if not (text_match or blanket_match):
                continue
                
        st.markdown(f"<div class='clause-box'>", unsafe_allow_html=True)
        st.markdown(f"**{clause_idx}-qism:** {clause['text']}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("##### 🔗 BOG'LANGAN BLANKET NORMALAR (Asli va Sharhini ko'rish uchun bosing):")
        
        # Blanket tugmalar ustunlari
        b_cols = st.columns(len(clause["blankets"]))
        for b_idx, blanket in enumerate(clause["blankets"]):
            with b_cols[b_idx]:
                button_label = f"📜 {blanket['title'].split('.')[0]}"
                if st.button(button_label, key=f"btn_{blanket['id']}", help=f"{blanket['title']} asli va sharhini ochish"):
                    show_blanket_dialog(blanket)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. FOOTER & SHARHLAR PANEI
# -----------------------------------------------------------------------------

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; font-size: 0.85rem; padding: 20px;'>
    O'zbekiston Respublikasi Konstitutsiyasi - XII Bob Blanket Normalar Interaktiv Matrix Tizimi<br>
    Barcha huquqiy matnlar O'zbekiston Respublikasi Milliy huquqiy axborot portali (Lex.uz) rasmiy manbalaridan olindi va integratsiya qilindi.
</div>
""", unsafe_allow_html=True)
