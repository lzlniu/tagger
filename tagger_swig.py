# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _tagger_swig
else:
    import _tagger_swig

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class GetMatchesParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    entity_types = property(_tagger_swig.GetMatchesParams_entity_types_get, _tagger_swig.GetMatchesParams_entity_types_set)
    auto_detect = property(_tagger_swig.GetMatchesParams_auto_detect_get, _tagger_swig.GetMatchesParams_auto_detect_set)
    allow_overlap = property(_tagger_swig.GetMatchesParams_allow_overlap_get, _tagger_swig.GetMatchesParams_allow_overlap_set)
    find_acronyms = property(_tagger_swig.GetMatchesParams_find_acronyms_get, _tagger_swig.GetMatchesParams_find_acronyms_set)
    protect_tags = property(_tagger_swig.GetMatchesParams_protect_tags_get, _tagger_swig.GetMatchesParams_protect_tags_set)
    tokenize_characters = property(_tagger_swig.GetMatchesParams_tokenize_characters_get, _tagger_swig.GetMatchesParams_tokenize_characters_set)
    max_tokens = property(_tagger_swig.GetMatchesParams_max_tokens_get, _tagger_swig.GetMatchesParams_max_tokens_set)

    def __init__(self, *args):
        _tagger_swig.GetMatchesParams_swiginit(self, _tagger_swig.new_GetMatchesParams(*args))

    def add_entity_type(self, entity_type):
        return _tagger_swig.GetMatchesParams_add_entity_type(self, entity_type)

    def load_entity_types(self, types_filename):
        return _tagger_swig.GetMatchesParams_load_entity_types(self, types_filename)
    __swig_destroy__ = _tagger_swig.delete_GetMatchesParams

# Register GetMatchesParams in _tagger_swig:
_tagger_swig.GetMatchesParams_swigregister(GetMatchesParams)

class Tagger(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serials_only = property(_tagger_swig.Tagger_serials_only_get, _tagger_swig.Tagger_serials_only_set)
    organisms = property(_tagger_swig.Tagger_organisms_get, _tagger_swig.Tagger_organisms_set)

    def __init__(self, serials_only, pattern=None):
        _tagger_swig.Tagger_swiginit(self, _tagger_swig.new_Tagger(serials_only, pattern))
    __swig_destroy__ = _tagger_swig.delete_Tagger

    def add_name(self, *args):
        return _tagger_swig.Tagger_add_name(self, *args)

    def allow_block_name(self, name, document_id, block):
        return _tagger_swig.Tagger_allow_block_name(self, name, document_id, block)

    def check_name(self, name, type, identifier):
        return _tagger_swig.Tagger_check_name(self, name, type, identifier)

    def is_blocked(self, document_id, name):
        return _tagger_swig.Tagger_is_blocked(self, document_id, name)

    def resolve_name(self, name):
        return _tagger_swig.Tagger_resolve_name(self, name)

    def load_global(self, global_filename):
        return _tagger_swig.Tagger_load_global(self, global_filename)

    def load_local(self, local_filename):
        return _tagger_swig.Tagger_load_local(self, local_filename)

    def load_names(self, *args):
        return _tagger_swig.Tagger_load_names(self, *args)

    def get_matches(self, document, document_id, params):
        return _tagger_swig.Tagger_get_matches(self, document, document_id, params)

# Register Tagger in _tagger_swig:
_tagger_swig.Tagger_swigregister(Tagger)


def quit():
    return _tagger_swig.quit()


