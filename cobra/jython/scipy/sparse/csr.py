# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _csr
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types



def expandptr(*args):
  """expandptr(int n_row, int Ap, int Bi)"""
  return _csr.expandptr(*args)

def csr_matmat_pass1(*args):
  """
    csr_matmat_pass1(int n_row, int n_col, int Ap, int Aj, int Bp, int Bj,
        int Cp)
    """
  return _csr.csr_matmat_pass1(*args)

def csr_count_blocks(*args):
  """csr_count_blocks(int n_row, int n_col, int R, int C, int Ap, int Aj) -> int"""
  return _csr.csr_count_blocks(*args)

def csr_has_sorted_indices(*args):
  """csr_has_sorted_indices(int n_row, int Ap, int Aj) -> bool"""
  return _csr.csr_has_sorted_indices(*args)


def csr_diagonal(*args):
  """
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        signed char Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        unsigned char Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, short Ax, short Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        unsigned short Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, int Ax, int Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        unsigned int Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, long long Ax,
        long long Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        unsigned long long Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, float Ax, float Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, double Ax, double Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, long double Ax,
        long double Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        npy_cfloat_wrapper Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        npy_cdouble_wrapper Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        npy_clongdouble_wrapper Yx)
    """
  return _csr.csr_diagonal(*args)

def csr_scale_rows(*args):
  """
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        signed char Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        unsigned char Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, short Ax, short Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        unsigned short Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, int Ax, int Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        unsigned int Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, long long Ax,
        long long Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        unsigned long long Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, float Ax, float Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, double Ax, double Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, long double Ax,
        long double Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        npy_cfloat_wrapper Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        npy_cdouble_wrapper Xx)
    csr_scale_rows(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        npy_clongdouble_wrapper Xx)
    """
  return _csr.csr_scale_rows(*args)

def csr_scale_columns(*args):
  """
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        signed char Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        unsigned char Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, short Ax, short Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        unsigned short Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, int Ax, int Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        unsigned int Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, long long Ax,
        long long Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        unsigned long long Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, float Ax, float Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, double Ax, double Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, long double Ax,
        long double Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        npy_cfloat_wrapper Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        npy_cdouble_wrapper Xx)
    csr_scale_columns(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        npy_clongdouble_wrapper Xx)
    """
  return _csr.csr_scale_columns(*args)

def csr_tocsc(*args):
  """
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int Bp, int Bi, signed char Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int Bp, int Bi, unsigned char Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp,
        int Bi, short Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int Bp, int Bi, unsigned short Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp,
        int Bi, int Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int Bp, int Bi, unsigned int Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int Bp, int Bi, long long Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int Bp, int Bi, unsigned long long Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp,
        int Bi, float Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp,
        int Bi, double Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int Bp, int Bi, long double Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int Bp, int Bi, npy_cfloat_wrapper Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int Bp, int Bi, npy_cdouble_wrapper Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int Bp, int Bi, npy_clongdouble_wrapper Bx)
    """
  return _csr.csr_tocsc(*args)

def csr_tobsr(*args):
  """
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        signed char Ax, int Bp, int Bj, signed char Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        unsigned char Ax, int Bp, int Bj, unsigned char Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        short Ax, int Bp, int Bj, short Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        unsigned short Ax, int Bp, int Bj, unsigned short Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        int Ax, int Bp, int Bj, int Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        unsigned int Ax, int Bp, int Bj, unsigned int Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        long long Ax, int Bp, int Bj, long long Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        unsigned long long Ax, int Bp, int Bj, unsigned long long Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        float Ax, int Bp, int Bj, float Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        double Ax, int Bp, int Bj, double Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        long double Ax, int Bp, int Bj, long double Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        npy_cfloat_wrapper Ax, int Bp, int Bj, npy_cfloat_wrapper Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        npy_cdouble_wrapper Ax, int Bp, int Bj, npy_cdouble_wrapper Bx)
    csr_tobsr(int n_row, int n_col, int R, int C, int Ap, int Aj,
        npy_clongdouble_wrapper Ax, int Bp, int Bj,
        npy_clongdouble_wrapper Bx)
    """
  return _csr.csr_tobsr(*args)

def csr_matmat_pass2(*args):
  """
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int Bp, int Bj, signed char Bx, int Cp, int Cj,
        signed char Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int Bp, int Bj, unsigned char Bx, int Cp,
        int Cj, unsigned char Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp,
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int Bp, int Bj, unsigned short Bx, int Cp,
        int Cj, unsigned short Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp,
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int Bp, int Bj, unsigned int Bx, int Cp,
        int Cj, unsigned int Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int Bp, int Bj, long long Bx, int Cp, int Cj,
        long long Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int Bp, int Bj, unsigned long long Bx,
        int Cp, int Cj, unsigned long long Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp,
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp,
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int Bp, int Bj, long double Bx, int Cp, int Cj,
        long double Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int Bp, int Bj, npy_cfloat_wrapper Bx,
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int Bp, int Bj, npy_cdouble_wrapper Bx,
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int Bp, int Bj, npy_clongdouble_wrapper Bx,
        int Cp, int Cj, npy_clongdouble_wrapper Cx)
    """
  return _csr.csr_matmat_pass2(*args)

