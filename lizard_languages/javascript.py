'''
Language parser for JavaScript
'''

from .code_reader import CodeReader
from .clike import CCppCommentsMixin
from .js_style_regex_expression import js_style_regex_expression
from .js_style_language_states import JavaScriptStyleLanguageStates


class JavaScriptReader(CodeReader, CCppCommentsMixin):
    # pylint: disable=R0903

    ext = ['js']
    language_names = ['javascript', 'js']

    @staticmethod
    @js_style_regex_expression
    def generate_tokens(source_code, extra='', tokener=None):
        extra += r"|(?:\$\w+)"
        return CodeReader.generate_tokens(source_code, extra, tokener)

    def __init__(self, context):
        super(JavaScriptReader, self).__init__(context)
        self.parallel_states = [JavaScriptStyleLanguageStates(context)]
