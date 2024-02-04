import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program0(self):
        """Simple program """
        input = """func foo(number a[5], string b)
        begin
                        var i <- 0
                        for i until i >= 5 by 1
                        begin
                            a[i] <- i * i + 5
                        end
                        return -1
                        end
                        """
        expect = "Error on line 10 col 24: <EOF>"
        self.assertTrue(TestParser.test(input,expect,200))
        
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() begin
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """func areDivisors(number y, number num2)
return ((y % num2 = 0) or (num2 % y = 0))
func main() begin
var y <- readNumber()
var num2 <- readNumber()
if (areDivisors(y, num2)) writeString("Yes")
else writeString("No")
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """func isPrime(number y)
func main() begin
number y <- readNumber()
if (isPrime(y)) writeString("Yes")
else writeString("No")
end
func isPrime(number y)
begin
if (y <= 1) return false
var i <- 2
for i until i > y / 2 by 1
begin
if (y % i = 0) return false
end
return true
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_simple_program_5(self):
        """Simple program """
        input = """func foo(number a[5], string b)
        begin
                        var i <- 0
                        for i until i >= 5 by 1
                        begin
                            a[i] <- i * i + 5
                        end
                        return -1
                        end
                        func main()
                        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """func main()
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test0(self):
        input = """func of(number x)
        func main() return x
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test1(self):
        input = """  func Program(string a)
        func main() begin
        a <- "string"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    
    def test2(self):
        input = """  func Program()
        func main()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test3(self):
        input = """ func main() begin
            number num1 <- 0
            bool b <- true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test4(self):
        input = """func main() begin
            number num1 <- 0
            string b <- "string"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    
    def test5(self):
        input = """func main() begin
            number num1 <- 0.1e12
            string b <- "string"
            bool bi <- true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    
    def test6(self):
        input = """ func main () return bool true <- True;
        """
        expect = "Error on line 1 col 21: bool"
        self.assertTrue(TestParser.test(input,expect,213))
    
    def test7(self):
        input = """ func Rectangle(number x)
                    func Program (string y)
                    """
        expect = "Error on line 3 col 20: <EOF>"
        self.assertTrue(TestParser.test(input,expect,214))
    
    def test8(self):
        input = """ func Rectangle(number x)
                    func Program (string y)
                    func main()
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    
    def test9(self):
        input = """ func Rectangle(number x)
                    func Program (string y)
                    func main()
                    func Square(number z)
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    
    def test10(self):
        input = """ func Rectangle()
                        func main()
                    func Program()
                        func doSomeThing(number a)
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    
    def test11(self):
        input = """ func Rectangle()
        return true
                    func main() begin
                    return false
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test12(self):
        input = """ func Rectangle(number i)
                    begin
                        number i <- i*3
                        return i
                    end
                    func main() begin
                        add(i)
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test13(self):
        input = """ func Rectangle()
                    begin
                        return simpleExpresion()
                    end
                    func main() begin
                        number r <- Rectangle()
                        return complexExpression(r)
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test14(self):
        input = """ func Rectangle()
                    begin
                        string a[1] <- ["a"]
                        return a[1]
                    end
                    func main() begin
                        string temp <- Rectangle() 
                        return complexExpression(temp)
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    
    def test15(self):
        input = """ func main() return true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    
    def test16(self):
        input = """ func main() return 2+4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    
    def test17(self):
        input = """ func main() begin
        var i <- 10
        for i until i >= 5 by 1
            i <- i+1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test18(self): 
        input = """func isprime(number a, number b) {}"""
        expect = "Error on line 1 col 33: {"
        self.assertTrue(TestParser.test(input,expect,225))
    
    def test19(self):  
        input = """ func main() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    
    def test20(self):
        input = """ func Rectangle()
        begin
                        number a <- 0.1 
                        number b <- 5 * 3 + 12 - 19 + 4
                        getArea(a,b)
                        inPrime(a,b)
        end
        func main()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test21(self): 
        input = """func main() begin
        if (a == 0) return 1
        else
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    
    def test22(self): 
        input = """ func A()
                    begin
                            set(number a, number b) 
                            afoo()
                    end
                    func main()
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229)) 
    
    
    
    def test23(self):  # ??? Return New X().Y()
        input = """ func main()
                    func Rec ()
                    func getArea()
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test24(self): 
        input = """ func main()
        begin
                    number a[-1] <- [1]
                    return a[1]
        end
                """
        expect = "Error on line 3 col 29: -"
        self.assertTrue(TestParser.test(input,expect,231)) 
    
    def test25(self): 
        input = """func main()
        begin
                    number a[0] <- [1]
                    return a[1]
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232)) 
    
    def test26(self): 
        input = """ func main()
        begin
                    number a[2] <- [1]
                    return a[1]
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233)) 

    def test27(self):
        input = """func main()
        begin
                    a <- 2
                    b <- 2
                    getArea(a,b)
        end
        func getArea(number a, number b)
        begin
            return a*b
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    
    def test28(self):
        input = """ func main()
        begin
                    number a1[5] <- [1,2,3,4,5]
                    number b1[5] <- [6,7,8,9,10]
                    a <- a1[0]
                    b <- b1[1]
                    getArea(a,b)
        end
        func getArea(number a, number b)
        begin
            return a*b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    
    def test29(self):
        input = """ func main()
        begin
                    number a1[5] <- [1,2,3,4,5]
                    a <- a1[0]
                    b <- 10
                    getArea(a,b)
        end
        func getArea(number a, number b)
        begin
            return a*b
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    
    def test30(self):
        input = """ func main()
        begin
                    number a1[2,2] <- [[1,1],[2,2]]
                    number b1[5] <- [6,7,8,9,10]
                    a <- a1[0,0]
                    b <- b1[1]
                    getArea(a,b)
        end
        func getArea(number a, number b)
        begin
            return a*b
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    
    def test31(self):
        input = """ func main()
        begin
        number a <- 100 + 100
        number b <- 54 + 55 
        if (2 > a and (b <= 1))
                   a <- 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    
    def test32(self):
        input = """ func main()
        begin
        number a <- 531.1
        number b <- 24.1 
        if (2 > a and (b <= 1))
                   a <- 1.01
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test33(self):
        input = """ func main()
        begin
        number a <- 531.2e5
        number b <- 24.1 
        if (2 > a and (b <= 1))
                   a <- 1.01
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test34(self):
        input = """func main()
        begin
        number a <- 531.2e5
        number b <- 24.1e5 
        if (2 > a and (b <= 1))
                   a <- 1.01
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    
    def test35(self):
        input = """ func main()
        begin
        bool a <- true
        number b <- 24 
        if ((b > 15) == a)
                   a <- 1.01
        end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    
    def test36(self):
        input = """  func main()
        begin
        string a <- "b"
        string b <- "a" 
        if (b != a)
            return a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    
    def test37(self):
        input = """  func Arr(number &a)
            func main ()
            begin
             number a[5] <- [1,5,9,4,3]
             Arr(a)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    
    def test38(self):
        input = """   func Arr(bool &a)
            func main ()
            begin
             bool a[5] <- [true,false,true,true,false]
             Arr(a)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    
    def test39(self):
        input = """  func Arr(string &a)
            func main ()
            begin
             string a[5] <- ["a","b","c","d","e"]
             Arr(a)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    
    def test40(self):
        input = """func Arr(string &a, string &b)
            func main ()
            begin
                string a[5] <- ["a","b","c","d","e"]
                string b[5] <- ["a","b","c","d","f"]
            Arr(a,b)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test41(self):
        input = """  func Arr(bool &a, bool &b)
            func main ()
            begin
             bool a[5] <- [true,false,true,true,false]
             bool b[5] <- [true,false,false,true,false]
             Arr(a,b)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    
    def test42(self):
        input = """ func Arr(number &a, number &b)
            func main ()
            begin
             number a[5] <- [1,5,9,4,3]
             number b[5] <- [9,7,6,3,8]
             Arr(a,b)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    
    def test43(self):
        input = """ func Arr(number &a, bool &b)
            func main ()
            begin
             number a[5] <- [1,5,9,4,3]
             bool b[5] <- [true,false,false,true,false]
             Arr(a,b)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    
    def test44(self):
        input = """func Arr(number &a, string &b)
            func main ()
            begin
             number a[5] <- [1,5,9,4,3]
             string b[5] <- ["a","b","c","d","f"]
             Arr(a,b)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    
    def test45(self):
        input = """func Arr(bool &a, string &b)
            func main ()
            begin
             bool a[5] <- [true,false,true,true,false]
             string b[5] <- ["a","b","c","d","f"]
             Arr(a,b)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    
    def test46(self):
        input = """ func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y)
                    break
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    
    def test47(self):
        input = """ func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y) return true
                elif (x == y) return true
                else return false
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    
    def test48(self):
        input = """  func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y and (x+y <= 2)) return true
                elif (x == y) return true
                else return false
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    
    def test49(self):
        input = """ func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y and (x+y >= 1)) return true
                elif (x+y > 2) return false
                else return false
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    
    def test50(self):
        input = """ func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y and (x+y == 1)) return true
                elif (x+y != 2) return true
                else return false
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    
    def test51(self):
        input = """  func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < (-y)) return true
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    
    def test52(self):
        input = """ func main ()
            begin
                bool x <- true
                bool y <- false
                if ((not x) == y) return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def test53(self):
        input = """
        func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y or (x+y <= 2)) return true
                elif (x == y) return true
                else return false
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    
    def test54(self):
        input = """
        func main ()
            begin
                number x <- 0
                number y <- 1
                if (x < y or (x*y <= 2)) return true
                elif (x == y) return true
                else return false
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    
    def test55(self):
        input = """
        func main ()
            begin
                number x <- 3
                number y <- 2
                if (x < y or (x/y <= 2)) return true
                elif (x == y) return true
                else return false
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    
    def test56(self):
        input = """func main ()
            begin
                number x <- 3
                number y <- 2
                if (x < y or (x%y <= 2)) return true
                elif (x == y) return true
                else return false
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    
    def test57(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i <= 8 by 1
                    if (i == 4) continue
                return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    
    def test58(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i = 8 by 1
                    if (i == 4) continue
                return i
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    
    def test59(self):
        input = """func main ()
            begin
                var i <- 0
                var x <- 2
                for i until i/x <= 3 by 1
                    if (i == 4) continue
                return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    
    def test60(self):
        input = """func main ()
            begin
                var i <- 0
                var x <- 2
                for i until i*x <= 3 by 1
                    if (i == 4) continue
                return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    
    def test61(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i < 8 by 1
                    if (i == 4) continue
                return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    
    def test62(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i > 8 by 1
                    if (i == 4) continue
                return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    
    def test63(self):
        input = """
        func main ()
            begin
                var i <- 0
                for i until i >= 8 by 1
                    if (i == 4) continue
                return i
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    
    def test64(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i >= 8 by 1
                    if (i == 4) continue
                else return i
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def test65(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i > 8 by 1
                    if (i == 4) continue
                else return i
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test66(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i < 8 by 1
                    if (i == 4) continue
                else return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test67(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i <= 8 by 1
                    if (i == 4) continue
                else return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    
    def test68(self):
        input = """func main ()
            begin
                var i <- 0
                for i until i = 8 by 1
                    if (i == 4) continue
                else return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test69(self):
        input = """func main ()
            begin
                var i <- 0
                var x <- 2
                for i until i*x <= 3 by 1
                    if (i == 4) continue
                else return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    def test70(self):
        input = """func main ()
            begin
                var i <- 0
                var x <- 2
                for i until i/x <= 3 by 1
                    if (i == 4) continue
                else return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test71(self):
        input = """func main ()
            begin
                var i <- 0
                var x <- 2
                for i until i%x <= 3 by 1
                    if (i == 4) continue
                else return i
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test72(self):
        input = """func main ()
            begin
                var i <- readNumber()
                var x <- readNumber()
                for i until i%x <= 3 by 1
                    if (i == 4) writeString("a")
                else writeString("b")
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test73(self):
        input = """func main ()
            begin
                var i <- readNumber()
                var x <- readNumber()
                for i until i%x <= 3 by 1
                    if (i == 4) writeNumber(0)
                else writeNumber(1)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    
    def test74(self):
        input = """func main ()
            begin
                var i <- readNumber()
                var x <- readNumber()
                for i until i%x <= 3 by 1
                    if (i == 4) writeBool(false)
                else writeBool(true)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    
    def test75(self):
        input = """func main ()
            begin
                var i <- readString()
                var x <- readString()
                if (i == x) writeBool(false)
                else writeBool(true)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    
    def test76(self):
        input = """func main ()
            begin
                var i <- readBool()
                var x <- readString()
                if ((x == "a") == i) writeBool(false)
                else writeBool(true)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test77(self):
        input = """func main ()
            begin
                var i <- readBool()
                var x <- readBool()
                if ((x != i)) writeBool(false)
                else writeBool(true)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test78(self):
        input = """func main ()
            begin
                var i <- readNumber()
                var x <- readNumber()
                if ((x != i)) writeNumber(3)
                else writeBool(true)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    
    def test79(self):
        input = """func S() {
                    a <- foo(1*2,"b"+."c","a"==."b")
                }
        """
        expect = "Error on line 1 col 9: {"
        self.assertTrue(TestParser.test(input, expect, 286))
    
    def test80(self): 
        input = """func S():
                    var s <- "No multiple inheritance";
                    Return False;
                } 
            }
        """
        expect = "Error on line 1 col 8: :"
        self.assertTrue(TestParser.test(input, expect, 287))
    
    def test81(self): 
        input = """func main()
        begin
                    if (0==0 and (0!=1) or (1 < (2*(3+4))) or (not 4)) a <- (5+ (4*8) + 10)
                    elif (b == true) b <- false
                    else b <- false
                        return true
                    return false
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    
    def test82(self):
        input = """func main()
        begin
                    if (0==0 and (0!=1) or (1 < (2*(3+4))) or (not 4)) a <- (5+ (4*8) + 10)
                    elif (b == true) b <- 0.9
                    else b <- 0.5
                        return b
                    return a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    
    def test83(self):
        input = """func main()
        begin
                    if (0==0 and (0!=1) or (1 >= (2*(3+4))) or (not 4)) a <- (5+ (4*8) + 10)
                    elif (b == true) b <- false
                    else b <- false
                        return true
                    return false
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))     
    
    def test84(self):
        input = """func main()
        begin
                    if (0==0 and (0!=1) or (1 < (2*(3+4))) and (not 4)) a <- (5+ (4*8) + 10)
                    elif (b == true) b <- 0.9
                    else b <- 0.5
                        return b
                    return a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))  
    
    def test85(self):
        input = """func main()
        begin
                number a[1] <- [1]
                if (a[1] < 3) writeNumber(3)
                else a[1] <- readNumber()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))  
       
    def test86(self):
        input = """func main()
        begin
                number a[1] <- [1]
                if (a[1] < 3) writeNumber(true)
                else a[1] <- readNumber()
        end
        """
        expect = "Error on line 4 col 42: true"
        self.assertTrue(TestParser.test(input, expect, 293)) 
    
    def test87(self):
        input = """2 + 1 + a.fox()"""
        expect = "Error on line 1 col 0: 2"
        self.assertTrue(TestParser.test(input,expect,294))
    
    def test88(self):
        input = """func main()
        begin
                number a[1] <- [1]
                if (a[1] < 3) writeNumber("true")
                else a[1] <- readNumber()
        end
        """
        expect = "Error on line 4 col 42: true"
        self.assertTrue(TestParser.test(input,expect,295))
    
    def test89(self):
        input = """func main()
        begin
                number a[1] <- [1]
                if (a[1] < 3) writeBool("true")
                else a[1] <- readNumber()
        end
        """
        expect = "Error on line 4 col 40: true"
        self.assertTrue(TestParser.test(input,expect,296))
    
    def test90(self):
        input = """func main()
        begin
                number a[1] <- [1]
                if (a[1] < 3) writeBool(1)
                else a[1] <- readNumber()
        end
        """
        expect = "Error on line 4 col 40: 1"
        self.assertTrue(TestParser.test(input,expect,297))
    
    def test91(self):
        input = """func main()
            begin
                a[1] <- [[1]]
            end
        """
        expect = "Error on line 3 col 25: ["
        self.assertTrue(TestParser.test(input,expect,298))
    
    def test92(self):
        input = """func main()
            begin
                a[1] <- [1]]
            end
        """
        expect = "Error on line 3 col 27: ]"
        self.assertTrue(TestParser.test(input,expect,299))
    