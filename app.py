import streamlit as st
import json
import re
import time
import pandas as pd

# Page configuration for high performance legal viewer
st.set_page_config(
    page_title="Konstitutsiya XII Bob | Blanket Normalar Portali",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Ambient Breathing Background Effect */
    @keyframes breathingGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
        50% { box-shadow: 0 0 30px rgba(99, 102, 241, 0.5); }
        100% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    }

    .stApp {
        background: linear-gradient(-45deg, #090d16, #111827, #0f172a, #1e1b4b, #030712);
        background-size: 400% 400%;
        animation: breathingGradient 16s ease infinite;
        color: #f1f5f9;
    }

    /* Glassmorphic Container Cards */
    .legal-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .legal-card:hover {
        border-color: rgba(56, 189, 248, 0.4);
        transform: translateY(-3px);
        box-shadow: 0 16px 40px rgba(14, 165, 233, 0.2);
    }

    .article-header {
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 1.8rem;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
    }

    .clause-box {
        background: rgba(30, 41, 59, 0.5);
        border-left: 4px solid #38bdf8;
        border-radius: 8px 12px 12px 8px;
        padding: 18px 22px;
        margin: 16px 0;
        font-size: 1.05rem;
        line-height: 1.7;
        color: #e2e8f0;
    }

    .blanket-tag {
        display: inline-flex;
        align-items: center;
        background: rgba(14, 165, 233, 0.15);
        border: 1px solid rgba(56, 189, 248, 0.35);
        color: #38bdf8;
        padding: 8px 16px;
        border-radius: 30px;
        font-size: 0.88rem;
        font-weight: 600;
        margin: 6px 6px 6px 0;
        cursor: pointer;
        transition: all 0.25s ease;
    }

    .blanket-tag:hover {
        background: rgba(14, 165, 233, 0.35);
        border-color: #38bdf8;
        color: #ffffff;
        box-shadow: 0 0 18px rgba(56, 189, 248, 0.5);
        transform: scale(1.03);
    }

    .stats-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
    }

    .stats-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: #38bdf8;
    }

    .stats-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Custom Streamlit Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.2), rgba(99, 102, 241, 0.2)) !important;
        border: 1px solid rgba(56, 189, 248, 0.4) !important;
        color: #38bdf8 !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #0284c7, #4f46e5) !important;
        color: #ffffff !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.6) !important;
        border-color: transparent !important;
        transform: translateY(-2px) !important;
    }

    /* Lex.uz link styling */
    .lex-link {
        color: #38bdf8;
        text-decoration: none;
        font-weight: 600;
        border-bottom: 1px dashed #38bdf8;
    }
    .lex-link:hover {
        color: #818cf8;
        border-bottom-style: solid;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_constitutional_database():
    """
    Returns the structured database of Chapter XII (Articles 65-68)
    with explicit blanket norms mapped to corresponding Codes and Laws of Uzbekistan.
    """
    return {
        "chapter": {
            "title": "UCHINCHI BOʻLIM. JAMIYAT VA SHAXS",
            "subtitle": "XII bob. Jamiyatning iqtisodiy negizlari",
            "source_doc": "Oʻzbekiston Respublikasi Konstitutsiyasi (30.04.2023 tahriri)",
            "lex_url": "https://lex.uz/docs/-6445145"
        },
        "articles": [
            {
                "number": "65-modda",
                "title": "Iqtisodiyotning negizi va mulk shakllarining teng huquqliligi",
                "clauses": [
                    {
                        "clause_id": "65-1",
                        "number": "1-qism",
                        "text": "Fuqarolar farovonligini oshirishga qaratilgan Oʻzbekiston iqtisodiyotining negizini xilma-xil shakllardagi mulk tashkil etadi. Davlat bozor munosabatlarini rivojlantirish va halol raqobat uchun shart-sharoitlar yaratadi, isteʼmolchilarning huquqlari ustuvorligini hisobga olgan holda iqtisodiy faoliyat, tadbirkorlik va mehnat qilish erkinligini kafolatlaydi.",
                        "blanket_norms": [
                            {
                                "id": "FK-164",
                                "code_title": "Oʻzbekiston Respublikasi Fuqarolik Kodeksi",
                                "article_ref": "164-modda",
                                "norm_name": "Mulk huquqining mazmuni va mulk shakllari",
                                "verbatim_text": "Mulk huquqi shaxsning oʻziga qarashli mol-mulkka oʻz xohishi bilan va oʻz manfaatlarini koʻzlab egalik qilish, undan foydalanish va uni tasarruf etish hamda oʻzining mulk huquqini, kim tomonidan boʻlmasin, har qanday buzishlarni bartaraf etishni talab qilish huquqidan iboratdir. Mulk daxlsizdir va qonun bilan muhofaza qilinadi.",
                                "commentary": "Ushbu modda Konstitutsiyaning 65-moddasi 1-qismidagi xilma-xil mulk shakllari (xususiy, davlat, munitsipal va boshqalar) hamda ularning teng huquqiy maqomini fuqarolik qonunchiligi darajasida mustahkamlaydi.",
                                "category": "Fuqarolik huquqi",
                                "lex_link": "https://lex.uz/docs/-111189#164",
                                "sanction": "Mulk huquqini buzganlik uchun yetkazilgan zararni to'liq qoplash (FK 14, 985-moddalar)."
                            },
                            {
                                "id": "RAQOBAT-13",
                                "code_title": "Oʻzbekiston Respublikasining 'Raqobat toʻgʻrisida'gi Qonuni (OʻRQ-850-son)",
                                "article_ref": "13-modda",
                                "norm_name": "Insofsiz raqobatni taqiqlash va halol raqobat kafolati",
                                "verbatim_text": "Insofsiz raqobatga, shu jumladan xoʻjalik yurituvchi subyektga maʼnaviy zarar yoki obroʻyiga putur yetkazishi mumkin boʻlgan notoʻgʻri, aniq boʻlmagan yoki buzib koʻrsatilgan maʼlumotlarni tarqatishga, tovarning kelib chiqishi va sifati boʻyicha isteʼmolchilarni chalgʻitishga yoʻl qoʻyilmaydi.",
                                "commentary": "Konstitutsiyadagi 'halol raqobat uchun shart-sharoitlar yaratish' prinsipi mazkur qonun normasi orqali monopoliyaga qarshi tartibga solish mexanizmini belgilaydi.",
                                "category": "Iqtisodiy qonunchilik",
                                "lex_link": "https://lex.uz/docs/-6483120",
                                "sanction": "Monopoliyaga qarshi organ tomonidan moliyaviy jarima va MJtK 178-moddasi bo'yicha ma'muriy javobgarlik."
                            },
                            {
                                "id": "ISTEMOLCHI-4",
                                "code_title": "Oʻzbekiston Respublikasining 'Isteʼmolchilarning huquqlarini himoya qilish toʻgʻrisida'gi Qonuni",
                                "article_ref": "4-modda",
                                "norm_name": "Isteʼmolchilarning asosiy huquqlari",
                                "verbatim_text": "Isteʼmolchilar quyidagi huquqlarga ega: tovar (ish, xizmat) haqida, shuningdek tayyorlovchi (ijrochi, sotuvchi) haqida toʻgʻri va yetarli maʼlumot olish; tovar (ish, xizmat)ning erkin tanlanishi va uning tegishli sifatli boʻlishi; tovar (ish, xizmat)ning xavfsiz boʻlishi; zararning toʻliq qoplanishi.",
                                "commentary": "Konstitutsiya iste'molchilar huquqlari ustuvorligini iqtisodiyotning asosiy tamoyili qilib qo'ydi. Ushbu qonun iste'molchi va tadbirkor o'rtasidagi munosabatni muvozanatlashtiradi.",
                                "category": "Iste'molchilar huquqi",
                                "lex_link": "https://lex.uz/docs/-48722",
                                "sanction": "Nuqsonli tovar uchun vositalarni qaytarish va ma'naviy zararni qoplash."
                            },
                            {
                                "id": "MK-15",
                                "code_title": "Oʻzbekiston Respublikasi Mehnat Kodeksi",
                                "article_ref": "15-modda",
                                "norm_name": "Mehnat qilish erkinligi va majburiy mehnatni taqiqlash",
                                "verbatim_text": "Har bir shaxs mehnat qilish, faoliyat turini, kasbni va mutaxassislikni, ish joyini hamda mehnat sharoitlarini erkin tanlash huquqiga ega. Majburiy mehnat taqiqlanadi.",
                                "commentary": "Konstitutsiyada belgilangan 'mehnat qilish erkinligi' kafolati Mehnat Kodeksi orqali fuqaroning xohlagan sohada qonuniy mehnat qilish huquqini ta'minlaydi.",
                                "category": "Mehnat huquqi",
                                "lex_link": "https://lex.uz/docs/-6257288",
                                "sanction": "Mehnat huquqlarini buzgan mansabdor shaxslarga MJtK 49-moddasi bo'yicha jarima."
                            }
                        ]
                    },
                    {
                        "clause_id": "65-2",
                        "number": "2-qism",
                        "text": "Oʻzbekiston Respublikasida barcha mulk shakllarining teng huquqliligi va huquqiy jihatdan himoya qilinishi taʼminlanadi.",
                        "blanket_norms": [
                            {
                                "id": "FK-166",
                                "code_title": "Oʻzbekiston Respublikasi Fuqarolik Kodeksi",
                                "article_ref": "166-modda",
                                "norm_name": "Mulk huquqining teng himoya qilinishi",
                                "verbatim_text": "Oʻzbekiston Respublikasida xususiy mulk va davlat mulki eʼtirof etiladi va teng himoya qilinadi. Mulkdor boʻlgan subyektlarning huquqlari va qonuniy manfaatlarini kamsitishga yoʻl qoʻyilmaydi.",
                                "commentary": "Davlat mulki va xususiy mulk sud tizimi hamda qonunlar oldida teng ustuvorlikka ega. Davlat o'z mulkini qanday himoya qilsa, fuqaro xususiy mulkini ham shunday himoya qiladi.",
                                "category": "Fuqarolik huquqi",
                                "lex_link": "https://lex.uz/docs/-111189#166",
                                "sanction": "Noqonuniy ravishda mulkka daxl qilgan har qanday subyektga nisbatan fuqarolik va jinoiy javobgarlik."
                            },
                            {
                                "id": "JK-167",
                                "code_title": "Oʻzbekiston Respublikasi Jinoyat Kodeksi",
                                "article_ref": "167, 168, 169-moddalar",
                                "norm_name": "Mulkka tajovuz qiluvchi jinoyatlar uchun javobgarlik",
                                "verbatim_text": "O'zlashtirish yoki rastrata yo'li bilan talon-toroj qilish, firibgarlik va o'g'rilik sodir etgan shaxslar qonunda belgilangan tartibda jinoiy javobgarlikka tortiladi hamda mulkdorga yetkazilgan zarar undiriladi.",
                                "commentary": "Ushbu jinoiy normalar barcha mulk shakllarini har qanday qonunsiz tajovuzlardan davlatning majburlov kuchi orqali himoya qiladi.",
                                "category": "Jinoyat huquqi",
                                "lex_link": "https://lex.uz/docs/-111453",
                                "sanction": "Ozarilayotgan summaga qarab o'zlashtirish, ozodlikni cheklash yoki ozodlikdan mahrum qilish jazosi."
                            },
                            {
                                "id": "MJTK-61",
                                "code_title": "Oʻzbekiston Respublikasi Ma'muriy Javobgarlik to'g'risidagi Kodeks",
                                "article_ref": "61-modda",
                                "norm_name": "Mulkni oz miqdorda talon-toroj qilish",
                                "verbatim_text": "O'zganing mol-mulkini o'g'rilik, o'zlashtirish, rastrata qilish, mansab mavqeini suiste'mol qilish yoki firibgarlik yo'li bilan oz miqdorda talon-toroj qilish ma'muriy javobgarlikka sabab bo'ladi.",
                                "commentary": "Mulkning teng huquqiy himoyasi kichik hajmdagi huquqbuzarliklarga nisbatan ham ma'muriy choralar orqali ta'minlanadi.",
                                "category": "Ma'muriy huquq",
                                "lex_link": "https://lex.uz/docs/-97661",
                                "sanction": "BHMning 1 baravaridan 5 baravarigacha jarima yoki 15 sutkagacha ma'muriy qamoq."
                            }
                        ]
                    },
                    {
                        "clause_id": "65-3",
                        "number": "3-qism",
                        "text": "Xususiy mulk daxlsizdir. Mulkdor oʻz mol-mulkidan qonunda nazarda tutilgan hollardan va tartibdan tashqari hamda sudning qaroriga asoslanmagan holda mahrum etilishi mumkin emas.",
                        "blanket_norms": [
                            {
                                "id": "XM-PROTECT-2",
                                "code_title": "Oʻzbekiston Respublikasining 'Xususiy mulkni himoya qilish va mulkdorlar huquqlarining kafolatlari toʻgʻrisida'gi Qonuni",
                                "article_ref": "2 va 3-moddalar",
                                "norm_name": "Xususiy mulk daxlsizligi va uni olib qo'yishni cheklash",
                                "verbatim_text": "Xususiy mulk daxlsizdir va davlat muhofazasidadir. Xususiy mulk huquqining cheklanishi hamda mol-mulkni olib qoʻyish faqat qonunda nazarda tutilgan hollarda sud qaroriga koʻra amalga oshiriladi.",
                                "commentary": "Sud qarorisiz hech qanday davlat organi yoki mansabdor shaxs xususiy mulkni musodara qila olmaydi yoki tortib ololmaydi. Bu 'Snos' va mulkni noqonuniy olib qo'yishga qarshi asosiy to'siqdir.",
                                "category": "Xususiy mulk kafolati",
                                "lex_link": "https://lex.uz/docs/-2059613",
                                "sanction": "Mulkni noqonuniy olib qo'ygan mansabdor shaxsdan yetkazilgan barcha zararlarni bozor qiymatida undirish."
                            },
                            {
                                "id": "FK-206",
                                "code_title": "Oʻzbekiston Respublikasi Fuqarolik Kodeksi",
                                "article_ref": "206-modda",
                                "norm_name": "Mulkdorning mol-mulkini olib qoʻyishni cheklash (Natsionalizatsiya va Rekvizitsiya)",
                                "verbatim_text": "Mulkdorning mol-mulkini olib qoʻyishga faqat qonunda belgilangan hollarda va tartibda, shuningdek rekvizitsiya va natsionalizatsiya holatlarida toʻliq kompensatsiya toʻlangan holda va sud qarori bilan yoʻl qoʻyiladi.",
                                "commentary": "Favqulodda holatlarda ham mulkdorga yetkazilayotgan zarar amaldagi bozor narxida oldindan to'liq qoplanishi shart.",
                                "category": "Fuqarolik huquqi",
                                "lex_link": "https://lex.uz/docs/-111189#206",
                                "sanction": "Kompensatsiya to'lanmagan taqdirda qaror o'z-o'zidan haqiqiy emas deb topiladi."
                            },
                            {
                                "id": "JAMOAT-YER-4",
                                "code_title": "Oʻzbekiston Respublikasining 'Jamoat ehtiyojlari uchun yer uchastkalarini kompensatsiya evaziga olib qoʻyish tartib-taomillari toʻgʻrisida'gi Qonuni (OʻRQ-781)",
                                "article_ref": "4 va 5-moddalar",
                                "norm_name": "Kompensatsiya berishning qat'iy va kafolatlangan tartibi",
                                "verbatim_text": "Jamoat ehtiyojlari uchun yer uchastkalarini olib qoʻyishda koʻchmas mulk obyekti qiymati, koʻchish va boshqa xarajatlar bozor qiymatida toʻliq va oldindan qoplanishi shart. Olib qo'yishga mulkdor roziligi va Oliy Majlis / Xalq deputatlari kengashi qarori zarur.",
                                "commentary": "Ushbu blanket norma mulkdorning uy-joyi yoki binosi jamoat ehtiyoji bahonasi bilan noqonuniy buzilishining oldini oladi.",
                                "category": "Ko'chmas mulk va yer huquqi",
                                "lex_link": "https://lex.uz/docs/-6087700",
                                "sanction": "Buzish to'g'risida chiqarilgan noqonuniy qarorlarni ma'muriy sudlar orqali bekor qilish."
                            }
                        ]
                    }
                ]
            },
            {
                "number": "66-modda",
                "title": "Mulkdorning vakolatlari va ularning cheklanishi",
                "clauses": [
                    {
                        "clause_id": "66-1",
                        "number": "1-qism",
                        "text": "Mulkdor oʻziga tegishli boʻlgan mol-mulkka oʻz xohishicha egalik qiladi, undan foydalanadi va uni tasarruf etadi. Mol-mulkdan foydalanish atrof-muhitga zarar yetkazmasligi, boshqa shaxslarning, jamiyat va davlatning huquqlari hamda qonuniy manfaatlarini buzmasligi kerak.",
                        "blanket_norms": [
                            {
                                "id": "FK-188",
                                "code_title": "Oʻzbekiston Respublikasi Fuqarolik Kodeksi",
                                "article_ref": "188, 189 va 192-moddalar",
                                "norm_name": "Egalik qilish, foydalanish va tasarruf etish huquqlarining mazmuni",
                                "verbatim_text": "Egalik qilish huquqi — mol-mulkni amalda egallab turish. Foydalanish huquqi — mol-mulkdan uning foydali xossalarini ajratib olish. Tasarruf etish huquqi — mol-mulkning huquqiy qismatining belgilanishi (sotish, hadya qilish, garovga qo'yish).",
                                "commentary": "Triada (uchlik) huquqlari mulkdorning mutloq huquqlarini belgilab beradi. Biroq bu huquqlar jamiyat va boshqa shaxslar zarariga ishlatilishi taqiqlanadi.",
                                "category": "Fuqarolik huquqi",
                                "lex_link": "https://lex.uz/docs/-111189#188",
                                "sanction": "Huquqni suiste'mol qilganda sud tartibida Bitimni haqiqiy emas deb topish (FK 113-modda)."
                            },
                            {
                                "id": "TABIAT-18",
                                "code_title": "Oʻzbekiston Respublikasining 'Tabiatni muhofaza qilish toʻgʻrisida'gi Qonuni",
                                "article_ref": "18-modda",
                                "norm_name": "Mol-mulkdan foydalanishda ekologik xavfsizlik va cheklovlar",
                                "verbatim_text": "Mulkdorlar oʻzlariga tegishli obyektlardan foydalanishda ekologik normativlar va standartlarga rioya etishlari, atrof-muhitning ifloslanishiga va tabiiy resurslarning kamayishiga yoʻl qoʻymasliklari shart.",
                                "commentary": "Mulkdor o'z yerida yoki zavodida xohlagan ishini qila olmaydi; agar atrof-muhitga, havoga, suvga zarar yetkazsa, davlat u subyekt faoliyatini to'xtatib qo'yishi mumkin.",
                                "category": "Ekologiya huquqi",
                                "lex_link": "https://lex.uz/docs/-107116",
                                "sanction": "Ekologik zarar uchun majburiy kompensatsiya undirish va ob'ekt faoliyatini to'xtatish."
                            },
                            {
                                "id": "FK-985",
                                "code_title": "Oʻzbekiston Respublikasi Fuqarolik Kodeksi",
                                "article_ref": "985-modda",
                                "norm_name": "Zarar yetkazganlik uchun javobgarlikning umumiy asoslari",
                                "verbatim_text": "Gʻayriqonuniy harakat (harakatsizlik) tufayli fuqaroning shaxsiga yoki mol-mulkiga, shuningdek yuridik shaxsga yetkazilgan zarar uni yetkazgan shaxs tomonidan toʻliq hajmda qoplanishi lozim.",
                                "commentary": "O'z mol-mulkidan foydalana turib qo'shnisining yoki jamiyatning mulkiga zarar yetkazgan mulkdor o'sha zararni moddiy qoplashga majburdir.",
                                "category": "Fuqarolik huquqi / Deliktual majburiyat",
                                "lex_link": "https://lex.uz/docs/-111189#985",
                                "sanction": "Moddiy va ma'naviy zararni sud orqali to'liq undirish."
                            },
                            {
                                "id": "OILA-23",
                                "code_title": "Oʻzbekiston Respublikasi Oila Kodeksi",
                                "article_ref": "23-modda",
                                "norm_name": "Er va xotinning birgalikdagi mulkiga egalik qilish va tasarruf etish",
                                "verbatim_text": "Er va xotin tomonidan nikoh davomida orttirilgan mol-mulk ularning birgalikdagi umumiy mulki hisoblanadi. Mol-mulkni tasarruf etish er va xotinning o'zaro roziligi bilan amalga oshiriladi.",
                                "commentary": "Mulkdor o'z xohishicha tasarruf etishi mumkin, lekin mulk nikoh davomida orttirilgan bo'lsa, ikkinchi tarafning huquqlari buzilmasligi shart.",
                                "category": "Oila huquqi",
                                "lex_link": "https://lex.uz/docs/-122042#23",
                                "sanction": "Notarial tasdiqlangan roziliksiz tuzilgan ko'chmas mulk bitimini haqiqiy emas deb topish."
                            }
                        ]
                    }
                ]
            },
            {
                "number": "67-modda",
                "title": "Investitsiyaviy muhit, tadbirkorlik va iqtisodiy makon erkinligi",
                "clauses": [
                    {
                        "clause_id": "67-1",
                        "number": "1-qism",
                        "text": "Davlat qulay investitsiyaviy va ishbilarmonlik muhitini taʼminlaydi.",
                        "blanket_norms": [
                            {
                                "id": "INVEST-12",
                                "code_title": "Oʻzbekiston Respublikasining 'Investitsiyalar va investitsiya faoliyati toʻgʻrisida'gi Qonuni (OʻRQ-598)",
                                "article_ref": "12 va 19-moddalar",
                                "norm_name": "Investorlar huquqlarining kafolatlari va rejim barqarorligi",
                                "verbatim_text": "Investorlarning huquqlari, invested qilingan kapitalning rekvizitsiya qilinmasligi va olingan foydani chet el valyutasida erkin olib chiqib ketish kafolatlanadi. Qonunchilik o'zgarganda investor uchun 10 yil davomida ilgarigi qonunchilikni qo'llash (Kafolat kaliti) huquqi beriladi.",
                                "commentary": "Ushbu norma investitsiyaviy muhitning barqarorligini va xorijiy hamda mahalliy sarmoyadorlar uchun huquqiy xavfsizlikni yaratadi.",
                                "category": "Investitsiya huquqi",
                                "lex_link": "https://lex.uz/docs/-4664127",
                                "sanction": "Davlat organlarining investor huquqini buzuvchi noqonuniy hujjatlarini bekor qilish va zararni davlat hisobidan qoplash."
                            },
                            {
                                "id": "SK-75",
                                "code_title": "Oʻzbekiston Respublikasi Soliq Kodeksi",
                                "article_ref": "75 va 76-moddalar",
                                "norm_name": "Soliq imtiyozlari va investitsiyaviy kreditlar",
                                "verbatim_text": "Investitsiya faoliyatini rag'batlantirish maqsadida qonun hujjatlari bilan investitsiyaviy soliq kreditlari, kamaytirilgan soliq stavkalari hamda soliq ta'tillari belgilanishi mumkin.",
                                "commentary": "Davlat biznes subyektlariga soliq yengilliklari berish orqali qulay ishbilarmonlik muhitini barpo etadi.",
                                "category": "Soliq huquqi",
                                "lex_link": "https://lex.uz/docs/-4674902",
                                "sanction": "Soliq organlari tomonidan imtiyozlarni asossiz rad etganlik uchun ma'muriy javobgarlik."
                            }
                        ]
                    },
                    {
                        "clause_id": "67-2",
                        "number": "2-qism",
                        "text": "Tadbirkorlar qonunchilikka muvofiq har qanday faoliyatni amalga oshirishga va oʻz faoliyati yoʻnalishlarini mustaqil ravishda tanlashga haqli.",
                        "blanket_norms": [
                            {
                                "id": "TADBIRKOR-8",
                                "code_title": "Oʻzbekiston Respublikasining 'Tadbirkorlik faoliyati erkinligining kafolatlari toʻgʻrisida'gi Qonuni",
                                "article_ref": "3, 4 va 8-moddalar",
                                "norm_name": "Tadbirkorlik subyektlarining faoliyat yo'nalishlarini erkin tanlash huquqi",
                                "verbatim_text": "Tadbirkorlik subyektlari qonun bilan taqiqlanmagan har qanday faoliyat turini amalga oshirishga, mahsulot narxlarini va foydani tasarruf etish yo'nalishlarini mustaqil belgilashga haqlidir.",
                                "commentary": "Davlat idoralari tadbirkorga qanday mahsulot ishlab chiqarishni yoki qancha narx qo'yishni majburlab tayinlay olmaydi.",
                                "category": "Tadbirkorlik huquqi",
                                "lex_link": "https://lex.uz/docs/-2059628",
                                "sanction": "Tadbirkor faoliyatiga g'ayriqonuniy aralashganlik uchun JK 192-1-moddasi bo'yicha jinoiy javobgarlik."
                            },
                            {
                                "id": "LITSENZIYA-7",
                                "code_title": "Oʻzbekiston Respublikasining 'Litsenziyalash, ruxsat berish va xabardor qilish tartib-taomillari toʻgʻrisida'gi Qonuni (OʻRQ-701)",
                                "article_ref": "7-modda",
                                "norm_name": "Faoliyat turlarini litsenziyalash shartlari va erkinligi",
                                "verbatim_text": "Faqat Inson hayoti va xavfsizligiga xavf tug'dirishi mumkin bo'lgan faoliyat turlari qonunda belgilangan tartibda litsenziyalanadi. Boshqa barcha faoliyat turlari mutlaqo erkindir.",
                                "commentary": "Litsenziyalanadigan faoliyat turlari ro'yxati cheklangan bo'lib, uni asossiz kengaytirishga yo'l qo'yilmaydi.",
                                "category": "Ma'muriy tartib-taomillar",
                                "lex_link": "https://lex.uz/docs/-5512211",
                                "sanction": "Litsenziyani berishni asossiz paysalga solganlik uchun ma'muriy jarima."
                            }
                        ]
                    },
                    {
                        "clause_id": "67-3",
                        "number": "3-qism",
                        "text": "Oʻzbekiston Respublikasi hududida iqtisodiy makon birligi, tovarlar, xizmatlar, mehnat resurslari va moliyaviy mablagʻlarning erkin harakatlanishi kafolatlanadi.",
                        "blanket_norms": [
                            {
                                "id": "BOJXONA-15",
                                "code_title": "Oʻzbekiston Respublikasi Bojxona Kodeksi",
                                "article_ref": "15-modda",
                                "norm_name": "Tovarlarning Oʻzbekiston hududida ichki erkin muomalasi",
                                "verbatim_text": "Oʻzbekiston Respublikasining bojxona hududi yagona hisoblanadi. Viloyatlar yoki shahar/tumanlar o'rtasida ichki bojxona postlari o'rnatish, tovarlar harakatiga to'siq qo'yish taqiqlanadi.",
                                "commentary": "Mahalliy hokimliklar o'z hududidan qishloq xo'jaligi yoki sanoat mahsulotlarini olib chiqib ketishga hech qanday taqiq yoki cheklov qo'ya olmaydi.",
                                "category": "Bojxona huquqi",
                                "lex_link": "https://lex.uz/docs/-2876354",
                                "sanction": "Noqonuniy ichki blokpost va taqiqlarni darhol bekor qilish hamda mansabdor shaxsni javobgarlikka tortish."
                            },
                            {
                                "id": "VALYUTA-18",
                                "code_title": "Oʻzbekiston Respublikasining 'Valyutani tartibga solish toʻgʻrisida'gi Qonuni (OʻRQ-573)",
                                "article_ref": "18-modda",
                                "norm_name": "Moliyaviy mablag'lar va valyuta operatsiyalarining erkinligi",
                                "verbatim_text": "Rezidentlar va noresidentlar moliyaviy mablag'larni va valyuta qimmatliklarini O'zbekiston Respublikasiga erkin o'tkazish hamda mamlakat ichida qonuniy muomalaga kiritish huquqiga ega.",
                                "commentary": "Kapitalning va moliyaviy resurslarning mamlakat hududida to'siqsiz aylanishi kafolatlanadi.",
                                "category": "Moliya va valyuta huquqi",
                                "lex_link": "https://lex.uz/docs/-4563820",
                                "sanction": "Noqonuniy valyuta cheklovlari va hisobraqamlarni bloklash uchun bank va soliq idoralariga chora ko'rish."
                            }
                        ]
                    },
                    {
                        "clause_id": "67-4",
                        "number": "67-modda 4-qism",
                        "text": "Monopol faoliyat qonun bilan tartibga solinadi va cheklanadi.",
                        "blanket_norms": [
                            {
                                "id": "MONOPOLIYA-18",
                                "code_title": "Oʻzbekiston Respublikasining 'Raqobat toʻgʻrisida'gi Qonuni",
                                "article_ref": "18 va 19-moddalar",
                                "norm_name": "Ustun mavqeni suiste'mol qilishni taqiqlash va monopoliyaga qarshi nazorat",
                                "verbatim_text": "Bozorda ustun mavqega ega bo'lgan subyektlar tomonidan narxlarni sun'iy oshirish yoki ushlab turish, boshqa subyektlarning bozorga kirishiga to'sqinlik qilish monopol faoliyat deb topiladi va qat'iyan taqiqlanadi.",
                                "commentary": "Monopoliyalar ustidan Raqobatni rivojlantirish va iste'molchilar huquqlarini himoya qilish qo'mitasi doimiy nazorat olib boradi.",
                                "category": "Raqobat huquqi",
                                "lex_link": "https://lex.uz/docs/-6483120",
                                "sanction": "Monopol daromadni davlat byudjetiga musodara qilish va asossiz oshirilgan narxlarni tushirish."
                            },
                            {
                                "id": "TABIIY-MONOPOLIYA-15",
                                "code_title": "Oʻzbekiston Respublikasining 'Tabiiy monopoliyalar toʻgʻrisida'gi Qonuni",
                                "article_ref": "15-modda",
                                "norm_name": "Tabiiy monopoliya subyektlari faoliyatini va tariflarini tartibga solish",
                                "verbatim_text": "Tabiiy monopoliya subyektlarining (gaz, elektr, suv, temir yo'l) xizmat ko'rsatish tariflari va narxlari davlat tomonidan belgilangan tartibda tartibga solinadi.",
                                "commentary": "Iqtisodiyotda tabiatan monopol bo'lgan sohalarda davlat narxlar asossiz oshib ketmasligi uchun narx chegaralarini belgilaydi.",
                                "category": "Monopoliyaga qarshi tartibga solish",
                                "lex_link": "https://lex.uz/docs/-15011",
                                "sanction": "Noqonuniy oshirilgan tarif summalarini iste'molchilarga qaytarish."
                            }
                        ]
                    }
                ]
            },
            {
                "number": "68-modda",
                "title": "Tabiiy resurslarga bo'lgan mulkchilik va yer resurslari",
                "clauses": [
                    {
                        "clause_id": "68-1",
                        "number": "1-qism",
                        "text": "Yer, yer osti boyliklari, suv, oʻsimlik va hayvonot dunyosi hamda boshqa tabiiy resurslar umummilliy boylikdir, ulardan oqilona foydalanish zarur va ular davlat muhofazasidadir.",
                        "blanket_norms": [
                            {
                                "id": "YK-1",
                                "code_title": "Oʻzbekiston Respublikasi Yer Kodeksi",
                                "article_ref": "1 va 8-moddalar",
                                "norm_name": "Yerning umummilliy boylikligi va yer fondi kategoriyalari",
                                "verbatim_text": "Yer — Oʻzbekiston Respublikasi xalqining hayoti va faoliyatini taʼminlovchi umummilliy boylikdir. Yer resurslaridan oqilona, samarali va belgilangan maqsadda foydalanish shart.",
                                "commentary": "Yer va tabiiy resurslar xalq manfaati uchun xizmat qilishi kerak. Ularni barbod qilish yoki asossiz ishg'ol etish taqiqlanadi.",
                                "category": "Yer huquqi",
                                "lex_link": "https://lex.uz/docs/-152653",
                                "sanction": "Yerni o'zboshimchalik bilan egallaganlik uchun JK 229-1-moddasi bo'yicha jinoiy javobgarlik."
                            },
                            {
                                "id": "YEROSTI-4",
                                "code_title": "Oʻzbekiston Respublikasining 'Yer osti boyliklari toʻgʻrisida'gi Qonuni",
                                "article_ref": "4 va 10-moddalar",
                                "norm_name": "Yer osti boyliklariga mulkchilik va konlardan foydalanish",
                                "verbatim_text": "Yer osti boyliklari, shu jumladan foydali qazilmalar davlat mulkidir. Yer osti boyliklaridan foydalanish litsenziyalar va kon ajratmalari asosida amalga oshiriladi.",
                                "commentary": "Xususiy shaxs o'z yerida oltin yoki neft topsa ham, yer osti boyligi davlat mulki bo'lib qolaveradi.",
                                "category": "Kon huquqi va Tabiiy resurslar",
                                "lex_link": "https://lex.uz/docs/-62423",
                                "sanction": "Foydali qazilmalarni noqonuniy qazib olganlik uchun kon mulkini musodara qilish va noqonuniy daromadni undirish."
                            },
                            {
                                "id": "SUV-3",
                                "code_title": "Oʻzbekiston Respublikasining 'Suv va suvdan foydalanish toʻgʻrisida'gi Qonuni",
                                "article_ref": "3-modda",
                                "norm_name": "Suv resurslariga davlat mulkchiligi va muhofazasi",
                                "verbatim_text": "Suv Oʻzbekiston Respublikasining davlat mulkidir — umummilliy boylikdir. Suv obyektlarini xususiylashtirishga va oldi-sotdi qilishga yoʻl qoʻyilmaydi.",
                                "commentary": "Daryolar, ko'llar va yer osti suvlari strategik boylik bo'lib, ular barcha fuqarolar ehtiyojiga xizmat qiladi.",
                                "category": "Suv huquqi",
                                "lex_link": "https://lex.uz/docs/-15000",
                                "sanction": "Suv havzalarini ifloslantirganlik va noqonuniy to'sib olganlik uchun ma'muriy va jinoiy choralar."
                            }
                        ]
                    },
                    {
                        "clause_id": "68-2",
                        "number": "2-qism",
                        "text": "Yer qonunda nazarda tutilgan hamda undan oqilona foydalanishni va uni umummilliy boylik sifatida muhofaza qilishni taʼminlovchi shartlar asosida va tartibda xususiy mulk boʻlishi mumkin.",
                        "blanket_norms": [
                            {
                                "id": "YK-18",
                                "code_title": "Oʻzbekiston Respublikasi Yer Kodeksi",
                                "article_ref": "18 va 18-1-moddalar",
                                "norm_name": "Jismoniy va yuridik shaxslarning yer uchastkalariga bo'lgan xususiy mulk huquqi",
                                "verbatim_text": "Qishloq xo'jaligiga mo'ljallanmagan yer uchastkalari O'zbekiston Respublikasi fuqarolari va yuridik shaxslariga xususiylashtirish va auksion orqali xususiy mulk huquqi bilan berilishi mumkin.",
                                "commentary": "2021-yildan e'tiboran O'zbekistonda tadbirkorlik va yakka tartibdagi uy-joy qurilishi uchun mo'ljallangan yerlarni xususiylashtirish huquqi belgilandi. Qishloq xo'jaligi yerlari esa xususiylashtirilmaydi, faqat ijaraga beriladi.",
                                "category": "Yer huquqi / Xususiylashtirish",
                                "lex_link": "https://lex.uz/docs/-152653#18",
                                "sanction": "Xususiy mulk bo'lgan yer uchastkasiga egalik huquqining daxlsizligi sud va davlat kadastri tomonidan kafolatlanadi."
                            },
                            {
                                "id": "YER-PRIVAT-8",
                                "code_title": "Oʻzbekiston Respublikasining 'Qishloq xoʻjaligiga moʻljallanmagan yer uchastkalarini xususiylashtirish toʻgʻrisida'gi Qonuni (OʻRQ-732)",
                                "article_ref": "8, 10 va 24-moddalar",
                                "norm_name": "Yerni xususiylashtirish ob'ektlari va shartlari",
                                "verbatim_text": "O'ziga tegishli bino va inshootlar joylashgan yer uchastkalari fuqarolar va yuridik shaxslar tomonidan qayta sotib olish (xususiylashtirish) orqali xususiy mulkka aylantirilishi mumkin.",
                                "commentary": "Yerga bo'lgan xususiy mulk investitsiya kiritish uchun eng barqaror huquqiy poydevor hisoblanadi.",
                                "category": "Xususiylashtirish huquqi",
                                "lex_link": "https://lex.uz/docs/-5725350",
                                "sanction": "Yer uchastkasiga bo'lgan xususiy mulk huquqini buzgan organ qarorlarini bekor qilish."
                            }
                        ]
                    }
                ]
            }
        ]
    }

db = load_constitutional_database()

if "selected_norm" not in st.session_state:
    st.session_state["selected_norm"] = None

if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""

if "favorite_norms" not in st.session_state:
    st.session_state["favorite_norms"] = []

def open_norm_modal(norm_data):
    st.session_state["selected_norm"] = norm_data

def close_norm_modal():
    st.session_state["selected_norm"] = None

def toggle_favorite(norm_id):
    if norm_id in st.session_state["favorite_norms"]:
        st.session_state["favorite_norms"].remove(norm_id)
    else:
        st.session_state["favorite_norms"].append(norm_id)

# Count total metrics
total_articles = len(db["articles"])
total_clauses = sum(len(a["clauses"]) for a in db["articles"])
all_norms = []
for a in db["articles"]:
    for c in a["clauses"]:
        for n in c["blanket_norms"]:
            all_norms.append(n)
total_norms = len(all_norms)

st.markdown(f"""
<div style="text-align: center; padding: 20px 0 10px 0;">
    <div style="display: inline-block; padding: 6px 16px; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 30px; color: #38bdf8; font-size: 0.85rem; font-weight: 700; letter-spacing: 1.5px; margin-bottom: 12px; text-transform: uppercase;">
        Oʻzbekiston Respublikasi Konstitutsiyasi
    </div>
    <h1 style="font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0 0 10px 0;">
        {db['chapter']['subtitle']}
    </h1>
    <p style="color: #94a3b8; font-size: 1.1rem; max-width: 800px; margin: 0 auto 25px auto;">
        Konstitutsiya moddalari va har bir qismiga bog'langan <b>Blanket Normalar</b> bazasi. Har bir havola ustiga bosib, tegishli O'zbekiston Qonuni yoki Kodeksining <u>asl matnini</u> o'rganishingiz mumkin.
    </p>
</div>
""", unsafe_allow_html=True)

# Top Analytical Statistics Row
col_s1, col_s2, col_s3, col_s4 = st.columns(4)

with col_s1:
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-number">4</div>
        <div class="stats-label">Moddalar (65-68)</div>
    </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-number">{total_clauses}</div>
        <div class="stats-label">Strukturaliy Qismlar</div>
    </div>
    """, unsafe_allow_html=True)

with col_s3:
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-number">{total_norms}</div>
        <div class="stats-label">Blanket Normalar</div>
    </div>
    """, unsafe_allow_html=True)

