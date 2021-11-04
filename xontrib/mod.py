import builtins


class _ModuleProxy:
    def __init__(self, module=None):
        self._module = module
        
    def __getattr__(self, name):
        import importlib
        import types
    
        if name == "xonsh_display":
            raise AttributeError(name)
           
        try:
            result = getattr(self._module, name)
        except AttributeError:
            if self._module is None:
                result = importlib.import_module(name)
            else:
                result = importlib.import_module(f".{name}", self._module.__package__)
           
        if isinstance(result, types.ModuleType):
            return self.__class__(result)
           
        return result
        
    def __repr__(self):
        if self._module is None:
            return super().__repr__(self)
            
        return repr(self._module)


builtins.mod = _ModuleProxy()
