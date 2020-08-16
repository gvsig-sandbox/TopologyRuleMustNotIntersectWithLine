# encoding: utf-8

import gvsig
import sys

from gvsig import uselib
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.fmap.geom import Geometry
from org.gvsig.tools.util import ListBuilder
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.spi import AbstractTopologyRuleFactory

from mustNotIntersectWithLineRule import MustNotIntersectWithLineRule

class MustNotIntersectWithLineRuleFactory(AbstractTopologyRuleFactory):
      
    def __init__(self):
        AbstractTopologyRuleFactory.__init__(
            self,
            "MustNotIntersectWithLineRule",
            "Must Not Intersect With",
            "This rule requires lines not to intersects.",
            ListBuilder().add(Geometry.TYPES.LINE).add(Geometry.TYPES.MULTILINE).asList(),
            ListBuilder().add(Geometry.TYPES.LINE).add(Geometry.TYPES.MULTILINE).asList()
        )
    
    def createRule(self, plan, dataSet1, dataSet2, tolerance):
        rule = MustNotIntersectWithLineRule(plan, self, tolerance, dataSet1, dataSet2)
        return rule

def selfRegister():
    try:
        manager = TopologyLocator.getTopologyManager()
        manager.addRuleFactories(MustNotIntersectWithLineRuleFactory())
    except:
        ex = sys.exc_info()[1]
        gvsig.logger("Can't register rule. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)

def main(*args):
    pass
