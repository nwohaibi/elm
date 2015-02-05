# -*- coding: utf-8 -*-

'''
# Based on Python 3
# No poetry, this is programming in Arabic. Please do not use your "heavy" Arabic.
 TODOs: 
   - cross mapping dict from Arabic to English
   - treating أ as ا and ـة as ـه
   - Long process and based on usage -> mapping_keywords dict: Must agree on one keyword or agree on several
   - Separate classes from keywords e.g. True is a class in python 
'''

# dict of the main mapping of Python English keywords to Arabic keywords. 
# Arabic mappings must truly reflect the meaning, in a most simplest way. 
mapping_keywords = {

    'and' : [u'و'],
    'as' : [u'كما', u'مثل', u'كانما', u'كانه', u'كانها', u'مثلما'], 
    'assert' : [u'اكد', u'تأكد', u'تاكد من'],
    'break' : [u'قف', u'توقف'],
    'class' : [u'فصيلة', u'صنف', u'عائلة', u'فصيل'],
    'continue' : [u'اكمل', u'كمل', u'تجاوز', u'تعدى', u'تخطى', ],
    'def' : [u'عرف', u'تعريف'],
    'del' : [u'احذف', u'حذف', u'ازل', u'اهمل'],
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
    'not' : [u'ليس'],
    'or' : [u'أو'],  # need a better keyword ? see 'else'
    'pass' : [u'تجاهل', u'تجاوز', u'تعدى'],
    'print' : [u'اكتب', u'اطبع', u'اظهر', u'اخرج'],
    'raise' : [u'خطا'],
    'return' : [u'النتيجة', u'ارجع'],
    'try' : [u'جرب'],
    'while' : [u'طالما',u'بينما',u'ما دام',u'ما دامت'],
    'with' : [u'مع'],
    'yield' : [u'انتج', u'اعط'],
        
}


# (TODO) consulting with Arabic math teacher.
mapping_inter_keywords = {
    'b' : [u'ب'], # بايت Bytes e.g. b'ascii' , B'bytes' they produce an instance of the bytes type instead of the str type
    'B' : [u'ب'], # بايت Bytes e.g. b'ascii' , B'bytes' they produce an instance of the bytes type instead of the str type
    'r' : [u'م'], # مجرد Raw e.g. r'\nn\n' , R'\nn\n' raw strings and treat backslashes as literal characters.
    'R' : [u'م'], # مجرد Raw e.g. r'\nn\n' , R'\nn\n' raw strings and treat backslashes as literal characters.
    'br' : [u'بم'], # بايت مجرد Raw Bytes e.g. br'ascii\n' 
    'rb' : [u'مب'], # مجرد بايت Raw Bytes e.g. rb'\nn\n' 
    '0o' : [u'0o'], # int e.g. 0o177 == 127 
    '0O' : [u'0O'], # int e.g. 0O177 == 127 
    '0b' : [u'0b'], # int e.g. 0b100110111 == 311 
    '0B' : [u'0B'], # int e.g. 0B100110111 == 311 
    '0x' : [u'0x'], # int e.g. 0x100000000 == 4294967296L 
    '0X' : [u'0X'], # int e.g. 0X100000000 == 4294967296L 
    'e' : [u'e'], # e.g. 3.14e-10 
    'E' : [u'E'], # e.g. 3.14E-10 
    'j' : [u'j'], # e.g. 10j 
    'J' : [u'J'], # e.g. 10J 
}

mapping_std_classes = {
    'set' : [u'مجموعة'],
    #'library' : [u'مكتبة'],
    'dict' : [u'فهرس', u'قاموس', u'دليل', u'قائمة'],
    'type' : [u'نوع'],
    #'matrix' : [u'مصفوفة'],
    'list' : [u'صف', u'سرد', u'سجل'],
    'None' : [u'صف', u'سرد', u'سجل'],

}

