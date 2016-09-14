# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pdd', [dirname(__file__)])
        except ImportError:
            import _pdd
            return _pdd
        if fp is not None:
            try:
                _mod = imp.load_module('_pdd', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pdd = swig_import_helper()
    del swig_import_helper
else:
    import _pdd
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_pdd.WRAPPER_ERROR_FILE_OPEN_swigconstant(_pdd)
WRAPPER_ERROR_FILE_OPEN = _pdd.WRAPPER_ERROR_FILE_OPEN

_pdd.WRAPPER_ERROR_NOT_IMPLEMENTED_swigconstant(_pdd)
WRAPPER_ERROR_NOT_IMPLEMENTED = _pdd.WRAPPER_ERROR_NOT_IMPLEMENTED

def ENepanet_wrap(f1, f2, f3, pviewprog):
    return _pdd.ENepanet_wrap(f1, f2, f3, pviewprog)
ENepanet_wrap = _pdd.ENepanet_wrap

def ENopen_wrap(a1, a2, a3):
    return _pdd.ENopen_wrap(a1, a2, a3)
ENopen_wrap = _pdd.ENopen_wrap

def ENsaveinpfile_wrap(a1):
    return _pdd.ENsaveinpfile_wrap(a1)
ENsaveinpfile_wrap = _pdd.ENsaveinpfile_wrap

def ENclose_wrap():
    return _pdd.ENclose_wrap()
ENclose_wrap = _pdd.ENclose_wrap

def ENsolveH_wrap():
    return _pdd.ENsolveH_wrap()
ENsolveH_wrap = _pdd.ENsolveH_wrap

def ENsaveH_wrap():
    return _pdd.ENsaveH_wrap()
ENsaveH_wrap = _pdd.ENsaveH_wrap

def ENopenH_wrap():
    return _pdd.ENopenH_wrap()
ENopenH_wrap = _pdd.ENopenH_wrap

def ENinitH_wrap(a1):
    return _pdd.ENinitH_wrap(a1)
ENinitH_wrap = _pdd.ENinitH_wrap

def ENrunH_wrap():
    return _pdd.ENrunH_wrap()
ENrunH_wrap = _pdd.ENrunH_wrap

def ENnextH_wrap():
    return _pdd.ENnextH_wrap()
ENnextH_wrap = _pdd.ENnextH_wrap

def ENcloseH_wrap():
    return _pdd.ENcloseH_wrap()
ENcloseH_wrap = _pdd.ENcloseH_wrap

def ENsavehydfile_wrap(a1):
    return _pdd.ENsavehydfile_wrap(a1)
ENsavehydfile_wrap = _pdd.ENsavehydfile_wrap

def ENusehydfile_wrap(a1):
    return _pdd.ENusehydfile_wrap(a1)
ENusehydfile_wrap = _pdd.ENusehydfile_wrap

def ENsolveQ_wrap():
    return _pdd.ENsolveQ_wrap()
ENsolveQ_wrap = _pdd.ENsolveQ_wrap

def ENopenQ_wrap():
    return _pdd.ENopenQ_wrap()
ENopenQ_wrap = _pdd.ENopenQ_wrap

def ENinitQ_wrap(a1):
    return _pdd.ENinitQ_wrap(a1)
ENinitQ_wrap = _pdd.ENinitQ_wrap

def ENrunQ_wrap():
    return _pdd.ENrunQ_wrap()
ENrunQ_wrap = _pdd.ENrunQ_wrap

def ENnextQ_wrap():
    return _pdd.ENnextQ_wrap()
ENnextQ_wrap = _pdd.ENnextQ_wrap

def ENstepQ_wrap():
    return _pdd.ENstepQ_wrap()
ENstepQ_wrap = _pdd.ENstepQ_wrap

def ENcloseQ_wrap():
    return _pdd.ENcloseQ_wrap()
ENcloseQ_wrap = _pdd.ENcloseQ_wrap

def ENwriteline_wrap(a1):
    return _pdd.ENwriteline_wrap(a1)
ENwriteline_wrap = _pdd.ENwriteline_wrap

def ENreport_wrap():
    return _pdd.ENreport_wrap()
ENreport_wrap = _pdd.ENreport_wrap

def ENresetreport_wrap():
    return _pdd.ENresetreport_wrap()
ENresetreport_wrap = _pdd.ENresetreport_wrap

def ENsetreport_wrap(a1):
    return _pdd.ENsetreport_wrap(a1)
ENsetreport_wrap = _pdd.ENsetreport_wrap

def ENgetcontrol_wrap(arg1):
    return _pdd.ENgetcontrol_wrap(arg1)
ENgetcontrol_wrap = _pdd.ENgetcontrol_wrap

def ENgetcount_wrap(a1):
    return _pdd.ENgetcount_wrap(a1)
ENgetcount_wrap = _pdd.ENgetcount_wrap

def ENgetoption_wrap(a1):
    return _pdd.ENgetoption_wrap(a1)
ENgetoption_wrap = _pdd.ENgetoption_wrap

def ENgettimeparam_wrap(a1):
    return _pdd.ENgettimeparam_wrap(a1)
ENgettimeparam_wrap = _pdd.ENgettimeparam_wrap

def ENgetflowunits_wrap():
    return _pdd.ENgetflowunits_wrap()
ENgetflowunits_wrap = _pdd.ENgetflowunits_wrap

def ENgetpatternindex_wrap(a1):
    return _pdd.ENgetpatternindex_wrap(a1)
ENgetpatternindex_wrap = _pdd.ENgetpatternindex_wrap

def ENgetpatternid_wrap(a1):
    return _pdd.ENgetpatternid_wrap(a1)
ENgetpatternid_wrap = _pdd.ENgetpatternid_wrap

def ENgetpatternlen_wrap(a1):
    return _pdd.ENgetpatternlen_wrap(a1)
ENgetpatternlen_wrap = _pdd.ENgetpatternlen_wrap

def ENgetpatternvalue_wrap(a1, a2):
    return _pdd.ENgetpatternvalue_wrap(a1, a2)
ENgetpatternvalue_wrap = _pdd.ENgetpatternvalue_wrap

def ENgetqualtype_wrap():
    return _pdd.ENgetqualtype_wrap()
ENgetqualtype_wrap = _pdd.ENgetqualtype_wrap

def ENgeterror_wrap(a1, a2, a3):
    return _pdd.ENgeterror_wrap(a1, a2, a3)
ENgeterror_wrap = _pdd.ENgeterror_wrap

def ENgetnodeindex_wrap(a2):
    return _pdd.ENgetnodeindex_wrap(a2)
ENgetnodeindex_wrap = _pdd.ENgetnodeindex_wrap

def ENgetnodeid_wrap(a1):
    return _pdd.ENgetnodeid_wrap(a1)
ENgetnodeid_wrap = _pdd.ENgetnodeid_wrap

def ENgetnodetype_wrap(a1):
    return _pdd.ENgetnodetype_wrap(a1)
ENgetnodetype_wrap = _pdd.ENgetnodetype_wrap

def ENgetnodevalue_wrap(a1, a2):
    return _pdd.ENgetnodevalue_wrap(a1, a2)
ENgetnodevalue_wrap = _pdd.ENgetnodevalue_wrap

def ENgetlinkindex_wrap(a1):
    return _pdd.ENgetlinkindex_wrap(a1)
ENgetlinkindex_wrap = _pdd.ENgetlinkindex_wrap

def ENgetlinkid_wrap(a1):
    return _pdd.ENgetlinkid_wrap(a1)
ENgetlinkid_wrap = _pdd.ENgetlinkid_wrap

def ENgetlinktype_wrap(a1):
    return _pdd.ENgetlinktype_wrap(a1)
ENgetlinktype_wrap = _pdd.ENgetlinktype_wrap

def ENgetlinknodes_wrap(a1):
    return _pdd.ENgetlinknodes_wrap(a1)
ENgetlinknodes_wrap = _pdd.ENgetlinknodes_wrap

def ENgetlinkvalue_wrap(a1, a2):
    return _pdd.ENgetlinkvalue_wrap(a1, a2)
ENgetlinkvalue_wrap = _pdd.ENgetlinkvalue_wrap

def ENgetversion_wrap(a1):
    return _pdd.ENgetversion_wrap(a1)
ENgetversion_wrap = _pdd.ENgetversion_wrap

def ENsetcontrol_wrap(a1, a2, a3, a4, a5, a6):
    return _pdd.ENsetcontrol_wrap(a1, a2, a3, a4, a5, a6)
ENsetcontrol_wrap = _pdd.ENsetcontrol_wrap

def ENsetnodevalue_wrap(a1, a2, a3):
    return _pdd.ENsetnodevalue_wrap(a1, a2, a3)
ENsetnodevalue_wrap = _pdd.ENsetnodevalue_wrap

def ENsetlinkvalue_wrap(a1, a2, a3):
    return _pdd.ENsetlinkvalue_wrap(a1, a2, a3)
ENsetlinkvalue_wrap = _pdd.ENsetlinkvalue_wrap

def ENaddpattern_wrap(a1):
    return _pdd.ENaddpattern_wrap(a1)
ENaddpattern_wrap = _pdd.ENaddpattern_wrap

def ENsetpattern_wrap(a1, a2, a3):
    return _pdd.ENsetpattern_wrap(a1, a2, a3)
ENsetpattern_wrap = _pdd.ENsetpattern_wrap

def ENsetpatternvalue_wrap(a1, a2, a3):
    return _pdd.ENsetpatternvalue_wrap(a1, a2, a3)
ENsetpatternvalue_wrap = _pdd.ENsetpatternvalue_wrap

def ENsettimeparam_wrap(a1, a2):
    return _pdd.ENsettimeparam_wrap(a1, a2)
ENsettimeparam_wrap = _pdd.ENsettimeparam_wrap

def ENsetoption_wrap(a1, a2):
    return _pdd.ENsetoption_wrap(a1, a2)
ENsetoption_wrap = _pdd.ENsetoption_wrap

def ENsetstatusreport_wrap(a1):
    return _pdd.ENsetstatusreport_wrap(a1)
ENsetstatusreport_wrap = _pdd.ENsetstatusreport_wrap

def ENsetqualtype_wrap(a1, a2, a3, a4):
    return _pdd.ENsetqualtype_wrap(a1, a2, a3, a4)
ENsetqualtype_wrap = _pdd.ENsetqualtype_wrap

def ENsetemitter_wrap(a1, a2):
    return _pdd.ENsetemitter_wrap(a1, a2)
ENsetemitter_wrap = _pdd.ENsetemitter_wrap

def ENgetemitter_wrap(a1, a2):
    return _pdd.ENgetemitter_wrap(a1, a2)
ENgetemitter_wrap = _pdd.ENgetemitter_wrap

def write_sign(str):
    return _pdd.write_sign(str)
write_sign = _pdd.write_sign

def getcurrenttime():
    return _pdd.getcurrenttime()
getcurrenttime = _pdd.getcurrenttime

def run_before_ENopen():
    return _pdd.run_before_ENopen()
run_before_ENopen = _pdd.run_before_ENopen

def run_before_ENsaveinpfile():
    return _pdd.run_before_ENsaveinpfile()
run_before_ENsaveinpfile = _pdd.run_before_ENsaveinpfile

def run_before_ENclose():
    return _pdd.run_before_ENclose()
run_before_ENclose = _pdd.run_before_ENclose

def run_before_ENsaveH():
    return _pdd.run_before_ENsaveH()
run_before_ENsaveH = _pdd.run_before_ENsaveH

def run_before_ENinitH():
    return _pdd.run_before_ENinitH()
run_before_ENinitH = _pdd.run_before_ENinitH

def run_before_ENrunH():
    return _pdd.run_before_ENrunH()
run_before_ENrunH = _pdd.run_before_ENrunH

def run_before_ENnextH():
    return _pdd.run_before_ENnextH()
run_before_ENnextH = _pdd.run_before_ENnextH

def run_before_ENcloseH():
    return _pdd.run_before_ENcloseH()
run_before_ENcloseH = _pdd.run_before_ENcloseH

def run_before_ENsavehydfile():
    return _pdd.run_before_ENsavehydfile()
run_before_ENsavehydfile = _pdd.run_before_ENsavehydfile

def run_before_ENusehydfile():
    return _pdd.run_before_ENusehydfile()
run_before_ENusehydfile = _pdd.run_before_ENusehydfile

def run_before_ENsolveQ():
    return _pdd.run_before_ENsolveQ()
run_before_ENsolveQ = _pdd.run_before_ENsolveQ

def run_before_ENopenQ():
    return _pdd.run_before_ENopenQ()
run_before_ENopenQ = _pdd.run_before_ENopenQ

def run_before_ENinitQ():
    return _pdd.run_before_ENinitQ()
run_before_ENinitQ = _pdd.run_before_ENinitQ

def run_before_ENrunQ():
    return _pdd.run_before_ENrunQ()
run_before_ENrunQ = _pdd.run_before_ENrunQ

def run_before_ENnextQ():
    return _pdd.run_before_ENnextQ()
run_before_ENnextQ = _pdd.run_before_ENnextQ

def run_before_ENstepQ():
    return _pdd.run_before_ENstepQ()
run_before_ENstepQ = _pdd.run_before_ENstepQ

def run_before_ENcloseQ():
    return _pdd.run_before_ENcloseQ()
run_before_ENcloseQ = _pdd.run_before_ENcloseQ

def run_before_ENwriteline():
    return _pdd.run_before_ENwriteline()
run_before_ENwriteline = _pdd.run_before_ENwriteline

def run_before_ENreport():
    return _pdd.run_before_ENreport()
run_before_ENreport = _pdd.run_before_ENreport

def run_before_ENresetreport():
    return _pdd.run_before_ENresetreport()
run_before_ENresetreport = _pdd.run_before_ENresetreport

def run_before_ENsetreport():
    return _pdd.run_before_ENsetreport()
run_before_ENsetreport = _pdd.run_before_ENsetreport

def run_before_ENgetcontrol():
    return _pdd.run_before_ENgetcontrol()
run_before_ENgetcontrol = _pdd.run_before_ENgetcontrol

def run_before_ENgetcount():
    return _pdd.run_before_ENgetcount()
run_before_ENgetcount = _pdd.run_before_ENgetcount

def run_before_ENgetoption():
    return _pdd.run_before_ENgetoption()
run_before_ENgetoption = _pdd.run_before_ENgetoption

def run_before_ENgettimeparam():
    return _pdd.run_before_ENgettimeparam()
run_before_ENgettimeparam = _pdd.run_before_ENgettimeparam

def run_before_ENgetflowunits():
    return _pdd.run_before_ENgetflowunits()
run_before_ENgetflowunits = _pdd.run_before_ENgetflowunits

def run_before_ENgetpatternindex():
    return _pdd.run_before_ENgetpatternindex()
run_before_ENgetpatternindex = _pdd.run_before_ENgetpatternindex

def run_before_ENgetpatternid():
    return _pdd.run_before_ENgetpatternid()
run_before_ENgetpatternid = _pdd.run_before_ENgetpatternid

def run_before_ENgetpatternlen():
    return _pdd.run_before_ENgetpatternlen()
run_before_ENgetpatternlen = _pdd.run_before_ENgetpatternlen

def run_before_ENgetpatternvalue():
    return _pdd.run_before_ENgetpatternvalue()
run_before_ENgetpatternvalue = _pdd.run_before_ENgetpatternvalue

def run_before_ENgetqualtype():
    return _pdd.run_before_ENgetqualtype()
run_before_ENgetqualtype = _pdd.run_before_ENgetqualtype

def run_before_ENgeterror():
    return _pdd.run_before_ENgeterror()
run_before_ENgeterror = _pdd.run_before_ENgeterror

def run_before_ENgetnodeindex():
    return _pdd.run_before_ENgetnodeindex()
run_before_ENgetnodeindex = _pdd.run_before_ENgetnodeindex

def run_before_ENgetnodeid():
    return _pdd.run_before_ENgetnodeid()
run_before_ENgetnodeid = _pdd.run_before_ENgetnodeid

def run_before_ENgetnodetype():
    return _pdd.run_before_ENgetnodetype()
run_before_ENgetnodetype = _pdd.run_before_ENgetnodetype

def run_before_ENgetnodevalue():
    return _pdd.run_before_ENgetnodevalue()
run_before_ENgetnodevalue = _pdd.run_before_ENgetnodevalue

def run_before_ENgetlinkindex():
    return _pdd.run_before_ENgetlinkindex()
run_before_ENgetlinkindex = _pdd.run_before_ENgetlinkindex

def run_before_ENgetlinkid():
    return _pdd.run_before_ENgetlinkid()
run_before_ENgetlinkid = _pdd.run_before_ENgetlinkid

def run_before_ENgetlinktype():
    return _pdd.run_before_ENgetlinktype()
run_before_ENgetlinktype = _pdd.run_before_ENgetlinktype

def run_before_ENgetlinknodes():
    return _pdd.run_before_ENgetlinknodes()
run_before_ENgetlinknodes = _pdd.run_before_ENgetlinknodes

def run_before_ENgetlinkvalue():
    return _pdd.run_before_ENgetlinkvalue()
run_before_ENgetlinkvalue = _pdd.run_before_ENgetlinkvalue

def run_before_ENgetversion():
    return _pdd.run_before_ENgetversion()
run_before_ENgetversion = _pdd.run_before_ENgetversion

def run_before_ENsetcontrol():
    return _pdd.run_before_ENsetcontrol()
run_before_ENsetcontrol = _pdd.run_before_ENsetcontrol

def run_before_ENsetnodevalue():
    return _pdd.run_before_ENsetnodevalue()
run_before_ENsetnodevalue = _pdd.run_before_ENsetnodevalue

def run_before_ENsetlinkvalue():
    return _pdd.run_before_ENsetlinkvalue()
run_before_ENsetlinkvalue = _pdd.run_before_ENsetlinkvalue

def run_before_ENaddpattern():
    return _pdd.run_before_ENaddpattern()
run_before_ENaddpattern = _pdd.run_before_ENaddpattern

def run_before_ENsetpattern():
    return _pdd.run_before_ENsetpattern()
run_before_ENsetpattern = _pdd.run_before_ENsetpattern

def run_before_ENsetpatternvalue():
    return _pdd.run_before_ENsetpatternvalue()
run_before_ENsetpatternvalue = _pdd.run_before_ENsetpatternvalue

def run_before_ENsettimeparam():
    return _pdd.run_before_ENsettimeparam()
run_before_ENsettimeparam = _pdd.run_before_ENsettimeparam

def run_before_ENsetoption():
    return _pdd.run_before_ENsetoption()
run_before_ENsetoption = _pdd.run_before_ENsetoption

def run_before_ENsetstatusreport():
    return _pdd.run_before_ENsetstatusreport()
run_before_ENsetstatusreport = _pdd.run_before_ENsetstatusreport

def run_before_ENsetqualtype():
    return _pdd.run_before_ENsetqualtype()
run_before_ENsetqualtype = _pdd.run_before_ENsetqualtype

def run_before_ENopenH():
    return _pdd.run_before_ENopenH()
run_before_ENopenH = _pdd.run_before_ENopenH

def getEmitterData(eexp_, ecup_):
    return _pdd.getEmitterData(eexp_, ecup_)
getEmitterData = _pdd.getEmitterData

def setEmitterData(eexp_, ecup_):
    return _pdd.setEmitterData(eexp_, ecup_)
setEmitterData = _pdd.setEmitterData

_pdd.EN_ELEVATION_swigconstant(_pdd)
EN_ELEVATION = _pdd.EN_ELEVATION

_pdd.EN_BASEDEMAND_swigconstant(_pdd)
EN_BASEDEMAND = _pdd.EN_BASEDEMAND

_pdd.EN_PATTERN_swigconstant(_pdd)
EN_PATTERN = _pdd.EN_PATTERN

_pdd.EN_EMITTER_swigconstant(_pdd)
EN_EMITTER = _pdd.EN_EMITTER

_pdd.EN_INITQUAL_swigconstant(_pdd)
EN_INITQUAL = _pdd.EN_INITQUAL

_pdd.EN_SOURCEQUAL_swigconstant(_pdd)
EN_SOURCEQUAL = _pdd.EN_SOURCEQUAL

_pdd.EN_SOURCEPAT_swigconstant(_pdd)
EN_SOURCEPAT = _pdd.EN_SOURCEPAT

_pdd.EN_SOURCETYPE_swigconstant(_pdd)
EN_SOURCETYPE = _pdd.EN_SOURCETYPE

_pdd.EN_TANKLEVEL_swigconstant(_pdd)
EN_TANKLEVEL = _pdd.EN_TANKLEVEL

_pdd.EN_DEMAND_swigconstant(_pdd)
EN_DEMAND = _pdd.EN_DEMAND

_pdd.EN_HEAD_swigconstant(_pdd)
EN_HEAD = _pdd.EN_HEAD

_pdd.EN_PRESSURE_swigconstant(_pdd)
EN_PRESSURE = _pdd.EN_PRESSURE

_pdd.EN_QUALITY_swigconstant(_pdd)
EN_QUALITY = _pdd.EN_QUALITY

_pdd.EN_SOURCEMASS_swigconstant(_pdd)
EN_SOURCEMASS = _pdd.EN_SOURCEMASS

_pdd.EN_INITVOLUME_swigconstant(_pdd)
EN_INITVOLUME = _pdd.EN_INITVOLUME

_pdd.EN_MIXMODEL_swigconstant(_pdd)
EN_MIXMODEL = _pdd.EN_MIXMODEL

_pdd.EN_MIXZONEVOL_swigconstant(_pdd)
EN_MIXZONEVOL = _pdd.EN_MIXZONEVOL

_pdd.EN_TANKDIAM_swigconstant(_pdd)
EN_TANKDIAM = _pdd.EN_TANKDIAM

_pdd.EN_MINVOLUME_swigconstant(_pdd)
EN_MINVOLUME = _pdd.EN_MINVOLUME

_pdd.EN_VOLCURVE_swigconstant(_pdd)
EN_VOLCURVE = _pdd.EN_VOLCURVE

_pdd.EN_MINLEVEL_swigconstant(_pdd)
EN_MINLEVEL = _pdd.EN_MINLEVEL

_pdd.EN_MAXLEVEL_swigconstant(_pdd)
EN_MAXLEVEL = _pdd.EN_MAXLEVEL

_pdd.EN_MIXFRACTION_swigconstant(_pdd)
EN_MIXFRACTION = _pdd.EN_MIXFRACTION

_pdd.EN_TANK_KBULK_swigconstant(_pdd)
EN_TANK_KBULK = _pdd.EN_TANK_KBULK

_pdd.EN_DIAMETER_swigconstant(_pdd)
EN_DIAMETER = _pdd.EN_DIAMETER

_pdd.EN_LENGTH_swigconstant(_pdd)
EN_LENGTH = _pdd.EN_LENGTH

_pdd.EN_ROUGHNESS_swigconstant(_pdd)
EN_ROUGHNESS = _pdd.EN_ROUGHNESS

_pdd.EN_MINORLOSS_swigconstant(_pdd)
EN_MINORLOSS = _pdd.EN_MINORLOSS

_pdd.EN_INITSTATUS_swigconstant(_pdd)
EN_INITSTATUS = _pdd.EN_INITSTATUS

_pdd.EN_INITSETTING_swigconstant(_pdd)
EN_INITSETTING = _pdd.EN_INITSETTING

_pdd.EN_KBULK_swigconstant(_pdd)
EN_KBULK = _pdd.EN_KBULK

_pdd.EN_KWALL_swigconstant(_pdd)
EN_KWALL = _pdd.EN_KWALL

_pdd.EN_FLOW_swigconstant(_pdd)
EN_FLOW = _pdd.EN_FLOW

_pdd.EN_VELOCITY_swigconstant(_pdd)
EN_VELOCITY = _pdd.EN_VELOCITY

_pdd.EN_HEADLOSS_swigconstant(_pdd)
EN_HEADLOSS = _pdd.EN_HEADLOSS

_pdd.EN_STATUS_swigconstant(_pdd)
EN_STATUS = _pdd.EN_STATUS

_pdd.EN_SETTING_swigconstant(_pdd)
EN_SETTING = _pdd.EN_SETTING

_pdd.EN_ENERGY_swigconstant(_pdd)
EN_ENERGY = _pdd.EN_ENERGY

_pdd.EN_DURATION_swigconstant(_pdd)
EN_DURATION = _pdd.EN_DURATION

_pdd.EN_HYDSTEP_swigconstant(_pdd)
EN_HYDSTEP = _pdd.EN_HYDSTEP

_pdd.EN_QUALSTEP_swigconstant(_pdd)
EN_QUALSTEP = _pdd.EN_QUALSTEP

_pdd.EN_PATTERNSTEP_swigconstant(_pdd)
EN_PATTERNSTEP = _pdd.EN_PATTERNSTEP

_pdd.EN_PATTERNSTART_swigconstant(_pdd)
EN_PATTERNSTART = _pdd.EN_PATTERNSTART

_pdd.EN_REPORTSTEP_swigconstant(_pdd)
EN_REPORTSTEP = _pdd.EN_REPORTSTEP

_pdd.EN_REPORTSTART_swigconstant(_pdd)
EN_REPORTSTART = _pdd.EN_REPORTSTART

_pdd.EN_RULESTEP_swigconstant(_pdd)
EN_RULESTEP = _pdd.EN_RULESTEP

_pdd.EN_STATISTIC_swigconstant(_pdd)
EN_STATISTIC = _pdd.EN_STATISTIC

_pdd.EN_PERIODS_swigconstant(_pdd)
EN_PERIODS = _pdd.EN_PERIODS

_pdd.EN_NODECOUNT_swigconstant(_pdd)
EN_NODECOUNT = _pdd.EN_NODECOUNT

_pdd.EN_TANKCOUNT_swigconstant(_pdd)
EN_TANKCOUNT = _pdd.EN_TANKCOUNT

_pdd.EN_LINKCOUNT_swigconstant(_pdd)
EN_LINKCOUNT = _pdd.EN_LINKCOUNT

_pdd.EN_PATCOUNT_swigconstant(_pdd)
EN_PATCOUNT = _pdd.EN_PATCOUNT

_pdd.EN_CURVECOUNT_swigconstant(_pdd)
EN_CURVECOUNT = _pdd.EN_CURVECOUNT

_pdd.EN_CONTROLCOUNT_swigconstant(_pdd)
EN_CONTROLCOUNT = _pdd.EN_CONTROLCOUNT

_pdd.EN_JUNCTION_swigconstant(_pdd)
EN_JUNCTION = _pdd.EN_JUNCTION

_pdd.EN_RESERVOIR_swigconstant(_pdd)
EN_RESERVOIR = _pdd.EN_RESERVOIR

_pdd.EN_TANK_swigconstant(_pdd)
EN_TANK = _pdd.EN_TANK

_pdd.EN_CVPIPE_swigconstant(_pdd)
EN_CVPIPE = _pdd.EN_CVPIPE

_pdd.EN_PIPE_swigconstant(_pdd)
EN_PIPE = _pdd.EN_PIPE

_pdd.EN_PUMP_swigconstant(_pdd)
EN_PUMP = _pdd.EN_PUMP

_pdd.EN_PRV_swigconstant(_pdd)
EN_PRV = _pdd.EN_PRV

_pdd.EN_PSV_swigconstant(_pdd)
EN_PSV = _pdd.EN_PSV

_pdd.EN_PBV_swigconstant(_pdd)
EN_PBV = _pdd.EN_PBV

_pdd.EN_FCV_swigconstant(_pdd)
EN_FCV = _pdd.EN_FCV

_pdd.EN_TCV_swigconstant(_pdd)
EN_TCV = _pdd.EN_TCV

_pdd.EN_GPV_swigconstant(_pdd)
EN_GPV = _pdd.EN_GPV

_pdd.EN_NONE_swigconstant(_pdd)
EN_NONE = _pdd.EN_NONE

_pdd.EN_CHEM_swigconstant(_pdd)
EN_CHEM = _pdd.EN_CHEM

_pdd.EN_AGE_swigconstant(_pdd)
EN_AGE = _pdd.EN_AGE

_pdd.EN_TRACE_swigconstant(_pdd)
EN_TRACE = _pdd.EN_TRACE

_pdd.EN_CONCEN_swigconstant(_pdd)
EN_CONCEN = _pdd.EN_CONCEN

_pdd.EN_MASS_swigconstant(_pdd)
EN_MASS = _pdd.EN_MASS

_pdd.EN_SETPOINT_swigconstant(_pdd)
EN_SETPOINT = _pdd.EN_SETPOINT

_pdd.EN_FLOWPACED_swigconstant(_pdd)
EN_FLOWPACED = _pdd.EN_FLOWPACED

_pdd.EN_CFS_swigconstant(_pdd)
EN_CFS = _pdd.EN_CFS

_pdd.EN_GPM_swigconstant(_pdd)
EN_GPM = _pdd.EN_GPM

_pdd.EN_MGD_swigconstant(_pdd)
EN_MGD = _pdd.EN_MGD

_pdd.EN_IMGD_swigconstant(_pdd)
EN_IMGD = _pdd.EN_IMGD

_pdd.EN_AFD_swigconstant(_pdd)
EN_AFD = _pdd.EN_AFD

_pdd.EN_LPS_swigconstant(_pdd)
EN_LPS = _pdd.EN_LPS

_pdd.EN_LPM_swigconstant(_pdd)
EN_LPM = _pdd.EN_LPM

_pdd.EN_MLD_swigconstant(_pdd)
EN_MLD = _pdd.EN_MLD

_pdd.EN_CMH_swigconstant(_pdd)
EN_CMH = _pdd.EN_CMH

_pdd.EN_CMD_swigconstant(_pdd)
EN_CMD = _pdd.EN_CMD

_pdd.EN_TRIALS_swigconstant(_pdd)
EN_TRIALS = _pdd.EN_TRIALS

_pdd.EN_ACCURACY_swigconstant(_pdd)
EN_ACCURACY = _pdd.EN_ACCURACY

_pdd.EN_TOLERANCE_swigconstant(_pdd)
EN_TOLERANCE = _pdd.EN_TOLERANCE

_pdd.EN_EMITEXPON_swigconstant(_pdd)
EN_EMITEXPON = _pdd.EN_EMITEXPON

_pdd.EN_DEMANDMULT_swigconstant(_pdd)
EN_DEMANDMULT = _pdd.EN_DEMANDMULT

_pdd.EN_LOWLEVEL_swigconstant(_pdd)
EN_LOWLEVEL = _pdd.EN_LOWLEVEL

_pdd.EN_HILEVEL_swigconstant(_pdd)
EN_HILEVEL = _pdd.EN_HILEVEL

_pdd.EN_TIMER_swigconstant(_pdd)
EN_TIMER = _pdd.EN_TIMER

_pdd.EN_TIMEOFDAY_swigconstant(_pdd)
EN_TIMEOFDAY = _pdd.EN_TIMEOFDAY

_pdd.EN_AVERAGE_swigconstant(_pdd)
EN_AVERAGE = _pdd.EN_AVERAGE

_pdd.EN_MINIMUM_swigconstant(_pdd)
EN_MINIMUM = _pdd.EN_MINIMUM

_pdd.EN_MAXIMUM_swigconstant(_pdd)
EN_MAXIMUM = _pdd.EN_MAXIMUM

_pdd.EN_RANGE_swigconstant(_pdd)
EN_RANGE = _pdd.EN_RANGE

_pdd.EN_MIX1_swigconstant(_pdd)
EN_MIX1 = _pdd.EN_MIX1

_pdd.EN_MIX2_swigconstant(_pdd)
EN_MIX2 = _pdd.EN_MIX2

_pdd.EN_FIFO_swigconstant(_pdd)
EN_FIFO = _pdd.EN_FIFO

_pdd.EN_LIFO_swigconstant(_pdd)
EN_LIFO = _pdd.EN_LIFO

_pdd.EN_NOSAVE_swigconstant(_pdd)
EN_NOSAVE = _pdd.EN_NOSAVE

_pdd.EN_SAVE_swigconstant(_pdd)
EN_SAVE = _pdd.EN_SAVE

_pdd.EN_INITFLOW_swigconstant(_pdd)
EN_INITFLOW = _pdd.EN_INITFLOW

def ENepanet(arg1, arg2, arg3, arg4):
    return _pdd.ENepanet(arg1, arg2, arg3, arg4)
ENepanet = _pdd.ENepanet

def ENopen(arg1, arg2, arg3):
    return _pdd.ENopen(arg1, arg2, arg3)
ENopen = _pdd.ENopen

def ENsaveinpfile(arg1):
    return _pdd.ENsaveinpfile(arg1)
ENsaveinpfile = _pdd.ENsaveinpfile

def ENclose():
    return _pdd.ENclose()
ENclose = _pdd.ENclose

def ENsolveH():
    return _pdd.ENsolveH()
ENsolveH = _pdd.ENsolveH

def ENsaveH():
    return _pdd.ENsaveH()
ENsaveH = _pdd.ENsaveH

def ENopenH():
    return _pdd.ENopenH()
ENopenH = _pdd.ENopenH

def ENinitH(arg1):
    return _pdd.ENinitH(arg1)
ENinitH = _pdd.ENinitH

def ENrunH():
    return _pdd.ENrunH()
ENrunH = _pdd.ENrunH

def ENnextH():
    return _pdd.ENnextH()
ENnextH = _pdd.ENnextH

def ENcloseH():
    return _pdd.ENcloseH()
ENcloseH = _pdd.ENcloseH

def ENsavehydfile(arg1):
    return _pdd.ENsavehydfile(arg1)
ENsavehydfile = _pdd.ENsavehydfile

def ENusehydfile(arg1):
    return _pdd.ENusehydfile(arg1)
ENusehydfile = _pdd.ENusehydfile

def ENsolveQ():
    return _pdd.ENsolveQ()
ENsolveQ = _pdd.ENsolveQ

def ENopenQ():
    return _pdd.ENopenQ()
ENopenQ = _pdd.ENopenQ

def ENinitQ(arg1):
    return _pdd.ENinitQ(arg1)
ENinitQ = _pdd.ENinitQ

def ENrunQ():
    return _pdd.ENrunQ()
ENrunQ = _pdd.ENrunQ

def ENnextQ():
    return _pdd.ENnextQ()
ENnextQ = _pdd.ENnextQ

def ENstepQ():
    return _pdd.ENstepQ()
ENstepQ = _pdd.ENstepQ

def ENcloseQ():
    return _pdd.ENcloseQ()
ENcloseQ = _pdd.ENcloseQ

def ENwriteline(arg1):
    return _pdd.ENwriteline(arg1)
ENwriteline = _pdd.ENwriteline

def ENreport():
    return _pdd.ENreport()
ENreport = _pdd.ENreport

def ENresetreport():
    return _pdd.ENresetreport()
ENresetreport = _pdd.ENresetreport

def ENsetreport(arg1):
    return _pdd.ENsetreport(arg1)
ENsetreport = _pdd.ENsetreport

def ENgetcontrol(arg1):
    return _pdd.ENgetcontrol(arg1)
ENgetcontrol = _pdd.ENgetcontrol

def ENgetcount(arg1):
    return _pdd.ENgetcount(arg1)
ENgetcount = _pdd.ENgetcount

def ENgetoption(arg1):
    return _pdd.ENgetoption(arg1)
ENgetoption = _pdd.ENgetoption

def ENgettimeparam(arg1):
    return _pdd.ENgettimeparam(arg1)
ENgettimeparam = _pdd.ENgettimeparam

def ENgetflowunits():
    return _pdd.ENgetflowunits()
ENgetflowunits = _pdd.ENgetflowunits

def ENgetpatternindex(arg1):
    return _pdd.ENgetpatternindex(arg1)
ENgetpatternindex = _pdd.ENgetpatternindex

def ENgetpatternid(arg1):
    return _pdd.ENgetpatternid(arg1)
ENgetpatternid = _pdd.ENgetpatternid

def ENgetpatternlen(arg1):
    return _pdd.ENgetpatternlen(arg1)
ENgetpatternlen = _pdd.ENgetpatternlen

def ENgetpatternvalue(arg1, arg2):
    return _pdd.ENgetpatternvalue(arg1, arg2)
ENgetpatternvalue = _pdd.ENgetpatternvalue

def ENgetqualtype():
    return _pdd.ENgetqualtype()
ENgetqualtype = _pdd.ENgetqualtype

def ENgeterror(arg1, arg3):
    return _pdd.ENgeterror(arg1, arg3)
ENgeterror = _pdd.ENgeterror

def ENgetnodeindex(arg1):
    return _pdd.ENgetnodeindex(arg1)
ENgetnodeindex = _pdd.ENgetnodeindex

def ENgetnodeid(arg1):
    return _pdd.ENgetnodeid(arg1)
ENgetnodeid = _pdd.ENgetnodeid

def ENgetnodetype(arg1):
    return _pdd.ENgetnodetype(arg1)
ENgetnodetype = _pdd.ENgetnodetype

def ENgetnodevalue(arg1, arg2):
    return _pdd.ENgetnodevalue(arg1, arg2)
ENgetnodevalue = _pdd.ENgetnodevalue

def ENgetlinkindex(arg1):
    return _pdd.ENgetlinkindex(arg1)
ENgetlinkindex = _pdd.ENgetlinkindex

def ENgetlinkid(arg1):
    return _pdd.ENgetlinkid(arg1)
ENgetlinkid = _pdd.ENgetlinkid

def ENgetlinktype(arg1):
    return _pdd.ENgetlinktype(arg1)
ENgetlinktype = _pdd.ENgetlinktype

def ENgetlinknodes(arg1):
    return _pdd.ENgetlinknodes(arg1)
ENgetlinknodes = _pdd.ENgetlinknodes

def ENgetlinkvalue(arg1, arg2):
    return _pdd.ENgetlinkvalue(arg1, arg2)
ENgetlinkvalue = _pdd.ENgetlinkvalue

def ENgetversion():
    return _pdd.ENgetversion()
ENgetversion = _pdd.ENgetversion

def ENsetcontrol(arg1, arg2, arg3, arg4, arg5, arg6):
    return _pdd.ENsetcontrol(arg1, arg2, arg3, arg4, arg5, arg6)
ENsetcontrol = _pdd.ENsetcontrol

def ENsetnodevalue(arg1, arg2, arg3):
    return _pdd.ENsetnodevalue(arg1, arg2, arg3)
ENsetnodevalue = _pdd.ENsetnodevalue

def ENsetlinkvalue(arg1, arg2, arg3):
    return _pdd.ENsetlinkvalue(arg1, arg2, arg3)
ENsetlinkvalue = _pdd.ENsetlinkvalue

def ENaddpattern(arg1):
    return _pdd.ENaddpattern(arg1)
ENaddpattern = _pdd.ENaddpattern

def ENsetpattern(arg1, floatarray):
    return _pdd.ENsetpattern(arg1, floatarray)
ENsetpattern = _pdd.ENsetpattern

def ENsetpatternvalue(arg1, arg2, arg3):
    return _pdd.ENsetpatternvalue(arg1, arg2, arg3)
ENsetpatternvalue = _pdd.ENsetpatternvalue

def ENsettimeparam(arg1, arg2):
    return _pdd.ENsettimeparam(arg1, arg2)
ENsettimeparam = _pdd.ENsettimeparam

def ENsetoption(arg1, arg2):
    return _pdd.ENsetoption(arg1, arg2)
ENsetoption = _pdd.ENsetoption

def ENsetstatusreport(arg1):
    return _pdd.ENsetstatusreport(arg1)
ENsetstatusreport = _pdd.ENsetstatusreport

def ENsetqualtype(arg1, arg2, arg3, arg4):
    return _pdd.ENsetqualtype(arg1, arg2, arg3, arg4)
ENsetqualtype = _pdd.ENsetqualtype
# This file is compatible with both classic and new-style classes.

cvar = _pdd.cvar

