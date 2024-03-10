from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


#MODIFY THIS FILE TO GENERATE PARSE TREE

class ASTGeneration(ZCodeVisitor):

    #program: newline_list decllist EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    #decllist:  decl decllist | decl ;   
    def visitDecllist(self,ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())

    #decl: vardecl | funcdecl ;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        else:
            return self.visit(ctx.vardecl())

    # vardecl: 
    # 	vardecl_only
    # 	|
    # 	vardecl_init
    # ;
    def visitVardecl(self,ctx:ZCodeParser.VardeclContext):
        if ctx.vardecl_only():
            return self.visit(ctx.vardecl_only())
        else:
            return self.visit(ctx.vardecl_init())

    # vardecl_only:	
    # 	typ IDENTIFIER NEWLINE newline_list
    # 	|
    # 	DYNAMIC_TYPE IDENTIFIER NEWLINE newline_list
    # 	|
    # 	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET NEWLINE newline_list
    # ;
    def visitVardecl_only(self,ctx:ZCodeParser.Vardecl_onlyContext):
        if ctx.OPEN_BRACKET():
            name = Id(ctx.IDENTIFIER().getText())
            size = self.visit(ctx.arrlist())
            eleType = self.visit(ctx.typ())
            varType = ArrayType(size,eleType)
            return VarDecl(name,varType,None,None)
        elif ctx.DYNAMIC_TYPE():
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.DYNAMIC_TYPE().getText()
            return VarDecl(name,None,modifier,None)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            varType = self.visit(ctx.typ())
            return VarDecl(name,varType,None,None)

    # vardecl_init:
    # 	//Declaration with initialization value
    # 	VAR_TYPE IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
    # 	|
    # 	typ IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
    # 	|
    # 	DYNAMIC_TYPE IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
    # 	|
    # 	//Array declaration with initialization values
    # 	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET ASSIGN_OPERATOR expression NEWLINE newline_list
    # ;
    def visitVardecl_init(self,ctx:ZCodeParser.Vardecl_initContext):
        if ctx.arrlist():
            name = Id(ctx.IDENTIFIER().getText())
            size = self.visit(ctx.arrlist())
            eleType = self.visit(ctx.typ())
            varType = ArrayType(size,eleType)
            varInit = self.visit(ctx.expression())
            return VarDecl(name,varType,None,varInit)
        elif ctx.DYNAMIC_TYPE():
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.DYNAMIC_TYPE().getText()
            varInit = self.visit(ctx.expression())
            return VarDecl(name,None,modifier,varInit)
        elif ctx.VAR_TYPE():
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.VAR_TYPE().getText()
            varInit = self.visit(ctx.expression())
            return VarDecl(name,None,modifier,varInit)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            varType = self.visit(ctx.typ())
            varInit = self.visit(ctx.expression())
            return VarDecl(name,varType,None,varInit)

    #arrlist: NUMBER COMMA arrlist | NUMBER;
    def visitArrlist(self, ctx:ZCodeParser.ArrlistContext):
        if ctx.getChildCount() == 1:
            value = float(ctx.NUMBER().getText())
            return [value]
        else:
            value = float(ctx.NUMBER().getText())
            return [value] + self.visit(ctx.arrlist())

    #OBSOLETE
    #array_expression: OPEN_BRACKET arrlist CLOSE_BRACKET | arrlist;
    def visitArray_expression(self,ctx:ZCodeParser.Array_expressionContext):
        pass

    #OBSOLETE
    #arrlist_expression: OPEN_BRACKET array_expression COMMA arrlist_expression CLOSE_BRACKET | array_expression;
    def visitArrlist_expression(self,ctx:ZCodeParser.Arrlist_expressionContext):
        pass

    #array_literal: OPEN_BRACKET array_literal_prime CLOSE_BRACKET | OPEN_BRACKET CLOSE_BRACKET;
    def visitArray_literal(self,ctx:ZCodeParser.Array_literalContext):
        if ctx.array_literal_prime():
            value = self.visit(ctx.array_literal_prime())
            return ArrayLiteral(value)
        else:
            return ArrayLiteral([])

    #array_literal_prime: expression COMMA array_literal_prime | expression;
    def visitArray_literal_prime(self,ctx:ZCodeParser.Array_literal_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.array_literal_prime())

    # expression: 
    # 	expression OPEN_BRACKET index_operators CLOSE_BRACKET	
    #   |
    #   //DENTIFIER OPEN_BRACKET index_operators CLOSE_BRACKET
    #   |
    #   //func_call OPEN_BRACKET index_operators CLOSE_BRACKET    
    #   |
	#   OPEN_PARENTHESIS expression CLOSE_PARENTHESIS
    #   |
    # 	<assoc=right>SUB_OPERATOR expression
    # 	|
    # 	<assoc=right>NOT_OPERATOR expression
    # 	|
    # 	expression mul_operators expression
    # 	|
    # 	expression add_operators expression
    # 	|
    # 	expression logic_operators expression
    # 	|
    # 	expression rel_operators expression
    # 	|
    # 	expression str_operators expression
    # 	|
    # 	IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS
    # 	|
    # 	literal
    # 	|
    # 	array_literal
    # ;
    def visitExpression(self,ctx:ZCodeParser.ExpressionContext):
        if ctx.index_operators():
            arr = self.visit(ctx.expression(0))
            idx = self.visit(ctx.index_operators())
            # print("expression with index operators is called")
            return ArrayCell(arr,idx)
        
        elif ctx.OPEN_PARENTHESIS() and ctx.expression():
            return self.visit(ctx.expression(0))

        elif ctx.SUB_OPERATOR():
            op = ctx.SUB_OPERATOR().getText()
            # print("unary op is called" + op)
            return UnaryOp(op,self.visit(ctx.expression(0)))
        
        elif ctx.NOT_OPERATOR():
            op = ctx.NOT_OPERATOR().getText()
            return UnaryOp(op,self.visit(ctx.expression(0)))
        
        elif ctx.mul_operators():
            op = self.visit(ctx.mul_operators())
            return BinaryOp(op,self.visit(ctx.expression(0)),self.visit(ctx.expression(1)))
        
        elif ctx.add_operators():
            op = self.visit(ctx.add_operators())
            return BinaryOp(op,self.visit(ctx.expression(0)),self.visit(ctx.expression(1)))
        
        elif ctx.logic_operators():
            op = self.visit(ctx.logic_operators())
            return BinaryOp(op,self.visit(ctx.expression(0)),self.visit(ctx.expression(1)))
        
        elif ctx.rel_operators():
            op = self.visit(ctx.rel_operators())
            return BinaryOp(op,self.visit(ctx.expression(0)),self.visit(ctx.expression(1)))

        elif ctx.str_operators():
            op = self.visit(ctx.str_operators())
            return BinaryOp(op,self.visit(ctx.expression(0)),self.visit(ctx.expression(1)))
        
        elif ctx.param_list():
            name = Id(ctx.IDENTIFIER().getText())
            args = self.visit(ctx.param_list())
            return CallExpr(name,args)
        
        elif ctx.literal():
            return self.visit(ctx.literal())
        
        # elif ctx.array_literal():
        #     # print("array literal is called")
        #     return self.visit(ctx.array_literal())

        else:        
            return self.visit(ctx.array_literal())


    #sign_operands: literal | SUB_OPERATOR ;
    def visitSign_operands(self,ctx:ZCodeParser.Sign_operandsContext):
        if ctx.SUB_OPERATOR():
            return ctx.SUB_OPERATOR().getText()
        else: return self.visit(ctx.literal())

    #not_operands: literal | NOT_OPERATOR;
    def visitNot_operands(self, ctx:ZCodeParser.Not_operandsContext):
        if ctx.NOT_OPERATOR():
            return ctx.NOT_OPERATOR().getText()
        else: return self.visit(ctx.literal())

    #index_operators: expression | expression COMMA index_operators;
    def visitIndex_operators(self,ctx:ZCodeParser.Index_operatorsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.index_operators())

    #func_call: IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS;
    def visitFunc_call(self,ctx: ZCodeParser.Func_callContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.param_list())
        return CallStmt(name,args)

    #param_list: param_prime | ;
    def visitParam_list(self,ctx: ZCodeParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param_prime())

    #param_prime: param COMMA param_prime | param;
    def visitParam_prime(self,ctx: ZCodeParser.Param_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.param_prime())

    #param: expression;
    def visitParam(self,ctx: ZCodeParser.ParamContext):
        return self.visit(ctx.expression())

    #THIS IS OBSOLETE
    def visitNon_rel_operators(self,ctx:ZCodeParser.Non_rel_operatorsContext):
        pass

    #THIS IS OBSOLETE
    def visitNon_str_operators(self,ctx: ZCodeParser.Non_str_operatorsContext):
        pass

    #THIS IS OBSOLETE
    def visitNon_associative_operands(self,ctx: ZCodeParser.Non_associative_operandsContext):
        pass

    #typ: BOOL_TYPE | NUMBER_TYPE | STRING_TYPE;
    def visitTyp(self,ctx:ZCodeParser.TypContext):
        if ctx.BOOL_TYPE():
            return BoolType()
        elif ctx.NUMBER_TYPE():
            return NumberType()
        else:
            return StringType()

    #literal: STRING | NUMBER | BOOLEAN | IDENTIFIER;
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
            return NumberLiteral(value)
        elif ctx.BOOLEAN():
            value = ctx.BOOLEAN().getText() == 'true'
            return BooleanLiteral(value)
        else:
            return Id(ctx.IDENTIFIER().getText())

    #mul_operators: MUL_OPERATOR | DIV_OPERATOR | MOD_OPERATOR;
    def visitMul_operators(self,ctx: ZCodeParser.Mul_operatorsContext):
        if ctx.MUL_OPERATOR():
            return ctx.MUL_OPERATOR().getText()
        elif ctx.DIV_OPERATOR():
            return ctx.DIV_OPERATOR().getText()
        else:
            return ctx.MOD_OPERATOR().getText()

    #add_operators: ADD_OPERATOR | SUB_OPERATOR;
    def visitAdd_operators(self,ctx: ZCodeParser.Add_operatorsContext):
        if ctx.ADD_OPERATOR():
            return ctx.ADD_OPERATOR().getText()
        else:
            return ctx.SUB_OPERATOR().getText()

    #logic_operators: AND_OPERATOR | OR_OPERATOR;   
    def visitLogic_operators(self, ctx: ZCodeParser.Logic_operatorsContext):
        if ctx.OR_OPERATOR():
            return ctx.OR_OPERATOR().getText()
        else: 
            return ctx.AND_OPERATOR().getText()

    # rel_operators: 
    # 	EQ_OPERATOR 
    # 	| 
    # 	SEQ_OPERATOR 
    # 	| 
    # 	NEQ_OPERATOR 
    # 	| 
    # 	LT_OPERATOR
    # 	|
    # 	GT_OPERATOR
    # 	|
    # 	LEQ_OPERATOR
    # 	|
    # 	GEQ_OPERATOR
    # ;
    def visitRel_operators(self, ctx: ZCodeParser.Rel_operatorsContext):
        if ctx.EQ_OPERATOR():
            return ctx.EQ_OPERATOR().getText()
        elif ctx.SEQ_OPERATOR():
            return ctx.SEQ_OPERATOR().getText()
        elif ctx.NEQ_OPERATOR():
            return ctx.NEQ_OPERATOR().getText()
        elif ctx.LT_OPERATOR():
            return ctx.LT_OPERATOR().getText()
        elif ctx.GT_OPERATOR():
            return ctx.GT_OPERATOR().getText()
        elif ctx.LEQ_OPERATOR():
            return ctx.LEQ_OPERATOR().getText()
        else:
            return ctx.GEQ_OPERATOR().getText()

    #str_operators: STRING_OPERATOR;
    def visitStr_operators(self, ctx: ZCodeParser.Str_operatorsContext):
        return ctx.STRING_OPERATOR()

    #funcdecl: 'func' IDENTIFIER OPEN_PARENTHESIS param_decl_list CLOSE_PARENTHESIS newline_list body  newline_list;
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = self.visit(ctx.param_decl_list())
        body = self.visit(ctx.body())
        return FuncDecl(name,param,body)

    #param_decl_list: param_decl_prime | ;
    def visitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param_decl_prime())

    # param_decl_prime: 
    # 	param_single_decl COMMA param_decl_prime 
    # 	| 
    # 	param_single_decl
    # ;
    def visitParam_decl_prime(self, ctx:ZCodeParser.Param_decl_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param_single_decl())]
        else:
            return [self.visit(ctx.param_single_decl())] + self.visit(ctx.param_decl_prime())

    # param_single_decl:
    # 	//Declaration only
    # 	typ IDENTIFIER 
    # 	|
    # 	//Array declaration only
    # 	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET 
    # ;
    def visitParam_single_decl(self, ctx:ZCodeParser.Param_single_declContext):
        if ctx.getChildCount() == 2:
            name = Id(ctx.IDENTIFIER().getText())
            varType = self.visit(ctx.typ())
            return VarDecl(name,varType,None,None)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            eleType = self.visit(ctx.typ())
            size = self.visit(ctx.arrlist())
            varType = ArrayType(size,eleType)
            return VarDecl(name,varType,None,None)
    
    #SKIP THIS AS PROGRAM IGNORES NEWLINES
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass
   