with col_s4:
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-number">10+</div>
        <div class="stats-label">Kodeks va Qonunlar</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

search_col1, search_col2 = st.columns([3, 1])

with search_col1:
    user_search = st.text_input(
        "🔍 Konstitutsiya moddalari yoki blanket normalar bo'yicha izlash:",
        placeholder="Masalan: Xususiy mulk, Raqobat, Yer Kodeksi, Soliq, Mulkdor...",
        key="global_search_input"
    )

with search_col2:
    category_filter = st.selectbox(
        "⚖️ Soha bo'yicha filter:",
        ["Barchasi", "Fuqarolik huquqi", "Tadbirkorlik huquqi", "Yer huquqi", "Investitsiya huquqi", "Iste'molchilar huquqi", "Raqobat huquqi"]
    )

st.markdown("---")

# Check if a modal/dialog should be rendered
if st.session_state["selected_norm"] is not None:
    norm = st.session_state["selected_norm"]
    
    st.markdown("""
    <div style="background: rgba(2, 6, 23, 0.85); position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 999; backdrop-filter: blur(10px);"></div>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown(f"""
        <div style="background: #0f172a; border: 2px solid #38bdf8; border-radius: 20px; padding: 30px; margin-bottom: 30px; box-shadow: 0 0 40px rgba(56, 189, 248, 0.4);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <span style="background: #0284c7; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">
                    ASLI VA SHARHI (BLANKET NORMA)
                </span>
                <span style="color: #94a3b8; font-size: 0.9rem;">Soha: <b>{norm['category']}</b></span>
            </div>
            <h2 style="color: #38bdf8; margin: 0 0 10px 0; font-size: 1.8rem;">{norm['code_title']}</h2>
            <h4 style="color: #e2e8f0; margin: 0 0 20px 0; font-weight: 600;">📌 {norm['article_ref']}: {norm['norm_name']}</h4>
            
            <div style="background: rgba(30, 41, 59, 0.8); border-left: 5px solid #10b981; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                <h5 style="color: #10b981; margin-top: 0; font-size: 1rem; text-transform: uppercase; letter-spacing: 1px;">📜 Qonun moddasining asl matni:</h5>
                <p style="color: #f8fafc; font-size: 1.1rem; line-height: 1.8; font-style: italic; margin: 0;">
                    "{norm['verbatim_text']}"
                </p>
            </div>

            <div style="background: rgba(30, 41, 59, 0.5); padding: 18px; border-radius: 12px; margin-bottom: 20px;">
                <h5 style="color: #818cf8; margin-top: 0;">💡 Konstitutsiyaviy bog'liqlik sharhi:</h5>
                <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.6; margin: 0;">
                    {norm['commentary']}
                </p>
            </div>

            <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); padding: 15px; border-radius: 10px; margin-bottom: 25px;">
                <h5 style="color: #f87171; margin-top: 0; margin-bottom: 5px;">⚖️ Huquqiy oqibat va sanksiya:</h5>
                <p style="color: #fca5a5; margin: 0; font-size: 0.95rem;">
                    {norm['sanction']}
                </p>
            </div>

            <div style="display: flex; gap: 15px; justify-content: flex-end;">
                <a href="{norm['lex_link']}" target="_blank" style="text-decoration: none;">
                    <button style="background: #0284c7; color: white; border: none; padding: 10px 20px; border-radius: 10px; font-weight: 600; cursor: pointer;">
                        🔗 Lex.uz da rasmiy matnini ko'rish
                    </button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("❌ Yopish (Asosiy sahifaga qaytish)", key="close_modal_btn"):
            close_norm_modal()
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Main Navigation Tabs
tab_main, tab_search_results, tab_matrix, tab_quiz = st.tabs([
    "📖 XII Bob Moddalari va Blanket Normalar",
    "🔍 Izlash va Natijalar",
    "📊 Qonunchilik Tarmog'i va Matritsa",
    "🎓 Interaktiv Bilim Sinovi (Quiz)"
])

