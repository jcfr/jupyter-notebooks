import arrow
import collections

class QueryBuilder(object):
    """
    Pythonic interface allowing to generate CDash API filtering URL query.
    """


    """
    Type of operators that can be used to select values associated
    with a filter.
    """
    IS               = "IS"
    IS_NOT           = "IS_NOT"
    IS_GREATER_THAN  = "IS_GREATER_THAN"
    IS_LESSER_THAN   = "IS_LESSER_THAN"
    CONTAINS         = "CONTAINS"
    DOES_NOT_CONTAIN = "DOES_NOT_CONTAIN"
    STARTS_WITH      = "STARTS_WITH"
    ENDS_WITH        = "ENDS_WITH"

    """
    Type of filter combination.
    """
    AND = "and"
    OR = "or"


    def __init__(self, project, filtercombine=AND, date=None):
        self._project = project
        self._filtercombine = filtercombine
        self._date = arrow.now('US/Eastern').format('YYYY-MM-DD') if date is None else date
        self._filters = []

    def _check(self, field, acceptableOperators, operator):
        if operator not in acceptableOperators:
            raise Exception("Field '%s' is associated with an invalid operator '%s'."
                            "Acceptable operators are %s." % (field, operator, ", ".join(acceptableOperators)))

    def _add(self, field, operator_id, value):
        self._filters.append({'field': field, 'compare': operator_id, 'value': value})

    def params(self):

        params = collections.OrderedDict()
        params['project'] = self._project
        params['date'] = self._date
        params['filtercount'] = len(self._filters)
        params['filtercombine'] = self._filtercombine
        for (index, _filter) in enumerate(self._filters, start=1):
            params['field%d' % index]= _filter['field']
            params['compare%d' % index]= _filter['compare']
            params['value%d' % index]= _filter['value']
        return params

    def __repr__(self):
        pass


    # START: List of query building functions automatically generated

    def buildduration(self, value, operator=IS):
        field = "buildduration"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def builderrors(self, value, operator=IS):
        field = "builderrors"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def buildgenerator(self, value, operator=IS):
        field = "buildgenerator"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def buildname(self, value, operator=IS):
        field = "buildname"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def buildstamp(self, value, operator=IS):
        field = "buildstamp"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def buildstarttime(self, value, operator=IS):
        field = "buildstarttime"
        self._check(field, QueryBuilder.DATE_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.DATE_OPERATORS[operator], value)
        return self

    def buildtype(self, value, operator=IS):
        field = "buildtype"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def buildwarnings(self, value, operator=IS):
        field = "buildwarnings"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def configureduration(self, value, operator=IS):
        field = "configureduration"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def configureerrors(self, value, operator=IS):
        field = "configureerrors"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def configurewarnings(self, value, operator=IS):
        field = "configurewarnings"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def coveredlines(self, value, operator=IS):
        field = "coveredlines"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def details(self, value, operator=IS):
        field = "details"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def expected(self, value, operator=IS):
        field = "expected"
        self._check(field, QueryBuilder.BOOL_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.BOOL_OPERATORS[operator], value)
        return self

    def filename(self, value, operator=IS):
        field = "filename"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def groupname(self, value, operator=IS):
        field = "groupname"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def hascoverage(self, value, operator=IS):
        field = "hascoverage"
        self._check(field, QueryBuilder.BOOL_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.BOOL_OPERATORS[operator], value)
        return self

    def hasctestnotes(self, value, operator=IS):
        field = "hasctestnotes"
        self._check(field, QueryBuilder.BOOL_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.BOOL_OPERATORS[operator], value)
        return self

    def hasdynamicanalysis(self, value, operator=IS):
        field = "hasdynamicanalysis"
        self._check(field, QueryBuilder.BOOL_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.BOOL_OPERATORS[operator], value)
        return self

    def hasusernotes(self, value, operator=IS):
        field = "hasusernotes"
        self._check(field, QueryBuilder.BOOL_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.BOOL_OPERATORS[operator], value)
        return self

    def label(self, value, operator=IS):
        field = "label"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def labels(self, value, operator=IS):
        field = "labels"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def priority(self, value, operator=IS):
        field = "priority"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def site(self, value, operator=IS):
        field = "site"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def status(self, value, operator=IS):
        field = "status"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def subproject(self, value, operator=IS):
        field = "subproject"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def testname(self, value, operator=IS):
        field = "testname"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def testsduration(self, value, operator=IS):
        field = "testsduration"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def testsfailed(self, value, operator=IS):
        field = "testsfailed"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def testsnotrun(self, value, operator=IS):
        field = "testsnotrun"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def testspassed(self, value, operator=IS):
        field = "testspassed"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def testtimestatus(self, value, operator=IS):
        field = "testtimestatus"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def timestatus(self, value, operator=IS):
        field = "timestatus"
        self._check(field, QueryBuilder.STRING_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.STRING_OPERATORS[operator], value)
        return self

    def time(self, value, operator=IS):
        field = "time"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def totallines(self, value, operator=IS):
        field = "totallines"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def uncoveredlines(self, value, operator=IS):
        field = "uncoveredlines"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def updatedfiles(self, value, operator=IS):
        field = "updatedfiles"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    def updateduration(self, value, operator=IS):
        field = "updateduration"
        self._check(field, QueryBuilder.NUMBER_OPERATORS.keys(), operator)
        self._add(field, QueryBuilder.NUMBER_OPERATORS[operator], value)
        return self

    # END: List of query building functions automatically generated

    # Comparison types - From js/cdashFilters.js and CDash/public/filterdataTemplate.xsl
    # Field types      - From include/filterdataFunctions.php / getFilterDefinitionsXML()
    _BOOL_IS_TRUE = 1
    _BOOL_IS_FALSE = 2
    BOOL_OPERATORS = {
        IS     : _BOOL_IS_TRUE,
        IS_NOT : _BOOL_IS_FALSE
    }
    BOOL_TYPE = 'bool'

    _DATE_IS = 81
    _DATE_IS_NOT = 82
    _DATE_IS_AFTER = 83
    _DATE_IS_BEFORE = 84
    DATE_OPERATORS = {
        IS              : _DATE_IS,
        IS_NOT          : _DATE_IS_NOT,
        IS_GREATER_THAN : _DATE_IS_AFTER,
        IS_LESSER_THAN  : _DATE_IS_BEFORE
    }
    DATE_TYPE = ''

    _NUMBER_IS = 41
    _NUMBER_IS_NOT = 42
    _NUMBER_IS_GREATER_THAN = 43
    _NUMBER_IS_LESS_THAN = 44
    NUMBER_OPERATORS = {
        IS              : _NUMBER_IS,
        IS_NOT          : _NUMBER_IS_NOT,
        IS_GREATER_THAN : _NUMBER_IS_GREATER_THAN,
        IS_LESSER_THAN  : _NUMBER_IS_LESS_THAN
    }
    NUMBER_TYPE = 'float'

    _STRING_IS = 61
    _STRING_IS_NOT = 62
    _STRING_CONTAINS = 63
    _STRING_DOES_NOT_CONTAIN = 64
    _STRING_STARTS_WITH = 65
    _STRING_ENDS_WITH = 66
    STRING_OPERATORS = {
        IS               : _STRING_IS,
        IS_NOT           : _STRING_IS_NOT,
        CONTAINS         : _STRING_CONTAINS,
        DOES_NOT_CONTAIN : _STRING_DOES_NOT_CONTAIN,
        STARTS_WITH      : _STRING_STARTS_WITH,
        ENDS_WITH        : _STRING_ENDS_WITH
    }
    STRING_TYPE = 'float'

