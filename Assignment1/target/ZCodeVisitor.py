# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#main_decl.
    def visitMain_decl(self, ctx:ZCodeParser.Main_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_body.
    def visitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#singDecl.
    def visitSingDecl(self, ctx:ZCodeParser.SingDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive.
    def visitPrimitive(self, ctx:ZCodeParser.PrimitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayT.
    def visitArrayT(self, ctx:ZCodeParser.ArrayTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexExpr.
    def visitIndexExpr(self, ctx:ZCodeParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexTail.
    def visitIndexTail(self, ctx:ZCodeParser.IndexTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argList.
    def visitArgList(self, ctx:ZCodeParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argT.
    def visitArgT(self, ctx:ZCodeParser.ArgTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argument.
    def visitArgument(self, ctx:ZCodeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramList.
    def visitParamList(self, ctx:ZCodeParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramT.
    def visitParamT(self, ctx:ZCodeParser.ParamTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtT.
    def visitStmtT(self, ctx:ZCodeParser.StmtTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_list.
    def visitFunc_list(self, ctx:ZCodeParser.Func_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcT.
    def visitFuncT(self, ctx:ZCodeParser.FuncTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sizeList.
    def visitSizeList(self, ctx:ZCodeParser.SizeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sizeT.
    def visitSizeT(self, ctx:ZCodeParser.SizeTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_op.
    def visitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcCall.
    def visitFuncCall(self, ctx:ZCodeParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statements.
    def visitStatements(self, ctx:ZCodeParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_declStmt.
    def visitVar_declStmt(self, ctx:ZCodeParser.Var_declStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignStmt.
    def visitAssignStmt(self, ctx:ZCodeParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifStmt.
    def visitIfStmt(self, ctx:ZCodeParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifStmt.
    def visitElifStmt(self, ctx:ZCodeParser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseifT.
    def visitElseifT(self, ctx:ZCodeParser.ElseifTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif1.
    def visitElif1(self, ctx:ZCodeParser.Elif1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseStmt.
    def visitElseStmt(self, ctx:ZCodeParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forStmt.
    def visitForStmt(self, ctx:ZCodeParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakStmt.
    def visitBreakStmt(self, ctx:ZCodeParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#contStmt.
    def visitContStmt(self, ctx:ZCodeParser.ContStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnStmt.
    def visitReturnStmt(self, ctx:ZCodeParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcCallStmt.
    def visitFuncCallStmt(self, ctx:ZCodeParser.FuncCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockStmt.
    def visitBlockStmt(self, ctx:ZCodeParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockBody.
    def visitBlockBody(self, ctx:ZCodeParser.BlockBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)



del ZCodeParser