def csr_matvec(*args):
  """
    csr_matvec(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        signed char Xx, signed char Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        unsigned char Xx, unsigned char Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, short Ax, short Xx,
        short Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        unsigned short Xx, unsigned short Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, int Ax, int Xx,
        int Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        unsigned int Xx, unsigned int Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, long long Ax,
        long long Xx, long long Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        unsigned long long Xx, unsigned long long Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, float Ax, float Xx,
        float Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, double Ax, double Xx,
        double Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, long double Ax,
        long double Xx, long double Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        npy_cfloat_wrapper Xx, npy_cfloat_wrapper Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        npy_cdouble_wrapper Xx, npy_cdouble_wrapper Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        npy_clongdouble_wrapper Xx, npy_clongdouble_wrapper Yx)
    """
  return _csr.csr_matvec(*args)

def csr_matvecs(*args):
  """
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, signed char Ax,
        signed char Xx, signed char Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, unsigned char Ax,
        unsigned char Xx, unsigned char Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, short Ax,
        short Xx, short Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, unsigned short Ax,
        unsigned short Xx, unsigned short Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, int Ax,
        int Xx, int Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, unsigned int Ax,
        unsigned int Xx, unsigned int Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, long long Ax,
        long long Xx, long long Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, unsigned long long Ax,
        unsigned long long Xx,
        unsigned long long Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, float Ax,
        float Xx, float Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, double Ax,
        double Xx, double Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, long double Ax,
        long double Xx, long double Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, npy_cfloat_wrapper Ax,
        npy_cfloat_wrapper Xx,
        npy_cfloat_wrapper Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, npy_cdouble_wrapper Ax,
        npy_cdouble_wrapper Xx,
        npy_cdouble_wrapper Yx)
    csr_matvecs(int n_row, int n_col, int n_vecs, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        npy_clongdouble_wrapper Xx,
        npy_clongdouble_wrapper Yx)
    """
  return _csr.csr_matvecs(*args)

def csr_elmul_csr(*args):
  """
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int Bp, int Bj, signed char Bx, int Cp, int Cj,
        signed char Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int Bp, int Bj, unsigned char Bx, int Cp,
        int Cj, unsigned char Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp,
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int Bp, int Bj, unsigned short Bx, int Cp,
        int Cj, unsigned short Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp,
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int Bp, int Bj, unsigned int Bx, int Cp,
        int Cj, unsigned int Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int Bp, int Bj, long long Bx, int Cp, int Cj,
        long long Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int Bp, int Bj, unsigned long long Bx,
        int Cp, int Cj, unsigned long long Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp,
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp,
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int Bp, int Bj, long double Bx, int Cp, int Cj,
        long double Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int Bp, int Bj, npy_cfloat_wrapper Bx,
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int Bp, int Bj, npy_cdouble_wrapper Bx,
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int Bp, int Bj, npy_clongdouble_wrapper Bx,
        int Cp, int Cj, npy_clongdouble_wrapper Cx)
    """
  return _csr.csr_elmul_csr(*args)

def csr_eldiv_csr(*args):
  """
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int Bp, int Bj, signed char Bx, int Cp, int Cj,
        signed char Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int Bp, int Bj, unsigned char Bx, int Cp,
        int Cj, unsigned char Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp,
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int Bp, int Bj, unsigned short Bx, int Cp,
        int Cj, unsigned short Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp,
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int Bp, int Bj, unsigned int Bx, int Cp,
        int Cj, unsigned int Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int Bp, int Bj, long long Bx, int Cp, int Cj,
        long long Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int Bp, int Bj, unsigned long long Bx,
        int Cp, int Cj, unsigned long long Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp,
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp,
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int Bp, int Bj, long double Bx, int Cp, int Cj,
        long double Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int Bp, int Bj, npy_cfloat_wrapper Bx,
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int Bp, int Bj, npy_cdouble_wrapper Bx,
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int Bp, int Bj, npy_clongdouble_wrapper Bx,
        int Cp, int Cj, npy_clongdouble_wrapper Cx)
    """
  return _csr.csr_eldiv_csr(*args)

def csr_plus_csr(*args):
  """
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int Bp, int Bj, signed char Bx, int Cp, int Cj,
        signed char Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int Bp, int Bj, unsigned char Bx, int Cp,
        int Cj, unsigned char Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp,
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int Bp, int Bj, unsigned short Bx, int Cp,
        int Cj, unsigned short Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp,
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int Bp, int Bj, unsigned int Bx, int Cp,
        int Cj, unsigned int Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int Bp, int Bj, long long Bx, int Cp, int Cj,
        long long Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int Bp, int Bj, unsigned long long Bx,
        int Cp, int Cj, unsigned long long Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp,
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp,
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int Bp, int Bj, long double Bx, int Cp, int Cj,
        long double Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int Bp, int Bj, npy_cfloat_wrapper Bx,
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int Bp, int Bj, npy_cdouble_wrapper Bx,
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int Bp, int Bj, npy_clongdouble_wrapper Bx,
        int Cp, int Cj, npy_clongdouble_wrapper Cx)
    """
  return _csr.csr_plus_csr(*args)

