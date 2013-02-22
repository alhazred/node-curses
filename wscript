srcdir = '.'
blddir = 'build'
VERSION = '0.0.10'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.cxxflags = '-I/usr/include/ncurses'
  obj.target = 'curses'
  obj.ldflags = ['-L/usr/gnu/lib','-lncurses', '-lpanel']
  obj.source = 'src/curses.cc'
