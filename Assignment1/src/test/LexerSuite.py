import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_case100(self):
        self.assertTrue(TestLexer.test("a b c d e", "a,b,c,d,e,<EOF>", 100))

    def test_case101(self):
        self.assertTrue(TestLexer.test("1 2 3 4 5", "1,2,3,4,5,<EOF>", 101))

    def test_case102(self):
        self.assertTrue(TestLexer.test("True False TRUE FaLse true", "True,False,TRUE,FaLse,true,<EOF>", 102))

    def test_case103(self):
        self.assertTrue(TestLexer.test("0.1 0.01 0.001 0.0001", "0.1,0.01,0.001,0.0001,<EOF>", 103))

    def test_case104(self):
        self.assertTrue(TestLexer.test("\"string1\" \"string2\" \"string3\"", "string1,string2,string3,<EOF>", 104))

    def test_case105(self):
        self.assertTrue(TestLexer.test("++ -- + - * /", "++,--,+,-,*,/,<EOF>", 105))

    def test_case106(self):
        self.assertTrue(TestLexer.test("== != > >= < <=", "==,!=,>,>=,<,<EOF>", 106))

    def test_case107(self):
        self.assertTrue(TestLexer.test("a[1] b[2] c[3]", "a[1],b[2],c[3],<EOF>", 107))

    def test_case108(self):
        self.assertTrue(TestLexer.test("Int FLOAT STRING BOOLEAN", "Int,FLOAT,STRING,BOOLEAN,<EOF>", 108))

    def test_case109(self):
        self.assertTrue(TestLexer.test("If Elseif Else", "If,Elseif,Else,<EOF>", 109))

    def test_case110(self):
        self.assertTrue(TestLexer.test("Return Array New", "Return,Array,New,<EOF>", 110))

    def test_case111(self):
        self.assertTrue(TestLexer.test("Class Val Var Self Null", "Class,Val,Var,Self,Null,<EOF>", 111))

    def test_case112(self):
        self.assertTrue(TestLexer.test("Constructor Destructor By", "Constructor,Destructor,By,<EOF>", 112))

    def test_case113(self):
        self.assertTrue(TestLexer.test("Var a :Int", "Var,a,:,Int,<EOF>", 113))

    def test_case114(self):
        self.assertTrue(TestLexer.test("Val b,c :String", "Val,b,,,c,:,String,<EOF>", 114))

    def test_case115(self):
        self.assertTrue(TestLexer.test("Foreach Break Continue In", "Foreach,Break,Continue,In,<EOF>", 115))

    def test_case116(self):
        self.assertTrue(TestLexer.test("####abc##", "<EOF>", 116))

    def test_case117(self):
        self.assertTrue(TestLexer.test("... :::", "...,:,:,<EOF>", 117))

    def test_case118(self):
        self.assertTrue(TestLexer.test("$$$ $$a$$ $$abc", "Error Token $", 118))

    def test_case119(self):
        self.assertTrue(TestLexer.test("1 2.5 3.0 4e2 5E-3", "1,2.5,3.0,4e2,5E-3,<EOF>", 119))

    def test_case120(self):
        self.assertTrue(TestLexer.test("\"abc\" \"123\" \"xyz\"", "abc,123,xyz,<EOF>", 120))

    def test_case121(self):
        self.assertTrue(TestLexer.test("if (a == b) then a else b", "if,(,a,==,b,),then,a,else,b,<EOF>", 121))

    def test_case122(self):
        self.assertTrue(TestLexer.test("for i in range(10): print(i)", "for,i,in,range,(,10,),:,print,(,i,),<EOF>", 122))

    def test_case123(self):
        self.assertTrue(TestLexer.test("var x = 5 + 3 * 2", "var,x,=,5,+,3,*,2,<EOF>", 123))

    def test_case124(self):
        self.assertTrue(TestLexer.test("func add(a, b) { return a + b }", "func,add,(,a,,,b,),{,return,a,+,b,},<EOF>", 124))

    def test_case125(self):
        self.assertTrue(TestLexer.test("while (x > 0) { x = x - 1 }", "while,(,x,>,0,),{,x,=,x,-,1,},<EOF>", 125))

    def test_case126(self):
        self.assertTrue(TestLexer.test("123.456 0.0 9876.54321", "123.456,0.0,9876.54321,<EOF>", 126))

    def test_case127(self):
        self.assertTrue(TestLexer.test("var str = \"Hello, World!\"", "var,str,=,\"Hello, World!\",<EOF>", 127))

    def test_case128(self):
        self.assertTrue(TestLexer.test("return true and false or true", "return,true,and,false,or,true,<EOF>", 128))

    def test_case129(self):
        self.assertTrue(TestLexer.test("if (a <= b) then a else b", "if,(,a,<=,b,),then,a,else,b,<EOF>", 129))

    def test_case130(self):
        self.assertTrue(TestLexer.test("for i in range(1, 10, 2): print(i)", "for,i,in,range,(,1,,,10,,,2,),:,print,(,i,),<EOF>", 130))

    def test_case131(self):
        self.assertTrue(TestLexer.test("var x = 5 + 3 * (2 - 1)", "var,x,=,5,+,3,*,(,2,-,1,),<EOF>", 131))

    def test_case132(self):
        self.assertTrue(TestLexer.test("func multiply(a, b) { return a * b }", "func,multiply,(,a,,,b,),{,return,a,*,b,},<EOF>", 132))

    def test_case133(self):
        self.assertTrue(TestLexer.test("while (x >= 0) { x = x + 1 }", "while,(,x,>=,0,),{,x,=,x,+,1,},<EOF>", 133))

    def test_case134(self):
        self.assertTrue(TestLexer.test("123_456_789 0_00 987_654_321", "123_456_789,0_00,987_654_321,<EOF>", 134))

    def test_case135(self):
        self.assertTrue(TestLexer.test("var str = \"Escape Sequences: \\t \\n \\r \\\" \\\' \\\\\"", "var,str,=,\"Escape Sequences: \\t \\n \\r \\\" \\\' \\\\\",<EOF>", 135))

    def test_case136(self):
        self.assertTrue(TestLexer.test("return 1e-10", "return,1e-10,<EOF>", 136))

    def test_case137(self):
        self.assertTrue(TestLexer.test("if (a != b) then a else b", "if,(,a,!=,b,),then,a,else,b,<EOF>", 137))

    def test_case138(self):
        self.assertTrue(TestLexer.test("for i in range(5): print(i)", "for,i,in,range,(,5,),:,print,(,i,),<EOF>", 138))

    def test_case139(self):
        self.assertTrue(TestLexer.test("var x = 10.5 - 2.5", "var,x,=,10.5,-,2.5,<EOF>", 139))

    def test_case140(self):
        self.assertTrue(TestLexer.test("func divide(a, b) { return a / b }", "func,divide,(,a,,,b,),{,return,a,/,b,},<EOF>", 140))

    def test_case141(self):
        self.assertTrue(TestLexer.test("while (x != 0) { x = x - 1 }", "while,(,x,!=,0,),{,x,=,x,-,1,},<EOF>", 141))

    def test_case142(self):
        self.assertTrue(TestLexer.test("123_456_789.0 0.00 987_654_321.123", "123_456_789.0,0.00,987_654_321.123,<EOF>", 142))

    def test_case143(self):
        self.assertTrue(TestLexer.test("var str = \"Hello,\\nWorld!\"", "var,str,=,\"Hello,\\nWorld!\",<EOF>", 143))

    def test_case144(self):
        self.assertTrue(TestLexer.test("return true or false and true", "return,true,or,false,and,true,<EOF>", 144))

    def test_case145(self):
        self.assertTrue(TestLexer.test("if (a < b) then a else b", "if,(,a,<,b,),then,a,else,b,<EOF>", 145))

    def test_case146(self):
        self.assertTrue(TestLexer.test("for i in range(1, 10): print(i)", "for,i,in,range,(,1,,,10,),:,print,(,i,),<EOF>", 146))

    def test_case147(self):
        self.assertTrue(TestLexer.test("var x = (5 + 3) * 2", "var,x,=,(,5,+,3,),*,2,<EOF>", 147))

    def test_case148(self):
        self.assertTrue(TestLexer.test("func power(a, b) { return a ** b }", "func,power,(,a,,,b,),{,return,a,**,b,},<EOF>", 148))

    def test_case149(self):
        self.assertTrue(TestLexer.test("while (x <= 0) { x = x + 1 }", "while,(,x,<=,0,),{,x,=,x,+,1,},<EOF>", 149))

    def test_case150(self):
        self.assertTrue(TestLexer.test("\" string with a space at head\"", " string with a space at head,<EOF>", 150))

    def test_case151(self):
        self.assertTrue(TestLexer.test("\"cam say : if I ?\"\"", "cam say : if I ?,Unclosed String: ", 151))

    def test_case152(self):
        self.assertTrue(TestLexer.test("\"he asked me : '\"Where is the book ?!?!'\" \"", "he asked me : '\"Where is the book ?!?!'\" ,<EOF>", 152))

    def test_case153(self):
        self.assertTrue(TestLexer.test("\"string with escpape char : \\b \\f \\r \\n \\t \\\\ \\'\"", "string with escpape char : \\b \\f \\r \\n \\t \\\\ \\',<EOF>", 153))

    def test_case154(self):
        self.assertTrue(TestLexer.test("\"some more escpape char: \\b \\f \\r \\n \\t \\\\ \\'\"", "some more escpape char: \\b \\f \\r \\n \\t \\\\ \\',<EOF>", 154))

    def test_case155(self):
        self.assertTrue(TestLexer.test("\"\\n \\' newline infront\"", "\\n \\' newline infront,<EOF>", 155))

    def test_case156(self):
        self.assertTrue(TestLexer.test("\"'\" some thing here\\n \\n \\t'\" some thing here\"", "'\" some thing here\\n \\n \\t'\" some thing here,<EOF>", 156))

    def test_case157(self):
        self.assertTrue(TestLexer.test("\"1st string\" \"2nd string \\t \\n\" \"3rd string \\t\\n\\b \"", "1st string,2nd string \\t \\n,3rd string \\t\\n\\b ,<EOF>", 157))

    def test_case158(self):
        self.assertTrue(TestLexer.test("\"....???!!!!!+-/*&^%$#@\" ", "....???!!!!!+-/*&^%$#@,<EOF>", 158))

    def test_case159(self):
        self.assertTrue(TestLexer.test("\"cau ca co con cho can cacao \"", "cau ca co con cho can cacao ,<EOF>", 159))

    def test_case160(self):
        self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 160))

    def test_case161(self):
        self.assertTrue(TestLexer.test("\"\\n \\t", "Unclosed String: \\n \\t", 161))

    def test_case162(self):
        self.assertTrue(TestLexer.test("\"This '\" string '\" is \"  \"unclosed","This '\" string '\" is ,Unclosed String: unclosed", 162))

    def test_case163(self):
        self.assertTrue(TestLexer.test("\" not close '\" '\" \\b\\b\\b\\b", "Unclosed String:  not close '\" '\" \\b\\b\\b\\b", 163))

    def test_case164(self):
        self.assertTrue(TestLexer.test("func divide(a, b) { return a / b }", "func,divide,(,a,,,b,),{,return,a,/,b,},<EOF>", 164))

    def test_case165(self):
        self.assertTrue(TestLexer.test("while (x != 0) { x = x - 1 }", "while,(,x,!=,0,),{,x,=,x,-,1,},<EOF>", 165))

    def test_case166(self):
        self.assertTrue(TestLexer.test("123_456_789.0 0.00 987_654_321.123", "123_456_789.0,0.00,987_654_321.123,<EOF>", 166))

    def test_case167(self):
        self.assertTrue(TestLexer.test("var str = \"Hello,\\nWorld!\"", "var,str,=,\"Hello,\\nWorld!\",<EOF>", 167))

    def test_case168(self):
        self.assertTrue(TestLexer.test("return true or false and true", "return,true,or,false,and,true,<EOF>", 168))

    def test_case169(self):
        self.assertTrue(TestLexer.test("if (a < b) then a else b", "if,(,a,<,b,),then,a,else,b,<EOF>", 169))

    def test_case170(self):
        self.assertTrue(TestLexer.test("for i in range(1, 10): print(i)", "for,i,in,range,(,1,,,10,),:,print,(,i,),<EOF>", 170))

    def test_case171(self):
        self.assertTrue(TestLexer.test("var x = (5 + 3) * 2", "var,x,=,(,5,+,3,),*,2,<EOF>", 171))

    def test_case172(self):
        self.assertTrue(TestLexer.test("func power(a, b) { return a ** b }", "func,power,(,a,,,b,),{,return,a,**,b,},<EOF>", 172))

    def test_case173(self):
        self.assertTrue(TestLexer.test("while (x <= 0) { x = x + 1 }", "while,(,x,<=,0,),{,x,=,x,+,1,},<EOF>", 173))

    def test_case174(self):
        self.assertTrue(TestLexer.test("123.456 0.0 9876.54321", "123.456,0.0,9876.54321,<EOF>", 174))

    def test_case175(self):
        self.assertTrue(TestLexer.test("var str = \"Hello,\\tWorld!\"", "var,str,=,\"Hello,\\tWorld!\",<EOF>", 175))

    def test_case176(self):
        self.assertTrue(TestLexer.test("return false or not true", "return,false,or,not,true,<EOF>", 176))

    def test_case177(self):
        self.assertTrue(TestLexer.test("if (a >= b) then a else b", "if,(,a,>=,b,),then,a,else,b,<EOF>", 177))

    def test_case178(self):
        self.assertTrue(TestLexer.test("for i in range(1, 10, 2): print(i)", "for,i,in,range,(,1,,,10,,,2,),:,print,(,i,),<EOF>", 178))

    def test_case179(self):
        self.assertTrue(TestLexer.test("var x = 5 + (3 * 2)", "var,x,=,5,+,(,3,*,2,),<EOF>", 179))

    def test_case180(self):
        self.assertTrue(TestLexer.test("func subtract(a, b) { return a - b }", "func,subtract,(,a,,,b,),{,return,a,-,b,},<EOF>", 180))

    def test_case181(self):
        self.assertTrue(TestLexer.test("while (x == 0) { x = x - 1 }", "while,(,x,==,0,),{,x,=,x,-,1,},<EOF>", 181))

    def test_case182(self):
        self.assertTrue(TestLexer.test("123_456_789 0_00 987_654_321", "123_456_789,0_00,987_654_321,<EOF>", 182))

    def test_case183(self):
        self.assertTrue(TestLexer.test("var str = \"Escape Sequences: \\t \\n \\r \\\" \\\' \\\\\"", "var,str,=,\"Escape Sequences: \\t \\n \\r \\\" \\\' \\\\\",<EOF>", 183))

    def test_case184(self):
        self.assertTrue(TestLexer.test("return 1e-10", "return,1e-10,<EOF>", 184))

    def test_case185(self):
        self.assertTrue(TestLexer.test("if (a != b) then a else b", "if,(,a,!=,b,),then,a,else,b,<EOF>", 185))

    def test_case186(self):
        self.assertTrue(TestLexer.test("for i in range(5): print(i)", "for,i,in,range,(,5,),:,print,(,i,),<EOF>", 186))

    def test_case187(self):
        self.assertTrue(TestLexer.test("var x = 10.5 - 2.5", "var,x,=,10.5,-,2.5,<EOF>", 187))

    def test_case188(self):
        self.assertTrue(TestLexer.test("func divide(a, b) { return a / b }", "func,divide,(,a,,,b,),{,return,a,/,b,},<EOF>", 188))

    def test_case189(self):
        self.assertTrue(TestLexer.test("while (x != 0) { x = x - 1 }", "while,(,x,!=,0,),{,x,=,x,-,1,},<EOF>", 189))

    def test_case190(self):
        self.assertTrue(TestLexer.test("123_456_789.0 0.00 987_654_321.123", "123_456_789.0,0.00,987_654_321.123,<EOF>", 190))

    def test_case191(self):
        self.assertTrue(TestLexer.test("var str = \"Hello,\\nWorld!\"", "var,str,=,\"Hello,\\nWorld!\",<EOF>", 191))

    def test_case192(self):
        self.assertTrue(TestLexer.test("return true or false and true", "return,true,or,false,and,true,<EOF>", 192))

    def test_case193(self):
        self.assertTrue(TestLexer.test("if (a < b) then a else b", "if,(,a,<,b,),then,a,else,b,<EOF>", 193))

    def test_case194(self):
        self.assertTrue(TestLexer.test("for i in range(1, 10): print(i)", "for,i,in,range,(,1,,,10,),:,print,(,i,),<EOF>", 194))

    def test_case195(self):
        self.assertTrue(TestLexer.test("var x = (5 + 3) * 2", "var,x,=,(,5,+,3,),*,2,<EOF>", 195))

    def test_case196(self):
        self.assertTrue(TestLexer.test("func power(a, b) { return a ** b }", "func,power,(,a,,,b,),{,return,a,*,*,b,},<EOF>", 196))

    def test_case197(self):
        self.assertTrue(TestLexer.test("while (x <= 0) { x = x + 1 }", "while,(,x,<=,0,),{,x,=,x,+,1,},<EOF>", 197))

    def test_case198(self):
        self.assertTrue(TestLexer.test("var str = \"Hello,\\tWorld!\"", "var,str,=,\"Hello,\\tWorld!\",<EOF>", 198))

    def test_case199(self):
        self.assertTrue(TestLexer.test("var str = \"Hello,\\tWorld!\"", "var,str,=,\"Hello,\\tWorld!\",<EOF>", 199))