def csr_minus_csr(*args):
  """
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int Bp, int Bj, signed char Bx, int Cp, int Cj,
        signed char Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int Bp, int Bj, unsigned char Bx, int Cp,
        int Cj, unsigned char Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp,
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int Bp, int Bj, unsigned short Bx, int Cp,
        int Cj, unsigned short Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp,
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int Bp, int Bj, unsigned int Bx, int Cp,
        int Cj, unsigned int Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int Bp, int Bj, long long Bx, int Cp, int Cj,
        long long Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int Bp, int Bj, unsigned long long Bx,
        int Cp, int Cj, unsigned long long Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp,
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp,
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int Bp, int Bj, long double Bx, int Cp, int Cj,
        long double Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int Bp, int Bj, npy_cfloat_wrapper Bx,
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int Bp, int Bj, npy_cdouble_wrapper Bx,
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int Bp, int Bj, npy_clongdouble_wrapper Bx,
        int Cp, int Cj, npy_clongdouble_wrapper Cx)
    """
  return _csr.csr_minus_csr(*args)

def csr_sort_indices(*args):
  """
    csr_sort_indices(int n_row, int Ap, int Aj, signed char Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, unsigned char Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, short Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, unsigned short Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, int Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, unsigned int Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, long long Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, unsigned long long Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, float Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, double Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, long double Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, npy_cfloat_wrapper Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, npy_cdouble_wrapper Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, npy_clongdouble_wrapper Ax)
    """
  return _csr.csr_sort_indices(*args)

def csr_eliminate_zeros(*args):
  """
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, signed char Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, unsigned char Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, short Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, unsigned short Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, int Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, unsigned int Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, long long Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, float Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, double Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, long double Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax)
    csr_eliminate_zeros(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax)
    """
  return _csr.csr_eliminate_zeros(*args)

def csr_sum_duplicates(*args):
  """
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, signed char Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, unsigned char Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, short Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, unsigned short Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, int Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, unsigned int Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, long long Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, float Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, double Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, long double Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax)
    """
  return _csr.csr_sum_duplicates(*args)

def get_csr_submatrix(*args):
  """
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(signed char)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(unsigned char)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, short Ax, int ir0,
        int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(short)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(unsigned short)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, int Ax, int ir0,
        int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(int)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(unsigned int)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(long long)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int ir0, int ir1, int ic0, int ic1,
        std::vector<(int)> Bp, std::vector<(int)> Bj,
        std::vector<(unsigned long long)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, float Ax, int ir0,
        int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, double Ax, int ir0,
        int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp,
        std::vector<(int)> Bj, std::vector<(long double)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int ir0, int ir1, int ic0, int ic1,
        std::vector<(int)> Bp, std::vector<(int)> Bj,
        std::vector<(npy_cfloat_wrapper)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int ir0, int ir1, int ic0, int ic1,
        std::vector<(int)> Bp, std::vector<(int)> Bj,
        std::vector<(npy_cdouble_wrapper)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int ir0, int ir1, int ic0, int ic1,
        std::vector<(int)> Bp, std::vector<(int)> Bj,
        std::vector<(npy_clongdouble_wrapper)> Bx)
    """
  return _csr.get_csr_submatrix(*args)

def csr_sample_values(*args):
  """
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, signed char Ax,
        int n_samples, int Bi, int Bj, signed char Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, unsigned char Ax,
        int n_samples, int Bi, int Bj, unsigned char Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, short Ax, int n_samples,
        int Bi, int Bj, short Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, unsigned short Ax,
        int n_samples, int Bi, int Bj, unsigned short Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, int Ax, int n_samples,
        int Bi, int Bj, int Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, unsigned int Ax,
        int n_samples, int Bi, int Bj, unsigned int Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, long long Ax,
        int n_samples, int Bi, int Bj, long long Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, unsigned long long Ax,
        int n_samples, int Bi, int Bj, unsigned long long Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, float Ax, int n_samples,
        int Bi, int Bj, float Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, double Ax, int n_samples,
        int Bi, int Bj, double Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, long double Ax,
        int n_samples, int Bi, int Bj, long double Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax,
        int n_samples, int Bi, int Bj, npy_cfloat_wrapper Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax,
        int n_samples, int Bi, int Bj, npy_cdouble_wrapper Bx)
    csr_sample_values(int n_row, int n_col, int Ap, int Aj, npy_clongdouble_wrapper Ax,
        int n_samples, int Bi, int Bj,
        npy_clongdouble_wrapper Bx)
    """
  return _csr.csr_sample_values(*args)

