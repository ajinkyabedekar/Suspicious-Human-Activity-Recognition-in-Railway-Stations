from pybuilder.core import init, use_plugin

use_plugin("python.install_dependencies")
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")

default_task = "publish"

@init
def set_properties(project):
	project.set_property("coverage_break_build", False) # default is True
	project.build_depends_on("mock")