mapping_builtins_classes = 
    'ArithmeticError': ArithmeticError,
    'AssertionError': AssertionError,
    'AttributeError': AttributeError,
    'BaseException': BaseException,
    'BufferError': BufferError,
    'BytesWarning': BytesWarning,
    'DeprecationWarning': DeprecationWarning,
    'EOFError': EOFError,
    'Ellipsis': Ellipsis,
    'EnvironmentError': EnvironmentError,
    'Exception': Exception,
    'False': False,
    'FloatingPointError': FloatingPointError,
    'FutureWarning': FutureWarning,
    'GeneratorExit': GeneratorExit,
    'IOError': IOError,
    'ImportError': ImportError,
    'ImportWarning': ImportWarning,
    'IndentationError': IndentationError,
    'IndexError': IndexError,
    'KeyError': KeyError,
    'KeyboardInterrupt': KeyboardInterrupt,
    'LookupError': LookupError,
    'MemoryError': MemoryError,
    'NameError': NameError,
    'None': None,
    'NotImplemented': NotImplemented,
    'NotImplementedError': NotImplementedError,
    'OSError': OSError,
    'OverflowError': OverflowError,
    'PendingDeprecationWarning': PendingDeprecationWarning,
    'ReferenceError': ReferenceError,
    'RuntimeError': RuntimeError,
    'RuntimeWarning': RuntimeWarning,
    'StandardError': StandardError,
    'StopIteration': StopIteration,
    'SyntaxError': SyntaxError,
    'SyntaxWarning': SyntaxWarning,
    'SystemError': SystemError,
    'SystemExit': SystemExit,
    'TabError': TabError,
    'True': True,
    'TypeError': TypeError,
    'UnboundLocalError': UnboundLocalError,
    'UnicodeDecodeError': UnicodeDecodeError,
    'UnicodeEncodeError': UnicodeEncodeError,
    'UnicodeError': UnicodeError,
    'UnicodeTranslateError': UnicodeTranslateError,
    'UnicodeWarning': UnicodeWarning,
    'UserWarning': UserWarning,
    'ValueError': ValueError,
    'Warning': Warning,
    'WindowsError': WindowsError,
    'ZeroDivisionError': ZeroDivisionError,
    '__IPYTHON__': True,
    '__IPYTHON__active': 'Deprecated, check for __IPYTHON__',
    '__debug__': True,
    '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.",
    '__import__': <function __import__>,
    '__name__': '__builtin__',
    '__package__': None,
    'abs': <function abs>,
    'all': <function all>,
    'any': <function any>,
    'apply': <function apply>,
    'basestring': basestring,
    'bin': <function bin>,
    'bool': bool,
    'buffer': buffer,
    'bytearray': bytearray,
    'bytes': str,
    'callable': <function callable>,
    'chr': <function chr>,
    'classmethod': classmethod,
    'cmp': <function cmp>,
    'coerce': <function coerce>,
    'compile': <function compile>,
    'complex': complex,
    'copyright': 
    'credits': 
    'delattr': <function delattr>,
    'dict': dict,
    'dir': <function dir>,
    'divmod': <function divmod>,
    'dreload': <function IPython.lib.deepreload.reload>,
    'enumerate': enumerate,
    'eval': <function eval>,
    'execfile': <function execfile>,
    'file': file,
    'filter': <function filter>,
    'float': float,
    'format': <function format>,
    'frozenset': frozenset,
    'get_ipython': <bound method ZMQInteractiveShell.get_ipython of <IPython.kernel.zmq.zmqshell.ZMQInteractiveShell object at 0x0000000004B03470>>,
    'getattr': <function getattr>,
    'globals': <function globals>,
    'hasattr': <function hasattr>,
    'hash': <function hash>,
    'help': Type help() for interactive help, or help(object) for help about object.,
    'hex': <function hex>,
    'id': <function id>,
    'input': <function IPython.kernel.zmq.ipkernel.<lambda>>,
    'int': int,
    'intern': <function intern>,
    'isinstance': <function isinstance>,
    'issubclass': <function issubclass>,
    'iter': <function iter>,
    'len': <function len>,
    'license': See http://www.python.org/2.7/license.html,
    'list': list,
    'locals': <function locals>,
    'long': long,
    'map': <function map>,
    'max': <function max>,
    'memoryview': memoryview,
    'min': <function min>,
    'next': <function next>,
    'object': object,
    'oct': <function oct>,
    'open': <function open>,
    'ord': <function ord>,
    'pow': <function pow>,
    'print': <function print>,
    'property': property,
    'range': <function range>,
    'raw_input': <function IPython.kernel.zmq.ipkernel.<lambda>>,
    'reduce': <function reduce>,
    'reload': <function reload>,
    'repr': <function repr>,
    'reversed': reversed,
    'round': <function round>,
    'set': set,
    'setattr': <function setattr>,
    'slice': slice,
    'sorted': <function sorted>,
    'staticmethod': staticmethod,
    'str': str,
    'sum': <function sum>,
    'super': super,
    'tuple': tuple,
    'type': type,
    'unichr': <function unichr>,
    'unicode': unicode,
    'vars': <function vars>,
    'xrange': xrange,
    'zip': <function zip>
 }


