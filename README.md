# TopologyRuleMustNotIntersectWithLine

The rule requires that the lines in the input layer must not cross or overlap any part of lines in the coverage layer. Lines errors are created if the lines cross or overlap with lines in the other layer and point errors are created where lines cross.

For example, is useful when lines should never occupy the same space with lines in the other layer, like loacal roads cannot cross or overlap with routes.

![Rule image](https://github.com/Maureque/TopologyRuleMustNotIntersectWithLine/blob/master/MustNotIntersectWithLine_d/mustNotIntersectWithLine2.png "Rule image")
