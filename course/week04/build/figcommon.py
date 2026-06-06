# -*- coding: utf-8 -*-
import collections, openpyxl
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import arabic_reshaper; from bidi.algorithm import get_display
plt.rcParams.update({'font.family':'DejaVu Sans','axes.grid':True,'grid.alpha':0.25,'axes.spines.top':False,'axes.spines.right':False})
NAVY='#1E2761'; TEAL='#0E9D8C'; RED='#A23B3B'; AMBER='#B8860B'; GREY='#64748B'
PAL=['#1E2761','#0E9D8C','#A23B3B','#B8860B','#5B7DB1','#6F9C8F','#C9A0A0']
def ar(s):
    return get_display(arabic_reshaper.reshape(str(s)))
def fa2ar(s):   # corpus Persian letterforms -> Arabic
    return (s.replace('ی','ي').replace('ک','ك').replace('ﻯ','ي'))
# Arabic surah names (MSA) for surahs used in figures
SUR={1: 'الفاتحة', 2: 'البقرة', 3: 'آل عمران', 4: 'النساء', 5: 'المائدة', 6: 'الأنعام', 7: 'الأعراف', 8: 'الأنفال', 9: 'التوبة', 10: 'يونس', 11: 'هود', 12: 'يوسف', 13: 'الرعد', 14: 'إبراهيم', 15: 'الحجر', 16: 'النحل', 17: 'الإسراء', 18: 'الكهف', 19: 'مريم', 20: 'طه', 21: 'الأنبياء', 22: 'الحج', 23: 'المؤمنون', 24: 'النور', 25: 'الفرقان', 26: 'الشعراء', 27: 'النمل', 28: 'القصص', 29: 'العنكبوت', 30: 'الروم', 31: 'لقمان', 32: 'السجدة', 33: 'الأحزاب', 34: 'سبأ', 35: 'فاطر', 36: 'يس', 37: 'الصافات', 38: 'ص', 39: 'الزمر', 40: 'غافر', 41: 'فصلت', 42: 'الشورى', 43: 'الزخرف', 44: 'الدخان', 45: 'الجاثية', 46: 'الأحقاف', 47: 'محمد', 48: 'الفتح', 49: 'الحجرات', 50: 'ق', 51: 'الذاريات', 52: 'الطور', 53: 'النجم', 54: 'القمر', 55: 'الرحمن', 56: 'الواقعة', 57: 'الحديد', 58: 'المجادلة', 59: 'الحشر', 60: 'الممتحنة', 61: 'الصف', 62: 'الجمعة', 63: 'المنافقون', 64: 'التغابن', 65: 'الطلاق', 66: 'التحريم', 67: 'الملك', 68: 'القلم', 69: 'الحاقة', 70: 'المعارج', 71: 'نوح', 72: 'الجن', 73: 'المزمل', 74: 'المدثر', 75: 'القيامة', 76: 'الإنسان', 77: 'المرسلات', 78: 'النبأ', 79: 'النازعات', 80: 'عبس', 81: 'التكوير', 82: 'الانفطار', 83: 'المطففين', 84: 'الانشقاق', 85: 'البروج', 86: 'الطارق', 87: 'الأعلى', 88: 'الغاشية', 89: 'الفجر', 90: 'البلد', 91: 'الشمس', 92: 'الليل', 93: 'الضحى', 94: 'الشرح', 95: 'التين', 96: 'العلق', 97: 'القدر', 98: 'البينة', 99: 'الزلزلة', 100: 'العاديات', 101: 'القارعة', 102: 'التكاثر', 103: 'العصر', 104: 'الهمزة', 105: 'الفيل', 106: 'قريش', 107: 'الماعون', 108: 'الكوثر', 109: 'الكافرون', 110: 'النصر', 111: 'المسد', 112: 'الإخلاص', 113: 'الفلق', 114: 'الناس'}
def surA(n): return ar(SUR.get(n,str(n)))
def norm(s): return (s.replace('ی','ي').replace('ک','ك').replace('ﻯ','ي').replace('ئ','ء').replace('ؤ','ء').replace('أ','ء').replace('إ','ء').replace('آ','ء'))
def load():
    wb=openpyxl.load_workbook('/sessions/kind-compassionate-feynman/mnt/RootCourse/Book6.xlsx', read_only=True); ws=wb.active
    sa=collections.Counter(); stok=collections.Counter()
    rsd=collections.defaultdict(lambda: collections.Counter()); rst=collections.defaultdict(lambda: collections.Counter())
    form=collections.defaultdict(collections.Counter)
    for i,r in enumerate(ws.iter_rows(values_only=True)):
        if i<8: continue
        s,roots,forms=r[5],r[8],r[9]
        if not roots: continue
        s=int(s); toks=[norm(x) for x in str(roots).split()]; fm=str(forms).split() if forms else []
        sa[s]+=1; stok[s]+=len(toks)
        for t in toks: rst[t][s]+=1
        for t in set(toks): rsd[t][s]+=1
        if len(fm)==len(toks):
            for rr,ff in zip(toks,fm): form[rr][fa2ar(ff)]+=1
    return sa,stok,rsd,rst,form
