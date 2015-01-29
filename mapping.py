# -*- coding: utf-8 -*-
#
# This is not poetry, this is programming in Arabic. Please do not use your "heavy" Arabic.
'''
 TODOs: 
   - cross mapping dict from Arabic to English
   - treating أ as ا and ـة as ـه
   - Long process and based on usage -> keyword_mapping dict: Must agree on one keyword or agree on several
   - Separate classes from keywords e.g. True is a class in python 
'''

# dict of the main mapping of Python English keywords to Arabic keywords. 
# Arabic mappings must truly reflect the meaning, in a most simplest way. 
keyword_mapping = {

    'and' : [u'و'],
    'as' : [u'كما', u'مثل', u'كانما', u'كانه', u'كانها', u'مثلما'], 
    'assert' : [u'اكد', u'تأكد', u'تاكد من'],
    'break' : [u'قف', u'توقف'],
    'class' : [u'فصيلة', u'صنف', u'عائلة', u'فصيل'],
    'continue' : [u'اكمل', u'كمل', u'تجاوز', u'تعدى', u'تخطى', ],
    'def' : [u'عرف', u'تعريف'],
    'del' : [u'احذف', u'حذف', u'ازل', u'اهمل'],
    'dict' : [u'فهرس', u'قاموس', u'دليل', u'قائمة'],
    'elif' : [u'او اذا', u'الا اذا'],
    'else' : [u'والا'], # need a better keyword ? see 'or'
    'except' : [u'الا', u'ما لم', u'اعترض', u'استثن', u'استثناء'],
    'exec' : [u'نفذ'],
    'finally' : [u'اخرا', u'اخيرا', u'ختاما', u'اختم'],
    'for' : [u'لكل'],
    'from' : [u'من'],
    'global' : [u'عام'], # need a better keyword ?
    'if' : [u'اذا'],
    'import' : [u'ادع', u'استدع', u'اجلب', u'استخدم'],
    'in' : [u'في'],
    'is' : [u'هو', u'هي'], # need a better keyword ?
    'lambda' : [u'دالة'],
    'library' : [u'مكتبة'],
    'list' : [u'صف', u'سرد', u'سجل'],
    'matrix' : [u'مصفوفة'],
    'not' : [u'ليس'],
    'or' : [u'أو'],  # need a better keyword ? see 'else'
    'pass' : [u'تجاهل', u'تجاوز', u'تعدى'],
    'print' : [u'اكتب', u'اطبع', u'اظهر', u'اخرج'],
    'raise' : [u'خطا'],
    'return' : [u'النتيجة', u'ارجع'],
    'set' : [u'مجموعة'],
    'try' : [u'جرب'],
    'type' : [u'نوع'],
    'while' : [u'طالما',u'بينما',u'ما دام',u'ما دامت'],
    'with' : [u'مع'],
    'yield' : [u'انتج', u'اعط'],
}

