# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01aa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\2\7\2m\n\2\f\2\16\2p\13\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3z\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u0081")
        buf.write("\n\4\3\5\3\5\5\5\u0085\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u008f\n\6\3\7\3\7\3\7\5\7\u0094\n\7\3\b\3\b\5")
        buf.write("\b\u0098\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\5\13\u00a5\n\13\3\f\3\f\3\f\3\f\5\f\u00ab\n\f\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00b1\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00b8\n\16\3\17\3\17\5\17\u00bc\n\17\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00c2\n\20\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00c9\n\21\3\22\5\22\u00cc\n\22\3\22\3\22\5\22\u00d0")
        buf.write("\n\22\3\23\3\23\3\23\3\23\5\23\u00d6\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00dd\n\24\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00e3\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00ea\n\26\3")
        buf.write("\27\3\27\3\27\5\27\u00ef\n\27\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00f5\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00fc\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u0103\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\7\33\u010b\n\33\f\33\16\33\u010e\13\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0116\n\34\f\34\16")
        buf.write("\34\u0119\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0121")
        buf.write("\n\35\f\35\16\35\u0124\13\35\3\36\3\36\3\36\5\36\u0129")
        buf.write("\n\36\3\37\3\37\3\37\5\37\u012e\n\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \7 \u0138\n \f \16 \u013b\13 \3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\5!\u0145\n!\3\"\3\"\3\"\3\"\3\"\5\"\u014c\n\"")
        buf.write("\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u015c\n")
        buf.write("$\3$\3$\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u016d\n\'\3(\3(\3(\3(\5(\u0173\n(\3)\3)\3)\3)\3)")
        buf.write("\5)\u017a\n)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3.\3.\3/\3/\5/\u0194\n/\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\6\62\u019e\n\62\r\62\16")
        buf.write("\62\u019f\5\62\u01a2\n\62\3\63\3\63\5\63\u01a6\n\63\3")
        buf.write("\64\3\64\3\64\2\6\64\668>\65\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdf\2\b\4\2 \"$%\4\2\65\66::\3\2\22\30\3\2\33\34\3\2")
        buf.write("\r\16\3\2\17\21\2\u01ab\2n\3\2\2\2\4s\3\2\2\2\6{\3\2\2")
        buf.write("\2\b\u0084\3\2\2\2\n\u008e\3\2\2\2\f\u0090\3\2\2\2\16")
        buf.write("\u0097\3\2\2\2\20\u0099\3\2\2\2\22\u009b\3\2\2\2\24\u00a4")
        buf.write("\3\2\2\2\26\u00aa\3\2\2\2\30\u00b0\3\2\2\2\32\u00b7\3")
        buf.write("\2\2\2\34\u00bb\3\2\2\2\36\u00c1\3\2\2\2 \u00c8\3\2\2")
        buf.write("\2\"\u00cf\3\2\2\2$\u00d5\3\2\2\2&\u00dc\3\2\2\2(\u00e2")
        buf.write("\3\2\2\2*\u00e9\3\2\2\2,\u00ee\3\2\2\2.\u00f4\3\2\2\2")
        buf.write("\60\u00fb\3\2\2\2\62\u0102\3\2\2\2\64\u0104\3\2\2\2\66")
        buf.write("\u010f\3\2\2\28\u011a\3\2\2\2:\u0128\3\2\2\2<\u012d\3")
        buf.write("\2\2\2>\u012f\3\2\2\2@\u0144\3\2\2\2B\u014b\3\2\2\2D\u014d")
        buf.write("\3\2\2\2F\u015b\3\2\2\2H\u015f\3\2\2\2J\u0161\3\2\2\2")
        buf.write("L\u0165\3\2\2\2N\u0172\3\2\2\2P\u0179\3\2\2\2R\u017b\3")
        buf.write("\2\2\2T\u0181\3\2\2\2V\u0184\3\2\2\2X\u018d\3\2\2\2Z\u018f")
        buf.write("\3\2\2\2\\\u0191\3\2\2\2^\u0195\3\2\2\2`\u0197\3\2\2\2")
        buf.write("b\u01a1\3\2\2\2d\u01a5\3\2\2\2f\u01a7\3\2\2\2hm\5F$\2")
        buf.write("im\5\6\4\2jm\5\4\3\2km\79\2\2lh\3\2\2\2li\3\2\2\2lj\3")
        buf.write("\2\2\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2oq\3\2\2")
        buf.write("\2pn\3\2\2\2qr\7\2\2\3r\3\3\2\2\2st\7&\2\2tu\7;\2\2uv")
        buf.write("\7\b\2\2vw\5\36\20\2wy\7\t\2\2xz\5\b\5\2yx\3\2\2\2yz\3")
        buf.write("\2\2\2z\5\3\2\2\2{|\7&\2\2|}\7\3\2\2}~\7\b\2\2~\u0080")
        buf.write("\7\t\2\2\177\u0081\5\b\5\2\u0080\177\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\7\3\2\2\2\u0082\u0085\5`\61\2\u0083\u0085")
        buf.write("\5\\/\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\t\3\2\2\2\u0086\u0087\t\2\2\2\u0087\u008f\5\f\7\2\u0088")
        buf.write("\u0089\5\22\n\2\u0089\u008a\7;\2\2\u008a\u008b\7\4\2\2")
        buf.write("\u008b\u008c\5,\27\2\u008c\u008d\7\5\2\2\u008d\u008f\3")
        buf.write("\2\2\2\u008e\u0086\3\2\2\2\u008e\u0088\3\2\2\2\u008f\13")
        buf.write("\3\2\2\2\u0090\u0093\7;\2\2\u0091\u0092\7\31\2\2\u0092")
        buf.write("\u0094\5\60\31\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2")
        buf.write("\2\u0094\r\3\2\2\2\u0095\u0098\5\20\t\2\u0096\u0098\5")
        buf.write("\22\n\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\17\3\2\2\2\u0099\u009a\t\3\2\2\u009a\21\3\2\2\2\u009b")
        buf.write("\u009c\5\20\t\2\u009c\u009d\7;\2\2\u009d\u009e\7\4\2\2")
        buf.write("\u009e\u009f\5\24\13\2\u009f\u00a0\7\5\2\2\u00a0\23\3")
        buf.write("\2\2\2\u00a1\u00a2\7\65\2\2\u00a2\u00a5\5\26\f\2\u00a3")
        buf.write("\u00a5\7\65\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a3\3\2\2")
        buf.write("\2\u00a5\25\3\2\2\2\u00a6\u00a7\7\n\2\2\u00a7\u00a8\7")
        buf.write("\65\2\2\u00a8\u00ab\5\26\f\2\u00a9\u00ab\3\2\2\2\u00aa")
        buf.write("\u00a6\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\27\3\2\2\2\u00ac")
        buf.write("\u00ad\5\34\17\2\u00ad\u00ae\5\32\16\2\u00ae\u00b1\3\2")
        buf.write("\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\31\3\2\2\2\u00b2\u00b3\7\n\2\2\u00b3\u00b4")
        buf.write("\5\34\17\2\u00b4\u00b5\5\32\16\2\u00b5\u00b8\3\2\2\2\u00b6")
        buf.write("\u00b8\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\33\3\2\2\2\u00b9\u00bc\7;\2\2\u00ba\u00bc\5f\64")
        buf.write("\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\35\3")
        buf.write("\2\2\2\u00bd\u00be\5\"\22\2\u00be\u00bf\5 \21\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bd\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\37\3\2\2\2\u00c3\u00c4\7\n")
        buf.write("\2\2\u00c4\u00c5\5\"\22\2\u00c5\u00c6\5 \21\2\u00c6\u00c9")
        buf.write("\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9!\3\2\2\2\u00ca\u00cc\5\20\t\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00d0\7;\2\2\u00ce\u00d0\5\22\n\2\u00cf\u00cb\3")
        buf.write("\2\2\2\u00cf\u00ce\3\2\2\2\u00d0#\3\2\2\2\u00d1\u00d2")
        buf.write("\5F$\2\u00d2\u00d3\5&\24\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6")
        buf.write("\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("%\3\2\2\2\u00d7\u00d8\79\2\2\u00d8\u00d9\5F$\2\u00d9\u00da")
        buf.write("\5&\24\2\u00da\u00dd\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc")
        buf.write("\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\'\3\2\2\2\u00de")
        buf.write("\u00df\5\4\3\2\u00df\u00e0\5*\26\2\u00e0\u00e3\3\2\2\2")
        buf.write("\u00e1\u00e3\3\2\2\2\u00e2\u00de\3\2\2\2\u00e2\u00e1\3")
        buf.write("\2\2\2\u00e3)\3\2\2\2\u00e4\u00e5\79\2\2\u00e5\u00e6\5")
        buf.write("\4\3\2\u00e6\u00e7\5*\26\2\u00e7\u00ea\3\2\2\2\u00e8\u00ea")
        buf.write("\3\2\2\2\u00e9\u00e4\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write("+\3\2\2\2\u00eb\u00ec\7\67\2\2\u00ec\u00ef\5.\30\2\u00ed")
        buf.write("\u00ef\7\67\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ed\3\2\2")
        buf.write("\2\u00ef-\3\2\2\2\u00f0\u00f1\7\n\2\2\u00f1\u00f2\7\67")
        buf.write("\2\2\u00f2\u00f5\5.\30\2\u00f3\u00f5\3\2\2\2\u00f4\u00f0")
        buf.write("\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5/\3\2\2\2\u00f6\u00f7")
        buf.write("\5\62\32\2\u00f7\u00f8\7\35\2\2\u00f8\u00f9\5\62\32\2")
        buf.write("\u00f9\u00fc\3\2\2\2\u00fa\u00fc\5\62\32\2\u00fb\u00f6")
        buf.write("\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\61\3\2\2\2\u00fd\u00fe")
        buf.write("\5\64\33\2\u00fe\u00ff\t\4\2\2\u00ff\u0100\5\64\33\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u0103\5\64\33\2\u0102\u00fd\3\2\2")
        buf.write("\2\u0102\u0101\3\2\2\2\u0103\63\3\2\2\2\u0104\u0105\b")
        buf.write("\33\1\2\u0105\u0106\5\66\34\2\u0106\u010c\3\2\2\2\u0107")
        buf.write("\u0108\f\4\2\2\u0108\u0109\t\5\2\2\u0109\u010b\5\66\34")
        buf.write("\2\u010a\u0107\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\65\3\2\2\2\u010e\u010c")
        buf.write("\3\2\2\2\u010f\u0110\b\34\1\2\u0110\u0111\58\35\2\u0111")
        buf.write("\u0117\3\2\2\2\u0112\u0113\f\4\2\2\u0113\u0114\t\6\2\2")
        buf.write("\u0114\u0116\58\35\2\u0115\u0112\3\2\2\2\u0116\u0119\3")
        buf.write("\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\67")
        buf.write("\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\b\35\1\2\u011b")
        buf.write("\u011c\5:\36\2\u011c\u0122\3\2\2\2\u011d\u011e\f\4\2\2")
        buf.write("\u011e\u011f\t\7\2\2\u011f\u0121\5:\36\2\u0120\u011d\3")
        buf.write("\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u01239\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126")
        buf.write("\7\32\2\2\u0126\u0129\5:\36\2\u0127\u0129\5<\37\2\u0128")
        buf.write("\u0125\3\2\2\2\u0128\u0127\3\2\2\2\u0129;\3\2\2\2\u012a")
        buf.write("\u012b\7\16\2\2\u012b\u012e\5<\37\2\u012c\u012e\5> \2")
        buf.write("\u012d\u012a\3\2\2\2\u012d\u012c\3\2\2\2\u012e=\3\2\2")
        buf.write("\2\u012f\u0130\b \1\2\u0130\u0131\5@!\2\u0131\u0139\3")
        buf.write("\2\2\2\u0132\u0133\f\4\2\2\u0133\u0134\7\4\2\2\u0134\u0135")
        buf.write("\5B\"\2\u0135\u0136\7\5\2\2\u0136\u0138\3\2\2\2\u0137")
        buf.write("\u0132\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a?\3\2\2\2\u013b\u0139\3\2\2")
        buf.write("\2\u013c\u0145\5f\64\2\u013d\u0145\5\22\n\2\u013e\u013f")
        buf.write("\7\b\2\2\u013f\u0140\5\60\31\2\u0140\u0141\7\t\2\2\u0141")
        buf.write("\u0145\3\2\2\2\u0142\u0145\7;\2\2\u0143\u0145\5^\60\2")
        buf.write("\u0144\u013c\3\2\2\2\u0144\u013d\3\2\2\2\u0144\u013e\3")
        buf.write("\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145A")
        buf.write("\3\2\2\2\u0146\u014c\5\60\31\2\u0147\u0148\5\60\31\2\u0148")
        buf.write("\u0149\7\n\2\2\u0149\u014a\5B\"\2\u014a\u014c\3\2\2\2")
        buf.write("\u014b\u0146\3\2\2\2\u014b\u0147\3\2\2\2\u014cC\3\2\2")
        buf.write("\2\u014d\u014e\7;\2\2\u014e\u014f\7\6\2\2\u014f\u0150")
        buf.write("\5\30\r\2\u0150\u0151\7\7\2\2\u0151E\3\2\2\2\u0152\u015c")
        buf.write("\5H%\2\u0153\u015c\5J&\2\u0154\u015c\5L\'\2\u0155\u015c")
        buf.write("\5V,\2\u0156\u015c\5X-\2\u0157\u015c\5Z.\2\u0158\u015c")
        buf.write("\5\\/\2\u0159\u015c\5^\60\2\u015a\u015c\5`\61\2\u015b")
        buf.write("\u0152\3\2\2\2\u015b\u0153\3\2\2\2\u015b\u0154\3\2\2\2")
        buf.write("\u015b\u0155\3\2\2\2\u015b\u0156\3\2\2\2\u015b\u0157\3")
        buf.write("\2\2\2\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\79\2\2\u015e")
        buf.write("G\3\2\2\2\u015f\u0160\5\n\6\2\u0160I\3\2\2\2\u0161\u0162")
        buf.write("\5d\63\2\u0162\u0163\7\31\2\2\u0163\u0164\5\60\31\2\u0164")
        buf.write("K\3\2\2\2\u0165\u0166\7,\2\2\u0166\u0167\7\b\2\2\u0167")
        buf.write("\u0168\5\60\31\2\u0168\u0169\7\t\2\2\u0169\u016a\5F$\2")
        buf.write("\u016a\u016c\5N(\2\u016b\u016d\5T+\2\u016c\u016b\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016dM\3\2\2\2\u016e\u016f\5R*")
        buf.write("\2\u016f\u0170\5P)\2\u0170\u0173\3\2\2\2\u0171\u0173\3")
        buf.write("\2\2\2\u0172\u016e\3\2\2\2\u0172\u0171\3\2\2\2\u0173O")
        buf.write("\3\2\2\2\u0174\u0175\79\2\2\u0175\u0176\5R*\2\u0176\u0177")
        buf.write("\5P)\2\u0177\u017a\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0174")
        buf.write("\3\2\2\2\u0179\u0178\3\2\2\2\u017aQ\3\2\2\2\u017b\u017c")
        buf.write("\7.\2\2\u017c\u017d\7\b\2\2\u017d\u017e\5\60\31\2\u017e")
        buf.write("\u017f\7\t\2\2\u017f\u0180\5F$\2\u0180S\3\2\2\2\u0181")
        buf.write("\u0182\7-\2\2\u0182\u0183\5F$\2\u0183U\3\2\2\2\u0184\u0185")
        buf.write("\7\'\2\2\u0185\u0186\7;\2\2\u0186\u0187\7(\2\2\u0187\u0188")
        buf.write("\5\60\31\2\u0188\u0189\7)\2\2\u0189\u018a\5\60\31\2\u018a")
        buf.write("\u018b\79\2\2\u018b\u018c\5$\23\2\u018cW\3\2\2\2\u018d")
        buf.write("\u018e\7*\2\2\u018eY\3\2\2\2\u018f\u0190\7+\2\2\u0190")
        buf.write("[\3\2\2\2\u0191\u0193\7#\2\2\u0192\u0194\5\60\31\2\u0193")
        buf.write("\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194]\3\2\2\2\u0195")
        buf.write("\u0196\5D#\2\u0196_\3\2\2\2\u0197\u0198\7/\2\2\u0198\u0199")
        buf.write("\5b\62\2\u0199\u019a\7\60\2\2\u019aa\3\2\2\2\u019b\u01a2")
        buf.write("\5$\23\2\u019c\u019e\79\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u01a2\3\2\2\2\u01a1\u019b\3\2\2\2\u01a1\u019d\3")
        buf.write("\2\2\2\u01a2c\3\2\2\2\u01a3\u01a6\7;\2\2\u01a4\u01a6\5")
        buf.write("> \2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6e\3")
        buf.write("\2\2\2\u01a7\u01a8\t\3\2\2\u01a8g\3\2\2\2+lny\u0080\u0084")
        buf.write("\u008e\u0093\u0097\u00a4\u00aa\u00b0\u00b7\u00bb\u00c1")
        buf.write("\u00c8\u00cb\u00cf\u00d5\u00dc\u00e2\u00e9\u00ee\u00f4")
        buf.write("\u00fb\u0102\u010c\u0117\u0122\u0128\u012d\u0139\u0144")
        buf.write("\u014b\u015b\u016c\u0172\u0179\u0193\u019f\u01a1\u01a5")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "','", "':'", "';'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'=='", "'!='", "'>'", "'<'", 
                     "'<='", "'>='", "'<-'", "'not'", "'and'", "'OR'", "'...'", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'int'", "'float'", 
                     "'const'", "'.'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LSB", "RSB", "LCB", "RCB", 
                      "LB", "RB", "CM", "COLON", "SM", "ADD", "MINUS", "MUL", 
                      "DIV", "MOD", "ASSIGN", "EQ", "DIFF", "GT", "LT", 
                      "LTEQ", "GTEQ", "WIS", "NOT", "AND", "OR", "STRCONCAT", 
                      "TRUE_", "FALSE_", "NUM", "BOOL_", "STR_", "RET_", 
                      "VAR_", "DYNAMIC", "FUNC_", "FOR_", "UNTIL", "BY", 
                      "BREAK_", "CONT", "IF_", "ELSE_", "ELSE_IF", "BEGIN", 
                      "END", "INT_", "FLOAT_", "CONST_", "DOT", "NUMBERS", 
                      "BOOLS", "INT_PART", "EXPO_PART", "NEWLINE", "STRS", 
                      "ID", "LINECMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_func_decl = 1
    RULE_main_decl = 2
    RULE_func_body = 3
    RULE_var_decl = 4
    RULE_singDecl = 5
    RULE_typ = 6
    RULE_primitive = 7
    RULE_arrayT = 8
    RULE_indexExpr = 9
    RULE_indexTail = 10
    RULE_argList = 11
    RULE_argT = 12
    RULE_argument = 13
    RULE_paramList = 14
    RULE_paramT = 15
    RULE_param = 16
    RULE_stmt_list = 17
    RULE_stmtT = 18
    RULE_func_list = 19
    RULE_funcT = 20
    RULE_sizeList = 21
    RULE_sizeT = 22
    RULE_expr = 23
    RULE_expr1 = 24
    RULE_expr2 = 25
    RULE_expr3 = 26
    RULE_expr4 = 27
    RULE_expr5 = 28
    RULE_expr6 = 29
    RULE_expr7 = 30
    RULE_expr8 = 31
    RULE_index_op = 32
    RULE_funcCall = 33
    RULE_statements = 34
    RULE_var_declStmt = 35
    RULE_assignStmt = 36
    RULE_ifStmt = 37
    RULE_elifStmt = 38
    RULE_elseifT = 39
    RULE_elif1 = 40
    RULE_elseStmt = 41
    RULE_forStmt = 42
    RULE_breakStmt = 43
    RULE_contStmt = 44
    RULE_returnStmt = 45
    RULE_funcCallStmt = 46
    RULE_blockStmt = 47
    RULE_blockBody = 48
    RULE_lhs = 49
    RULE_literals = 50

    ruleNames =  [ "program", "func_decl", "main_decl", "func_body", "var_decl", 
                   "singDecl", "typ", "primitive", "arrayT", "indexExpr", 
                   "indexTail", "argList", "argT", "argument", "paramList", 
                   "paramT", "param", "stmt_list", "stmtT", "func_list", 
                   "funcT", "sizeList", "sizeT", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "index_op", "funcCall", "statements", "var_declStmt", 
                   "assignStmt", "ifStmt", "elifStmt", "elseifT", "elif1", 
                   "elseStmt", "forStmt", "breakStmt", "contStmt", "returnStmt", 
                   "funcCallStmt", "blockStmt", "blockBody", "lhs", "literals" ]

    EOF = Token.EOF
    T__0=1
    LSB=2
    RSB=3
    LCB=4
    RCB=5
    LB=6
    RB=7
    CM=8
    COLON=9
    SM=10
    ADD=11
    MINUS=12
    MUL=13
    DIV=14
    MOD=15
    ASSIGN=16
    EQ=17
    DIFF=18
    GT=19
    LT=20
    LTEQ=21
    GTEQ=22
    WIS=23
    NOT=24
    AND=25
    OR=26
    STRCONCAT=27
    TRUE_=28
    FALSE_=29
    NUM=30
    BOOL_=31
    STR_=32
    RET_=33
    VAR_=34
    DYNAMIC=35
    FUNC_=36
    FOR_=37
    UNTIL=38
    BY=39
    BREAK_=40
    CONT=41
    IF_=42
    ELSE_=43
    ELSE_IF=44
    BEGIN=45
    END=46
    INT_=47
    FLOAT_=48
    CONST_=49
    DOT=50
    NUMBERS=51
    BOOLS=52
    INT_PART=53
    EXPO_PART=54
    NEWLINE=55
    STRS=56
    ID=57
    LINECMT=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementsContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementsContext,i)


        def main_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Main_declContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Main_declContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Func_declContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Func_declContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.LB) | (1 << ZCodeParser.NUM) | (1 << ZCodeParser.BOOL_) | (1 << ZCodeParser.STR_) | (1 << ZCodeParser.RET_) | (1 << ZCodeParser.VAR_) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC_) | (1 << ZCodeParser.FOR_) | (1 << ZCodeParser.BREAK_) | (1 << ZCodeParser.CONT) | (1 << ZCodeParser.IF_) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.NUMBERS) | (1 << ZCodeParser.BOOLS) | (1 << ZCodeParser.NEWLINE) | (1 << ZCodeParser.STRS) | (1 << ZCodeParser.ID))) != 0):
                self.state = 106
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 102
                    self.statements()
                    pass

                elif la_ == 2:
                    self.state = 103
                    self.main_decl()
                    pass

                elif la_ == 3:
                    self.state = 104
                    self.func_decl()
                    pass

                elif la_ == 4:
                    self.state = 105
                    self.match(ZCodeParser.NEWLINE)
                    pass


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_(self):
            return self.getToken(ZCodeParser.FUNC_, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamListContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ZCodeParser.FUNC_)
            self.state = 114
            self.match(ZCodeParser.ID)
            self.state = 115
            self.match(ZCodeParser.LB)
            self.state = 116
            self.paramList()
            self.state = 117
            self.match(ZCodeParser.RB)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 118
                self.func_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_(self):
            return self.getToken(ZCodeParser.FUNC_, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_decl" ):
                return visitor.visitMain_decl(self)
            else:
                return visitor.visitChildren(self)




    def main_decl(self):

        localctx = ZCodeParser.Main_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ZCodeParser.FUNC_)
            self.state = 122
            self.match(ZCodeParser.T__0)
            self.state = 123
            self.match(ZCodeParser.LB)
            self.state = 124
            self.match(ZCodeParser.RB)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 125
                self.func_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_body)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.blockStmt()
                pass
            elif token in [ZCodeParser.RET_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.returnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singDecl(self):
            return self.getTypedRuleContext(ZCodeParser.SingDeclContext,0)


        def NUM(self):
            return self.getToken(ZCodeParser.NUM, 0)

        def BOOL_(self):
            return self.getToken(ZCodeParser.BOOL_, 0)

        def STR_(self):
            return self.getToken(ZCodeParser.STR_, 0)

        def VAR_(self):
            return self.getToken(ZCodeParser.VAR_, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def arrayT(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayTContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def sizeList(self):
            return self.getTypedRuleContext(ZCodeParser.SizeListContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM, ZCodeParser.BOOL_, ZCodeParser.STR_, ZCodeParser.VAR_, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM) | (1 << ZCodeParser.BOOL_) | (1 << ZCodeParser.STR_) | (1 << ZCodeParser.VAR_) | (1 << ZCodeParser.DYNAMIC))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.singDecl()
                pass
            elif token in [ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.arrayT()
                self.state = 135
                self.match(ZCodeParser.ID)
                self.state = 136
                self.match(ZCodeParser.LSB)
                self.state = 137
                self.sizeList()
                self.state = 138
                self.match(ZCodeParser.RSB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def WIS(self):
            return self.getToken(ZCodeParser.WIS, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_singDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingDecl" ):
                return visitor.visitSingDecl(self)
            else:
                return visitor.visitChildren(self)




    def singDecl(self):

        localctx = ZCodeParser.SingDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_singDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(ZCodeParser.ID)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.WIS:
                self.state = 143
                self.match(ZCodeParser.WIS)
                self.state = 144
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitiveContext,0)


        def arrayT(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.arrayT()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERS(self):
            return self.getToken(ZCodeParser.NUMBERS, 0)

        def BOOLS(self):
            return self.getToken(ZCodeParser.BOOLS, 0)

        def STRS(self):
            return self.getToken(ZCodeParser.STRS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive" ):
                return visitor.visitPrimitive(self)
            else:
                return visitor.visitChildren(self)




    def primitive(self):

        localctx = ZCodeParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primitive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBERS) | (1 << ZCodeParser.BOOLS) | (1 << ZCodeParser.STRS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitiveContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def indexExpr(self):
            return self.getTypedRuleContext(ZCodeParser.IndexExprContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayT" ):
                return visitor.visitArrayT(self)
            else:
                return visitor.visitChildren(self)




    def arrayT(self):

        localctx = ZCodeParser.ArrayTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayT)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.primitive()
            self.state = 154
            self.match(ZCodeParser.ID)
            self.state = 155
            self.match(ZCodeParser.LSB)
            self.state = 156
            self.indexExpr()
            self.state = 157
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERS(self):
            return self.getToken(ZCodeParser.NUMBERS, 0)

        def indexTail(self):
            return self.getTypedRuleContext(ZCodeParser.IndexTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)




    def indexExpr(self):

        localctx = ZCodeParser.IndexExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_indexExpr)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(ZCodeParser.NUMBERS)
                self.state = 160
                self.indexTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(ZCodeParser.NUMBERS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def NUMBERS(self):
            return self.getToken(ZCodeParser.NUMBERS, 0)

        def indexTail(self):
            return self.getTypedRuleContext(ZCodeParser.IndexTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexTail" ):
                return visitor.visitIndexTail(self)
            else:
                return visitor.visitChildren(self)




    def indexTail(self):

        localctx = ZCodeParser.IndexTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_indexTail)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(ZCodeParser.CM)
                self.state = 165
                self.match(ZCodeParser.NUMBERS)
                self.state = 166
                self.indexTail()
                pass
            elif token in [ZCodeParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentContext,0)


        def argT(self):
            return self.getTypedRuleContext(ZCodeParser.ArgTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = ZCodeParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argList)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.argument()
                self.state = 171
                self.argT()
                pass
            elif token in [ZCodeParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def argument(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentContext,0)


        def argT(self):
            return self.getTypedRuleContext(ZCodeParser.ArgTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgT" ):
                return visitor.visitArgT(self)
            else:
                return visitor.visitChildren(self)




    def argT(self):

        localctx = ZCodeParser.ArgTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argT)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.CM)
                self.state = 177
                self.argument()
                self.state = 178
                self.argT()
                pass
            elif token in [ZCodeParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ZCodeParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argument)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(ZCodeParser.ID)
                pass
            elif token in [ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.literals()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramT(self):
            return self.getTypedRuleContext(ZCodeParser.ParamTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ZCodeParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramList)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.param()
                self.state = 188
                self.paramT()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramT(self):
            return self.getTypedRuleContext(ZCodeParser.ParamTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamT" ):
                return visitor.visitParamT(self)
            else:
                return visitor.visitChildren(self)




    def paramT(self):

        localctx = ZCodeParser.ParamTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramT)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(ZCodeParser.CM)
                self.state = 194
                self.param()
                self.state = 195
                self.paramT()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def primitive(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitiveContext,0)


        def arrayT(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBERS) | (1 << ZCodeParser.BOOLS) | (1 << ZCodeParser.STRS))) != 0):
                    self.state = 200
                    self.primitive()


                self.state = 203
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.arrayT()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(ZCodeParser.StatementsContext,0)


        def stmtT(self):
            return self.getTypedRuleContext(ZCodeParser.StmtTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt_list)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LB, ZCodeParser.NUM, ZCodeParser.BOOL_, ZCodeParser.STR_, ZCodeParser.RET_, ZCodeParser.VAR_, ZCodeParser.DYNAMIC, ZCodeParser.FOR_, ZCodeParser.BREAK_, ZCodeParser.CONT, ZCodeParser.IF_, ZCodeParser.BEGIN, ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.statements()
                self.state = 208
                self.stmtT()
                pass
            elif token in [ZCodeParser.END, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def statements(self):
            return self.getTypedRuleContext(ZCodeParser.StatementsContext,0)


        def stmtT(self):
            return self.getTypedRuleContext(ZCodeParser.StmtTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtT" ):
                return visitor.visitStmtT(self)
            else:
                return visitor.visitChildren(self)




    def stmtT(self):

        localctx = ZCodeParser.StmtTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmtT)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(ZCodeParser.NEWLINE)
                self.state = 214
                self.statements()
                self.state = 215
                self.stmtT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def funcT(self):
            return self.getTypedRuleContext(ZCodeParser.FuncTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_list" ):
                return visitor.visitFunc_list(self)
            else:
                return visitor.visitChildren(self)




    def func_list(self):

        localctx = ZCodeParser.Func_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_func_list)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.func_decl()
                self.state = 221
                self.funcT()
                pass
            elif token in [ZCodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def funcT(self):
            return self.getTypedRuleContext(ZCodeParser.FuncTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncT" ):
                return visitor.visitFuncT(self)
            else:
                return visitor.visitChildren(self)




    def funcT(self):

        localctx = ZCodeParser.FuncTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcT)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(ZCodeParser.NEWLINE)
                self.state = 227
                self.func_decl()
                self.state = 228
                self.funcT()
                pass
            elif token in [ZCodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_PART(self):
            return self.getToken(ZCodeParser.INT_PART, 0)

        def sizeT(self):
            return self.getTypedRuleContext(ZCodeParser.SizeTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizeList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeList" ):
                return visitor.visitSizeList(self)
            else:
                return visitor.visitChildren(self)




    def sizeList(self):

        localctx = ZCodeParser.SizeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_sizeList)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.INT_PART)
                self.state = 234
                self.sizeT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(ZCodeParser.INT_PART)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def INT_PART(self):
            return self.getToken(ZCodeParser.INT_PART, 0)

        def sizeT(self):
            return self.getTypedRuleContext(ZCodeParser.SizeTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizeT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeT" ):
                return visitor.visitSizeT(self)
            else:
                return visitor.visitChildren(self)




    def sizeT(self):

        localctx = ZCodeParser.SizeTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sizeT)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(ZCodeParser.CM)
                self.state = 239
                self.match(ZCodeParser.INT_PART)
                self.state = 240
                self.sizeT()
                pass
            elif token in [ZCodeParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def STRCONCAT(self):
            return self.getToken(ZCodeParser.STRCONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.expr1()
                self.state = 245
                self.match(ZCodeParser.STRCONCAT)
                self.state = 246
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def DIFF(self):
            return self.getToken(ZCodeParser.DIFF, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTEQ(self):
            return self.getToken(ZCodeParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(ZCodeParser.GTEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.expr2(0)
                self.state = 252
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.ASSIGN) | (1 << ZCodeParser.EQ) | (1 << ZCodeParser.DIFF) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTEQ) | (1 << ZCodeParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.expr3(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.expr4(0) 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 283
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 284
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 285
                    self.expr5() 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr5)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(ZCodeParser.NOT)
                self.state = 292
                self.expr5()
                pass
            elif token in [ZCodeParser.LB, ZCodeParser.MINUS, ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr6)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(ZCodeParser.MINUS)
                self.state = 297
                self.expr6()
                pass
            elif token in [ZCodeParser.LB, ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    self.match(ZCodeParser.LSB)
                    self.state = 306
                    self.index_op()
                    self.state = 307
                    self.match(ZCodeParser.RSB) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def arrayT(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayTContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funcCallStmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCallStmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr8)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.arrayT()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.match(ZCodeParser.LB)
                self.state = 317
                self.expr()
                self.state = 318
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 321
                self.funcCallStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_index_op)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.expr()
                self.state = 326
                self.match(ZCodeParser.CM)
                self.state = 327
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LCB(self):
            return self.getToken(ZCodeParser.LCB, 0)

        def argList(self):
            return self.getTypedRuleContext(ZCodeParser.ArgListContext,0)


        def RCB(self):
            return self.getToken(ZCodeParser.RCB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = ZCodeParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.ID)
            self.state = 332
            self.match(ZCodeParser.LCB)
            self.state = 333
            self.argList()
            self.state = 334
            self.match(ZCodeParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def var_declStmt(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakStmtContext,0)


        def contStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStmtContext,0)


        def funcCallStmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCallStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = ZCodeParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 336
                self.var_declStmt()
                pass

            elif la_ == 2:
                self.state = 337
                self.assignStmt()
                pass

            elif la_ == 3:
                self.state = 338
                self.ifStmt()
                pass

            elif la_ == 4:
                self.state = 339
                self.forStmt()
                pass

            elif la_ == 5:
                self.state = 340
                self.breakStmt()
                pass

            elif la_ == 6:
                self.state = 341
                self.contStmt()
                pass

            elif la_ == 7:
                self.state = 342
                self.returnStmt()
                pass

            elif la_ == 8:
                self.state = 343
                self.funcCallStmt()
                pass

            elif la_ == 9:
                self.state = 344
                self.blockStmt()
                pass


            self.state = 347
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_declStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declStmt" ):
                return visitor.visitVar_declStmt(self)
            else:
                return visitor.visitChildren(self)




    def var_declStmt(self):

        localctx = ZCodeParser.Var_declStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_var_declStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def WIS(self):
            return self.getToken(ZCodeParser.WIS, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = ZCodeParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.lhs()
            self.state = 352
            self.match(ZCodeParser.WIS)
            self.state = 353
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_(self):
            return self.getToken(ZCodeParser.IF_, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def statements(self):
            return self.getTypedRuleContext(ZCodeParser.StatementsContext,0)


        def elifStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStmtContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ZCodeParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ZCodeParser.IF_)
            self.state = 356
            self.match(ZCodeParser.LB)
            self.state = 357
            self.expr()
            self.state = 358
            self.match(ZCodeParser.RB)
            self.state = 359
            self.statements()
            self.state = 360
            self.elifStmt()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ELSE_:
                self.state = 361
                self.elseStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif1(self):
            return self.getTypedRuleContext(ZCodeParser.Elif1Context,0)


        def elseifT(self):
            return self.getTypedRuleContext(ZCodeParser.ElseifTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStmt" ):
                return visitor.visitElifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elifStmt(self):

        localctx = ZCodeParser.ElifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elifStmt)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELSE_IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.elif1()
                self.state = 365
                self.elseifT()
                pass
            elif token in [ZCodeParser.ELSE_, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def elif1(self):
            return self.getTypedRuleContext(ZCodeParser.Elif1Context,0)


        def elseifT(self):
            return self.getTypedRuleContext(ZCodeParser.ElseifTContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseifT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifT" ):
                return visitor.visitElseifT(self)
            else:
                return visitor.visitChildren(self)




    def elseifT(self):

        localctx = ZCodeParser.ElseifTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elseifT)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(ZCodeParser.NEWLINE)
                self.state = 371
                self.elif1()
                self.state = 372
                self.elseifT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_IF(self):
            return self.getToken(ZCodeParser.ELSE_IF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def statements(self):
            return self.getTypedRuleContext(ZCodeParser.StatementsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif1" ):
                return visitor.visitElif1(self)
            else:
                return visitor.visitChildren(self)




    def elif1(self):

        localctx = ZCodeParser.Elif1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_elif1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(ZCodeParser.ELSE_IF)
            self.state = 378
            self.match(ZCodeParser.LB)
            self.state = 379
            self.expr()
            self.state = 380
            self.match(ZCodeParser.RB)
            self.state = 381
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(ZCodeParser.ELSE_, 0)

        def statements(self):
            return self.getTypedRuleContext(ZCodeParser.StatementsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = ZCodeParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(ZCodeParser.ELSE_)
            self.state = 384
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_(self):
            return self.getToken(ZCodeParser.FOR_, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = ZCodeParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(ZCodeParser.FOR_)
            self.state = 387
            self.match(ZCodeParser.ID)
            self.state = 388
            self.match(ZCodeParser.UNTIL)
            self.state = 389
            self.expr()
            self.state = 390
            self.match(ZCodeParser.BY)
            self.state = 391
            self.expr()
            self.state = 392
            self.match(ZCodeParser.NEWLINE)
            self.state = 393
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(ZCodeParser.BREAK_, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = ZCodeParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(ZCodeParser.BREAK_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT(self):
            return self.getToken(ZCodeParser.CONT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_contStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContStmt" ):
                return visitor.visitContStmt(self)
            else:
                return visitor.visitChildren(self)




    def contStmt(self):

        localctx = ZCodeParser.ContStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_contStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.CONT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RET_(self):
            return self.getToken(ZCodeParser.RET_, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = ZCodeParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(ZCodeParser.RET_)
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 400
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcCallStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallStmt" ):
                return visitor.visitFuncCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def funcCallStmt(self):

        localctx = ZCodeParser.FuncCallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_funcCallStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.funcCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def blockBody(self):
            return self.getTypedRuleContext(ZCodeParser.BlockBodyContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = ZCodeParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_blockStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(ZCodeParser.BEGIN)
            self.state = 406
            self.blockBody()
            self.state = 407
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockBody" ):
                return visitor.visitBlockBody(self)
            else:
                return visitor.visitChildren(self)




    def blockBody(self):

        localctx = ZCodeParser.BlockBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_blockBody)
        self._la = 0 # Token type
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LB, ZCodeParser.NUM, ZCodeParser.BOOL_, ZCodeParser.STR_, ZCodeParser.RET_, ZCodeParser.VAR_, ZCodeParser.DYNAMIC, ZCodeParser.FOR_, ZCodeParser.BREAK_, ZCodeParser.CONT, ZCodeParser.IF_, ZCodeParser.BEGIN, ZCodeParser.END, ZCodeParser.NUMBERS, ZCodeParser.BOOLS, ZCodeParser.STRS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.stmt_list()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 410
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 413 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_lhs)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.expr7(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERS(self):
            return self.getToken(ZCodeParser.NUMBERS, 0)

        def BOOLS(self):
            return self.getToken(ZCodeParser.BOOLS, 0)

        def STRS(self):
            return self.getToken(ZCodeParser.STRS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBERS) | (1 << ZCodeParser.BOOLS) | (1 << ZCodeParser.STRS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.expr2_sempred
        self._predicates[26] = self.expr3_sempred
        self._predicates[27] = self.expr4_sempred
        self._predicates[30] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




