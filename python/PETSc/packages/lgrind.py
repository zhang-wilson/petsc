#!/usr/bin/env python
from __future__ import generators
import config.base
import os
import re
import PETSc.package

class Configure(PETSc.package.Package):
  def __init__(self, framework):
    PETSc.package.Package.__init__(self, framework)
    self.download     = ['ftp://ftp.mcs.anl.gov/pub/petsc/externalpackages/lgrind-dev.tar.gz']
    #
    #  lgrind is currently not used by PETSc
    #
    self.required     = 0
    return

  def Install(self):

    # Get the LGRIND directories
    if os.path.isfile(os.path.join(self.installDir,'bin','lgrind')) or os.path.isfile(os.path.join(self.installDir,'bin','lgrind.exe')):
      self.framework.log.write('Found Lgrind executable; skipping compile\n')
      lgrindexe = os.path.join(self.installDir,'source','lgrind')
      if os.path.exists(lgrindexe+'.exe'):
        lgrindexe = lgrindexe+'.exe'
        lgrind    = 'lgrind.exe'
      else: lgrind = 'lgrind'
    else:
      self.framework.log.write('Did not find Lgrind executable; compiling lgrind\n')
      try:
        self.framework.pushLanguage('C')
        output = config.base.Configure.executeShellCommand('cd '+os.path.join(self.packageDir,'source')+'; make clean; make CC=\''+self.framework.getCompiler()+'\'',timeout=2500,log = self.framework.log)[0]
        self.framework.popLanguage()
      except RuntimeError, e:
        self.framework.popLanguage()
        if self.framework.argDB['with-batch']:
          self.logPrintBox('Batch build that could not generate lgrind, you will not be able to build documentation')
          return
        raise RuntimeError('Error running make on lgrind: '+str(e))
      try:
        lgrindexe = os.path.join(self.packageDir,'source','lgrind')
        if os.path.exists(lgrindexe+'.exe'):
          lgrindexe = lgrindexe+'.exe'
          lgrind    = 'lgrind.exe'
        else: lgrind = 'lgrind'
        output  = config.base.Configure.executeShellCommand('mv '+lgrindexe+' '+os.path.join(self.installDir,'bin'), timeout=25, log = self.framework.log)[0]
      except RuntimeError, e:
        raise RuntimeError('Error copying lgrind executable: '+str(e))
    output = config.base.Configure.executeShellCommand('cd '+os.path.join(self.packageDir,'source')+'; make clean',timeout=25, log = self.framework.log)[0]
    self.framework.actions.addArgument('lgrind', 'Install', 'Installed lgrind into '+self.installDir)
    self.lgrind = lgrindexe
    self.addMakeMacro('LGRIND',os.path.join(self.installDir,'bin',lgrind))
    self.addMakeMacro('LGRIND_DIR',self.packageDir)
    return

  def configure(self):
    '''Determine whether the Lgrind exist or not'''
    if self.petscdir.isClone:
      if self.framework.argDB['with-lgrind']:
        self.framework.logPrint('PETSc clone, checking for Lgrind\n')
        self.installDir  = os.path.join(self.petscdir.dir,self.arch.arch)
        self.packageDir  = self.getDir()
        self.Install()
      else:
        self.framework.logPrint('Disabled Lgrind\n')
    else:
      self.framework.logPrint("Not a clone of PETSc, don't need Lgrind\n")
    return

if __name__ == '__main__':
  import config.framework
  import sys
  framework = config.framework.Framework(sys.argv[1:])
  framework.setupLogging(sys.argv[1:])
  framework.children.append(Configure(framework))
  framework.configure()
  framework.dumpSubstitutions()
