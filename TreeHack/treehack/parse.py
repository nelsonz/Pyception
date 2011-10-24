import ast, sys

globals = { "classes" : {}, "variables" : {}, "functions" : {} }

# BUILDS UP THE REPRESENATION OF THE TREE
def Hack( node, scope ):
    if hasattr( node, "Hack" ):
        node.Hack( scope )

def HackMap( nodes, scope ):
    for node in nodes:
        Hack( node, scope )

def ModuleHack( self, scope ):
    HackMap( self.body, scope )

def ImportHack( self, scope ):
    for name in self.names:
        name.Variablize( scope )

def ImportFormHack( self, scope ):
    pass
    
def ClassHack( self, scope ):
    classScope = scope[ "classes" ][ self.name ] = { "classes" : {}, "variables" : {}, "functions" : {}, "lineno" : self.lineno, "doc" : ast.get_docstring( self ) }
    HackMap( self.body, classScope )

def FunctionDefHack( self, scope ):
    newScope = scope["functions"][ self.name ] = { "lineno": self.lineno, "doc" : ast.get_docstring( self ), "classes" : {}, "functions" : {}, "variables": {} }
    for arg in self.args.args:
        arg.Variablize( newScope )
    if self.args.vararg:
        newScope[ "variables" ][ "*" + self.args.vararg ] = { "lineno": self.lineno, "classes" : {}, "functions" : {}, "variables" : {} }
    if self.args.kwarg:
        newScope[ "variables" ][ "**" + self.args.kwarg ] = { "lineno": self.lineno, "classes" : {}, "functions" : {}, "variables" : {} }

def AssignHack( self, scope ):
    for target in self.targets:
        target.Variablize( scope )

def IfHack( self, scope ):
    HackMap( self.body, scope )
    HackMap( self.orelse, scope )

# VARIABLIZES
def NameVariablize( self, scope ):
    if self.id != "self":
        scope[ "variables" ][ self.id ] = { "lineno": self.lineno, "classes" : {}, "functions" : {}, "variables" : {} }

def TupleVariablize( self, scope ):
    for name in self.elts:
        name.Variablize( scope )

def AttributeVariablize( self, scope ):
    scope[ "variables" ][ self.Id() ] = ""

def aliasVariablize( self, scope ):
    scope[ "variables" ][ self.name ] = self.asname if self.asname else ""

def NameId( self ):
    return self.id

def AttributeId( self ):
    return self.value.Id() + "." + self.attr

ast.Name.Id = NameId
ast.Attribute.Id = AttributeId

ast.Name.Variablize = NameVariablize
ast.Tuple.Variablize = TupleVariablize
ast.Attribute.Variablize = AttributeVariablize
ast.alias.Variablize = aliasVariablize

ast.Module.Hack = ModuleHack
ast.Import.Hack = ImportHack
ast.FunctionDef.Hack = FunctionDefHack
ast.ClassDef.Hack = ClassHack
ast.Assign.Hack = AssignHack
ast.If.Hack = IfHack
ast.Pass.Hack = ast.Assert.Hack = ast.Raise.Hack = ast.Print.Hack = ast.AugAssign.Hack = ast.Delete.Hack = ast.Expr.Hack = lambda self, scope: None

def printStr( d, indent=0 ):
    if type( d ) != dict:
        print "%s%s" % ( ' ' * indent * 5 , d )
    else:
        for key, val in d.items():
            print "%s{ %s : " % ( ' ' * indent * 5 , key )
            printStr( val, indent + 1)
            print "%s}" % ( ' ' * indent * 5 )


def HACK( text ):
    global globals
    try:
        Hack( ast.parse( text ), globals )
    except SyntaxError as e:
        return "Syntax Error " + str( e )
    ret = globals
    globals = { "classes" : {}, "variables" : {}, "functions" : {} }
    return ret


if __name__ == '__main__':
    if len( sys.argv ) > 1:
        printStr( HACK( ast.parse( "\n".join( open( sys.argv[-1] ).readlines() ) ) ) )