with tab_main:
    st.subheader("Oʻzbekiston Respublikasi Konstitutsiyasi — XII Bob")
    st.info("💡 Har bir moddaning tegishli qismidagi **Blanket Norma** tugmachasini bosing. O'sha zahotiyoq qonunning asl matni va huquqiy oqibatlari namoyon bo'ladi.")
    
    for article in db["articles"]:
        st.markdown(f"""
        <div class="legal-card">
            <div class="article-header">{article['number']}. {article['title']}</div>
        """, unsafe_allow_html=True)
        
        for clause in article["clauses"]:
            st.markdown(f"""
            <div class="clause-box">
                <strong style="color: #38bdf8;">[{clause['number']}]</strong> {clause['text']}
            </div>
            """, unsafe_allow_html=True)
            
            st.write("<b>Ushbu qismga bog'liq blanket normalar (O'zR Qonunchiligi):</b>", unsafe_allow_html=True)
            
            # Display blanket norms as clickable buttons grid
            norm_cols = st.columns(len(clause["blanket_norms"]))
            for idx, norm in enumerate(clause["blanket_norms"]):
                with norm_cols[idx]:
                    btn_label = f"📜 {norm['article_ref']}\n({norm['code_title'].split(' ')[-1]})"
                    if st.button(f"🔗 {norm['article_ref']}: {norm['norm_name'][:25]}...", key=f"btn_{clause['clause_id']}_{norm['id']}"):
                        open_norm_modal(norm)
                        st.rerun()
            st.markdown("<hr style='border-color: rgba(255,255,255,0.05); margin: 20px 0;'>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

with tab_search_results:
    st.subheader("🔍 blanket Normalar Bo'yicha Qidiruv Markazi")
    
    query = user_search.strip().lower()
    
    matched_norms = []
    for article in db["articles"]:
        for clause in article["clauses"]:
            for norm in clause["blanket_norms"]:
                # Filter check
                category_match = (category_filter == "Barchasi") or (norm["category"] == category_filter)
                text_match = (
                    query in norm["code_title"].lower() or
                    query in norm["article_ref"].lower() or
                    query in norm["norm_name"].lower() or
                    query in norm["verbatim_text"].lower() or
                    query in norm["commentary"].lower() or
                    query in clause["text"].lower()
                )
                if category_match and (text_match or not query):
                    matched_norms.append((article["number"], clause["number"], norm))
    
    if matched_norms:
        st.success(f"Jami **{len(matched_norms)}** ta mos keluvchi blanket norma topildi.")
        
        for art_num, cl_num, norm in matched_norms:
            with st.expander(f"📌 [{art_num}, {cl_num}] {norm['code_title']} — {norm['article_ref']}: {norm['norm_name']}"):
                st.markdown(f"**Soha:** `{norm['category']}`")
                st.markdown(f"**Asl Matni:** *\"{norm['verbatim_text']}\"*")
                st.markdown(f"**Sharh:** {norm['commentary']}")
                st.markdown(f"**Sanksiya / Oqibat:** `{norm['sanction']}`")
                
                if st.button("🔎 To'liq oynada ochish", key=f"search_open_{norm['id']}"):
                    open_norm_modal(norm)
                    st.rerun()
    else:
        st.warning("Kiritilgan so'rov bo'yicha hech qanday blanket norma topilmadi. Qidiruv so'zini o'zgartirib ko'ring.")

with tab_matrix:
    st.subheader("📊 XII Bob Blanket Normalarining Iqtisodiy Sohalar Kesimidagi Tahlili")
    
    matrix_data = []
    for article in db["articles"]:
        for clause in article["clauses"]:
            for norm in clause["blanket_norms"]:
                matrix_data.append({
                    "Konstitutsiya Moddasi": article["number"],
                    "Qismi": clause["number"],
                    "Hujjat Nomi": norm["code_title"],
                    "Modda": norm["article_ref"],
                    "Soha": norm["category"]
                })
    
    df = pd.DataFrame(matrix_data)
    
    col_m1, col_m2 = st.columns([2, 1])
    
    with col_m1:
        st.write("### Blanket normalar jadvali")
        st.dataframe(df, use_container_width=True)
        
    with col_m2:
        st.write("### Sohalar bo'yicha taqsimot")
        category_counts = df["Soha"].value_counts()
        st.bar_chart(category_counts)
        
    st.markdown("""
    ### 🏛️ Huquqiy Ierarxiya va Blanket Texnikasi
    Konstitutsiya — O'zbekiston Respublikasining Oliy yuridik kuchga ega Bosh Qonunidir. 
    XII bobdagi normalar **blanket norma** uslubida tuzilgan. Bu degani:
    1. **Konstitutsiyaviy Tamoyil:** Mulk daxlsizligi, halol raqobat va erkinlik belgilab beriladi.
    2. **Qonuniy Rivojlantirish:** Ushbu tamoyillar Fuqarolik, Yer, Soliq Kodekslari va Maxsus Qonunlar orqali batafsil mexanizmlar bilan ta'minlanadi.
    """)

with tab_quiz:
    st.subheader("🎓 Konstitutsiya va Blanket Normalarni Sinash Testi")
    st.write("O'zingizning huquqiy bilimlaringizni sinab ko'ring:")
    
    q1 = st.radio(
        "1. Konstitutsiyaning 65-moddasiga ko'ra, xususiy mulk shaxsidan qaysi organning qaroriga ko'ra va qonunda belgilangan tartibda mahrum etilishi mumkin?",
        ["Tuman hokimligi qarori bilan", "Sud qarori bilan", "Iste'molchilar uyushmasi bilan", "Soliq inspeksiyasi bilan"],
        index=None
    )
    
    if q1:
        if q1 == "Sud qarori bilan":
            st.success("✅ To'g'ri! Konstitutsiyaning 65-moddasi 3-qismiga ko'ra, mulkdor sud qarorisiz mol-mulkidan mahrum etilishi mumkin emas (FK 206-modda).")
        else:
            st.error("❌ Noto'g'ri. Konstitutsiya bo'yicha faqat SUD qarori asosida mahrum etilishi mumkin.")
            
    st.markdown("---")
    
    q2 = st.radio(
        "2. Yer qaysi shartlarda va qaysi toifadagi yerlar uchun xususiy mulk bo'lishi mumkin (68-modda 2-qism)?",
        ["Barcha qishloq xo'jaligi yerlari", "Qishloq xo'jaligiga mo'ljallanmagan yerlar va qonunda belgilangan shartlarda", "Faqat chet el fuqarolariga", "Hech qachon xususiy mulk bo'la olmaydi"],
        index=None
    )
    
    if q2:
        if q2 == "Qishloq xo'jaligiga mo'ljallanmagan yerlar va qonunda belgilangan shartlarda":
            st.success("✅ To'g'ri! Yer Kodeksining 18-moddasi hamda O'RQ-732-sonli qonun bo'yicha qishloq xo'jaligiga mo'ljallanmagan yerlar xususiylashtirilishi mumkin.")
        else:
            st.error("❌ Noto'g'ri. Qishloq xo'jaligiga mo'ljallanmagan yerlar xususiy mulk bo'lishi mumkin.")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.85rem; padding: 20px 0;">
    Oʻzbekiston Respublikasi Konstitutsiyasi XII bobining Blanket Normalari Portali • 2026<br>
    Rasmiy manba: <a href="https://lex.uz/docs/-6445145" target="_blank" class="lex-link">Lex.uz Oʻzbekiston Respublikasi Qonunchilik maʼlumotlari milliy bazasi</a>
</div>
""", unsafe_allow_html=True)