############################ --------------------- Statements --------------------------- #####################################
# done stmt
        # statements: (var_declStmt | assignStmt | ifStmt | forStmt | breakStmt | contStmt | returnStmt | funcCallStmt | blockStmt) NEWLINE;
    def visitStatements(self,ctx:ZCodeParser.StatementContext):
        if ctx.var_declStmt():
            return self.visit(ctx.var_declStmt())
        elif ctx.assignmentStmt():
            return self.visit(ctx.assignmentStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.contStmt():
            return self.visit(ctx.contStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.funcCallStmt():
            return self.visit(ctx.funcCallStmt())
        else:
            return self.visit(ctx.blockStmt())        

    
    #assignmentStmt: lhs ASSIGN_OPERATOR rhs NEWLINE newline_list;
    def visitAssignmentStmt(self,ctx: ZCodeParser.AssignmentStmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return Assign(lhs,rhs)

    # lhs: expression;
    def visitLhs(self,ctx:ZCodeParser.LhsContext):
        return self.visit(ctx.expr())


    # returnStmt: RET_ expr?;
    def visitReturnStmt(self,ctx:ZCodeParser.ReturnStmtContext):
        if ctx.getChildCount() >=1:
            return Return(self.visit(ctx.expr()))
        return Return(None)
    
        #rewrite for easier reading
        # expr = self.visit(ctx.expr()) if self.visit(ctx.expr()) else None
        # return Return(expr)

    #func_callStmt: func_call NEWLINE newline_list;
    def visitFuncCallStmt(self,ctx:ZCodeParser.Func_callStmtContext):
        return self.visit(ctx.funcCall())

    def visitIfStmt(self,ctx:ZCodeParser.IfStmtContext):
        # elifStmt: elif1 elseifT | ;
        # elseifT: NEWLINE elif1 elseifT | ;
        # elif1: ELSE_IF LB expr RB statements;
        # elseStmt: ELSE_ statements;
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.statements())        
        elifStmt = self.visit(ctx.elifStmt())
        elseStmt = self.visit(ctx.elseStmt())
        return If(expr,thenStmt,elifStmt,elseStmt)

    def visitElifStmt(self,ctx:ZCodeParser.ElifStmtContext):
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        if ctx.getChildCount() >=2:
            return [self.visit(ctx.elif1()) + self.visit(ctx.elifT())]
        return []
    
    # list of tuple + list of recursive tail
    def visitElifT(self,ctx:ZCodeParser.ElifTContext):
        if (ctx.getChildCount() >= 2):
            return self.visit(ctx.elseif1()) + [self.visit(ctx.elseifT())]
        return []
    
    #list of tuple(expr, stmt)
    def visitElif1(self,ctx:ZCodeParser.Elif1Context):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.statement()) #may need correction statements 
        return [ElseIf(expr, smt) for smt in stmt]

    #elseStmt: ELSE statement;
    def visitElseStmt(self,ctx:ZCodeParser.ElseStmtContext):
        return Else(self.visit(ctx.statement()))

    # forStmt: FOR_ ID UNTIL expr BY expr NEWLINE stmt_list;
    def visitForStmt(self,ctx:ZCodeParser.ForStmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = self.visit(ctx.expr(0))
        updExpr = self.visit(ctx.expr(1))
        body = self.visit(ctx.stmt_list())
        return For(name,condExpr,updExpr,body)
    
    #breakStmt: BREAKStmt NEWLINE newline_list;
    def visitBreakStmt(self,ctx:ZCodeParser.BreakStmtContext):
        return Break()

    #continueStmt: CONTINUEStmt NEWLINE newline_list;
    def visitContStmt(self,ctx:ZCodeParser.ContStmtContext):
        return Continue()

     #body: statement_block | ret |  ;
    

    # //not done
    def visitBody(self,ctx:ZCodeParser.BodyContext):
        if ctx.statement_block():
            return self.visit(ctx.statement_block())
        elif ctx.ret(): 
            return self.visit(ctx.ret())
        else:
            return None

    #statement_block: BEGIN statement_list END NEWLINE newline_list;
    def visitStatement_block(self, ctx: ZCodeParser.Statement_blockContext):
        stmt = self.visit(ctx.statement_list())
        return Block(stmt)

    #statement_list: newline_list statement newline_list statement_list | newline_list;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 1:
            return []
        else:
            return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())