#!/usr/bin/env bash

pushd /tmp  > /dev/null 2>&1

rm -f filterdataFunctions.php && wget -nv "https://raw.githubusercontent.com/Kitware/CDash/master/include/filterdataFunctions.php" 2>&1

while read rawdef; do
    echo ""
    field=$(echo $rawdef | cut -d"'" -f2);
    field_pretty_name=$(echo $rawdef | cut -d"'" -f4);
    operator_type=$(echo $rawdef | cut -d"'" -f6);
    #echo "field=$field";
    #echo "field_pretty_name=$field_pretty_name";
    #echo "operator_type=$operator_type";

    echo "    def $field(self, value, operator=IS):"
    echo "        field = \"$field\""
    echo "        self._check(field, QueryBuilder.${operator_type^^}_OPERATORS.keys(), operator)"
    echo "        self._add(field, QueryBuilder.${operator_type^^}_OPERATORS[operator], value)"
    echo "        return self"

done <<< "$(cat ./filterdataFunctions.php  | egrep  "^[^//]+getFilterDefinitionXML\('" | sort | uniq)";

popd > /dev/null 2>&1
